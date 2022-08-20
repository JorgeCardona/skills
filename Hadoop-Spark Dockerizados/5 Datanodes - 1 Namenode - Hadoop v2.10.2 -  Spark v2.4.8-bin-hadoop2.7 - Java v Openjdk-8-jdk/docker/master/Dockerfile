FROM jorgecardona/hadoop-2.7.7-java-8-cluster-datanode:v1
MAINTAINER Jorge Cardona

WORKDIR /root

# install Spark
# define el repositorio donde se va a descargar Hadoop
ENV SPARK_DISTRIBUTION=spark-2.4.8

# define el repositorio donde se va a descargar Hadoop
ENV HADOOP_DISTRIBUTION=hadoop2.7

# define el repositorio donde se va a descargar Hadoop
ENV SPARK_WEB=https://archive.apache.org/dist/spark/${SPARK_DISTRIBUTION}

# defina la version de Hadoop a descargar
ENV SPARK_VERSION=${SPARK_DISTRIBUTION}-bin-${HADOOP_DISTRIBUTION}

# descarga Spark
RUN wget ${SPARK_WEB}/${SPARK_VERSION}.tgz

# descomprime el archivo de Spark
RUN tar -xzvf ${SPARK_VERSION}.tgz
	
# copia la carpeta descomprimida con el instalador de Spark	
RUN mv ${SPARK_VERSION} /usr/local/spark
	
# elimina el archivo de Spark comprimido que se descargo
RUN rm ${SPARK_VERSION}.tgz

ENV PATH=$PATH:/usr/local/spark/bin
ENV SPARK_HOME=/usr/local/spark
ENV LD_LIBRARY_PATH=/usr/local/hadoop/lib/native:$LD_LIBRARY_PATH

ADD config/spark-defaults.conf /usr/local/spark/conf
RUN chown root:root /usr/local/spark/conf/spark-defaults.conf

ADD bin/stackanswer_2.12-1.0.jar /usr/local/spark/jars

ADD config/bootstrap.sh /etc/bootstrap.sh
RUN chown root:root /etc/bootstrap.sh
RUN chmod 777 /etc/bootstrap.sh

ENV BOOTSTRAP /etc/bootstrap.sh

VOLUME /data

CMD ["/etc/bootstrap.sh", "-d"]

EXPOSE 18080

# docker build -f docker/master/Dockerfile -t jorgecardona/spark-2.4.8-hadoop-2.7-java-8-cluster-namenode:v1 docker/master

# docker network create --driver=bridge hadoop-network 
# docker run --rm -itd  --net=hadoop-network  --name hadoop-slave1 --hostname hadoop-slave1 jorgecardona/hadoop-2.7.7-java-8-cluster-datanode:v1
# docker run --rm -itd  --net=hadoop-network  --name hadoop-slave2 --hostname hadoop-slave2 jorgecardona/hadoop-2.7.7-java-8-cluster-datanode:v1
# docker run --rm -itd  --net=hadoop-network  --name hadoop-slave3 --hostname hadoop-slave3 jorgecardona/hadoop-2.7.7-java-8-cluster-datanode:v1
# docker run --rm -itd  --net=hadoop-network  --name hadoop-slave4 --hostname hadoop-slave4 jorgecardona/hadoop-2.7.7-java-8-cluster-datanode:v1
# docker run --rm -itd  --net=hadoop-network  --name hadoop-slave5 --hostname hadoop-slave5 jorgecardona/hadoop-2.7.7-java-8-cluster-datanode:v1
# docker run --rm -itd --net=hadoop-network -p 50070:50070  -p 8088:8088  -p 18080:18080  --name hadoop-master --hostname hadoop-master -v $PWD/data:/data jorgecardona/hadoop-cluster-java-8-spark-2.4.8-hadoop-2.7-namenode:v1

# hadoop 
# http://localhost:50070
# http://localhost:8088

# spark 
# http://localhost:18080