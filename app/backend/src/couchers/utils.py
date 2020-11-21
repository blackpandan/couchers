from datetime import datetime

import pytz
from google.protobuf.timestamp_pb2 import Timestamp
from sqlalchemy.sql import func

utc = pytz.UTC


def Timestamp_from_datetime(dt: datetime):
    pb_ts = Timestamp()
    pb_ts.FromDatetime(dt)
    return pb_ts


def to_aware_datetime(ts: Timestamp):
    """
    Turns a protobuf Timestamp object into a timezone-aware datetime
    """
    return utc.localize(ts.ToDatetime())


def now():
    return datetime.now(utc)


def create_coordinate(lat, lng):
    return func.ST_SetSRID(func.ST_MakePoint(lng, lat), 4326)
