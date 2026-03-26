# Utility functions
from datetime import datetime

def calculate_cycle_time(created_at, resolved_at):
    delta = resolved_at - created_at
    return delta.days

def is_after_hours(timestamp: datetime) -> bool:
    return timestamp.hour < 9 or timestamp.hour > 18
