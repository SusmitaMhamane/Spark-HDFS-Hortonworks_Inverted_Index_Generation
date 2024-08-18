#!/usr/bin/python
#
# Author: Susmita Mhamane
# Date: 8 June 2024
#

from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("Spark SQL basic example").enableHiveSupport().getOrCreate()
sc = spark.sparkContext


from pyspark import SparkContext, SparkConf

# Read the input file from HDFS
lines = sc.textFile("hortonworks.txt")

# Create key-value pairs (URL, terms)
pairs = lines.map(lambda line: line.split(',', 1))

# Explode pairs to create (term, URL) pairs for each term in terms list
term_url_pairs = pairs.flatMap(lambda pair: [(term.strip(), pair[0]) for term in pair[1].split(',')])

# Group by key (term) to collect all URLs where each term appears
inverted_index = term_url_pairs.groupByKey().mapValues(list)

# Print the inverted index (term, list of URLs)
for term, urls in inverted_index.collect():
    print(f"{term}: {', '.join(urls)}")


