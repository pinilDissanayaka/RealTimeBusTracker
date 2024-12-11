from pykafka import KafkaClient



client= KafkaClient(hosts='localhost:9092')

topic = client.topics["busdata"]


producer= topic.get_sync_producer()





def preduce_data():
    producer.produce("Hello World".encode("utf-8"))
     