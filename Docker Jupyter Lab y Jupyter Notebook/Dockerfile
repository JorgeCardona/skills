#define la version de python a instalar basado en la imagen oficial
FROM python:latest

#RUN apt-get install default-jdk -y
#RUN apt install openjdk-17-jre -y -> instala el jdk por default del sistema
#RUN apt install openjdk-17-jdk -y -> instala especificamente el jdk de java 17 
#!java --version -> openjdk 17.0.2 2022-01-18
#!update-alternatives --list java -> valida el directorio donde esta instalado el binario de java
#!echo $JAVA_HOME -> /usr/lib/jvm/java-17-openjdk-amd64/bin/java

#actualiza el pip e instala los paquetes de las versiones de los notebooks
RUN apt-get update
# para dar soporte a librerias que necesiten java como SPARK
RUN apt-get install default-jdk -y 

# configura el directorio de inicializacion de java
#ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64/bin/java

RUN pip3 -q install pip --upgrade
RUN pip3 install jupyterlab
RUN pip3 install notebook
RUN pip3 install itables

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
#docker run --name lab --rm -i -t -p 8888:8888 jorgecardona/jupyter
#docker run --name notebook --rm -i -t -p 8888:8888 -e TYPE=notebook jorgecardona/jupyter

# cuando se quiera crear un contenedor y se mantenga incluso despues de cerrar la sesion
#docker run --name lab -i -t -p 8888:8888 jorgecardona/jupyter
#docker run --name notebook -i -t -p 8888:8888 -e TYPE=notebook jorgecardona/jupyter

# cuando se quiera detener la ejecucion del contenedor
#docker stop lab
#docker stop notebook

# cuando se quiera continuar o reiniciar la ejecucion en un contenedor persistido
#docker start -i lab
#docker start -i notebook

# para subir o actualizar la imagen
#docker login
#docker push jorgecardona/jupyter
