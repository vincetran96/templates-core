'''Tests time functions
'''
import timeit


NUMBER = 100000
results = {}


if __name__ == "__main__":
    results["time.time()"] = timeit.timeit(
        setup="import time", stmt="time.time()",
        number=NUMBER
    )
    results["datetime.now().timestamp()"] = timeit.timeit(
        setup="import datetime", stmt="datetime.datetime.now().timestamp()",
        number=NUMBER
    )
    results["datetime.now()"] = timeit.timeit(
        setup="import datetime", stmt="datetime.datetime.now()",
        number=NUMBER
    )
    results["datetime.utcnow()"] = timeit.timeit(
        setup="import datetime", stmt="datetime.datetime.utcnow()",
        number=NUMBER
    )
    results["pytz.UTC.localize(datetime.utcnow())"] = timeit.timeit(
        setup="import datetime; import pytz",
        stmt="pytz.UTC.localize(datetime.datetime.utcnow())",
        number=NUMBER,
    )
    results["tz.localize(datetime.utcnow())"] = timeit.timeit(
        setup="import datetime; import pytz; a_timezone = pytz.timezone('America/Los_Angeles')",
        stmt="a_timezone.localize(datetime.datetime.utcnow())",
        number=NUMBER,
    )
