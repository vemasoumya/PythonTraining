from pyspark.sql import SparkSession
from commonpackage.utils import Utils
spark = SparkSession.builder.getOrCreate()
parquet_input = "abfss://output1@vematest2.dfs.core.windows.net/testparquet1"

ut = Utils()
df_parquet = ut.read_parquet(spark, parquet_input)
df_parquet.show(5)


