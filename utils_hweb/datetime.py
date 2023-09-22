'''Datetime utils
'''
from datetime import datetime, timedelta
from utils.configs import DATE_FORMAT


def generate_dates(start: str, end: str, format=DATE_FORMAT):
    '''Generates dates between two dates (inclusive)

    Returns a list of string representing the dates

    ---
    :params:
    ---
    start: date as string (e.g., '2022-01-01')
    end: date as string (e.g., '2022-01-01')

    Useful when getting daily data (e.g., event_date = ...)

    >>> generate_dates('2023-01-01', '2023-01-31')
    '''
    start_date = datetime.strptime(start, format)
    end_date = datetime.strptime(end, format)
    check = end_date >= start_date
    if not check:
        raise ValueError

    current_date = start_date
    dates = [current_date]
    while current_date < end_date:
        current_date = current_date + timedelta(days = 1)
        dates.append(current_date)
    dates = [ date.strftime(format) for date in dates ]
    return dates

def generate_dates_step(start: str, end: str, step: int, format=DATE_FORMAT):
    '''Generate dates between two dates (inclusive), with step as number of days;
    Does not go pass the end date

    Returns a list of tuples of string representing the start, end dates for each period
    
    ---
    :params:
    ---
    step: number of steps in days

    ---
    For example: with start = '2023-01-01', end = '2023-01-31' and step = 6,
    we have:

    generate_dates_step('2023-01-01', '2023-01-31', 6)
    [(2023-01-01, 2023-01-07), ..., (2023-01-29, 2023-01-31)]
    '''
    start_date = datetime.strptime(start, format)
    max_date = datetime.strptime(end, format)
    check = max_date >= start_date and step >= 0
    if not check:
        raise ValueError("Check your date arguments")
    
    dates = []
    current_date = start_date
    
    # Step forward `step` days, limit the value of end_date to be max_date
    #   so we don't go pass the `end` param
    while current_date <= max_date:
        end_date = current_date + timedelta(days = step)
        dates.append((current_date, min(end_date, max_date)))
        current_date = end_date + timedelta(days = 1)
    dates = [ tuple(map(lambda x: x.strftime(format), date_tuple)) for date_tuple in dates ]
    
    # If the last tuple contains only one day, move it to the 2nd-last tuple
    if dates[-1][0] == dates[-1][1] and len(dates) > 1:
        last_date = dates.pop()
        dates[-1] = (dates[-1][0], last_date[1])
    return dates

def date_to_str(d: datetime, format=DATE_FORMAT):
    '''Date to str of format
    '''
    return d.strftime(format)

def str_to_date(str: str, format=DATE_FORMAT):
    '''Str to date of format
    '''
    return datetime.strptime(str, format)

def now():
    '''Returns datetime of now
    '''
    return datetime.now()
