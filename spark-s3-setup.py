ACCESS_KEY = "AWS_ACCESS_KEY"
SECRET_KEY = "AWS_SECRET_KEY"
ENDPOINT_URL = "https://s3.MY_ENDPOINT.com/"
S3_FILE_PATH = "s3a://FILE_PATH/file"
TEMP_TABLE_NAME = "TEMP_TABLE"

import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages "org.apache.hadoop:hadoop-aws:2.7.3" pyspark-shell'

from pyspark.context import SparkContext
from pyspark.sql import SparkSession, SQLContext 
sc = SparkContext('local')
spark = SparkSession(sc)

#Configure AWS credentials
hadoopConf=spark.sparkContext._jsc.hadoopConfiguration()
hadoopConf.set("fs.s3.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
hadoopConf.set("fs.s3a.endpoint", ENDPOINT_URL)
hadoopConf.set("fs.s3a.access.key", ACCESS_KEY)
hadoopConf.set("fs.s3a.secret.key", SECRET_KEY)

#Create dataframe from S3
df0 = spark.read.parquet(S3_FILE_PATH)

from py4j.java_gateway import java_import
import time

#Create SparkSession to run thrift server 
spark = SparkSession.builder \
  .appName("Embedding Spark Thrift Server") \
  .config("spark.sql.hive.thriftServer.singleSession", "True") \
  .config("hive.server2.thrift.port", "10001") \
  .config("javax.jdo.option.ConnectionURL", \
  "jdbc:derby:;databaseName=metastore_db2;create=true") \
  .enableHiveSupport() \
  .getOrCreate()

#Store Spark dataframe as temp table
df0.createOrReplaceTempView(TEMP_TABLE_NAME)
sc = spark.sparkContext
java_import(sc._gateway.jvm, "")
#Start Spark Thrift Server using the jvm and passing the SparkSession
sc._gateway.jvm.org.apache.spark.sql.hive.thriftserver \
  .HiveThriftServer2.startWithContext(spark._jwrapped)
while True:
  time.sleep(5)
