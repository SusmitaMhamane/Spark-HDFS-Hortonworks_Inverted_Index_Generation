# Hortonworks Inverted Index Generation with Apache Spark

## Author

- **Name:** Susmita Mhamane
- **Date:** 7 June 2024

## Overview

This project demonstrates a basic use case of Apache Spark for processing and analyzing a simple dataset. The dataset consists of URLs and associated terms, which are used to create an inverted index. The inverted index maps each term to a list of URLs where that term appears.

## Files and Scripts

### `hortonworks.py`

This Python script utilizes PySpark to process the input file from HDFS. The key steps are:

1. **Initialize Spark Session**: Creates a Spark session with Hive support enabled.
2. **Read Input File**: Reads the `hortonworks.txt` file from HDFS into an RDD.
3. **Parse and Transform Data**: Splits each line into URL and terms, and then creates key-value pairs where the key is a term and the value is the URL.
4. **Generate Inverted Index**: Groups the data by term and aggregates the URLs.
5. **Output Results**: Prints the inverted index to the console.

### `hortonworks.sh`

This shell script manages the lifecycle of the input file on HDFS and submits the Spark job. It performs the following tasks:

1. **Check for Existing File**: Verifies if `hortonworks.txt` exists on HDFS. If it does, the script deletes the file.
2. **Upload File**: Copies the local `hortonworks.txt` file to the HDFS location.
3. **Submit Spark Job**: Runs the `hortonworks.py` script using `spark-submit`.

### `unset-jupyter.sh`

This script unsets environment variables related to Jupyter to ensure that PySpark runs in a non-Jupyter environment. It does the following:

- Unsets `PYSPARK_DRIVER_PYTHON` and `PYSPARK_DRIVER_PYTHON_OPTS`.

### `hortonworks.txt`

This text file contains a list of URLs, each followed by a comma-separated list of terms. The file is used as input for the Spark job to create the inverted index.

## Execution

1. **Prepare Environment**: Ensure that the necessary environment variables are unset by running `unset-jupyter.sh`.
2. **Run Shell Script**: Execute `hortonworks.sh` to check for the file on HDFS, upload the new file if needed, and submit the Spark job.
3. **View Results**: The results will be printed to the console, displaying the inverted index where each term is mapped to a list of URLs.

