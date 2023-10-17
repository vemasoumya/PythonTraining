# Pythontraining

# Prerequisites:

- Installed Java (tested 1.8.0_371)
- Installed Python (tested 3.10.11)
- Setup Python

Within the repository root directory run python -m venv .venv
1. Start virtual environment using ..venv\Scripts\activate.
2. Create a file requirements.txt in root directory.
3. Add required libraries which you want to use.
4. Install required python libraries using pip install -r requirements.txt


""" Settings required for running Pyspark applications locally."""
## General
os.environ["ENV"] = "dev"

## Spark and Hadoop ##
os.environ["PYSPARK_PYTHON"] = "python"
os.environ["HADOOP_OPTIONAL_TOOLS"] = "hadoop-azure"
os.environ["HADOOP_HOME"] = "C:\\Spark\\spark-3.3.2-bin-hadoop3\\hadoop"
os.environ["SPARK_HOME"] = "C:\\Spark\\spark-3.3.2-bin-hadoop3"
os.environ["SPARK_LOCAL_IP"] = "localhost"


How to create a wheel file 

1. Set your Python project directory
        $projectDirectory = "C:\Users\makum\Desktop\python\Pythontraining\Session4New"
2. Navigate to the project directory
        Set-Location -Path $projectDirectory
3. Specify the custom name for the Wheel file
        $customWheelFilename = $customWheelFilename = "Streaming_utils.whl" 
3. Create the Wheel file
        python setup.py bdist_wheel $customWheelFilename             

# Or you can directly use below code to create whl file

python setup.py bdist_wheel


# Cluster Setup

First you need to enable the feature on your Databricks cluster. Your cluster must be using Databricks Runtime 5.1 or higher. In the web UI edit your cluster and add this/these lines to the spark.conf:

spark.databricks.service.server.enabled true

If you are using Azure Databricks also add this line:

spark.databricks.service.port 8787

Restart your cluster.
