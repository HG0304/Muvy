def isOverNight(segment) -> bool:
    """Return True if segment date is overnight (before 06:00 or from 22:00)."""
    dt = segment.date
    return dt.hour < 6 or dt.hour >= 22

def isSunday(segment) -> bool:
    """Return True if segment date is Sunday."""
    dt = segment.date
    return dt.weekday() == 6

