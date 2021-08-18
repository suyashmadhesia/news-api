from datetime import datetime, date, time, timedelta
from pytz import timezone
from secrets import token_urlsafe


def get_ist():
    return datetime.now(timezone('Asia/Kolkata'))


def get_ist_time():
    return get_ist().time()


def get_ist_date():
    return get_ist().date()


def comment_id_generator() -> str:
    uid = token_urlsafe(11) + str(get_ist_time())
    return f'{uid}'


def news_id_generator() -> str:
    nid = token_urlsafe(5) + str(get_ist_time())
    return f"{nid}"
