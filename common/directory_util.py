import os


def do_get_picture_filename(file_root, file_list):
    """
    help to get picture filenames list
    :param file_root: target file root
    :param file_list: target files list
    :return: picture filenames list
    """
    picture_list = []
    for file in file_list:
        suffix = file.split('.')[-1]
        # if you want other files, change 'jpg' and 'png' in the condition
        if suffix == 'jpg' or suffix == 'png':
            picture_list.append(file_root + '/' + file)
    return picture_list


def get_picture_filename_list(directory, layers=0):
    """
    get picture filenames list
    :param directory: home directory
    :param layers:
        how many layers of picture file to the home directory.
        default value is 0, and the max layers supported is 3
    :return: picture filenames list
    """
    picture_name_list = []
    for home_root, home_dirs, home_files in os.walk(directory):
        if layers == 0:
            picture_name_list.extend(do_get_picture_filename(home_root, home_files))
        else:
            for home_dir in home_dirs:
                for first_root, first_dirs, first_files in os.walk(home_root + '/' + home_dir):
                    if layers == 1:
                        picture_name_list.extend(do_get_picture_filename(first_root, first_files))
                    else:
                        for first_dir in first_dirs:
                            for second_root, second_dirs, second_files in os.walk(first_root + '/' + first_dir):
                                if layers == 2:
                                    picture_name_list.extend(do_get_picture_filename(second_root, second_files))
                                else:  # layers == 3
                                    for second_dir in second_dirs:
                                        for third_root, third_dirs, third_files in os.walk(
                                                second_root + '/' + second_dir):
                                            picture_name_list.extend(
                                                do_get_picture_filename(third_root, third_files))
                                            break  # os.walk(second_root + '/' + second_dir)
                                break  # os.walk(first_root + '/' + first_dir)
                    break  # os.walk(home_root + '/' + home_dir)
        break  # os.walk(directory)
    print('*************** Get Picture Filenames From', directory, 'Finished *****************')
    return picture_name_list
