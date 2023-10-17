from pyspark.sql import DataFrame
from pyspark.sql.functions import col, lit

class DataFrameHelper:
    def __init__(self, dataframe: DataFrame):
        self.dataframe = dataframe

    def filter_by_column_value(self, column_name, value):
        return self.dataframe.filter(self.dataframe[column_name] == value)

    def remove_null_values(self, columns=None):
        if columns is not None:
            return self.dataframe.na.drop(subset=columns)
        else:
            return self.dataframe.na.drop()

    def remove_duplicates(self, columns=None):
        if columns is not None:
            return self.dataframe.dropDuplicates(subset=columns)
        else:
            return self.dataframe.dropDuplicates()

    def get_record_count(self):
        return self.dataframe.count()
