from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
l = [('Ankit',25, 1),('Jalfaizy',22, 2),('saurabh',20, 3),('Bala',26, 4)]
print(l)
