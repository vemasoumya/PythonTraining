class Utils:
    def read_parquet(self, spark, path):
        df_parquet = spark.read.parquet(path)
        return df_parquet
    
    def read_csv(self, spark, path , **kw):
        if "delimiter" in kw:
            delimiter = kw["delimiter"]
        else:
            delimiter = ","

        if "header" in kw:
            print("header is passed")
            header = kw["header"]
        else:
            header = False 

        df_csv = spark.read.format("csv")\
                .option("header", header)\
                .option("delimiter",delimiter)\
                .option("inferSchema", "true")\
                .load(path)
        
        return df_csv