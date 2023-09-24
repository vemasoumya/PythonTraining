# Databricks notebook source
l = [('Ankit',25, 1),('Jalfaizy',22, 2),('saurabh',20, 3),('Bala',26, 4)]
rdd=sc.parallelize(l)
print(rdd.getNumPartitions())
df = rdd.toDF(['name', 'age', 'eno'])
df.show(5)

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *
fields = [StructField("name1", StringType(), True),StructField("date1", StringType(), True)]
schema = StructType(fields)
l = [('Ankit','2021-01-02'),('Jalfaizy','2021-01-02'),('saurabh','2021-01-02'),('Bala','2021-01-02')]
rdd=sc.parallelize(l)
dftest = rdd.toDF(schema).select(col("name1"),col("date1").cast("date").alias("dob"))
dftest.printSchema()
# COMMAND ----------
