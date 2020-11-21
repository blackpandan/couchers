from datetime import datetime

import pytz
from geoalchemy2.shape import to_shape
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
    """
    Creates a WKT point from a (lat, lng) tuple in EPSG4326 coordinate system (normal GPS-coordinates)
    """
    return func.ST_SetSRID(func.ST_MakePoint(lng, lat), 4326)


def get_coordinates(geom):
    """
    Returns EPSG4326 (lat, lng) pair for a given WKT geom object
    """
    shp = to_shape(geom)
    # note the funiness with 4326 normally being (x, y) = (lng, lat)
    return (shp.y, shp.x)
