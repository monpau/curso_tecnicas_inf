"""Genera los archivos de datos del módulo 10 (lectura y escritura de archivos).

Uso (desde curso/datasets):  python3 _generadores/modulo10.py
Los datos son simulados; la semilla fija hace que el resultado sea reproducible.
"""
import gzip
import math
import random
from datetime import datetime, timedelta

random.seed(2026)

BASES = "ACGT"
AMINOACIDOS = "ACDEFGHIKLMNPQRSTVWY"


def envolver(secuencia, ancho):
    return "\n".join(secuencia[i:i + ancho] for i in range(0, len(secuencia), ancho))


def adn_aleatorio(longitud, gc=0.5):
    pesos = [(1 - gc) / 2, gc / 2, gc / 2, (1 - gc) / 2]
    return "".join(random.choices(BASES, weights=pesos, k=longitud))


# ---------------------------------------------------------------------------
# Ejemplo de la teoría: muestras de suelo
# ---------------------------------------------------------------------------
def muestras_suelo():
    parcelas = ["Encinar", "Pinar", "Pradera", "Cultivo"]
    ph_medio = {"Encinar": 6.2, "Pinar": 5.4, "Pradera": 6.8, "Cultivo": 7.3}
    with open("muestras_suelo.tsv", "w", encoding="utf-8") as f:
        f.write("muestra\tparcela\tph\tmateria_organica\n")
        for i in range(1, 13):
            parcela = parcelas[(i - 1) % 4]
            ph = random.gauss(ph_medio[parcela], 0.25)
            mo = random.uniform(1.0, 8.0)
            f.write(f"S{i:02d}\t{parcela}\t{ph:.2f}\t{mo:.1f}\n")


# ---------------------------------------------------------------------------
# 1. Incubadora de cultivos celulares
# ---------------------------------------------------------------------------
def incubadora():
    inicio = datetime(2026, 3, 1, 0, 0)
    aperturas = set(random.sample(range(2880), 25))
    with open("incubadora_temperaturas.tsv", "w", encoding="utf-8") as f:
        f.write("fecha_hora\ttemperatura_C\n")
        caida = 0
        for i in range(2880):
            momento = inicio + timedelta(minutes=15 * i)
            if i in aperturas:
                caida = random.choice([2, 3, 4])
            if caida > 0:
                temp = random.uniform(35.2, 36.4)
                caida -= 1
            else:
                temp = random.gauss(37.0, 0.12)
            if 1500 <= i < 1512:  # fallo del termostato
                temp = random.uniform(37.6, 38.3)
            f.write(f"{momento:%Y-%m-%d %H:%M}\t{temp:.2f}\n")


# ---------------------------------------------------------------------------
# 2. Censo de aves en transectos
# ---------------------------------------------------------------------------
def censo_aves():
    especies = {
        "gorrión común": 30, "mirlo común": 14, "estornino negro": 18,
        "paloma torcaz": 12, "verdecillo": 9, "jilguero europeo": 8,
        "carbonero común": 10, "herrerillo común": 7, "petirrojo europeo": 6,
        "urraca común": 5, "colirrojo tizón": 4, "abubilla": 2,
        "curruca capirotada": 4, "lavandera blanca": 3, "pinzón vulgar": 6,
    }
    nombres = list(especies)
    pesos = list(especies.values())
    observadores = ["L. Martínez", "A. Ruiz", "C. Soler"]
    fecha = datetime(2026, 4, 6)

    def deformar(nombre):
        r = random.random()
        if r < 0.10:
            nombre = nombre.upper()
        elif r < 0.25:
            nombre = nombre.capitalize()
        if random.random() < 0.12:
            nombre = nombre + " " * random.randint(1, 3)
        if random.random() < 0.05:
            nombre = " " + nombre
        return nombre

    with open("censo_aves.txt", "w", encoding="utf-8") as f:
        f.write("# Censo primaveral de aves - Parque fluvial\n")
        f.write("# Cada línea es un individuo observado en el transecto\n")
        for t in range(1, 13):
            f.write("\n")
            f.write(f"# Transecto {t} - {fecha:%Y-%m-%d} - Observador: {random.choice(observadores)}\n")
            for _ in range(random.randint(55, 110)):
                f.write(deformar(random.choices(nombres, weights=pesos)[0]) + "\n")
            fecha += timedelta(days=random.choice([2, 3, 4]))


# ---------------------------------------------------------------------------
# 3. Glucemias en ayunas
# ---------------------------------------------------------------------------
def glucemias():
    with open("glucemias_pacientes.csv", "w", encoding="utf-8") as f:
        f.write("id_paciente,edad,sexo,glucosa_mg_dl\n")
        for i in range(1, 651):
            edad = random.randint(18, 90)
            sexo = random.choice("HM")
            base = 82 + (edad - 18) * 0.15
            r = random.random()
            if r < 0.12:
                glucosa = random.gauss(155, 30)
            elif r < 0.30:
                glucosa = random.gauss(112, 7)
            else:
                glucosa = random.gauss(base, 8)
            f.write(f"P{i:04d},{edad},{sexo},{max(60, round(glucosa))}\n")


# ---------------------------------------------------------------------------
# 4. Proteoma parcial (FASTA de proteínas, multilínea)
# ---------------------------------------------------------------------------
def proteoma():
    funciones = [
        "ATP synthase subunit", "DNA polymerase", "Ribosomal protein",
        "ABC transporter permease", "Chaperone protein", "Transcriptional regulator",
        "Outer membrane protein", "Glutamate dehydrogenase", "Cell division protein",
        "Two-component sensor kinase", "Elongation factor", "Uncharacterized protein",
    ]
    with open("proteoma_parcial.fasta", "w", encoding="utf-8") as f:
        for i in range(1, 361):
            acc = f"Q{random.randint(10000, 99999)}"
            nombre = f"PRT{i:03d}"
            longitud = int(random.lognormvariate(math.log(320), 0.55))
            longitud = max(45, min(longitud, 2400))
            secuencia = "M" + "".join(random.choices(AMINOACIDOS, k=longitud - 1))
            funcion = random.choice(funciones)
            f.write(f">sp|{acc}|{nombre}_BACSU {funcion} OS=Bacillus subtilis OX=1423\n")
            f.write(envolver(secuencia, 60) + "\n")


# ---------------------------------------------------------------------------
# 5. Contigs de un ensamblaje (FASTA de ADN, multilínea)
# ---------------------------------------------------------------------------
def contigs():
    with open("contigs_ensamblaje.fasta", "w", encoding="utf-8") as f:
        for i in range(1, 301):
            longitud = int(random.lognormvariate(math.log(1400), 1.0))
            longitud = max(200, min(longitud, 60000))
            gc = random.gauss(0.42, 0.04)
            secuencia = adn_aleatorio(longitud, gc)
            if random.random() < 0.15:  # huecos de andamiaje
                pos = random.randint(0, max(0, longitud - 100))
                n = random.randint(10, 100)
                secuencia = secuencia[:pos] + "N" * n + secuencia[pos + n:]
                secuencia = secuencia[:longitud]
            cobertura = random.uniform(5, 80)
            f.write(f">contig_{i:04d} len={len(secuencia)} cov={cobertura:.1f}\n")
            f.write(envolver(secuencia, 80) + "\n")


# ---------------------------------------------------------------------------
# 6. Lecturas Illumina (FASTQ comprimido)
# ---------------------------------------------------------------------------
def fastq():
    adaptador = "AGATCGGAAGAGC"
    with gzip.open("lecturas_illumina.fastq.gz", "wt", encoding="utf-8") as f:
        for i in range(1, 5001):
            longitud = random.choice([150] * 6 + [random.randint(30, 149)])
            secuencia = adn_aleatorio(longitud)
            if random.random() < 0.08:
                pos = random.randint(10, max(11, longitud - len(adaptador)))
                secuencia = (secuencia[:pos] + adaptador + secuencia[pos:])[:longitud]
            buena = random.random() < 0.85
            calidades = []
            for j in range(longitud):
                media = (36 if buena else 24) - 10 * j / longitud
                q = int(max(2, min(41, random.gauss(media, 4))))
                calidades.append(chr(q + 33))
            x, y = random.randint(1000, 29000), random.randint(1000, 29000)
            f.write(f"@M04512:88:000000000-KX2P7:1:1101:{x}:{y} 1:N:0:7\n")
            f.write(secuencia + "\n+\n" + "".join(calidades) + "\n")


# ---------------------------------------------------------------------------
# 7. Variantes de una cohorte (VCF comprimido)
# ---------------------------------------------------------------------------
def vcf():
    muestras = [f"IND{i:02d}" for i in range(1, 9)]
    longitudes = {"chr1": 2_500_000, "chr2": 1_800_000, "chr3": 1_200_000}
    with gzip.open("variantes_cohorte.vcf.gz", "wt", encoding="utf-8") as f:
        f.write("##fileformat=VCFv4.2\n")
        f.write("##source=SimuladorCurso\n")
        for crom, lon in longitudes.items():
            f.write(f"##contig=<ID={crom},length={lon}>\n")
        f.write('##FILTER=<ID=LowQual,Description="Calidad baja">\n')
        f.write('##INFO=<ID=DP,Number=1,Type=Integer,Description="Profundidad total">\n')
        f.write('##INFO=<ID=AF,Number=A,Type=Float,Description="Frecuencia alélica">\n')
        f.write('##FORMAT=<ID=GT,Number=1,Type=String,Description="Genotipo">\n')
        f.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\t" + "\t".join(muestras) + "\n")
        n = 1
        for crom, lon in longitudes.items():
            num = int(2600 * lon / sum(longitudes.values()))
            for pos in sorted(random.sample(range(1000, lon), num)):
                ref = random.choice(BASES)
                tipo = random.random()
                if tipo < 0.82:
                    alt = random.choice([b for b in BASES if b != ref])
                elif tipo < 0.91:
                    alt = ref + adn_aleatorio(random.randint(1, 6))
                else:
                    ref = ref + adn_aleatorio(random.randint(1, 6))
                    alt = ref[0]
                qual = round(random.expovariate(1 / 60), 1)
                filtro = "PASS" if qual >= 20 and random.random() > 0.04 else "LowQual"
                genotipos = random.choices(["0/0", "0/1", "1/1", "./."], weights=[50, 30, 15, 5], k=8)
                alelos = sum(g.count("1") for g in genotipos)
                llamados = sum(2 for g in genotipos if g != "./.")
                af = alelos / llamados if llamados else 0
                dp = random.randint(40, 400)
                ident = f"rs{random.randint(100000, 9999999)}" if random.random() < 0.4 else "."
                f.write(f"{crom}\t{pos}\t{ident}\t{ref}\t{alt}\t{qual}\t{filtro}\t"
                        f"DP={dp};AF={af:.3f}\tGT\t" + "\t".join(genotipos) + "\n")
                n += 1


# ---------------------------------------------------------------------------
# 8. Anotación de un genoma (GFF3)
# ---------------------------------------------------------------------------
def gff():
    silabas = ["pho", "nit", "lea", "gat", "rbc", "psb", "hsp", "myb", "wrk", "nac", "bzr", "cbf"]
    with open("anotacion_genes.gff3", "w", encoding="utf-8") as f:
        f.write("##gff-version 3\n")
        g = 1
        for crom, lon in [("chr1", 3_000_000), ("chr2", 2_200_000), ("chr3", 1_700_000),
                          ("chr4", 1_400_000), ("chr5", 900_000)]:
            f.write(f"##sequence-region {crom} 1 {lon}\n")
            pos = random.randint(1000, 8000)
            while pos < lon - 20000:
                hebra = random.choice("+-")
                exones = []
                inicio = pos
                for _ in range(random.choice([1, 1, 2, 2, 3, 3, 4, 5, 6, 8])):
                    lon_exon = random.randint(80, 600)
                    exones.append((pos, pos + lon_exon - 1))
                    pos += lon_exon + random.randint(80, 900)
                fin = exones[-1][1]
                gid = f"gen{g:04d}"
                nombre = f"{random.choice(silabas).upper()}{random.randint(1, 40)}"
                col = f"{crom}\tCursoAnnot\t"
                f.write(f"{col}gene\t{inicio}\t{fin}\t.\t{hebra}\t.\tID={gid};Name={nombre}\n")
                f.write(f"{col}mRNA\t{inicio}\t{fin}\t.\t{hebra}\t.\tID={gid}.t1;Parent={gid}\n")
                for k, (a, b) in enumerate(exones, 1):
                    f.write(f"{col}exon\t{a}\t{b}\t.\t{hebra}\t.\tID={gid}.t1.exon{k};Parent={gid}.t1\n")
                for k, (a, b) in enumerate(exones, 1):
                    f.write(f"{col}CDS\t{a}\t{b}\t.\t{hebra}\t0\tID={gid}.t1.cds{k};Parent={gid}.t1\n")
                g += 1
                pos = fin + random.randint(2000, 25000)


# ---------------------------------------------------------------------------
# 9. BLAST de amplicones 16S (tabular, outfmt 6)
# ---------------------------------------------------------------------------
def blast():
    referencias = [
        "Pseudomonas_fluorescens", "Pseudomonas_putida", "Bacillus_subtilis", "Bacillus_cereus",
        "Escherichia_coli", "Streptomyces_griseus", "Rhizobium_leguminosarum", "Flavobacterium_johnsoniae",
        "Arthrobacter_globiformis", "Burkholderia_cepacia", "Acinetobacter_baumannii",
        "Clostridium_perfringens", "Lactobacillus_plantarum", "Mycobacterium_smegmatis",
        "Sphingomonas_paucimobilis", "Nitrosomonas_europaea",
    ]
    accesiones = {r: f"NR_{random.randint(10000, 199999)}.1" for r in referencias}
    with open("blast_amplicones_16S.tsv", "w", encoding="utf-8") as f:
        for q in range(1, 701):
            consulta = f"ASV_{q:04d}"
            verdadera = random.choice(referencias)
            longitud = random.randint(240, 260)
            mejor_ident = random.choice([random.uniform(97, 100)] * 4 + [random.uniform(85, 97)])
            hits = [verdadera] + random.sample([r for r in referencias if r != verdadera], random.randint(0, 7))
            filas = []
            for k, ref in enumerate(hits):
                ident = mejor_ident - k * random.uniform(0.5, 2.5)
                alin = longitud - random.randint(0, 6)
                desaj = round(alin * (100 - ident) / 100)
                huecos = random.randint(0, 2)
                bits = alin * 1.85 * ident / 100 - 3 * (desaj + huecos)
                evalue = 10 ** -(bits * 0.25)
                inicio_s = random.randint(400, 600)
                filas.append((bits, f"{consulta}\t{accesiones[ref]}|{ref}\t{ident:.2f}\t{alin}\t{desaj}\t"
                                    f"{huecos}\t1\t{alin}\t{inicio_s}\t{inicio_s + alin - 1}\t"
                                    f"{evalue:.2e}\t{bits:.1f}\n"))
            for bits, fila in sorted(filas, reverse=True):
                f.write(fila)


# ---------------------------------------------------------------------------
# 10. Fototrampeo
# ---------------------------------------------------------------------------
def fototrampeo():
    # especie: (peso, horas de actividad, grupo máximo)
    especies = {
        "jabalí": (25, list(range(21, 24)) + list(range(0, 6)), 6),
        "zorro": (20, list(range(20, 24)) + list(range(0, 7)), 2),
        "corzo": (16, [6, 7, 8, 19, 20, 21], 3),
        "ciervo": (10, [5, 6, 7, 8, 18, 19, 20, 21], 5),
        "tejón": (8, list(range(22, 24)) + list(range(0, 5)), 2),
        "garduña": (7, list(range(21, 24)) + list(range(0, 6)), 1),
        "ardilla roja": (9, list(range(8, 19)), 1),
        "liebre": (5, list(range(19, 24)) + list(range(0, 8)), 1),
    }
    nombres = list(especies)
    pesos = [especies[e][0] for e in nombres]
    camaras = [f"CT{i:02d}" for i in range(1, 11)]
    registros = []
    inicio = datetime(2026, 5, 1)
    for _ in range(2400):
        sp = random.choices(nombres, weights=pesos)[0]
        horas = especies[sp][1]
        hora = random.choice(horas) if random.random() < 0.88 else random.randint(0, 23)
        momento = inicio + timedelta(days=random.randint(0, 60), hours=hora,
                                     minutes=random.randint(0, 59), seconds=random.randint(0, 59))
        individuos = random.randint(1, especies[sp][2])
        registros.append((momento, random.choice(camaras), sp, individuos))
    registros.sort()
    with open("fototrampeo_sierra.csv", "w", encoding="utf-8") as f:
        f.write("fecha,hora,camara,especie,individuos\n")
        for momento, cam, sp, ind in registros:
            f.write(f"{momento:%Y-%m-%d},{momento:%H:%M:%S},{cam},{sp},{ind}\n")


# ---------------------------------------------------------------------------
# 11. Sensores de un embalse
# ---------------------------------------------------------------------------
def sensores():
    estaciones = {"E1-Presa": (8.5, 3.0), "E2-Centro": (7.8, 2.5), "E3-Cola": (6.5, 3.5), "E4-Afluente": (9.2, 1.5)}
    inicio = datetime(2026, 7, 1)
    with open("sensores_embalse.csv", "w", encoding="utf-8") as f:
        f.write("fecha_hora,estacion,temperatura_C,oxigeno_mg_l,ph,conductividad_uS\n")
        for h in range(24 * 31):
            momento = inicio + timedelta(hours=h)
            for est, (o2_medio, amplitud) in estaciones.items():
                dia = math.sin((momento.hour - 9) / 24 * 2 * math.pi)
                temp = 22 + 2.5 * dia + random.gauss(0, 0.4) + h / 300
                o2 = o2_medio + amplitud * dia + random.gauss(0, 0.6) - (h / 200 if est == "E3-Cola" else 0)
                o2 = max(0.2, o2)
                ph = 7.8 + 0.3 * dia + random.gauss(0, 0.08)
                cond = random.gauss(420, 25)
                valores = [f"{temp:.2f}", f"{o2:.2f}", f"{ph:.2f}", f"{cond:.0f}"]
                for k in range(4):
                    r = random.random()
                    if r < 0.02:
                        valores[k] = "NA"
                    elif r < 0.03:
                        valores[k] = "-999"
                f.write(f"{momento:%Y-%m-%d %H:%M},{est}," + ",".join(valores) + "\n")


# ---------------------------------------------------------------------------
# 12. Lector de microplacas (curvas de crecimiento)
# ---------------------------------------------------------------------------
def placas():
    cepas = {
        "A": ("Silvestre", 0.45, 1.25), "B": ("Mutante dacA", 0.40, 1.10),
        "C": ("Mutante pbpB", 0.25, 0.80), "D": ("Mutante ftsZ", 0.10, 0.35),
        "E": ("Silvestre + ampicilina", 0.15, 0.50), "F": ("Mutante dacA + ampicilina", 0.30, 0.95),
        "G": ("Aislado clínico 1", 0.50, 1.40), "H": ("Aislado clínico 2", 0.35, 1.20),
    }
    with open("lector_placas.txt", "w", encoding="utf-8") as f:
        f.write("Lector de microplacas - Exportación de datos\n")
        f.write("Experimento: curvas de crecimiento E. coli, 37 °C, DO 600 nm\n")
        f.write("Columna 1: blanco (medio sin inocular). Columnas 2-12: réplicas.\n")
        f.write("Filas: " + "; ".join(f"{fila}={datos[0]}" for fila, datos in cepas.items()) + "\n")
        for t in range(0, 25, 2):
            f.write("\n")
            f.write(f"Lectura: {t // 2 + 1}\n")
            f.write(f"Tiempo (h): {t}\n")
            f.write("\t" + "\t".join(str(c) for c in range(1, 13)) + "\n")
            for fila, (_, tasa, maximo) in cepas.items():
                blanco = random.gauss(0.045, 0.003)
                valores = [blanco]
                for _ in range(11):
                    k = tasa * random.gauss(1, 0.05)
                    logistica = 1 / (1 + math.exp(-k * (t - 8)))
                    inicial = 1 / (1 + math.exp(8 * k))
                    do = 0.01 + maximo * (logistica - inicial) / (1 - inicial)
                    valores.append(blanco + do + random.gauss(0, 0.015))
                f.write(fila + "\t" + "\t".join(f"{v:.3f}" for v in valores) + "\n")


# ---------------------------------------------------------------------------
# 13. Expresión génica (RNA-seq)
# ---------------------------------------------------------------------------
def expresion():
    with open("expresion_rnaseq.tsv", "w", encoding="utf-8") as f:
        f.write("# Recuentos normalizados (CPM). Control: plantas a 22 °C. Tratamiento: 6 h a 4 °C\n")
        f.write("gen\tctrl_1\tctrl_2\tctrl_3\tfrio_1\tfrio_2\tfrio_3\n")
        for i in range(1, 3001):
            media = random.lognormvariate(math.log(40), 1.6)
            if random.random() < 0.05:
                media = 0
            r = random.random()
            efecto = 1
            if r < 0.06:
                efecto = random.uniform(2.5, 30)
            elif r < 0.11:
                efecto = random.uniform(0.03, 0.4)
            ctrl = [max(0, random.gauss(media, media * 0.15)) for _ in range(3)]
            frio = [max(0, random.gauss(media * efecto, media * efecto * 0.15)) for _ in range(3)]
            f.write(f"AT{random.randint(1, 5)}G{i * 10:05d}\t" + "\t".join(f"{v:.1f}" for v in ctrl + frio) + "\n")


# ---------------------------------------------------------------------------
# 14. Inventario forestal + códigos de especies
# ---------------------------------------------------------------------------
def inventario():
    especies = {
        "PIHA": ("Pinus halepensis", 30, 28, 9), "PINI": ("Pinus nigra", 20, 32, 9),
        "PISY": ("Pinus sylvestris", 14, 30, 8), "QUIL": ("Quercus ilex", 16, 22, 7),
        "QUFA": ("Quercus faginea", 8, 20, 6), "JUTH": ("Juniperus thurifera", 6, 18, 6),
        "ARUN": ("Arbutus unedo", 4, 10, 3), "FRAN": ("Fraxinus angustifolia", 2, 25, 7),
    }
    with open("codigos_especies.tsv", "w", encoding="utf-8") as f:
        f.write("codigo\tnombre_cientifico\n")
        for codigo, datos in especies.items():
            f.write(f"{codigo}\t{datos[0]}\n")
    codigos = list(especies)
    pesos = [especies[c][1] for c in codigos]
    with open("inventario_forestal.csv", "w", encoding="utf-8") as f:
        f.write("parcela,arbol,especie,diametro_cm,altura_m,estado\n")
        for p in range(1, 41):
            for a in range(1, random.randint(60, 140)):
                cod = random.choices(codigos, weights=pesos)[0]
                diam = max(7.5, random.gauss(especies[cod][2], especies[cod][3]))
                altura = max(1.5, 1.3 + diam * random.uniform(0.25, 0.45))
                estado = "muerto" if random.random() < 0.06 else "vivo"
                f.write(f"P{p:02d},{a},{cod},{diam:.1f},{altura:.1f},{estado}\n")


if __name__ == "__main__":
    for generador in [muestras_suelo, incubadora, censo_aves, glucemias, proteoma, contigs, fastq,
                      vcf, gff, blast, fototrampeo, sensores, placas, expresion, inventario]:
        generador()
