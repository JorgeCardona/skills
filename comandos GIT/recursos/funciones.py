from simple_colors import *
## <center> OBTENER LISTA CON LOS NOMBRES DE TODAS LAS RAMAS LOCALES DE UN REPOSITORIO GIT</center>
def obtener_lista_nombres_ramas_git():

    stdout = subprocess.check_output('git branch'.split())
    out = stdout.decode()
    branches = [b.strip('* ') for b in out.splitlines()]
    return branches


# <center> EJECUTAR COMANDOS SHELL DESDE FUNCION PYTHON</center>
import subprocess

def ejecutar_comando_shell(comando='git branch', response=False):

    print('############################################# COMANDO A EJECUTAR #############################################')
    print(cyan(comando, ['reverse','bold']))
    
    try:
        resultado_comando_ejecutado = subprocess.check_output(comando, shell=True, text=True)
    except Exception:
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& SE HA GENERADO UNA EXCEPCION &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
        print(red('EL COMANDO {comando} NO SE PUDO EJECUTAR'.format(comando=comando)))
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& FINAL DE EXCEPCION GENERADA &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
    else:
        print('####################################### RESULTADO DE COMANDO EJECUTADO #######################################')
        #para evitar el salto de linea usa el parametro end=''
        print(resultado_comando_ejecutado, end='')
        print('##############################################################################################################')
        print()
        if response:
            return resultado_comando_ejecutado
        
# <center> FUNCION LAMBDA PARA EJECUTAR COMANDOS GIT</center>
ejecutar_comando_git = lambda comando : ejecutar_comando_shell(comando)

# <center> CREAR ARCHIVOS</center>
import time
from datetime import datetime

def crear_fecha():
    
    import time
    from datetime import datetime

    # detiene el tiempo para que no todos los archivos generados queden con la misma fecha de timestamp
    time.sleep(0.1)
        
    # Getting the current date and time
    dt = datetime.now()

    # getting the timestamp
    ts = datetime.timestamp(dt)

    return ts

def copiar_archivo(nombre_del_repositorio, archivo, recursos=False):
    
    import os
    import shutil
    source = '{source}\{archivo}'.format(source=os.getcwd().split(nombre_del_repositorio,1)[0], archivo=archivo)
    
    if recursos:
        source = '{source}\{archivo}'.format(source=os.getcwd(), archivo=archivo).replace(nombre_del_repositorio, 'recursos')
    
    target = '{target}\{archivo}'.format(target=os.getcwd(), archivo=archivo)
    
    print('source', source)
    print('target', target)
    
    shutil.copyfile(source, target)
    
    print(f'archivo {archivo} copiado con exito a target')
    
def generar_archivos(todos_los_archivos=True, cantidad=1):

    lista_de_archivos = ['info.txt','Dockerfile','Manifest.yaml','imagen.png','main.py','connection.java','calculos.c','addon.php','utils.gif','query.sql','dataset.avro','link.vs']
    
    
    lista_de_archivos = lista_de_archivos if todos_los_archivos else lista_de_archivos[:cantidad]
    
    print('lista_de_archivos = {lista_de_archivos}'.format(lista_de_archivos=lista_de_archivos))
    
    for archivo in lista_de_archivos:
        comando = 'echo {crear_archivo} >> {archivo}'.format(crear_archivo=crear_fecha(), archivo=archivo)
        ejecutar_comando_shell(comando)

    return lista_de_archivos

def modificar_autor_commit(autor='cienciagoku@gmail.com'):
    comando = 'git commit --amend --no-edit --author={autor}'.format(autor=autor)
    ejecutar_comando_git(comando)
            
        
def crear_commits(total_commits=5, todos_los_archivos=False):
    
    import random
    
    for commit_numero in range(total_commits):
        
        numero_aleatorio = random.randint(1, 10_000_000)
        lista_de_archivos = generar_archivos()
        archivo_aleatorio = random.choice(lista_de_archivos)
        commit_indice = commit_numero + 1

        comando = 'git status'
        ejecutar_comando_git(comando)

        comando = 'git add .'
        ejecutar_comando_git(comando)

        comando = 'git status'
        ejecutar_comando_git(comando)

        comando = 'git commit -m "PRUEBA de COMMIT numero {commit_indice} con fecha {fecha} y valor aleatorio {numero_aleatorio} y contiene el archivo {archivo_aleatorio}"'.format(commit_indice=commit_indice, numero_aleatorio=numero_aleatorio, fecha=crear_fecha(), archivo_aleatorio=archivo_aleatorio)
        ejecutar_comando_git(comando)
        
        if commit_numero %2 ==0:
            modificar_autor_commit()

    comando = 'git log --oneline'
    ejecutar_comando_git(comando)

    comando = 'git status'
    ejecutar_comando_git(comando)
    
def cambiar_a_directorio_del_repositorio(nombre_del_repositorio):
    #importing the os module
    import os

    #to get the current working directory
    directory = os.getcwd()
    print(f'directorio base = {directory}')
          
    os.chdir('{directory}/{repository}'.format(directory=directory, repository=nombre_del_repositorio))
    directory = os.getcwd()
    print(f'directorio actual del repositorio clonado = {directory}')

def clonar_repositorio(repositorio_base, nombre_del_repositorio):

    repositorio_base = 'https://github.com/JorgeCardona'
    nombre_del_repositorio = 'comandos_git'

    eliminar_directorio(nombre_repositorio=nombre_del_repositorio)

    comando = 'git clone {repositorio_base}/{nombre_del_repositorio}.git'.format(repositorio_base=repositorio_base, nombre_del_repositorio=nombre_del_repositorio)
    ejecutar_comando_git(comando)
          
    # se ubica en el directorio donde esta el repositorio clonado
    cambiar_a_directorio_del_repositorio(nombre_del_repositorio=nombre_del_repositorio)

def abrir_archivo_con_editor_de_texto(ruta_archivo):
    comando = "notepad.exe {ruta_archivo}".format(ruta_archivo=ruta_archivo)
    ejecutar_comando_shell(comando=comando)

def abrir_git_config(tipo='local'):
    comando = "git config --{tipo} --edit".format(tipo=tipo)
    ejecutar_comando_shell(comando=comando)       
    
def configuracion_detallada_git():
    print('MOSTRAR CONFIGURACION DETALLADA DEL .gitconfig')
    comando = 'git config --list --show-origin'
    ejecutar_comando_git(comando)

def verificar_directorio_e_informacion_del_git_config():
    print('MOSTRAR UBICACION DEL .gitconfig')
    comando = 'git config --show-origin --global --list'
    ejecutar_comando_git(comando)

def verificar_git_config(tipo='local'):
    print('VERIFICAR EL CONTENIDO DEL .gitconfig {tipo}'.format(tipo=tipo.upper()))
    comando = 'git config --{tipo} --list'.format(tipo=tipo)
    ejecutar_comando_git(comando)
    
def eliminar_alias_repetido(alias_a_aliminar, tipo='local'):
    
    comando = 'git config --{tipo} --unset-all alias.{alias_a_aliminar}'.format(tipo=tipo,alias_a_aliminar=alias_a_aliminar)
    try:
        ejecutar_comando_git(comando)
    except Exception:
        print('------------------------------------- INICIA EXCEPCION ENCONTRADA -------------------------------------')
        print('EL ALIAS MULTIPLE {alias_a_aliminar} que busca eliminar, NO EXISTE EN {tipo}'.format(alias_a_aliminar=alias_a_aliminar, tipo=tipo.upper()))
        print('------------------------------------- TERMINA EXCEPCION ENCONTRADA -------------------------------------')
    else:
        comando = 'git aliases'
        ejecutar_comando_git(comando)

def eliminar_alias_git(alias_a_aliminar, tipo='local'):
    
    # si se tienen varios alias con el mismo nombre
    # git config --global --unset-all alias.nombre_del_alias_repetido

    comando = 'git config --{tipo} --unset alias.{alias_a_aliminar}'.format(alias_a_aliminar=alias_a_aliminar, tipo=tipo)
    try:
        ejecutar_comando_git(comando)
    except Exception:
        print('------------------------------------- INICIA EXCEPCION ENCONTRADA -------------------------------------')
        print('EL ALIAS {alias_a_aliminar} que busca eliminar, NO EXISTE EN {tipo}'.format(alias_a_aliminar=alias_a_aliminar, tipo=tipo.upper()))
        print('------------------------------------- TERMINA EXCEPCION ENCONTRADA -------------------------------------')
    else:
        verificar_git_config(tipo=tipo) 


def crear_alias_y_validarlos(tipo='local'):
    local = [
    "git config --local alias.colocal checkout",
    "git config --local alias.brlocal branch",
    "git config --local alias.rlocal restore .",
    "git config --local alias.loglocal log --oneline -3",
    "git config --local alias.aalocal add "
    ]
    
    globall =  [      
    "git config --global alias.co checkout",
    "git config --global alias.br branch",
    "git config --global alias.ci commit",
    "git config --global alias.st status",
    'git config --global alias.aliases "config --get-regexp {alias}"'.format(alias="'^alias\\.'")
                  ]
     
    comandos_para_alias = local if tipo=='local' else globall
                                                  
    for comando in comandos_para_alias:
        ejecutar_comando_shell(comando=comando)
                                                  
    verificar_git_config(tipo=tipo)
    
# <center> CREAR CARPETAS Y RETORNAR EL DIRECTORIO DE ACCESO</center>
def crear_carpeta(carpeta):
    import os
    
    directorio =  f'./{carpeta}'
    
    print('directorio', directorio)

    os.makedirs(f'{carpeta}', exist_ok=True)
    
    return directorio

# <center> ELIMINAR ARCHIVOS</center>
def listar_archivos_eliminables_en_directorio():
    import os
    
    directory = os.getcwd()
    listado_de_archivos = os.listdir(directory)
    
    archivos_eliminables = [archivo for archivo in listado_de_archivos if '.git' not in archivo if '.ipynb_checkpoints' not in archivo]
    
    return archivos_eliminables

    
def eliminar_directorio(nombre_repositorio):
    
    import shutil
    import os
    import stat
    from os import path
    
    for root, dirs, files in os.walk("./{nombre_repositorio}".format(nombre_repositorio=nombre_repositorio)):  
        for dir in dirs:
            try:
                os.chmod(path.join(root, dir), stat.S_IRWXU)
            except:
                print('el archivo {archivo} no existe'.format(archivo=archivo))                
        for file in files:
            try:
                os.chmod(path.join(root, file), stat.S_IRWXU)
            except:
                print('el archivo {archivo} no existe'.format(archivo=archivo))
    try: 
        shutil.rmtree("./{nombre_repositorio}".format(nombre_repositorio=nombre_repositorio))
    except:
        print('el repositorio {nombre_repositorio} no existe'.format(nombre_repositorio=nombre_repositorio))

def eliminar_archivo(archivo):
    from os import remove
    remove(archivo)

def eliminar_archivos_directorio():
    import os
    
    lista_de_archivos_eliminables = listar_archivos_eliminables_en_directorio()
    
    for archivo in lista_de_archivos_eliminables:
            os.remove(archivo)
        
    return 'Eliminacion Completada con Exito!!! de {lista_de_archivos_eliminables}'.format(lista_de_archivos_eliminables=lista_de_archivos_eliminables)


def volver_al_commit_sin_cambios(commit_id):
    print("REGRESANDO AL COMMIT' {commit_id}".format(commit_id=commit_id))

    comando = 'git reset --hard {commit_id}'.format(commit_id=commit_id)
    ejecutar_comando_git(comando)
    
    comando = 'git status'
    ejecutar_comando_git(comando)
    
def eliminar_todos_los_archivos_hasta_el_commit(commit_id):
    print("REGRESANDO AL COMMIT' {commit_id}".format(commit_id=commit_id))

    comando = 'git reset {commit_id}'.format(commit_id=commit_id)
    ejecutar_comando_git(comando)

    print('ELIMINANDO ARCHIVOS DEL STAGE')
    # eliminar los archivos que no estan en el local repo, para evitar errores al cambiar de rama
    comando = 'git rm --cached "*"'
    ejecutar_comando_git(comando)

    print('ELIMINANDO ARCHIVOS DEL WORKING DIRECTORY')
    # elimina los archivos que estan en el working directory
    comando = 'git clean -f'
    ejecutar_comando_git(comando)

    comando = 'git status'
    ejecutar_comando_git(comando)

    comando = 'git log --oneline'
    ejecutar_comando_git(comando)

    ejecutar_comando_shell()
    
# <center> CREAR ARCHIVOS, COMMITS Y PUBLICAR RAMAS AL REPOSITORIO </center>
def crear_o_actualizar_archivo(actualizaciones=10, archivo='info.txt', mensaje=None):
    
    mensaje = mensaje if mensaje else 'actualizacion'
    for index in range(actualizaciones):
        comando = "echo {mensaje} {index} fecha {fecha} >> {archivo}".format(mensaje=mensaje, index=index+1, fecha=datetime.timestamp(datetime.now()), archivo=archivo)
        ejecutar_comando_shell(comando)

def validar_si_existe_rama(nombre_rama, local=False):
    
    comando ='git branch -a'
    resultado = ejecutar_comando_shell(comando, response=True)
    
    rama_base = '{nombre_rama}'.format(nombre_rama=nombre_rama) if local else 'origin/{nombre_rama}'.format(nombre_rama=nombre_rama)

    if rama_base in resultado:
        return True
    return False

def elimina_ramas_en_local_o_remoto_si_existen(nombre_rama, rama_local, rama_remota):
    
    # valida si las ramas existen en REMOTO y LOCAL
    rama_remota_existe = validar_si_existe_rama(nombre_rama=nombre_rama)
    rama_local_existe = validar_si_existe_rama(nombre_rama=nombre_rama, local=True)
    
    # verifica si existe la rama la elimina
    if rama_remota and rama_remota_existe:
        # elimina rama REMOTA existente
        comando = 'git push origin -d {nombre_rama}'.format(nombre_rama=nombre_rama)
        ejecutar_comando_git(comando)

     # verifica si existe la rama la elimina
    if rama_local and rama_local_existe:                                                                                                            
        # elimina la rama
        comando = 'git branch -D {nombre_rama}'.format(nombre_rama=nombre_rama)
        ejecutar_comando_git(comando)
        
    # verifica las ramas actuales
    ejecutar_comando_shell()
    
def crear_commit_por_cada_archivo(todos_los_archivos):
    
    import datetime

    fecha_ahora = datetime.datetime.now()
    
    # crea el listado de archivos
    lista_de_archivos = generar_archivos(todos_los_archivos=todos_los_archivos)
    
    # basado en el listado de archivos, adiciona uno a uno y crea un commit por cada uno
    for indice, archivo in enumerate(lista_de_archivos):

        comando = 'git add {archivo}'.format(archivo=archivo)
        ejecutar_comando_git(comando)
        
        comando = 'git commit -m "ADICIONADO ARCHIVO {archivo} {fecha_ahora}" -m "- El proposito es generar un registro de archivos con su fecha correspondiente, - Se adiciono el archivo {archivo} al commit, - La fecha donde se creao este commit es {fecha_ahora}"'.format(archivo=archivo, fecha_ahora=fecha_ahora)
        ejecutar_comando_git(comando)
        
        if indice %2 ==0:
            modificar_autor_commit()

    # verifica si todos los archivos estan en los commits creados
    comando = 'git status'
    ejecutar_comando_git(comando)
    
def generar_archivos_y_hacer_commit(nombre_rama, rama_local, rama_remota, todos_los_archivos):
    
    # elimina cambios a la rama remota si los tiene
    comando = 'git restore .'
    ejecutar_comando_git(comando)
    
    # cambiar a la rama remota, 
    comando = 'git checkout {nombre_rama_principal} --force'.format(nombre_rama_principal=nombre_rama_principal)
    ejecutar_comando_git(comando)
    
    # valida si las ramas existen en REMOTO y LOCAL y las elimina
    elimina_ramas_en_local_o_remoto_si_existen(nombre_rama=nombre_rama, rama_local=rama_local, rama_remota=rama_remota)
    
    if rama_local:
        # crea la rama local
        comando = 'git checkout -b {nombre_rama}'.format(nombre_rama=nombre_rama)
        ejecutar_comando_shell(comando)
    
    # adiciona archivos de 1 en 1 y genera 1 commit por cada archivo
    crear_commit_por_cada_archivo(todos_los_archivos=todos_los_archivos)

    # mostrar el log de las ramas en forma resumida y con diagrama de uniones como grafo 
    comando = 'git log --graph --oneline'
    ejecutar_comando_git(comando)

    if rama_remota:
        # crea la rama en remoto
        comando = 'git push --set-upstream origin {nombre_rama}'.format(nombre_rama=nombre_rama)
        ejecutar_comando_git(comando)
    
    ejecutar_comando_shell()

def crear_rama_local_y_remota(nombre_rama, rama_local=True, rama_remota=True, todos_los_archivos=True):
    generar_archivos_y_hacer_commit(nombre_rama=nombre_rama, rama_local=rama_local, rama_remota=rama_remota, todos_los_archivos=todos_los_archivos)
    

def eliminar_rama_local_y_remota(nombre_rama, rama_local=True, rama_remota=True):

    comando = 'git checkout {nombre_rama_principal}'.format(nombre_rama_principal=nombre_rama_principal)
    ejecutar_comando_git(comando)

    if rama_local:
        comando = 'git branch -D {nombre_rama}'.format(nombre_rama=nombre_rama)
        ejecutar_comando_git(comando)
    
    if rama_remota:
        comando = 'git push origin -d {nombre_rama}'.format(nombre_rama=nombre_rama)
        ejecutar_comando_git(comando)

    comando = 'git branch -a'
    ejecutar_comando_git(comando)