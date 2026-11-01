"""Scrape JAPAY's news section (japay.yucatan.gob.mx/noticias) (one request per article id, 0.5 s apart) and
flag articles about outages, low pressure, contamination or maintenance."""
import csv
import html
import re
import time
import urllib.request
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "04_web_scraping" / "japay_news" / "japay_noticias.csv"
BASE = "https://japay.yucatan.gob.mx/noticias/verarticulo.php?IdArticulo={}"
HEADERS = {"User-Agent": "Mozilla/5.0 (school research project; water in Yucatan)"}
KEYWORDS = {
    "outage": r"suspensi[oó]n|sin agua|baja presi[oó]n|interrup|corte|desabasto|afectaci[oó]n del servicio|restablec",
    "maintenance": r"mantenimiento|reparaci[oó]n|fuga|rehabilitaci[oó]n|obra",
    "quality": r"contamina|calidad del agua|cloro|cloraci[oó]n|potabiliza|nitrat|coliform|sargazo|salin",
    "drought": r"sequ[ií]a|estiaje|calor|ola de calor|consumo",
    "sewer": r"drenaje|alcantarillado|aguas residuales|saneamiento|fosa s[eé]ptica|biodigestor",
}


def text_of(raw: str) -> str:
    raw = re.sub(r"<(script|style)[\s\S]*?</\1>", " ", raw)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", raw))).strip()


def main(max_id: int = 520) -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    rows, misses = [], 0
    for i in range(1, max_id + 1):
        try:
            with urllib.request.urlopen(urllib.request.Request(BASE.format(i), headers=HEADERS), timeout=60) as r:
                raw = r.read().decode("utf-8", "replace")
        except Exception as e:  # keep going on single failures
            rows.append({"id": i, "status": f"error {e}"})
            time.sleep(1)
            continue
        cuerpo = raw.split('id="cuerpo"', 1)[-1]
        title_m = re.search(r"<h5[^>]*>([\s\S]*?)</h5>", cuerpo, re.I)
        title = text_of(title_m.group(1)) if title_m else ""
        date_m = re.search(r"Por\s+[^<]*<br>\s*(\d{1,2}/\d{1,2}/\d{4})", cuerpo, re.I)
        # article text = the #cuerpo block (minus share widgets), capped
        body = text_of(cuerpo)
        body = re.sub(r"Comparta este art[ií]culo.*?Haga clic en la opci[oó]n deseada\.", " ", body)
        snippet = body[:1500] if title else ""
        if not snippet or len(snippet) < 80:
            misses += 1
        row = {"id": i, "status": "ok", "date_text": date_m.group(1) if date_m else "", "title": title[:300],
               "url": BASE.format(i), "snippet": snippet[:600]}
        for k, pat in KEYWORDS.items():
            row[f"kw_{k}"] = int(bool(re.search(pat, snippet, re.I)))
        rows.append(row)
        time.sleep(0.5)
    fields = ["id", "status", "date_text", "title", "url", "kw_outage", "kw_maintenance", "kw_quality", "kw_drought", "kw_sewer", "snippet"]
    with open(OUT, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    ok = [r for r in rows if r.get("status") == "ok"]
    print(f"rows {len(rows)}, ok {len(ok)}, empty-looking {misses}")
    for k in KEYWORDS:
        print(k, sum(r.get(f"kw_{k}", 0) for r in ok))


if __name__ == "__main__":
    main()
