from datetime import datetime


def get_date_time():
    now = datetime.now()
    date_time_string = now.strftime("%d/%m/%Y %H:%M:%S")

    return date_time_string
