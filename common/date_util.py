import datetime


def date_to_string(date, fmt=None, n=0):
    """
    transfer datetime to string
    :param date: datetime
    :param fmt: self defined format, like '%Y%m%d', etc.
    :param n: format list index from 0 to 3
    :return: string
    """
    format_list = ['%Y/%m/%d', '%Y-%m-%d', '%Y/%m/%d %H:%M:%S', '%Y-%m-%d %H:%M:%S']
    if not fmt:
        fmt = format_list[n]
    return date.strftime(fmt)


def string_to_date(date_str, fmt=None, n=0):
    """
    transfer string to datetime
    :param date_str: string
    :param fmt: self defined format, like '%Y%m%d', etc.
    :param n: format list index from 0 to 3
    :return: datetime
    """
    format_list = ['%Y/%m/%d', '%Y-%m-%d', '%Y/%m/%d %H:%M:%S', '%Y-%m-%d %H:%M:%S']
    if not fmt:
        fmt = format_list[n]
    return datetime.datetime.strptime(date_str, fmt)
