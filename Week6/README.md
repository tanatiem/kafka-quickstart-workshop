Week6 (Outline)
6.1 What you've learned so far.
6.2 Spark streaming
6.3 Mobile sensors and user behaviors
6.4 Exercise

Setup Spark
1. Install java (version 8)
2. Install python
3. Download spark https://downloads.apache.org/spark/spark-2.4.7/spark-2.4.7-bin-hadoop2.6.tgz
4. Setup spark home SPARK_HOME=C:\spark-2.4.7-bin-hadoop2.6\
5. Test run "pyspark"

For window only
6. Create a hadoop\bin folder inside the SPARK_HOME folder
7. Download http://github.com/steveloughran/winutils/raw/master/hadoop-2.6.0/bin/winutils.exe to hadoop\bin
8. Setup hadoop home HADOOP_HOME=%SPARK_HOME%\hadoop

To run program (Wordcount)
1. Start a kafker cluster (zoo + brokers)
2. Create a topic
3. Run spark with the following commandline: spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.3.0 kafka_spark_demo.py
4. Run a producer to generate a list of words

REF
[1] https://spark.apache.org/docs/latest/streaming-programming-guide.html
