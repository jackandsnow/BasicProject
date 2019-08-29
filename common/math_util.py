def get_median(data_list):
    """
    get median form data list
    :param data_list: data list
    :return: median
    """
    data_list.sort()
    length = len(data_list)
    half = length // 2
    if length % 2 == 0:
        return (data_list[half] + data_list[~half]) / 2
    else:
        return data_list[half]
