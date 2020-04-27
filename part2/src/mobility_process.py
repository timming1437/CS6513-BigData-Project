'''
Use Global_Mobility_Report.csv as first argument and source data file
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

dfMobility = spark.read.format('csv').options(header='true', inferschema='true').load(sys.argv[1])

dfMobility.createOrReplaceTempView("mobility")

result = spark.sql("SELECT date, \
    workplaces_percent_change_from_baseline, \
    transit_stations_percent_change_from_baseline, \
    residential_percent_change_from_baseline \
    FROM mobility \
    WHERE sub_region_1='New York' \
    AND (sub_region_2='' OR sub_region_2 IS NULL)")

result.write.csv('mobility.out')
