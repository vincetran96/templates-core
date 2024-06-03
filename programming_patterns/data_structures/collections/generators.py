"""Generators
"""


def gen():
    """Generator, like from consuming a Kafka topic
    """
    for i in range(100):
        yield f"number {i}"
        print(f"commit {i}")


def process():
    """Process data from generator;
    After processing, consumption is committed
    """
    for s in gen():
        print(f"process: {s}")


if __name__ == "__main__":
    process()
