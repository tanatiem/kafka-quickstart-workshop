Week3
1. Basic setup (My first topic)
1.1 Start kafka cluster --> double click "1_1_start_cluster.bat".
1.2 Create a topic --> double click "create_my_first_topic.bat"
1.3 Start consumer --> double click "1_3_run_consumer_my_first_topic.bat"
1.4 Start producer --> double click "1_4_run_producer_my_first_topic.bat"
1.5 After finish testing, close all windows.

2. Word count
2.1 Start kafka cluster --> double click "1_1_start_cluster.bat".
2.2 Create a topic --> double click "2_1_create_streams_plaintext_input.bat"
2.3 Start producer --> double click "2_2_run_producer_wordcount.bat"
2.4	Start wordcount program --> double click "2_3_compile_word_count.bat" --> If built success, Click to continue.
2.5 Start consumer --> double click "2_4_run_producer_wordcount.bat"
2.6 Test it. You can type
"a a a" --> then enter
"a a b" --> then enter
in producer, and you will get a 5, b 1 in consumer
2.7 After finish testing, close all windows.
2.8. Install python https://github.com/confluentinc/confluent-kafka-python
2.9 close the consumer window (2.5)
2.10 Start a new consumer by using python --> type "python consumer-local.py" for text-mode version
2.11 After finish testing, close all windows.

3. Adding a filter functiont to word count (Allow only the value higher than 10 to stream to a consumer)
3.1 Start kafka cluster --> double click "1_1_start_cluster.bat".
3.2 Create a topic --> double click "2_1_create_streams_plaintext_input.bat"
3.3 Start producer --> double click "2_2_run_producer_wordcount.bat"
3.4	Modify code and then --> double click "2_3_compile_word_count.bat" --> If built success, Click to continue.
3.5 Start a new consumer by using python --> type "python consumer-local-plotgraph.py" for graph-mode version
3.6 Check your result

Homework1: หาคำที่มีนัยสำคัญ (ไม่ใช่ article a, an ,the, ...) ในนิยาย Harry potter
4. You can try iot by yourself














Reference
1. https://kafka.apache.org/20/javadoc/org/apache/kafka/streams/kstream/KStream.html#filter-org.apache.kafka.streams.kstream.Predicate-

Todo: register free cloud (Duck)
2. https://www.cloudkarafka.com/plans.html