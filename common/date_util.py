import datetime


def date_to_string(date, n=0):
    """
    transfer datetime to string
    :param date: datetime
    :param n: format index from 0 to 3
    :return: string
    """
    fmt = ['%Y/%m/%d', '%Y-%m-%d', '%Y/%m/%d %H:%M:%S', '%Y-%m-%d %H:%M:%S']
    return date.strftime(fmt[n])


def string_to_date(date_str, n=0):
    """
    transfer string to datetime
    :param date_str: string
    :param n: format index from 0 to 3
    :return: datetime
    """
    fmt = ['%Y/%m/%d', '%Y-%m-%d', '%Y/%m/%d %H:%M:%S', '%Y-%m-%d %H:%M:%S']
    return datetime.datetime.strptime(date_str, fmt[n])
