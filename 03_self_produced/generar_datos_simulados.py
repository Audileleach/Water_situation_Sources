"""Generate SIMULATED data for the self-produced sources (survey + water tests).

THIS IS NOT REAL FIELD DATA. It is synthetic data, calibrated where possible to
real public statistics, so the team can build the pipeline and dashboards
before (or instead of) running the real survey and tests. Every row carries
simulado = "SI". Replace these files with the real responses when available.

Run:  python generar_datos_simulados.py   (Python 3.9+, no extra packages)
Same seed -> same output.
"""
import csv
import json
import math
import random
from pathlib import Path

SEED = 2026
HERE = Path(__file__).parent
rng = random.Random(SEED)

# ---------------------------------------------------------------------------
# REAL calibration values (sources in comments; files are in this repository)
# ---------------------------------------------------------------------------
# INEGI Censo 2020: piped water inside / only in yard / none, drainage
# destination (sewer / septic / none), rooftop tank, cistern, people per home.
# From 09_INEGI/censo2020_tabulados_vivienda (sheets 12 and 14) and ITER.
CENSUS = {
    "Ciudad de México": dict(dentro=.905, patio=.083, no=.011, red=.942, fosa=.051, sin=.006, tinaco=.846, cisterna=.605, ocup=3.32),
    "México":           dict(dentro=.751, patio=.222, no=.026, red=.865, fosa=.089, sin=.044, tinaco=.779, cisterna=.387, ocup=3.71),
    "Nuevo León":       dict(dentro=.971, patio=.019, no=.007, red=.949, fosa=.037, sin=.009, tinaco=.143, cisterna=.026, ocup=3.49),
    "Jalisco":          dict(dentro=.946, patio=.041, no=.007, red=.934, fosa=.046, sin=.013, tinaco=.772, cisterna=.388, ocup=3.56),
    "Chihuahua":        dict(dentro=.936, patio=.047, no=.015, red=.887, fosa=.076, sin=.034, tinaco=.356, cisterna=.037, ocup=3.25),
    "Quintana Roo":     dict(dentro=.855, patio=.117, no=.016, red=.738, fosa=.229, sin=.021, tinaco=.906, cisterna=.250, ocup=3.22),
    "Campeche":         dict(dentro=.647, patio=.309, no=.040, red=.094, fosa=.848, sin=.053, tinaco=.724, cisterna=.203, ocup=3.55),
    "Puebla":           dict(dentro=.600, patio=.354, no=.044, red=.813, fosa=.120, sin=.066, tinaco=.728, cisterna=.424, ocup=3.83),
    "Guanajuato":       dict(dentro=.815, patio=.155, no=.027, red=.827, fosa=.128, sin=.042, tinaco=.807, cisterna=.286, ocup=3.87),
    "Sonora":           dict(dentro=.892, patio=.092, no=.014, red=.859, fosa=.091, sin=.048, tinaco=.440, cisterna=.061, ocup=3.34),
    # Mérida municipality: piped water / tank / cistern / occupants from ITER;
    # drainage destination only exists by state, so Yucatán state shares are used.
    "Yucatán (Mérida)": dict(dentro=.781, patio=.205, no=.012, red=.130, fosa=.788, sin=.080, tinaco=.869, cisterna=.223, ocup=3.27),
}
# CONAGUA SINA 2024: commercial water tariff ($/m3) in each state capital.
# Campeche has no value in SINA -> ASSUMED 20.
TARIFF = {"Ciudad de México": 57.14, "México": 49.01, "Nuevo León": 45.04, "Jalisco": 36.87, "Chihuahua": 27.21,
          "Quintana Roo": 54.57, "Campeche": 20.0, "Puebla": 35.10, "Guanajuato": 46.11, "Sonora": 64.11,
          "Yucatán (Mérida)": 7.97}
# CONAGUA SINA 2023: water stress (grado de presión, %) of each state's main hydrological region.
STRESS = {"Ciudad de México": 128.71, "México": 128.71, "Nuevo León": 73.86, "Jalisco": 45.47, "Chihuahua": 73.86,
          "Quintana Roo": 28.75, "Campeche": 28.75, "Puebla": 46.93, "Guanajuato": 45.47, "Sonora": 82.66,
          "Yucatán (Mérida)": 28.75}
# CONAGUA RENAMECA 2012-2025, 20 groundwater sites in Mérida (raw well water):
# SDT median 763.5 mg/L; conductivity median 1283 uS/cm (p10 943, p90 2419);
# hardness median 470 mg/L CaCO3 (p10 367, p90 527); N-NO3 median 4.2 mg/L (p10 2.5, p90 8.6).
RENAMECA_MERIDA = dict(cond_median=1283, hard_median=470.1, hard_sd=60, nno3_median=4.20, nno3_p90=8.55)

# ---------------------------------------------------------------------------
# ASSUMPTIONS (not from real data; change them if you find better sources)
# ---------------------------------------------------------------------------
ASSUMPTIONS = {
    "sample": "160 Mérida households + 100 relatives in 10 other states (Google Forms style).",
    "merida_zones": "Weights norte .30, sur .20, oriente .17, poniente .18, centro .15. NO systematic difference between zones is simulated: any zone gap in this data is random noise.",
    "drinking_source": "Peninsula (Mérida, Campeche, Q. Roo): garrafón .78, filtro .10, hervida .04, llave .05, otro .03. Other states: garrafón .62, filtro .16, hervida .08, llave .12, otro .02.",
    "garrafones_per_week": "Only for garrafón users: Poisson with mean 0.55 x people in the home (min 1).",
    "garrafon_price": "Peninsula 32 MXN per 20 L refill, other states 38 MXN (assumed refill-station prices).",
    "consumption": "Water use per home = 4.2 m3 per person per month x lognormal noise (sd 0.35).",
    "bill": "Monthly bill = consumption x (0.55 x commercial tariff of the state capital) + 35 MXN fixed charge, x lognormal noise (sd 0.25). Domestic tariff assumed 55% of the commercial one.",
    "outages": "Probabilities (nunca, 1-2 veces, cada mes, cada semana) depend on the regional water stress: <35% -> (.45,.38,.12,.05); 35-80% -> (.28,.40,.21,.11); >80% -> (.15,.33,.30,.22).",
    "outage_duration": "(horas, 1 día, varios días) = (.62,.26,.12).",
    "septic_detail": "Homes with septic drainage split into fosa séptica .68, pozo/sumidero .17, biodigestor .10, no sé .05. Peninsula homes 'no sé' adds .04 to sewer answers (people unsure).",
    "septic_emptying": "(nunca, cada 1-2 años, más de 2 años, no sé) = (.30,.18,.27,.25).",
    "trust_tap": "Trust in tap water 1-5: peninsula mean 1.9, other states 2.4 (normal sd 1, rounded, clipped).",
    "scale_marks": "Probability of noticing scale (sarro): peninsula .86, Nuevo León/Chihuahua/Sonora .62, others .48.",
    "water_tests": "5 Mérida zones x 3 tap replicates + 3 bottled samples x 3 replicates. Meter TDS = 0.5 x conductivity (typical meter factor). Zone means drawn at random around the RENAMECA median (sd 90 ppm). Strip readings are rounded to the nearest strip pad. Bottled water: TDS 15-150 ppm, hardness 0-50, nitrate 0-10 (assumed reverse-osmosis water).",
}

PENINSULA = {"Yucatán (Mérida)", "Campeche", "Quintana Roo"}
OTHER_SAMPLE = {"Ciudad de México": 18, "México": 14, "Nuevo León": 14, "Jalisco": 10, "Chihuahua": 8,
                "Quintana Roo": 10, "Campeche": 6, "Puebla": 7, "Guanajuato": 7, "Sonora": 6}
MUNI = {"Ciudad de México": ["Iztapalapa", "Coyoacán", "Gustavo A. Madero", "Tlalpan", "Benito Juárez"],
        "México": ["Ecatepec", "Nezahualcóyotl", "Toluca", "Naucalpan"], "Nuevo León": ["Monterrey", "Guadalupe", "Apodaca", "San Nicolás de los Garza"],
        "Jalisco": ["Guadalajara", "Zapopan", "Tlaquepaque"], "Chihuahua": ["Chihuahua", "Juárez"],
        "Quintana Roo": ["Benito Juárez (Cancún)", "Othón P. Blanco", "Solidaridad"], "Campeche": ["Campeche", "Carmen"],
        "Puebla": ["Puebla", "San Andrés Cholula"], "Guanajuato": ["León", "Irapuato", "Celaya"], "Sonora": ["Hermosillo", "Cajeme"]}
ZONES = [("Norte", .30), ("Sur", .20), ("Oriente", .17), ("Poniente", .18), ("Centro", .15)]


def pick(options):
    """options: list of (value, weight)"""
    r, acc = rng.random() * sum(w for _, w in options), 0.0
    for v, w in options:
        acc += w
        if r <= acc:
            return v
    return options[-1][0]


def poisson(lam):
    L, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= L:
            return k
        k += 1


def bin_value(x, edges, labels):
    for e, lab in zip(edges, labels):
        if x < e:
            return lab
    return labels[-1]


def household(state, idx):
    c = CENSUS[state]
    pen = state in PENINSULA
    people = max(1, min(9, round(rng.gauss(c["ocup"], 1.3))))
    agua = pick([("Sí, dentro de la vivienda", c["dentro"]), ("Solo en el patio o terreno", c["patio"]), ("No", c["no"])])
    source = pick([("Garrafón", .78), ("Filtro o purificador en casa", .10), ("Agua hervida", .04), ("Llave sin tratar", .05), ("Otro", .03)] if pen else
                  [("Garrafón", .62), ("Filtro o purificador en casa", .16), ("Agua hervida", .08), ("Llave sin tratar", .12), ("Otro", .02)])
    garr = max(1, poisson(0.55 * people)) if source == "Garrafón" else poisson(0.15)
    m3 = 4.2 * people * math.exp(rng.gauss(0, .35))
    bill = (m3 * 0.55 * TARIFF[state] + 35) * math.exp(rng.gauss(0, .25)) if agua != "No" else 0
    spend = garr * 4.3 * (32 if pen else 38)
    s = STRESS[state]
    probs = (.45, .38, .12, .05) if s < 35 else (.28, .40, .21, .11) if s <= 80 else (.15, .33, .30, .22)
    outage = pick(list(zip(["Nunca", "1–2 veces", "Cada mes", "Cada semana"], probs)))
    duration = "" if outage == "Nunca" else pick([("Horas", .62), ("1 día", .26), ("Varios días", .12)])
    tinaco, cisterna = rng.random() < c["tinaco"], rng.random() < c["cisterna"]
    storage = "Ambos" if tinaco and cisterna else "Tinaco" if tinaco else "Cisterna" if cisterna else "Ninguno"
    d = pick([("red", c["red"]), ("fosa", c["fosa"]), ("sin", c["sin"])])
    if d == "red":
        drain = "No sé" if pen and rng.random() < .04 else "Red de drenaje público"
    elif d == "fosa":
        drain = pick([("Fosa séptica", .68), ("Pozo o sumidero", .17), ("Biodigestor", .10), ("No sé", .05)])
    else:
        drain = pick([("Pozo o sumidero", .6), ("No sé", .4)])
    emptying = pick([("Nunca", .30), ("Cada 1–2 años", .18), ("Más de 2 años", .27), ("No sé", .25)]) if drain in ("Fosa séptica", "Biodigestor") else ""
    trust = max(1, min(5, round(rng.gauss(1.9 if pen else 2.4, 1))))
    p_scale = .86 if pen else .62 if state in ("Nuevo León", "Chihuahua", "Sonora") else .48
    if state == "Yucatán (Mérida)":
        estado, municipio, zona = "Yucatán", "Mérida", pick(ZONES)
    else:
        estado, municipio, zona = state, rng.choice(MUNI[state]), ""
    return {
        "simulado": "SI", "id_respuesta": f"SIM-{idx:04d}", "grupo": "Mérida" if state == "Yucatán (Mérida)" else "Comparación",
        "p01_estado": estado, "p02_municipio": municipio, "p02_zona_merida": zona, "p03_personas": people,
        "p04_agua_entubada": agua, "p05_fuente_agua_beber": source, "p06_garrafones_semana": min(garr, 4) if garr < 4 else "4 o más",
        "p07_pago_agua_mes": bin_value(bill, [1, 100, 200, 400, 700], ["$0 / no paga", "Menos de $100", "$100–199", "$200–399", "$400–699", "$700 o más"]),
        "p08_gasto_garrafon_mes": bin_value(spend, [1, 150, 300, 500], ["$0", "$1–149", "$150–299", "$300–499", "$500 o más"]),
        "p09_sin_agua_12m": outage, "p10_duracion": duration, "p11_almacenamiento": storage, "p12_drenaje": drain,
        "p13_vaciado_fosa": emptying, "p14_confianza_llave_1a5": trust, "p15_sarro": "Sí" if rng.random() < p_scale else "No",
    }


def snap(value, pads):
    return min(pads, key=lambda p: abs(p - value))


def water_tests():
    rows = []
    cond = RENAMECA_MERIDA["cond_median"]
    for zona, _ in ZONES:
        zone_tds = rng.gauss(0.5 * cond, 90)
        zone_hard = rng.gauss(RENAMECA_MERIDA["hard_median"], RENAMECA_MERIDA["hard_sd"])
        zone_nno3 = math.exp(rng.gauss(math.log(RENAMECA_MERIDA["nno3_median"]), .4))
        for rep in (1, 2, 3):
            rows.append(test_row(f"Llave - zona {zona}", "Llave (red JAPAY)", zona, rep,
                                 zone_tds * rng.gauss(1, .03), zone_hard, zone_nno3 * 4.43, rng.uniform(27.5, 31)))
    for marca in ("Garrafón purificadora local", "Garrafón marca comercial A", "Garrafón marca comercial B"):
        tds, hard, no3 = rng.uniform(15, 150), rng.uniform(0, 50), rng.uniform(0, 10)
        for rep in (1, 2, 3):
            rows.append(test_row(marca, "Embotellada / garrafón", "", rep, tds * rng.gauss(1, .03), hard, no3, rng.uniform(24, 27)))
    return rows


def test_row(muestra, tipo, zona, rep, tds, hard, no3, temp):
    hard_pads, no3_pads = [0, 25, 50, 120, 250, 425], [0, 10, 25, 50, 100, 250, 500]
    h = snap(hard, hard_pads)
    return {"simulado": "SI", "muestra": muestra, "tipo": tipo, "zona_merida": zona, "replica": rep,
            "tds_ppm_medidor": round(max(tds, 1)), "temperatura_c": round(temp, 1),
            "dureza_tira_ppm": f"{h}+" if h == 425 and hard > 425 else h,
            "nitratos_tira_ppm_NO3": snap(no3, no3_pads),
            "valor_simulado_dureza_mg_L": round(hard, 1), "valor_simulado_nitrato_mg_L_NO3": round(no3, 1)}


def write(path, rows):
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print("wrote", path.name, len(rows), "rows")


def main():
    rows, i = [], 1
    for _ in range(160):
        rows.append(household("Yucatán (Mérida)", i)); i += 1
    for state, n in OTHER_SAMPLE.items():
        for _ in range(n):
            rows.append(household(state, i)); i += 1
    rng.shuffle(rows)
    write(HERE / "SIMULADO_encuesta_hogares.csv", rows)
    write(HERE / "SIMULADO_pruebas_agua.csv", water_tests())
    (HERE / "SIMULADO_supuestos.json").write_text(json.dumps(
        {"seed": SEED, "warning": "SIMULATED DATA - not real survey responses or measurements",
         "real_calibration": {"census": CENSUS, "tariff_commercial_mxn_m3": TARIFF, "water_stress_pct": STRESS, "renameca_merida": RENAMECA_MERIDA},
         "assumptions": ASSUMPTIONS}, ensure_ascii=False, indent=2), encoding="utf-8")
    print("wrote SIMULADO_supuestos.json")


if __name__ == "__main__":
    main()
