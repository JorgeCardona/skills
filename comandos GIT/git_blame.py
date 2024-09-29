''' git commnand
git blame -l --color-lines --color-by-age main.py | while IFS= read -r line; do
    # Extraer el commit ID, eliminando secuencias ANSI de colores
    commit_id=$(echo "$line" | sed -E 's/\x1b\[[0-9;]*m//g' | awk '{print $1}')
    
    # Obtener el número de línea usando una expresión regular
    line_number=$(echo "$line" | sed -E 's/^.*([^0-9]*)([0-9]+)\).*/\2/')

    # Obtener el contenido de la línea usando una expresión regular que capture solo el código
    content_line=$(echo "$line" | sed -E 's/^.*[0-9]+\) //; s/\x1b\[[0-9;]*m//g')

    # Obtener los detalles del commit correspondiente: mensaje, autor, email, fecha
    commit_message=$(git log -1 --pretty=format:"%s" $commit_id)
    commit_author=$(git log -1 --pretty=format:"%an" $commit_id)
    commit_email=$(git log -1 --pretty=format:"%ae" $commit_id)
    commit_date=$(git log -1 --pretty=format:"%ad" --date=short $commit_id)

    # Imprimir la línea modificada con los detalles del commit, usando colores
    echo -e "\e[1;34mLine Number:\e[0m $line_number - \e[1;32mContent:\e[0m $content_line  - \e[0;33mCommit Message:\e[0m $commit_message - \e[1;36mCommit Id:\e[0m $commit_id - \e[1;35mAuthor:\e[0m $commit_author - \e[1;31mEmail:\e[0m $commit_email - \e[1;38;5;214mDate:\e[0m $commit_date"
done
'''

import subprocess
import re

def git_blame_with_commit_details(file_path):
    # Ejecutar git blame con las opciones correspondientes
    process = subprocess.Popen(
        ['git', 'blame', '-l', '--color-lines', '--color-by-age', file_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Leer la salida línea por línea
    for line in process.stdout:
        # Extraer el commit ID eliminando secuencias ANSI de colores
        commit_id = re.sub(r'\x1b\[[0-9;]*m', '', line).split()[0]

        # Obtener el número de línea usando una expresión regular
        line_number_match = re.search(r'[^0-9]*([0-9]+)\)', line)
        line_number = line_number_match.group(1) if line_number_match else 'Unknown'

        # Obtener el contenido de la línea eliminando el número de línea y secuencias de colores
        content_line = re.sub(r'\x1b\[[0-9;]*m', '', re.sub(r'^.*[0-9]+\) ', '', line))

        # Obtener detalles del commit
        commit_message = subprocess.check_output(
            ['git', 'log', '-1', '--pretty=format:%s', commit_id], text=True).strip()
        commit_author = subprocess.check_output(
            ['git', 'log', '-1', '--pretty=format:%an', commit_id], text=True).strip()
        commit_email = subprocess.check_output(
            ['git', 'log', '-1', '--pretty=format:%ae', commit_id], text=True).strip()
        commit_date = subprocess.check_output(
            ['git', 'log', '-1', '--pretty=format:%ad', '--date=short', commit_id], text=True).strip()

        # Imprimir la línea con los detalles del commit
        print(
            f"\033[1;34mLine Number:\033[0m {line_number} - "
            f"\033[1;32mContent:\033[0m {content_line}  - "
            f"\033[0;33mCommit Message:\033[0m {commit_message} - "
            f"\033[1;36mCommit Id:\033[0m {commit_id} - "
            f"\033[1;35mAuthor:\033[0m {commit_author} - "
            f"\033[1;31mEmail:\033[0m {commit_email} - "
            f"\033[1;38;5;214mDate:\033[0m {commit_date}"
        )

# Uso de la función
git_blame_with_commit_details('main.py')
