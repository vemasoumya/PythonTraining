from pyspark.sql import SparkSession
from commonpackage.utils import Utils
spark = SparkSession.builder.getOrCreate()
ut = Utils()

# parquet_input = "abfss://output1@vematest2.dfs.core.windows.net/testparquet1"
# df_parquet = ut.read_parquet(spark, parquet_input)
# df_parquet.show(5)
# df_parquet.printSchema()

csv_input = "abfss://samplefiles@vematest2.dfs.core.windows.net/folder1/FL_insurance_sample.csv"
df_parquet = ut.read_csv(spark, csv_input)
df_parquet.show(5)
df_parquet.printSchema()


