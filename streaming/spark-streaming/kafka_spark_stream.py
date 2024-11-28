from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("KafkaSparkStreaming").getOrCreate()

df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "server-logs").load()

df.selectExpr("CAST(value AS STRING)").writeStream.outputMode("append").format("console").start().awaitTermination()
