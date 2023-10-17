from pyspark.sql import SparkSession
class CSVStreamReader:
    
    def __init__(self, spark, input_path, output_path, checkpoint_location, schema, trigger_interval="10 seconds"):
        """
        Initialize the CSVStreamReader with SparkSession and configuration parameters.

        :param spark: PySpark SparkSession.
        :param input_path: The path to the input CSV file or directory.
        :param output_path: The path where to write the streaming output.
        :param checkpoint_location: The path for checkpointing (must be a directory).
        :param trigger_interval: Trigger interval for streaming processing (e.g., "10 seconds").
        """
        self.spark = spark
        self.input_path = input_path
        self.output_path = output_path
        self.checkpoint_location = checkpoint_location
        self.trigger_interval = trigger_interval
        self.schema = schema

    def read_csv_streaming(self):
        # Read the CSV file as a streaming DataFrame
        df = self.spark.readStream \
            .option("header", "true") \
            .schema(self.schema) \
            .csv(self.input_path)
        
        return df

    def write_csv_streaming(self, df):
        # Define your processing logic on csv_stream here if needed

        # Write the streaming DataFrame to an output path
        query = df.writeStream \
            .outputMode("append") \
            .format("delta")  \
            .option("path", self.output_path) \
            .option("checkpointLocation", self.checkpoint_location) \
            .trigger(processingTime='0 seconds')  # Set the trigger interval as needed
            #.trigger(once=True)  # Set the trigger interval as needed
            

        # Start the streaming query
        streaming_query = query.start()

        # Wait for the streaming query to terminate
        streaming_query.awaitTermination()