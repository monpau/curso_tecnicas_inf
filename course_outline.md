# Curso práctico: Técnicas informáticas para estudiantes de 4º de Biología

Público objetivo: estudiantes de 4º de Biología (orientaciones molecular-biosanitaria y naturalista-de campo). Nivel: principiantes absolutos en Linux y programación.

Notas generales:
- Enfoque eminentemente práctico: cada lección incluye objetivos, ejemplos listos para copiar/pegar, ejercicios paso a paso y soluciones o pistas.
- No se asume ejecución automática desde el material: indicar siempre cómo guardar con `gedit` y ejecutar localmente.

Requisitos mínimos para los alumnos:
- Un equipo con Linux (o WSL/macOS con `bash`) y Python 3 instalado.
- Editor de texto: `gedit` u otro similar.

Módulo 1 — Introducción a computación en biología (T: 1 h)
- Objetivos: entender la necesidad de análisis masivo de datos en biología; conocer ejemplos de aplicaciones (secundarias, transcriptómica, ecología de comunidades).
- Actividades prácticas: lectura de un caso de uso, discusión guiada, identificar formatos de datos comunes (CSV, FASTA, FASTQ, VCF).
- Ejercicios: 3 preguntas cortas para relacionar formatos con ejemplos.

Módulo 2 — Navegación y manejo de directorios en la terminal (I: 2 h)
- Objetivos: usar `pwd`, `ls`, `cd`, crear/eliminar directorios (`mkdir`, `rmdir`, `rm -r`), copiar/mover archivos (`cp`, `mv`), permisos básicos (`chmod`).
- Ejemplos: comandos listos para copiar/pegar y su explicación.
- Ejercicios prácticos: 6–8 tareas, p. ej. crear estructura de proyecto, mover archivos, cambiar permisos.
- Soluciones: comandos exactos.

Módulo 3 — Manejo de archivos de texto mediante línea de comandos (I: 4 h)
- Objetivos: visualizar y manipular archivos con `cat`, `less`, `head`, `tail`, `cut`, `paste`, `sort`, `uniq`, `wc`, `tr`.
- Actividades: ejemplos con un archivo CSV pequeño (proporcionado como bloque de texto) y ejercicios para extraer columnas, ordenar y filtrar.
- Ejercicios: 8 ejercicios paso a paso con soluciones.

Módulo 4 — Expresiones regulares (I: 2 h)
- Objetivos: entender patrones básicos, usar `grep`/`egrep`/`sed` para búsquedas simples.
- Ejercicios: 6 ejercicios con secuencias y cabeceras FASTA para seleccionar entradas.

Módulo 5 — Pipelines y programación en shell (I: 2 h)
- Objetivos: encadenar comandos con `|`, redirecciones (`>`, `>>`, `<`), usar `xargs`, crear pequeños scripts shell.
- Ejercicios: 6 tareas para construir pipelines que procesen un archivo CSV/FASTA de ejemplo.

Módulo 7 — Introducción a la programación y Python (I: 2 h)
- Objetivos: explicar variables, ejecutar scripts Python desde la terminal, usar `python3 script.py`.
- Actividad: escribir un script simple que lea un archivo y cuente líneas.
- Ejercicios: 4 ejercicios básicos con soluciones.

Módulo 8 — Tipos y operadores (I: 2 h)
- Objetivos: tipos básicos en Python (strings, int, float, listas, diccionarios) y operadores esenciales.
- Ejercicios: 6 ejercicios cortos para manipular datos pequeños.

Módulo 9 — Bucles y condicionales (I: 4 h)
- Objetivos: `for`, `while`, `if/else` en Python; ejemplos aplicados a secuencias biológicas.
- Ejercicios: 8 ejercicios incluyendo lectura de FASTA, filtrado por longitud, conteo de bases.

Módulo 10 — Lectura, modificación y escritura de archivos (I: 4 h)
- Objetivos: usar `open()`, `read()`, `write()`, manejo de CSV con `csv` estándar; buenas prácticas.
- Ejercicios: 8 ejercicios para transformar archivos CSV/FASTA y guardar resultados.

Módulo 11 — Acceso a datos en línea via APIs (I: 2 h)
- Objetivos: aprender a obtener datos biológicos desde recursos en línea mediante peticiones HTTP (`curl` o la librería `requests` en Python); consultar accesiones de bancos de germoplasma o registros de genes; procesar la respuesta y guardarla en archivos locales para su análisis.
- Materiales: ejemplos de endpoints públicos (p. ej. NCBI/Entrez E-utilities, ENA, Ensembl REST, GBIF), y ejemplos de `curl` y `requests` listos para copiar/pegar.
- Actividades prácticas: ejecución de peticiones para recuperar metadatos de una accession (gen o secuencia) y para descargar registros de ocurrencias de una especie.
- Ejercicios sugeridos:
	1. Usar `curl` para obtener el resumen de una accession en NCBI (p. ej. con E-utilities `esummary` o `efetch`) y guardar la salida en `record.xml` o `record.json` según el endpoint.
	2. Escribir un pequeño script Python usando `requests` que consulte Ensembl REST para una ID de gen y extraiga la secuencia o anotaciones; guardar el resultado en un archivo `gene_<id>.json`.
	3. Consultar GBIF con `curl` o `requests` para obtener ocurrencias de una especie (formato JSON), y combinar esos registros con `species_observations.csv` para comparar datos de campo con registros públicos.
	4. (Opcional) Usar la API de un banco de germoplasma público (o ENA/NCBI) para buscar información sobre una accession de germoplasma y extraer metadatos relevantes (procedencia, colección, identificadores relacionados).
- Soluciones / Pistas: proporcionar comandos `curl` y snippet Python `requests` con manejo básico de JSON/XML y guardado en disco. Ejemplo mínimo (Python `requests`):

```python
import requests
url = 'https://rest.ensembl.org/lookup/id/ENSG00000139618?content-type=application/json'
resp = requests.get(url, headers={'Content-Type':'application/json'})
open('gene_ENSG00000139618.json','w').write(resp.text)
```

Nota: si `requests` no está instalado, se puede usar `curl` o `urllib` de la librería estándar; el material explicará ambas opciones y cómo instalar `requests` localmente si el alumno lo desea.

Materiales de ejemplo incluidos:
- Pequeños bloques de datos (CSV y FASTA) para copiar/pegar en archivos de prueba.
- Plantilla sugerida de estructura de proyecto y un ejemplo de `.qmd` para la lección 2 (opcionalmente).

Siguientes pasos propuestos:
1. ¿Quieres que genere plantillas `.qmd` completas para cada lección o sólo para 1–2 lecciones de ejemplo?
2. ¿Deseas que incluya datasets reales (pequeños) o prefieres que use datos sintéticos para copiar/pegar?
