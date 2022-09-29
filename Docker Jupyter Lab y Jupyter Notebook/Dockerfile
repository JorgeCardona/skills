# define la version de python a instalar basado en la imagen oficial
FROM python:3.10.7

# etiqueta creador de la imagen
MAINTAINER JorgeCardona

# actualiza los repositorios
RUN apt-get update

# instala el JDK para ejecutar aplicaciones que necesiten de la maquina virtual de java
RUN apt-get install default-jdk -y

#actualiza el pip e instala los paquetes de las versiones de los notebooks
RUN pip3 -q install pip --upgrade
RUN pip3 install jupyterlab
RUN pip3 install itables

# crea un directorio para guardar archivos
RUN mkdir src
# define el directorio donde se van a guardar y a leer los notebooks por defecto
WORKDIR src/notebooks

# configura por defecto que el contenedor inicie con jupyter lab, pero se puede enviar la variable cuando se da la instruccion para iniciar el contenedor
ENV TYPE=lab

# Instala lenguaje R
RUN apt-get install r-base -y

# Instala R Jupyter Kernel
RUN echo 'install.packages(c("IRkernel"),repos="http://cran.us.r-project.org", dependencies=TRUE)' > /tmp/packages.R && Rscript /tmp/packages.R

# Instala R kernel
RUN echo 'IRkernel::installspec()' > /tmp/temp.R && Rscript /tmp/temp.R

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