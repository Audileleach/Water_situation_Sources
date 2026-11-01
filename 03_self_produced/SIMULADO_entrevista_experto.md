# ⚠️ ENTREVISTA SIMULADA — NO ES UNA ENTREVISTA REAL

- **Persona entrevistada:** personaje ficticio ("Especialista simulado en hidrogeología"). **No representa** a la UADY, al CICY, a la JAPAY ni a ninguna persona real.
- **Cómo se hizo:** cada respuesta se construyó solo con datos públicos reales descargados en esta carpeta `sources/`. La fuente va entre corchetes al final de cada dato. Las frases de opinión son del personaje simulado.
- **Uso:** sirve como guion de prueba y para montar la infraestructura del proyecto. Si la presentan, debe decir que es **simulada**. Lo ideal es reemplazarla por una entrevista real.

---

**1. ¿Qué hace diferente al agua de Yucatán comparada con el resto de México?**

Que casi no hay agua en la superficie. En la red hidrográfica de INEGI para la cuenca Yucatán (RH32B), 3,369 de 3,381 tramos de corriente son intermitentes, solo 12 son perennes, y 418 líneas de drenaje terminan infiltrándose en "suelos permeables" [09_INEGI/hidrografia_red_50k, RH32]. Toda el agua que usamos es subterránea, de un solo acuífero enorme, el 3105 "Península de Yucatán", de 124,409 km² [08_datos_gob_mx, disponibilidad_agua_subterranea]. Y está muy cerca de la superficie: en los pozos de monitoreo de Yucatán el agua está a unos 4 m de profundidad, mientras que en la Ciudad de México está a unos 78 m [05_public_replacement, piezometria_resumen_por_estado; pocos pozos de Yucatán tienen dato 2025].

**2. ¿Hay suficiente agua?**

En cantidad, sí, comparado con el norte y el centro. El acuífero recibe una recarga de 14,931.8 hm³ al año y todavía tiene 2,059.6 hm³ disponibles [disponibilidad_agua_subterranea, CONAGUA 2023]. El grado de presión de la región Península de Yucatán es de 28.75% ("medio"), contra 128.7% en el Valle de México [04_web_scraping/conagua_sina, grado de presión 2023]. El problema de aquí no es tanto la cantidad: es la calidad.

**3. ¿Qué tan vulnerable es el acuífero a la contaminación?**

Mucho, porque el suelo es roca caliza fracturada: lo que se tira en la superficie llega rápido al agua. Además, el 78.8% de las viviendas de Yucatán desaloja su drenaje en fosa o tanque séptico y solo el 13.1% en la red pública; a nivel nacional es al revés, 78.1% red pública [09_INEGI, censo2020_drenaje_lugar_desalojo_por_entidad]. En Mérida, el municipio reporta que su red de drenaje cubre al 21% de la población, cuando en Monterrey o Guadalajara es de 98 a 100% [05_public_replacement/japay_operador, CNGMD 2025].

**4. ¿Hay nitratos o bacterias en el agua de Mérida?**

En los 20 sitios de monitoreo de CONAGUA en Mérida, el nitrógeno de nitratos tiene una mediana de 4.2 mg/L, por debajo del límite de 11 mg/L (como N). Pero en el agua cruda de pozo sí aparecen coliformes fecales, con una mediana de 14.7 NMP/100 mL en 17 sitios [RENAMECA 2012–2025, renameca_calidad_subterranea_yucatan]. Por eso el agua de la red se tiene que clorar. Y la eficiencia de cloración reportada para Yucatán bajó de 86.2% en 2010 a 83.1% en 2023 [SINA, eficiencia de cloración por estado].

**5. ¿Qué papel tienen las granjas porcícolas?**

Yucatán es el tercer estado con más cerdos del país: 1.6 millones, después de Jalisco y Sonora [Censo Agropecuario 2022, cerdos_por_entidad]. SEMARNAT identificó 507 coordenadas de posibles granjas; 23 de ellas tienen más de 20 naves [SEMARNAT 2023, Dictamen diagnóstico ambiental]. En octubre de 2026 Greenpeace analizó 17 pozos y cenotes cerca de granjas y encontró indicadores fecales, y en algunas muestras nitratos por encima del límite de 48.7 mg/L de NO₃ [Greenpeace 2026; organización civil, no dato oficial].

**6. ¿Por qué tanta gente compra garrafón si hay agua entubada?**

(Opinión del personaje simulado.) Por desconfianza y por la dureza. El agua de los pozos de Mérida tiene una dureza mediana de 470 mg/L y unos 764 mg/L de sólidos disueltos [RENAMECA, sitios de Mérida]: deja sarro y no sabe bien, aunque esté clorada. Al mismo tiempo, el agua de la red es muy barata: la tarifa comercial de Mérida es de 7.97 $/m³, la más baja de todas las capitales [SINA, tarifas 2024].

**7. ¿Quién saca el agua del acuífero?**

En Yucatán hay 2,465 hm³ al año de agua subterránea concesionada. La mayor parte está registrada como "usos múltiples" (1,301 hm³) y agrícola (789 hm³); el abastecimiento público urbano suma 271 hm³, y de eso 159 hm³ son de Mérida [SINA, REPDA 2023 por municipio]. Mérida reporta 304 obras de captación, la mayoría pozos [CNGMD 2025].

**8. ¿Cómo protege la Reserva del Anillo de Cenotes el agua?**

Es una reserva estatal geohidrológica de 219,207.83 ha decretada en 2013 y modificada en 2025 [07_SIEGY/anillo_de_cenotes_SDS]. Protege la zona por donde el agua se mueve y se recarga hacia el norte. (Opinión del personaje simulado:) el reto es que dentro y cerca de ella hay granjas y crecimiento urbano.

**9. ¿Hay riesgo de intrusión salina?**

Sí, sobre todo cerca de la costa, porque debajo del agua dulce hay agua salada. En la red de calidad de CONAGUA en Yucatán, la conductividad tiene una mediana de 1,210 µS/cm, pero llega hasta 5,810 µS/cm en algunos sitios [RENAMECA, sitios de Yucatán].

**10. Si pudiera cambiar una política, ¿cuál sería?**

(Opinión del personaje simulado.) Ampliar el drenaje con tratamiento en Mérida y vigilar las granjas y las fosas sépticas, porque en un suelo kárstico lo que se descarga hoy es el agua que se toma mañana.
