def time_difference(duration):
    minutes, seconds = divmod(duration, 60)
    hours, minutes = divmod(minutes, 60)

    formatted_duration = ""

    if hours > 0:
        formatted_duration += f"{int(hours)}h"
    if minutes > 0:
        formatted_duration += f"{int(minutes)}m"
    if seconds > 0 or not formatted_duration:
        formatted_duration += f"{int(seconds)}s"

    return formatted_duration

def clean_datetime(datetime):
    return datetime.strftime("%b %d %Y %I:%M:%S%p")