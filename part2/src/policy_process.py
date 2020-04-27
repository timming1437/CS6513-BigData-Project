'''
Use 20200416_acaps_-_covid-19_goverment_measures_dataset_v8.csv as first argument and source data file
Process data cleaning and data integration
'''
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from pyspark.sql.functions import format_string
import sys
import pyspark.sql.functions as F

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.debug.maxToStringFields", "500") \
    .getOrCreate()

dfPolicy = spark.read.format('csv').options(header='true', inferschema='true').load(sys.argv[1])

dfPolicy.createOrReplaceTempView("policy")

result = spark.sql("SELECT * FROM policy \
    WHERE MEASURE LIKE 'New York' \
    OR COMMENTS LIKE 'New York'")

result.write.csv('policy.out')
