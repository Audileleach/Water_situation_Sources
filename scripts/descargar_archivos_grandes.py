"""Download the files that are listed in manifest.csv but not stored in this
repository (too big for GitHub, or third-party reports), into their folders.

Run from the repository root:   python scripts/descargar_archivos_grandes.py
Optional: pass part of a path to download only some files, e.g.
    python scripts/descargar_archivos_grandes.py hells_bells
Needs only the Python standard library. Files already present are skipped.
"""
import csv
import hashlib
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXCLUDED = (
    "01_AR_cenotes/hells_bells/Mesh_seg_bright.ply",
    "01_AR_cenotes/hells_bells/Mesh_seg_bright.nxz",
    "02_LiDAR/nasa_gliht_2013/dtm/",
    "02_LiDAR/nasa_gliht_2013/dtm_sample/",
    "05_public_replacement/sds_salud_granjas_cenotes/greenpeace_2026/",
)
HEADERS = {"User-Agent": "Mozilla/5.0 (school research project; water in Yucatan)"}


def wanted(path: str, filters) -> bool:
    if not any(path == e or path.startswith(e) for e in EXCLUDED):
        return False
    return not filters or any(f in path for f in filters)


def main() -> None:
    filters = sys.argv[1:]
    rows = list(csv.DictReader(open(ROOT / "manifest.csv", encoding="utf-8")))
    todo = [r for r in rows if wanted(r["file"], filters) and r["url"].startswith("http")]
    print(f"{len(todo)} file(s) to check")
    for r in todo:
        dest = ROOT / r["file"]
        if dest.exists() and dest.stat().st_size == int(r["bytes"]):
            print("already here:", r["file"])
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        print(f"downloading {int(r['bytes']) / 1e6:,.0f} MB -> {r['file']}")
        h = hashlib.sha256()
        with urllib.request.urlopen(urllib.request.Request(r["url"], headers=HEADERS), timeout=600) as resp, \
                open(dest, "wb") as out:
            while chunk := resp.read(1 << 20):
                out.write(chunk)
                h.update(chunk)
        status = "OK" if h.hexdigest() == r["sha256"] else "WARNING: checksum differs from the manifest (the source may have changed)"
        print("  ", status)


if __name__ == "__main__":
    main()
