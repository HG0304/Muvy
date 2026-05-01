from datetime import datetime

def isOverNight(segment) -> bool:
    """Return True if segment date is overnight (before 06:00 or from 22:00)."""
    dt = segment.date
    return dt.hour < 6 or dt.hour >= 22

def isSunday(segment) -> bool:
    """Return True if segment date is Sunday."""
    dt = segment.date
    return dt.weekday() == 6

def isValidDistance(segment) -> bool:
    """Return True if the segment distance is valid (a positive number)."""
    return (segment.distance is not None
            and isinstance(segment.distance, (int, float))
            and segment.distance > 0)

def isValidDate(segment) -> bool:
    """Return True if the segment date is valid (a datetime object)."""
    return segment.date is not None and isinstance(segment.date, datetime)