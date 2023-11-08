mkdir MapReduceTutorial
chmod 777 MapReduceTutorial

cp /opt/hdfiles.zip MapReduceTutorial/hdfiles.zip
cd MapReduceTutorial
unzip -j hdfiles.zip

export CLASSPATH=`hadoop classpath`:.:

javac -d . SalesMapper.java SalesCountryReducer.java SalesCountryDriver.java
echo "Main-Class: SalesCountry.SalesCountryDriver" >> Manifest.txt
jar cfm ProductSalePerCountry.jar Manifest.txt SalesCountry/*.class

HADOOP_USER_NAME=root hdfs dfs -mkdir hdfs://hadoop-hadoop-hdfs-nn:9000/inputMapReduce
HADOOP_USER_NAME=root hdfs dfs -cp  SalesJan2009.csv hdfs://hadoop-hadoop-hdfs-nn:9000/inputMapReduce
HADOOP_USER_NAME=root hadoop jar ProductSalePerCountry.jar hdfs://hadoop-hadoop-hdfs-nn:9000/inputMapReduce hdfs://hadoop-hadoop-hdfs-nn:9000/mapreduce_output_sales
HADOOP_USER_NAME=root hdfs dfs -cp hdfs://hadoop-hadoop-hdfs-nn:9000/mapreduce_output_sales/part-00000 /opt/output
HADOOP_USER_NAME=root hdfs dfs -cat hdfs://hadoop-hadoop-hdfs-nn:9000/mapreduce_output_sales/part-00000


HADOOP_USER_NAME=root hdfs dfs -rm  hdfs://hadoop-hadoop-hdfs-nn:9000/inputMapReduce/SalesJan2009.csv
HADOOP_USER_NAME=root hdfs dfs -rmdir  hdfs://hadoop-hadoop-hdfs-nn:9000/inputMapReduce

HADOOP_USER_NAME=root hdfs dfs -rm  hdfs://hadoop-hadoop-hdfs-nn:9000/mapreduce_output_sales/*
HADOOP_USER_NAME=root hdfs dfs -rmdir  hdfs://hadoop-hadoop-hdfs-nn:9000/mapreduce_output_sales