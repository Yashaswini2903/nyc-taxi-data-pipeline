from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("NYC Taxi Analysis").getOrCreate()

df = spark.read.csv("data/sample_data.csv", header=True, inferSchema=True)

# Data Cleaning
df = df.dropna()

# Aggregation
result = df.groupBy("payment_type").count()

result.show()

# Save as Parquet
result.write.mode("overwrite").parquet("output/parquet_data")

spark.stop()
