import pandas as pd


def get_memory_usage(pandas_obj):
    """
    return the memory usage of a pandas object
    :param pandas_obj: DataFrame or Series
    :return: How many memory used
    """
    if isinstance(pandas_obj, pd.DataFrame):  # It's a DataFrame
        usage_b = pandas_obj.memory_usage(deep=True).sum()
    else:  # It's a Series
        usage_b = pandas_obj.memory_usage(deep=True)
    # Transfer Byte to MByte
    usage_mb = usage_b / 1024 ** 2
    return "{:03.2f} MB".format(usage_mb)


def optimize_dataframe_datatype(pandas_df, fill_missing):
    """
    optimize the data type of DataFrame to decrease memory usage
    :param pandas_df: pandas DataFrame
    :param fill_missing: bool tag of whether to fill missing values
    :return: optimized DataFrame
    """
    # True: fill all missing values with 0
    if fill_missing is True:
        pandas_df.fillna(0, inplace=True)
    # False: drop all rows which contain missing values
    else:
        pandas_df.dropna(axis=0, how='any')
    print('Original Memory Usage: ', get_memory_usage(pandas_df))

    # Firstly transfer 'int64' to 'unsigned' or 'int'
    int64_series = pandas_df.select_dtypes(include=['int64']).dtypes
    if int64_series.empty is False:
        int64_index = int64_series.index
        # judge data, which is less than zero, is totally NaN or not
        if pandas_df[pandas_df[int64_index] < 0].isna().all().all():
            # print('*********************** No Negative Numbers **********************')
            pandas_df[int64_index] = pandas_df[int64_index].apply(pd.to_numeric, downcast='unsigned')
        else:
            # print('*********************** Negative Numbers Exist **********************')
            pandas_df[int64_index] = pandas_df[int64_index].apply(pd.to_numeric, downcast='integer')
        print('After Optimize "int64" type: ', get_memory_usage(pandas_df))

    # Secondly transfer 'float64' to 'float'
    float64_series = pandas_df.select_dtypes(include=['float64']).dtypes
    if float64_series.empty is False:
        float64_index = float64_series.index
        pandas_df[float64_index] = pandas_df[float64_index].apply(pd.to_numeric, downcast='float')
        print('After Optimize "float64" type: ', get_memory_usage(pandas_df))

    # Thirdly transfer 'object' to 'category'
    object_series = pandas_df.select_dtypes(include=['object']).dtypes
    if object_series.empty is False:
        object_index = object_series.index
        pandas_df[object_index] = pandas_df[object_index].astype('category')
        print('After Optimize "object" type: ', get_memory_usage(pandas_df))
    return pandas_df
