from datetime import datetime


def to_integer(datestring):
  dt_time=datetime.fromisoformat(datestring)
  return 10000*dt_time.year + 100*dt_time.month + dt_time.day
