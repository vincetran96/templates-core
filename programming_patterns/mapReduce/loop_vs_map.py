"""Compares code style between looping and mapping
"""
from typing import List


x_range = range(1000)
fake_data: dict = dict(map(lambda x: (x, f"c_{x}"), x_range))
fake_data[1000] = "broken"


def _process(i: int) -> None:
    """Creates some side effect instead of
    returning a value
    """
    print(f"Processed {i}")


def _process_chunk(chunk: List[int]) -> None:
    """Processes a chunk of data
    """
    for i in chunk:
        _process(i)


def looper(data: dict, chunksize: int = 7) -> None:
    """Uses loop to process data
    """
    suffixes = []
    for _, value in data.items():
        try:
            suffix = value.split("_")[1]
            suffixes.append(suffix)
        except IndexError:
            print(f"Skipping broken data: {value}")
            continue
        if len(suffixes) == chunksize:
            _process_chunk(suffixes)
            suffixes = []
    if suffixes:
        _process_chunk(suffixes)


def mapper(data: dict, chunksize: int = 7):
    """Users map to process data
    """
    def generate():
        """Generates lists of data
        """
        suffixes = []
        for _, value in data.items():
            try:
                suffix = value.split("_")[1]
                suffixes.append(suffix)
            except IndexError:
                print(f"Skipping broken data: {value}")
                continue
            if len(suffixes) == chunksize:
                yield suffixes
                suffixes = []
        if suffixes:
            yield suffixes

    results = list(map(_process_chunk, generate()))
    return results


if __name__ == "__main__":
    looper(fake_data)
    mapper(fake_data)
