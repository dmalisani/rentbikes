import iso8601
from datetime import datetime, timedelta
import math

RATE_RENT = {
    "hour": 5,
    "day": 20,
    "week": 60
}
FAMILY_DISCOUNT_PERCENTAJE = 30

def _normalize_datetime(dt):
    if isinstance(dt, str):
        try:
            parse = iso8601.parse_date(dt)
        except iso8601.iso8601.ParseError:
            raise ValueError('Invalid given datetime')
        return parse
    elif isinstance(dt, datetime):
        return dt
    else:
        raise ValueError('Invalid given datetime')

def _split_datetime(difference):
    weeks = int(difference.days / 7)
    days = difference.days - (weeks * 7)
    hours = math.ceil(difference.seconds / 3600)
    return weeks, days, hours


class Rent():
    rented_periods = []
    def __init__(self, customer_name, passport=None):
        self.customer = customer_name
        self.passport = passport
    
    def add_rented_period(self, bikes, start_datetime, end_datetime):
        budget = getquote(bikes, start_datetime, end_datetime)
        if not isinstance(budget, float) and not isinstance(budget, int):
            raise ValueError(budget)
        current_rent = {
            "bikes": bikes,
            "starts_at": start_datetime,
            "ends_at": start_datetime,
            "paid": budget
            }
        self.rented_periods.append(current_rent)
        return current_rent


def getquote(bikes, start_datetime, end_datetime):
    try:
        start = _normalize_datetime(start_datetime)
        end = _normalize_datetime(end_datetime)
        assert (bikes > 0 and bikes <= 5)
        assert start < end
    except Exception:
        return "Parameters error"
    
    difference = end - start
    try:
        assert difference >= timedelta(hours=1)
        assert difference <= timedelta(days=90)
    except AssertionError:
        return "At least 1h and less than 3 months rental is required"

    weeks, days, hours = _split_datetime(difference)
    budget = (
        weeks * RATE_RENT["week"] + \
        days * RATE_RENT["day"] + \
        hours * RATE_RENT["hour"])
    if bikes >= 3:
        budget -= budget * FAMILY_DISCOUNT_PERCENTAJE / 100
    budget = budget * bikes
    return budget
