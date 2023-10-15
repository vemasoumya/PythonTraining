class Utils:
    def read_parquet(self, spark, path):
        df_parquet = spark.read.parquet(path)
        return df_parquet
    
    def read_csv(self, spark, path , **kw):
        if kw["delimiter"]:
            delimiter = kw["delimiter"]
        else:
            delimiter = ","

        if kw["header"]:
            header = True
        else:
            header = False 

        df_csv = spark.read.format("csv")\
                .option("header", header)\
                .option("delimiter",delimiter)\
                .option("inferSchema", "true")\
                .load(path)
        
        return df_csv