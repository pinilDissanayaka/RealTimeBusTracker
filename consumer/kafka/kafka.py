from pykafka import KafkaClient
import json



def get_client(host="localhost", port = 9092):
    client = KafkaClient(hosts=f"{host}:{port}")
    return client


def get_topic(client, topic_name):
    return client.topics[topic_name]    


def get_producer(topic_name="busdatat"):
    client = get_client()
    topic = get_topic(client, topic_name)
    return topic.get_producer()


def preduce_data(data:dict, topic_name="busdatat"):
    data=json.dumps(data)
    producer = get_producer(topic_name)
    producer.produce(data.encode("utf-8"))
    
    




