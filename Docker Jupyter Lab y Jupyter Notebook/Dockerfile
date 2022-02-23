#define la version de python a instalar basado en la imagen oficial
FROM python:latest

#actualiza el pip e instala los paquetes de las versiones de los notebooks
RUN pip3 -q install pip --upgrade
RUN pip3 install jupyterlab
RUN pip3 install notebook

# crea un directorio para guardar archivos
RUN mkdir src
# define el directorio donde se van a guardar y a leer los notebooks por defecto
WORKDIR src/notebooks

# configura por defecto que el contenedor inicie con jupyter lab, pero se puede enviar la variable cuando se da la instruccion para iniciar el contenedor
ENV TYPE=lab

# ejecuta los comandos al iniciar jupyter en el contenedor para ejecutar 
CMD jupyter ${TYPE} --port=8888 --no-browser --ip=0.0.0.0 --allow-root

# cuando se quiera construir la imagen
#docker build -t jorgecardona/jupyter .

# cuando se quiera crear un contenedor que solo este disponible hasta que se cierre la sesion
#docker run --rm -i -t -p 8888:8888 jorgecardona/jupyter
#docker run --rm -i -t -p 8888:8888 -e TYPE=notebook jorgecardona/jupyter

# cuando se quiera crear un contenedor y se mantenga incluso despues de cerrar la sesion
#docker run -i -t -p 8888:8888 jorgecardona/jupyter
#docker run --rm -i -t -p 8888:8888 -e TYPE=notebook jorgecardona/jupyter

# cuando se quiera detener la ejecucion del contenedor
#docker stop ID_DEL_CONTENEDOR

# cuando se quiera continuar la ejecucion en un contenedor persistido
#docker start -i ID_DEL_CONTENEDOR
