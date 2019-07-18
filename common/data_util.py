import numpy as np

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

from common.memory_util import optimize_dataframe_datatype


def one_hot_manually(data_list, categories):
    """
    One-Hot encode manually
    :param data_list: data need to be one-hot encoded , like labels
    :param categories: how many categories
    :return: encoded data array

    Other One-Hot Methods:
        1. sklearn.preprocessing.OneHotEncoder:
            OneHotEncoder().fit_transform(data_list.reshape(-1, 1)).toarray()
        2. keras.utils.to_categorical:
            to_categorical(data_list)
    """
    data_array = np.zeros((len(data_list), categories))
    for i in range(len(data_list)):
        data_array[i, data_list[i]] = 1
    return data_array


def generator_batches(x, y, bsize=50):
    """
    generator batch data from data x and y
    :param x: data x, like train_data
    :param y: data y, like train_label
    :param bsize: batch size
    :return: generator batch data
        Usage:  for b_x, b_y in generator_batches(x, y, 50) ...
    """
    n = len(x) // bsize
    x, y = x[:n * bsize], y[:n * bsize]
    for i in range(0, len(x), bsize):
        yield x[i:i + bsize], y[i:i + bsize]


def feature_extract_by_sklearn(pandas_df, col_names):
    """
    extract features by sklearn tool of pandas DataFrame at specific columns
    :param pandas_df: pandas DataFrame
    :param col_names: names of specific columns, like ['uId', 'gender', 'age', ...]
    :return: features array
    """
    feature_array = []
    # optimize the data type, and fill missing value with 0
    pandas_df = optimize_dataframe_datatype(pandas_df, fill_missing=True)
    for col_name in col_names:
        # integer encode
        pandas_df[col_name] = LabelEncoder().fit_transform(pandas_df[col_name].values)
        # binary encode
        col_feature = OneHotEncoder().fit_transform(pandas_df[col_name].values.reshape(-1, 1))
        # print(col_feature.shape)
        if len(feature_array) > 0:
            # 'np.hstack' with low efficiency, which needs to be improved for very large data
            feature_array = np.hstack((feature_array, col_feature.toarray()))
        else:
            feature_array = col_feature.toarray()
    return feature_array
