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

dfConfirm = spark.read.format('csv').options(header='true', inferschema='true').load(sys.argv[1])

dfConfirm.createOrReplaceTempView("confirm")

result = spark.sql("SELECT Country_Region,3/1/2020,3/2/2020,3/3/2020,3/4/2020,3/5/2020,3/6/2020,3/7/2020,3/8/2020,3/9/2020,3/10/2020,\
    3/11/2020,3/12/2020,3/13/2020,3/14/2020,3/15/2020,3/16/2020,3/17/2020,3/18/2020,3/19/2020,3/20/2020,\
    3/21/2020,3/22/2020,3/23/2020,3/24/2020,3/25/2020,3/26/2020,3/27/2020,3/28/2020,3/29/2020,3/30/2020,3/31/2020,\
    4/1/2020,4/2/2020,4/3/2020,4/4/2020,4/5/2020,4/6/2020,4/7/2020,4/8/2020,4/9/2020,4/10/2020,\
    4/11/2020,4/12/2020,4/13/2020,4/14/2020,4/15/2020\
    FROM confirm \
    WHERE Province_State='New York' ")

result.write.csv('confirm.out')
