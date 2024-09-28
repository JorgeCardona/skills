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