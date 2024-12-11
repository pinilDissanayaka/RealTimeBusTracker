from pykafka import KafkaClient
import json



def get_client(host="localhost", port = 9092):
    client = KafkaClient(hosts=f"{host}:{port}")
    return client


def get_topic(client, topic_name):
    return client.topics[topic_name]    


def get_consumer(topic_name="busdatat"):
    client = get_client()
    topic = get_topic(client, topic_name)
    return topic.get_simple_consumer()


def get_checkpoint():    
    for checkpoint in get_consumer():
            yield f'{checkpoint.value.decode()}\n\n'

