import datetime
import re


def is_valid_phone(number):
    pattern = r'^\+\d{1,25}$'
    return re.match(pattern, number) is not None


def is_valid_email(address):
    pattern = r'^[\w\.-]+@[\w\.-]+\.[\w\.-]+$'
    return re.match(pattern, address) is not None


def is_valid_site(link):
    pattern = r'^(https?:\/\/)+[\w\.-]+$'
    return re.match(pattern, link) is not None


def is_valid_date(number, method):
    try:
        date_str = datetime.datetime.strptime(number, "%d %m %Y")
        date_now = datetime.datetime.now()

        if method == 'more':
            if date_str >= date_now:
                return True
        else:
            if date_str <= date_now:
                return True
    except ValueError:
        return False
