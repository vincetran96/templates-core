'''Kafka Producer sample
'''
from kafka import KafkaProducer

from config import BOOTSTRAP_SERVER


def main():
    '''Main program
    '''
    producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVER)
    topic = "topic0"
    key = b"greeting"
    for i in range(10):
        message = f"Hello_{i}".encode()
        producer \
            .send(topic, key=key, value=message) \
            .add_callback(lambda rec: print(rec)) \
            .add_errback(lambda exc: print(exc))

    producer.flush()


if __name__ == "__main__":
    main()
