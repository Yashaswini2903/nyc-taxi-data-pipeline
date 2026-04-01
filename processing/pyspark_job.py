from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("NYC Taxi Analysis").getOrCreate()

# Load dataset
df = spark.read.csv("data/sample_data.csv", header=True, inferSchema=True)

# Remove null values for better data quality
df = df.dropna()

# Aggregate data to count trips by payment type
result = df.groupBy("payment_type").count()

result.show()

# Save output in Parquet format for efficient storage
result.write.mode("overwrite").parquet("output/parquet_data")

spark.stop()
