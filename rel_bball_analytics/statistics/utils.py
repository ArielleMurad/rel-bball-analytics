def time_to_int(time: str):
    """Convert time strings from api response to int"""
    if time is None:
        return time

    if ":" in time:
        mins, secs = time.split(":")
        result = int(mins) + int(secs) / 60
    else:
        result = int(time)

    return round(result, 2)
