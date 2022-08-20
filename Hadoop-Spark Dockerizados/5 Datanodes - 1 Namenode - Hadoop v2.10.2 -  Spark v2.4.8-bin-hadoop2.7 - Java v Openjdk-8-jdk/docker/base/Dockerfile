FROM ubuntu:20.04
MAINTAINER Jorge Cardona

WORKDIR /root

# actualiza los paquete
RUN apt-get update

# instala openssh-server
RUN apt-get install -y openssh-server

# define la version de Java que se va a instalar
ENV JAVA_VERSION=openjdk-8-jdk

# instala Java
RUN apt-get install -y ${JAVA_VERSION}

# instala WGET
RUN apt-get install -y wget

# define el repositorio donde se va a descargar Hadoop
ENV HADOOP_WEB=https://archive.apache.org/dist/hadoop/common

# defina la version de Hadoop a descargar
ENV HADOOP_VERSION=hadoop-2.7.7

# descarga hadoop
RUN wget ${HADOOP_WEB}/${HADOOP_VERSION}/${HADOOP_VERSION}.tar.gz

# descomprime el archivo de Hadoop
RUN tar -xzvf ${HADOOP_VERSION}.tar.gz
	
# copia la carpeta descomprimida con el instalador de hadoop	
RUN mv ${HADOOP_VERSION} /usr/local/hadoop
	
# elimina el archivo de hadoop comprimido que se descargo
RUN rm ${HADOOP_VERSION}.tar.gz

# set environment variable
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 
ENV HADOOP_HOME=/usr/local/hadoop 
ENV HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop/
ENV YARN_CONF_DIR=/usr/local/hadoop/etc/hadoop/
ENV PATH=$PATH:/usr/local/hadoop/bin:/usr/local/hadoop/sbin 

# ssh without key
RUN ssh-keygen -t rsa -f ~/.ssh/id_rsa -P '' 
RUN cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

RUN mkdir -p ~/hdfs/namenode
RUN mkdir -p ~/hdfs/datanode
RUN mkdir $HADOOP_HOME/logs

COPY config/* /tmp/

RUN mv /tmp/ssh_config ~/.ssh/config
RUN mv /tmp/hadoop-env.sh /usr/local/hadoop/etc/hadoop/hadoop-env.sh
RUN mv /tmp/hdfs-site.xml $HADOOP_HOME/etc/hadoop/hdfs-site.xml 
RUN mv /tmp/core-site.xml $HADOOP_HOME/etc/hadoop/core-site.xml
RUN mv /tmp/mapred-site.xml $HADOOP_HOME/etc/hadoop/mapred-site.xml
RUN mv /tmp/yarn-site.xml $HADOOP_HOME/etc/hadoop/yarn-site.xml
RUN mv /tmp/slaves $HADOOP_HOME/etc/hadoop/slaves
RUN mv /tmp/start-hadoop.sh ~/start-hadoop.sh

RUN chmod 777 ~/start-hadoop.sh
RUN chmod 777 $HADOOP_HOME/sbin/start-dfs.sh
RUN chmod 777 $HADOOP_HOME/sbin/start-yarn.sh 

# format namenode
RUN /usr/local/hadoop/bin/hdfs namenode -format

CMD [ "sh", "-c", "service ssh start; bash"]

# Hdfs ports
EXPOSE 9000 50010 50020 50070 50075 50090
EXPOSE 9871 9870 9820 9869 9868 9867 9866 9865 9864

# Mapred ports
EXPOSE 19888

#Yarn ports
EXPOSE 8030 8031 8032 8033 8040 8042 8088 8188

#Other ports
EXPOSE 49707 2122

# docker build -f docker/base/Dockerfile -t jorgecardona/hadoop-2.7.7-java-8-cluster-datanode:v1 docker/base

# docker network create --driver=bridge hadoop-network 
# docker run --rm -itd  --net=hadoop-network  --name hadoop-slave1 --hostname hadoop-slave1 jorgecardona/hadoop-2.7.7-java-8-cluster-datanode:v1
# docker run --rm -itd  --net=hadoop-network  --name hadoop-slave2 --hostname hadoop-slave2 jorgecardona/hadoop-2.7.7-java-8-cluster-datanode:v1
# docker run --rm -itd  --net=hadoop-network  --name hadoop-slave3 --hostname hadoop-slave3 jorgecardona/hadoop-2.7.7-java-8-cluster-datanode:v1
# docker run --rm -itd  --net=hadoop-network  --name hadoop-slave4 --hostname hadoop-slave4 jorgecardona/hadoop-2.7.7-java-8-cluster-datanode:v1
# docker run --rm -itd  --net=hadoop-network  --name hadoop-slave5 --hostname hadoop-slave5 jorgecardona/hadoop-2.7.7-java-8-cluster-datanode:v1
# docker run --rm -itd --net=hadoop-network -p 50070:50070  -p 8088:8088  -p 18080:18080  --name hadoop-master --hostname hadoop-master -v $PWD/data:/data jorgecardona/spark-2.4.8-hadoop-2.7-java-8-cluster-namenode:v1

# hadoop 
# http://localhost:50070
# http://localhost:8088

# spark 
# http://localhost:18080
