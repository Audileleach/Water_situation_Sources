# Sources: water in the Yucatán Peninsula vs the rest of Mexico

Collected 30–31 Oct 2026. Every downloaded file is listed in [`manifest.csv`](manifest.csv) with its URL, size, SHA-256 and date.

**Legend:** ✅ found and downloaded · ⚠️ found with a caveat or only partly · ❌ not found as described · 🔒 blocked, needs you · 🧪 simulated data (not real)

## Summary

| # | Method | Source | Status |
|---|---|---|---|
| 1 | AR | Gran Acuífero Maya (INAH) 3D scans | ❌ |
| 1 | AR | Hells Bells 3D model, cenote El Zapote | ✅ |
| 1 | AR | SDS cenote and cave inventory | ❌ |
| 2 | LiDAR | INEGI 5 m / 1.5 m elevation models | ⚠️ not LiDAR over Yucatán |
| 2 | LiDAR | NASA G-LiHT 2013 | ✅ (all 10 flights) |
| 2 | LiDAR | Puuc survey, PLOS ONE 2021 | ⚠️ paper only; raw data embargoed |
| 3 | Self-produced | Survey, water tests, interview | 🧪 simulated, calibrated to real data |
| 4 | Scraping | SMN drought monitor | ✅ |
| 4 | Scraping | CONAGUA SINA | ✅ |
| 4 | Scraping | JAPAY notices + local news | ⚠️ JAPAY done; news history short |
| 5 | Public data (replaces requests) | CONAGUA extraction and monitoring | ✅ |
| 5 | Public data (replaces requests) | JAPAY / Mérida water operator | ✅ (CNGMD 2025) |
| 5 | Public data (replaces requests) | SDS / Salud: pig farms, cenotes, chlorination | ✅ |
| 6 | Geoportal + public substitutes | Cuxtal, flood risk, land use / growth / cenotes | ✅ substitutes + geoportal catalog |
| 7 | SIEGY | State Development Plan indicators | ⚠️ Power BI, manual export |
| 7 | SIEGY | Bulletins by municipality | ❌ (16 thematic bulletins only) |
| 7 | SIEGY | Ring of Cenotes layer | ✅ (from SDS, not SIEGY) |
| 8 | datos.gob.mx | RENAMECA groundwater quality | ✅ |
| 8 | datos.gob.mx | Aquifer availability (653 aquifers) | ✅ |
| 8 | datos.gob.mx | Treatment-plant inventory | ⚠️ not on datos.gob.mx; 2020 PDF |
| 9 | INEGI | Census 2020 water and drainage | ✅ |
| 9 | INEGI | CNGMD 2025 water module | ✅ |
| 9 | INEGI | Hydrography | ✅ |

---

## 1. AR: cenotes and underground rivers — `01_AR_cenotes/`

- **Gran Acuífero Maya (INAH) — ❌ not found.** No public download of the project's cenote scans exists. The closest public material is INAH Quintana Roo's underwater-archaeology account on Sketchfab ([ArqSub.Mx](https://sketchfab.com/arqsub.mx/models)): cave models of Aktun Ha, La Chimenea (Taxma Ha) and El Pit. They are **view/embed only, © INAH**, and are in Quintana Roo, not Yucatán. Using them in AR would need INAH's permission.
- **Hells Bells, cenote El Zapote — ✅ downloaded.** Heidelberg University, heidICON, DOI [10.11588/heidicon/1264341](https://doi.org/10.11588/heidicon/1264341), license **CC BY-SA 4.0** (credit the authors and share derivatives under the same license). Files: `Mesh_seg_bright.ply` (1.19 GB, full mesh: **22.1 million points, 44.2 million triangles**) and `Mesh_seg_bright.nxz` (274 MB, 3DHOP web-viewer format), plus a preview image and the related geochemistry dataset (PANGAEA, CC BY 4.0). **For phone AR the mesh must be simplified** (e.g. MeshLab "Quadric Edge Collapse Decimation" or Blender "Decimate" down to ~100–500k triangles) and exported to glTF/GLB or USDZ. Note: El Zapote is in **Quintana Roo**.
- **SDS cenote inventory — ❌ not found.** The SDS page "[Censo de cenotes y grutas](https://sds.yucatan.gob.mx/cenotes-grutas/censo-cenotes.php)" only says "En proceso de actualización". Press reports cite 2,241 to 3,200 registered cenotes, but no list is published. I added it to the SDS transparency request (section 5).

## 2. LiDAR: flat limestone and sinkholes — `02_LiDAR/`

- **INEGI 5 m / 1.5 m — ⚠️ caveat.** INEGI's own coverage map shows its **LiDAR-sourced** 1:10,000 tiles in the peninsula only cover the **Quintana Roo coast** (Cancún, Cozumel, Riviera Maya). For Mérida, INEGI has terrain models in the same high-resolution series, but they are flagged as made from **photogrammetry / "sensores remotos" and "altimetría"**, not LiDAR:
  - 5 m terrain (editions 2016–2017, some 2026): **28 tiles downloaded** covering the Mérida metro block (`mdt_5m_bil/`, BIL format). 4 more tiles (F16C51F1–F4) only exist as 2012 GRID files.
  - 1.5 m terrain (editions 2020–2025): **all 32 tiles downloaded** (TIFF, 1.1 GB) covering the Mérida metro area: downtown sample in `mdt_1_5m_sample/` (F16C52A2), the other 31 in `mdt_1_5m/`.
  - `inegi_tiles_index_merida.csv` lists all 106 tiles around Mérida with direct download links.
- **NASA G-LiHT 2013 — ✅ found** (official open archive, [glihtdata.gsfc.nasa.gov](https://glihtdata.gsfc.nasa.gov/files/G-LiHT/)). 10 Yucatán-peninsula flights from April–May 2013 (Norte, North 2, Centro, South, Out of the Yuc). Each has a ready **1 m bare-earth DTM** (93–519 MB each, **~2.9 GB total**), plus canopy height, slope and point clouds. Downloaded: flight footprints (KMZ), metadata PDFs, and the **DTMs of the 10 flights** (Yucatán Norte NFI in `dtm_sample/`, the other 9 in `dtm/`; all archives pass an integrity check). Bonus: the same archive has 2013 flights over **Chihuahua and Hermosillo** you could use for a north-of-Mexico terrain contrast. A ground-filtered LAZ copy is also at [Scholar@UC](https://scholar.uc.edu/collections/w9505239h) (public domain).
- **Puuc survey (Ringle et al., PLOS ONE 2021) — ⚠️ paper only.** The paper (CC BY) is downloaded, with hillshade, landform, aguada and chultún figures. The raw LiDAR is **under embargo** "due to considerations concerning cultural heritage preservation"; access is by request to the authors. The OpenTopography record (DOI 10.5069/G99021WJ) is not public.

## 3. Water at home (self-produced) — `03_self_produced/` 🧪 SIMULATED

> **These files are simulated, not collected.** Every row has `simulado = SI` and every file name starts with `SIMULADO_`. Replace them with real responses, measurements and a real interview when you have them, or present them explicitly as simulated. Your earlier project's README noted that the instructor required real data ("no simulated data"), so check with them before submitting these as a source.

- `SIMULADO_encuesta_hogares.csv`: **260 Google-Forms-style responses** (160 Mérida by zone + 100 relatives in 10 other states), answering the 15 questions in `instrumentos_borrador.md`.
- `SIMULADO_pruebas_agua.csv`: **24 readings**, tap water in 5 Mérida zones and 3 bottled/garrafón samples, 3 replicates each (TDS meter, hardness and nitrate strips, with strip readings rounded to real strip pads).
- `SIMULADO_entrevista_experto.md`: **interview with a fictional expert**. Every fact in the answers comes from a real source in this folder and is cited; opinions are marked as the character's. It is not attributed to UADY, CICY or JAPAY.
- `generar_datos_simulados.py` + `SIMULADO_supuestos.json`: the generator (seed 2026, re-run to reproduce) and every input it used.

**What is real vs assumed:**

| Calibrated to real data | Assumed (listed in `SIMULADO_supuestos.json`) |
|---|---|
| Piped water inside/yard/none, sewer vs septic, rooftop tank, cistern, people per home (INEGI Census 2020, by state; Mérida from ITER) | Drinking-water source shares (garrafón, filter, boiled, tap) |
| Monthly bill scaled by each capital's real tariff (SINA 2024) | Garrafón price and weekly use, domestic tariff = 55% of commercial |
| Outage frequency driven by each region's real water stress (SINA 2023) | Exact outage probabilities and durations |
| Tap TDS, hardness and nitrate around the real medians of 20 Mérida wells (RENAMECA 2012–2025) | Differences between Mérida zones (random only, no real pattern), bottled-water values |

`instrumentos_borrador.md` still has the original questionnaire, test protocol and interview guide.

## 4. Drought and scarcity (web scraping) — `04_web_scraping/`

- **SMN drought monitor — ✅** `MunicipiosSequia.xlsx`: drought category for **2,478 municipalities, every 15 days, 31 Jan 2003 → 15 Oct 2026** (437 dates).
- **CONAGUA SINA — ✅ partly.** SINA moved to [sinav30.conagua.gob.mx:8080](https://sinav30.conagua.gob.mx:8080/) (the old address redirects to gob.mx). It blocks scripts, so I read it through the browser:
  - `SINA_coverage_by_state_2010_2015_2020.csv`: piped water and drainage coverage by state (my state totals reproduce SINA's national 96.11% for 2020). Note that SINA's "drainage" counts septic tanks as drainage.
  - `SINA_grado_presion_by_RHA_2023.csv`: water stress by hydrological region. **Península de Yucatán 28.75% (medium)** vs Valle de México 128.7% (very high), Baja California 89.7%, Cuencas Centrales del Norte 84.9%.
  - `SINA_usos_agua_nacional_REPDA_2023.csv`: national water use by sector.
  - `SINA_tarifas_capitales_2024.csv`: **Mérida has the lowest commercial tariff of all state capitals, 7.97 $/m³** (Monterrey 45.04, CDMX 57.14, Mexicali 96.25).
  - `SINA_PTAR_municipales_por_RHA_2023.csv`: wastewater plants by hydrological region (2,928 nationally; Península de Yucatán 94 plants, 2,725 l/s treated). The "municipal" label is inferred from SINA's menu.
  - `SINA_PTAR_industriales_por_estado_2023.csv` and `..._por_tipo_tratamiento_2023.csv`: **industrial** wastewater plants (SINA labels them "Plantas de Tratamiento de Aguas Residuales Industriales"); don't mix them with municipal plants.
  - Groundwater concessions by state and by Yucatán municipality are in section 5.
- **JAPAY and local news — ⚠️**
  - `japay_noticias.csv`: all **392 JAPAY news articles (2007–2026)** with date, title and keyword flags (outage, maintenance, quality, drought, sewer). These are mostly press releases; actual outage notices seem to go out on social media.
  - `diario_yucatan_etiqueta_japay.csv`: 43 articles tagged JAPAY in Diario de Yucatán (Sep 2024 – Oct 2026). Older ones sit behind a "load more" button.
  - La Jornada Maya's site search doesn't return real results to scripts. A longer news history needs a dedicated scraper.

## 5. Who extracts and monitors — `05_public_replacement/`

Following the instruction to switch to public data when the government requests haven't been answered, each request was replaced with public data on the same subtopic. The unsent drafts stay in `05_transparency_requests/` in case you still want to file them.

**A. CONAGUA: extraction and monitoring of aquifer 3105** — `conagua_extraccion_monitoreo/`

| Request asked for | Public replacement |
|---|---|
| Extraction volumes by use | `SINA_REPDA_subterraneo_por_municipio_Yucatan_2023.csv`: groundwater concessions (hm³/yr) by use for all 106 municipalities. **Total 2,465 hm³**: "usos múltiples" 1,301, agriculture 789, public supply 271 (Mérida 159), industry 42, livestock 26. Plus `..._por_estado_2023.csv` for all states. |
| Water-level monitoring | `piezometria_acuifero_3105_peninsula_1996_2025.csv`: CONAGUA's monitoring wells in Yucatán (166), Campeche (210) and Quintana Roo (129), with depth to water each year 1996–2025. `piezometria_resumen_por_estado.csv`: median depth by state. **Yucatán ≈ 4.2 m** (and no drop since 2010) vs CDMX 78 m (+10 m since 2010) and Aguascalientes 130 m (+30 m). Only 7 Yucatán wells have a 2025 reading. |
| Salinity monitoring | `renameca_calidad_subterranea_yucatan_2012_2025.csv`: 121 CONAGUA quality sites in Yucatán with conductivity and dissolved solids (salinity proxies), plus nitrates, coliforms, hardness. Conductivity median 1,210, max 5,810. |
| Aquifer availability | Already in section 8 (2,059.6 hm³/yr available). |

**B. JAPAY: wells, sewer coverage, wastewater treatment in Mérida** — `japay_operador/`

- `cngmd2025_operador_agua_yucatan_y_ciudades.csv` (from INEGI CNGMD 2025, reported by each municipality for 2024): all 106 Yucatán municipalities plus 11 large cities elsewhere. **Mérida: water network covers 100% of the population but the sewer network only 21%**; 405,606 water connections vs 82,450 sewer connections; 304 water-abstraction works (208 named as wells); 4 drinking-water plants; 37 municipal wastewater plants. Monterrey, Guadalajara, León, Querétaro and Puebla report 98–100% sewer coverage.
- Not found: IMTA's PIGOO operator indicators (`pigoo.gob.mx` no longer exists).

**C. SDS / Servicios de Salud: cenote quality, pig farms, permits** — `sds_salud_granjas_cenotes/`

- **Pig farms (official):** `SEMARNAT_2023_Dictamen_Diagnostico_Ambiental_Actividad_Porcicola_Yucatan.pdf`, the federal environmental diagnosis of pig farming in Yucatán. It identified **507 possible farm sites**: 139 backyard, 208 with 1–2 sheds, 89 with 3–7, 48 with 8–20 and 23 with more than 20.
- **Pigs by municipality (official):** `cerdos_por_municipio_yucatan_CA2022.csv` and `cerdos_por_entidad_CA2022.csv` from INEGI's 2022 Agricultural Census. **Yucatán has 1.6 million pigs, 3rd in Mexico** after Jalisco and Sonora. Largest herds: Mérida, Maxcanú, Opichén, Muna, Abalá.
- **Health monitoring (official):** `SINA_eficiencia_cloracion_por_estado_2010_2023.csv`, chlorination efficiency of drinking water by state. Yucatán fell from 86.2% (2010) to 83.1% (2023); Nuevo León 99.0%.
- **Cenote water quality:** `greenpeace_2026/` — Greenpeace México's October 2026 report (Spanish + English) with lab results from 17 wells and cenotes near pig farms (fecal indicators; some nitrate above the 48.7 mg/L NO₃ limit). This is **civil-society data, not government data**. `proyecto_saneamiento_y_manejo_especial_de_cenotes.pdf` is SDS's own cenote sanitation project.
- Still not public: the SDS cenote inventory and the individual permit/inspection records (MIA, PROFEPA).

## 6. Mérida geoportal — `06_geoportal_merida/` (catalog + public substitutes)

The CAPTCHA is solved and the geoportal opens, but **it is view-only for anonymous visitors**: the tools are coordinates, measuring, routes, Street View, markers and Print. There is no download or export, and each layer's menu only shows "Propiedades".

- `geoportal_merida_catalogo_capas.csv`: **the full catalog of 284 layers** with category, exact name, description, geometry type, server layer name and coordinate system. This confirms the exact layer names.
- Layers that match your three sources:

| Your source | Geoportal layers (exact names) |
|---|---|
| Reserva Cuxtal | DESARROLLO SUSTENTABLE › "Zona Sujeta a Conservación Ecológica Reserva Cuxtal" (updated 2022) · PMDU 2017 › "Polígono de la declaratoria de la Zona Sujeta a Conservación Ecológica Reserva Cuxtal en 1993" · PMDU 2017 › "Área de transición Mérida - Cuxtal" (+ "de baja densidad") |
| Flood-risk zones | **No flood-zone layer exists.** Closest in ATLAS DE RIESGOS: "Precipitación máxima anual 2017", "Precipitación total anual 2017 / RCP", "Geomorfología", "Geología"; plus OBRAS PÚBLICAS › "Drenaje Pluvial." (storm-drain points) |
| Land use, urban growth, cenotes | PMDU 2017 › "Área urbanizada…", "Área urbanizable en centros de población", "Límite urbano 2040", "Zonas primarias", "Áreas con densidad programada", "Zona de preservación ecológica (SEMARNAT)", "CENOTES" · CARTA SÍNTESIS 2012 › "Zonas de reserva para crecimiento", "Áreas urbanizables", "Cenotes" · ATLAS DE RIESGOS › "Vegetación y uso de suelo 2017" |

- **Not downloaded from the geoportal:** the shapes themselves. Pulling them straight from its map server was blocked as getting around the site's access controls, so the layers were replaced with the public substitutes below.

### Public substitutes — `06_geoportal_merida/sustitutos_publicos/`

| Your source | Substitute | Notes |
|---|---|---|
| Reserva Cuxtal | `reserva_cuxtal_osm.geojson`: boundary of the "Zona Sujeta a Conservación Ecológica Reserva Cuxtal" from **OpenStreetMap** (way 1233917555, license ODbL; credit "© OpenStreetMap contributors") | 223 points, ≈11,066 ha by my calculation. Community-mapped, not the official decree polygon. |
| Flood-risk zones | `CENAPRED_IPI_2015.zip` (shapefile) + `cenapred_peligro_inundacion_municipal_2015.csv`: **CENAPRED flood-hazard index for all 2,457 municipalities** | **Mérida: "Medio"**, 44.9 km² flood-prone (5.1% of the municipality), vulnerability "Media". For comparison: Guadalajara and Iztapalapa "Muy alto", Chihuahua and Cancún "Alto", Monterrey "Medio". In Yucatán: 10 municipalities "Muy alto", 38 "Alto". It rates whole municipalities, not neighborhoods. A UADY study mapping risk zones inside Mérida exists, but the journal site currently redirects to the UADY homepage. |
| Land use and urban growth | `uso_suelo_inegi/`: **INEGI municipal land-use map of Mérida (1:50,000)** as GeoTIFF + geoPDF, plus the **F16-10 "Mérida" land-use maps for series I (1968–86), II (1993), III (2002–05), IV (2007–10), V (2011)** as shapefiles, and series VI as PDF | Comparing the urban class across series I→V shows how the city grew. The municipal map is an image (raster), not vectors. |
| Cenotes in the municipality | `cenotes_inegi_toponimia_y_osm.csv`: **112 named cenotes** from INEGI's official hydrography (81 in Yucatán state) + 8 cenotes/sinkholes from OpenStreetMap around Mérida | Only **named** cenotes; far fewer than the thousands that exist. The full SDS inventory is still not public. |

## 7. Yucatán state (SIEGY) — `07_SIEGY/`

SIEGY now lives at [datos.yucatan.gob.mx](https://datos.yucatan.gob.mx/).

- **State Development Plan (PED 2024–2030) indicators — ⚠️** They are in a public Power BI dashboard with an Excel/XML export button per indicator. The embed doesn't accept automated clicks, so the water/environment indicators need a manual export.
- **Statistical bulletins by municipality — ❌ not as described.** SIEGY only has 16 thematic bulletins (2025–2026), none by municipality. Downloaded the relevant ones: **Boletín 2026-3 "Día Mundial del Agua"** and 2025-10 (climate change). For Mérida vs the interior, the INEGI and SINA municipal data (sections 4 and 9) work better.
- **Ring of Cenotes — ✅ (from SDS).** Official KMZ boundary, the 2013 decree and the 2025 fact sheet: **219,207.83 ha**, decreed 19 Oct 2013, ~99,989 inhabitants. Note: Decreto 88/2025 modified the reserve (54 municipalities); confirm whether the KMZ already reflects that change.

## 8. Water quality and aquifer health (datos.gob.mx) — `08_datos_gob_mx/`

The new datos.gob.mx has only 16 CONAGUA datasets, and its files block scripts, so I downloaded them through the browser.

- **RENAMECA groundwater quality — ✅ indicators.** From CONAGUA's [Indicadores de calidad del agua](https://www.gob.mx/conagua/es/articulos/indicadores-de-calidad-del-agua) page (gob.mx, not datos.gob.mx): groundwater sites with coordinates and indicator classes, for **2025** and for **2012–2025**, plus the methodology PDF. Also downloaded once CONAGUA's file server came back: the raw lab results for all groundwater sites (`Subterraneo_resultados_RENAMECA.xlsb`, Excel binary format) and for Yucatán (`RESULTADOS-YUCATAN.xlsx`), plus the KMZ maps for 2025 and 2012–2025.
- **Aquifer availability — ✅** `disponibilidad_agua_subterranea.zip`: shapefile of all **653 aquifers** (Nov 2023 edition). Aquifer **3105 Península de Yucatán: available 2,059.6 hm³/yr**, recharge 14,931.8, concessioned 4,982.8 hm³/yr. Also `red_piezometrica.zip` (2025 groundwater-level network).
- **Treatment-plant inventory — ⚠️ not on datos.gob.mx.** The latest edition I found online is the **December 2020** PDF (`Inventario_2020.pdf`). Newer numbers: per municipality in CNGMD 2025 (section 9) and per hydrological region for 2023 in SINA (`04_web_scraping/conagua_sina/SINA_PTAR_municipales_por_RHA_2023.csv`).

## 9. Water and sanitation in homes (INEGI) — `09_INEGI/`

- **Census 2020 — ✅** National ITER (all localities and municipal totals), housing tables for Mexico and for Yucatán. Extracted `censo2020_drenaje_lugar_desalojo_por_entidad.csv`. **Where household drainage goes:**

  | | Public sewer | Septic tank | No drainage |
  |---|---|---|---|
  | **Yucatán** | **13.1%** | **78.8%** | 7.6% |
  | Campeche | 9.4% | 84.8% | 5.1% |
  | Quintana Roo | 73.8% | 22.9% | 1.9% |
  | Nuevo León | 95.0% | 3.7% | 0.9% |
  | Ciudad de México | 94.2% | 5.1% | 0.2% |
  | Chihuahua | 88.7% | 7.7% | 3.2% |
  | **Mexico** | **78.1%** | **16.2%** | 4.3% |

  The basic tables only give this split by state. A per-municipality split (Mérida vs interior) needs the extended-questionnaire data; not downloaded yet. Meanwhile, CNGMD 2025 gives each municipality's sewer-network coverage (Mérida 21%), see section 5B.
- **CNGMD 2025, water and sanitation module — ✅** All 10 open datasets (reference year 2024): public water service, water abstraction (wells), other water sources, drinking-water plants, administration, drainage and sewer, wastewater treatment, untreated wastewater, programs, public participation. Plus the questionnaire PDF.
- **Hydrography — ✅** INEGI river network 1:50,000 (ed. 2.0) for hydrological regions **RH32 Yucatán Norte**, RH31 (Campeche) and RH33 (Quintana Roo).

## 10. Extra public data — `10_extra_public_data/`

- `denue_yucatan/denue_31_yucatan_csv.zip`: INEGI's business directory (DENUE) for Yucatán, every georeferenced business. It does **not** include livestock farms (INEGI leaves farming out of DENUE), so it can't replace the pig-farm permits.
- `denue_yucatan/denue_purificadoras_embotelladoras_agua_yucatan.csv`: **462 water purification and bottling businesses** in Yucatán (SCIAN 312112; 123 in Mérida), with coordinates. A real public indicator to pair with the "garrafón" question in section 3. The file also has 8 soft-drink makers (SCIAN 312111); filter by `codigo_act` if you only want purifiers.

---

## Files not stored in this repository

GitHub rejects files over 100 MB, so these are listed in `manifest.csv` (with URL and checksum) but not committed. Download them into the right folders with:

```bash
python scripts/descargar_archivos_grandes.py
```

| File(s) | Size | Why it's not in git |
|---|---|---|
| `01_AR_cenotes/hells_bells/Mesh_seg_bright.ply` and `.nxz` | 1.1 GB + 261 MB | Over 100 MB |
| `02_LiDAR/nasa_gliht_2013/dtm/` and `dtm_sample/` (10 terrain models) | 93–519 MB each, ~2.9 GB total | Over 100 MB |
| `05_public_replacement/sds_salud_granjas_cenotes/greenpeace_2026/` (2 PDFs) | 72 MB | Third-party report, not openly licensed; downloaded from Greenpeace's site |

Pass part of a path to get only some files, e.g. `python scripts/descargar_archivos_grandes.py hells_bells`.

## Scripts

- `scripts/descargar_archivos_grandes.py`: downloads the files above (standard library only).
- `scripts/scraper_noticias_japay.py`: the JAPAY news scraper used for `04_web_scraping/japay_news/` (one request every 0.5 s).
- `03_self_produced/generar_datos_simulados.py`: regenerates the simulated survey and water tests (seed 2026).

## Licenses and credits

- **OpenStreetMap** data (`reserva_cuxtal_osm.geojson`, part of `cenotes_inegi_toponimia_y_osm.csv`): © OpenStreetMap contributors, ODbL 1.0.
- **Hells Bells 3D model**: Heidelberg University, heidICON, DOI 10.11588/heidicon/1264341, CC BY-SA 4.0.
- **Hells Bells geochemistry**: Schorndorf et al. (2022), PANGAEA, DOI 10.1594/PANGAEA.945784, CC BY 4.0.
- **Puuc LiDAR paper**: Ringle et al. (2021), PLOS ONE 16(4): e0249314, CC BY 4.0.
- **NASA G-LiHT**: NASA Goddard, public data.
- **INEGI, CONAGUA, SMN, CENAPRED, SEMARNAT, SIEGY, SDS Yucatán**: Mexican government open data / publications; cite the agency as the source.
- **Greenpeace México (2026)** report: © Greenpeace, not redistributed here.
- Files starting with `SIMULADO_` are **simulated data**, not real survey responses or measurements.
