import pickle


def save_pkl_file(save_data, file_name):
    """
    save data to pkl file
    :param save_data: array data for saving
    :param file_name: filename for saving, like '/path/filename.pkl'
    :return: None
    """
    p = open(file_name, 'wb')
    pickle.dump(save_data, p)
    p.close()
    print('**************** Save Data To', file_name, 'Finished **************')


def load_pkl_file(file_name):
    """
    load data from pkl file
    :param file_name: pkl filename, like '/path/filename.pkl'
    :return: array data
    """
    p = open(file_name, 'rb')
    data = pickle.load(p, encoding='utf-8')
    p.close()
    print('*************** Load Data From', file_name, 'Finished *************')
    return data


def load_multi_pkl_file(file_name_list):
    """
    load data from multi pkl files
    :param file_name_list: filenames list, like ['/path/filename1.pkl', '/path/filename2.pkl', ...]
    :return: data list following the filename's order
    """
    all_data = []
    for file_name in file_name_list:
        p = open(file_name, 'rb')
        data = pickle.load(p, encoding='utf-8')
        all_data.append(data)
        p.close()
    print('*************** Load Data From Multi-pkl Files Finished *************')
    return all_data
