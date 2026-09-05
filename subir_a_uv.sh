#!/bin/bash
# Sube la pagina de aterrizaje y el curso compilado al espacio web personal
# de la Universitat de Valencia (servicio "Disco", ver
# https://www.uv.es/wikisiuv/cas/seri/espacios/ActualizaEspacio.wiki#A21167).
#
# Uso:
#   ./subir_a_uv.sh
#
# Antes de ejecutarlo:
#   1. Comprueba que USUARIO_UV es correcto (lo he deducido de tu blog
#      "monpauja.blogs.uv.es" y de la URL de tu ficha institucional -
#      confirmalo antes de la primera subida).
#   2. Te pedira tu contrasena de la universidad de forma interactiva
#      (no se guarda en ningun sitio).
#
# El script compila el curso con 'quarto render' antes de subirlo, asi que
# siempre sube la version mas reciente de los modulos.

set -euo pipefail

USUARIO_UV="monpauja"          # <-- confirma que es tu usuario UV
SERVIDOR="disco.uv.es"
# Al conectar por sftp ya aterrizas en tu home de Disco; "web" es la carpeta
# publicada dentro de esa home (ruta relativa, no absoluta).
DESTINO="web"

DIR_PROYECTO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LANDING="${DIR_PROYECTO}/index.html"
SITIO="${DIR_PROYECTO}/curso/_site"

if [ ! -f "${LANDING}" ]; then
    echo "No encuentro ${LANDING}." >&2
    exit 1
fi

echo "Compilando el curso con quarto render..."
(cd "${DIR_PROYECTO}/curso" && quarto render)
echo

if [ ! -d "${SITIO}" ]; then
    echo "No encuentro ${SITIO} tras la compilacion." >&2
    exit 1
fi

echo "Conectando a sftp://${USUARIO_UV}@${SERVIDOR}/~/${DESTINO}"
echo "Te pedira la contrasena de la universidad."
echo

# El sftp de Disco no crea bien subdirectorios "al vuelo" con put -r, asi que
# creamos primero todas las carpetas y luego subimos los archivos uno a uno.
BATCH="$(mktemp)"
trap 'rm -f "${BATCH}"' EXIT

{
    echo "-mkdir ${DESTINO}"
    echo "cd ${DESTINO}"
    echo "-mkdir curso"
    echo "put \"${LANDING}\" index.html"
    echo "cd curso"

    while IFS= read -r -d '' dir; do
        printf -- '-mkdir "%s"\n' "${dir#"${SITIO}"/}"
    done < <(find "${SITIO}" -mindepth 1 -type d -print0 | sort -z)

    while IFS= read -r -d '' file; do
        printf 'put "%s" "%s"\n' "${file}" "${file#"${SITIO}"/}"
    done < <(find "${SITIO}" -type f -print0)

    echo "cd .."
    echo "bye"
} > "${BATCH}"

sftp "${USUARIO_UV}@${SERVIDOR}" < "${BATCH}"

echo
echo "Subida completada."
echo "index.html y curso/ deberian quedar visibles en tu espacio web personal."
