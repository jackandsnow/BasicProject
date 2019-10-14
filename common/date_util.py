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


def get_between_days(f_date, t_date):
    """
    get between days from f_date to t_date
    :param f_date: datetime or str, like '%Y-%m-%d'
    :param t_date: datetime or str, like '%Y-%m-%d'
    :return: everyday str list
    """
    days_list = []
    if isinstance(f_date, str):
        f_date = datetime.datetime.strptime(f_date, '%Y-%m-%d')
    if isinstance(t_date, str):
        t_date = datetime.datetime.strptime(t_date, '%Y-%m-%d')

    while f_date <= t_date:
        day_str = datetime.datetime.strftime(f_date, '%Y%m%d')
        days_list.append(day_str)
        f_date += datetime.timedelta(days=1)
    return days_list
