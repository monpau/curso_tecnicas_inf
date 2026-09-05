Datasets de ejemplo para el curso

Descripción
Este directorio contiene pequeños datasets reales/sintéticos pensados para las prácticas del curso. Los archivos son deliberadamente pequeños para facilitar la copia/pegado desde el tutorial y la edición en `gedit`.

Archivos
- `species_observations.csv`: observaciones de campo (CSV) — ideal para prácticas de manejo de CSV.
- `sequences.fasta`: secuencias de ADN en formato FASTA — para prácticas con `grep`, `sed`, y Python.
- `gene_expression.csv`: tabla de expresión génica simplificada — para prácticas en Python y manipulación de archivos.
- `registro_campo_bruto.csv`: registro de campo con errores típicos de captura de datos reales (mayúsculas/minúsculas inconsistentes, erratas de especie como "sylvestris"/"silvestris", espacios extra) — usado en el módulo de expresiones regulares para practicar `grep`/`sed` sobre datos "sucios".
- `codigos_muestreo.csv`: códigos de muestreo (localidad + sustrato + época + altura) junto a la especie encontrada — usado en el módulo de expresiones regulares para practicar contenedores (clases de caracteres) y rangos numéricos.
- `muestras_con_comas.csv`: notas de campo entre comillas que contienen comas — usado en el módulo de lectura/escritura de archivos para mostrar por qué `split(",")` a mano es frágil y el módulo `csv` no.

Uso recomendado
1. Abrir `gedit` y pegar el contenido del archivo que se necesite practicar.
2. Guardar con el nombre indicado, por ejemplo `species_observations.csv`.
3. Seguir los ejercicios de la lección: copiar/pegar comandos `bash` o ejecutar scripts Python localmente.

Licencia
Los datos son de ejemplo y pueden usarse libremente para fines docentes.
