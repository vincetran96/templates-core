'''Kafka Consumer sample

Here we use the `closing` class from contextlib
and use a context maneger to properly close the consumer instance
'''
from contextlib import closing

from kafka import KafkaConsumer


def main():
    '''Main program
    '''
    def create_consumer(topic: str) -> closing[KafkaConsumer]:
        return closing(
            KafkaConsumer(
                topic,
                bootstrap_servers="localhost:9094",
                group_id="group0",
                enable_auto_commit=True
            )
        )

    with create_consumer("topic0") as consumer:
        for msg in consumer:
            msg_content: str = msg.value.decode()
            print(msg.offset)
            print(msg_content)


if __name__ == "__main__":
    main()
