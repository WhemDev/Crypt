from datetime import datetime

TIME_STAMP_PATTERN = '%m/%d/%Y, %H:%M:%S'

def is_more_than_1_minutes(time: str):
    datetime_obj = datetime.strptime(time, TIME_STAMP_PATTERN)
    now = datetime.now()

    calculated_time = now - datetime_obj
    print(calculated_time)
    print(bool(calculated_time.seconds // 90))
    return bool(calculated_time.seconds // 90)

is_more_than_1_minutes('09/11/2022, 17:29:00')