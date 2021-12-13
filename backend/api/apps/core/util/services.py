from enum import Enum
from datetime import datetime, time, timedelta
from dateutil.relativedelta import relativedelta
from typing import Tuple


class ServiceChoices(Enum):
    Hour = "Hour"
    Foot = "Foot"
    Yard = "Yard"
    Mile = "Mile"
    Unit = "Unit"

def rounder(n: int, nearest=15) -> float:
    return nearest * round(n/nearest)

def duration(service_date: datetime, in_time: Tuple, out_time: Tuple) -> float:
    in_time = datetime(*service_date, in_time.hour, rounder(in_time.minute), in_time.second)
    out_time = datetime(*service_date, out_time.hour, rounder(out_time.minute), out_time.second)
    diff = relativedelta(out_time, in_time)
    hours = diff.hours + (diff.minutes/60)
    if hours >= 0:
        return hours
    out_time += timedelta(days=1)
    diff = relativedelta(out_time, in_time)
    hours = diff.hours + (diff.minutes/60)
    return hours