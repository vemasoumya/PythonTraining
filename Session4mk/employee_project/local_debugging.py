from pyspark.sql import SparkSession

class DataFrameHandler:
    def __init__(self, app_name="DataFrameApp"):
        # Create a SparkSession
        self.spark = SparkSession.builder.appName(app_name).getOrCreate()

    def create_dataframe(self, data, schema=None):
        """
        Create a DataFrame.

        Args:
            data (list of tuples or list of lists): The data to populate the DataFrame.
            schema (list of str or None): Optional schema for the DataFrame.

        Returns:
            pyspark.sql.DataFrame: The created DataFrame.
        """
        if schema:
            return self.spark.createDataFrame(data, schema)
        else:
            return self.spark.createDataFrame(data)

    def read_dataframe(self, path):
        """
        Read a DataFrame from a data source.

        Args:
            path (str): The path to the data source (e.g., CSV file).

        Returns:
            pyspark.sql.DataFrame: The read DataFrame.
        """
        return self.spark.read.format("csv").option("header", "true").option("inferSchema", "true").load(path)

    def display_dataframe(self, dataframe):
        """
        Display the contents of a DataFrame.

        Args:
            dataframe (pyspark.sql.DataFrame): The DataFrame to display.
        """
        dataframe.show()

    def close_session(self):
        """
        Close the SparkSession.
        """
        self.spark.stop()


# Example usage
data = [("Alice", 28), ("Bob", 25), ("Charlie", 22)]
schema = ["Name", "Age"]
df_handler = DataFrameHandler()
df = df_handler.create_dataframe(data, schema)
df_handler.display_dataframe(df)
df_handler.close_session()




