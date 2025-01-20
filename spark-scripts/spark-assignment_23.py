import pyspark
from pyspark.sql import functions as F
from pyspark.sql.functions import *

postgres_host = "dataeng-postgres"
postgres_dw_db = "warehouse"
postgres_user = "user"
postgres_password = "password"

sparkcontext = pyspark.SparkContext.getOrCreate(conf=(pyspark.SparkConf().setAppName("Dibimbing")))
sparkcontext.setLogLevel("WARN")

spark = pyspark.sql.SparkSession(sparkcontext.getOrCreate())

jdbc_url = f"jdbc:postgresql://{postgres_host}/{postgres_dw_db}"
jdbc_properties = {
    "user": postgres_user,
    "password": postgres_password,
    "driver": "org.postgresql.Driver",
    "stringtype": "unspecified",
}
# print(jdbc_properties)
df_retail = spark.read.jdbc(jdbc_url, "public.retail", properties=jdbc_properties)
print("===================== All Data Retail =====================")
df_retail = df_retail.withColumn("eom", last_day("invoicedate"))
df_retail = df_retail.withColumn("total_amount", round(df_retail["unitprice"]*df_retail["quantity"],2))
df_retail.show()
df_retail.printSchema()
# df_retail.select("country").distinct().show()
# df_retail.select("invoicedate").distinct().show()
# df_retail.select("eom").distinct().show()

print("===================== Top 10 Most Ordered Product =====================")
df_ordered = df_retail.groupBy("description").agg(F.sum("quantity").alias("quantity"))
df_ordered = df_ordered.orderBy("quantity", ascending=False).limit(10)
df_ordered.show()

print("===================== Sales Trend by Month =====================")
df_sales = df_retail.groupBy("eom").agg(round(F.sum("total_amount"),2).alias("total_amount"))
df_sales = df_sales.orderBy("eom", ascending=False).limit(10)
df_sales.show()

print("===================== Customer Segmentation by Country =====================")
df_sales = df_retail.groupBy("country") \
                    .agg(F.round(F.countDistinct("customerid"), 2).alias("total"))
df_sales = df_sales.orderBy("total", ascending=False).limit(10)
df_sales.show()

