"""Tests time functions
"""
import timeit
from pprint import pprint


TEST_TIMES = 100000
RESULTS = {}


if __name__ == "__main__":
    RESULTS["time.time()"] = timeit.timeit(
        setup="import time", stmt="time.time()",
        number=TEST_TIMES
    )
    RESULTS["datetime.now().timestamp()"] = timeit.timeit(
        setup="import datetime", stmt="datetime.datetime.now().timestamp()",
        number=TEST_TIMES
    )
    RESULTS["datetime.now()"] = timeit.timeit(
        setup="import datetime", stmt="datetime.datetime.now()",
        number=TEST_TIMES
    )
    RESULTS["datetime.utcnow()"] = timeit.timeit(
        setup="import datetime", stmt="datetime.datetime.utcnow()",
        number=TEST_TIMES
    )
    RESULTS["pytz.UTC.localize(datetime.utcnow())"] = timeit.timeit(
        setup="import datetime; import pytz",
        stmt="pytz.UTC.localize(datetime.datetime.utcnow())",
        number=TEST_TIMES,
    )
    RESULTS["tz.localize(datetime.utcnow())"] = timeit.timeit(
        setup="import datetime; import pytz; a_timezone = pytz.timezone('America/Los_Angeles')",
        stmt="a_timezone.localize(datetime.datetime.utcnow())",
        number=TEST_TIMES,
    )
    pprint(sorted(RESULTS.items(), key=lambda x: x[1]))
