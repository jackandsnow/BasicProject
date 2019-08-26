def generate_dict_with_same_value(key_list, value):
    """
    generate a dict with key list and single value
    :param key_list: dict keys
    :param value: specific value
    :return: new dict
    """
    return dict.fromkeys(key_list, value)


def generate_dict(key_list, value_list):
    """
    generate dict with key list and value list
    :param key_list: dict keys
    :param value_list: dict values
    :return: new dict
    """
    return dict(zip(key_list, value_list))


def get_sub_dict(all_dict, sub_keys):
    """
    get subset of a dict for specific sub_keys
    :param all_dict: target dict
    :param sub_keys: wanting keys
    :return: sub_dict
    """
    return dict((key, value) for key, value in all_dict.items() if key in sub_keys)
