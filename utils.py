import os
from os.path import isfile, join

def create_file_if_not_exist(file):
    if not os.path.exists(os.path.dirname(file)):
        os.makedirs(os.path.dirname(file))

def get_all_files_in_dir(dir):
    return [join(dir, path) for path in os.listdir(dir) if isfile(join(dir, path))]

def get_date_from_raw(raw):
    return raw.split(' ', 2)[1]

def group_by_1000s(created_dirs):
    for created_dir in created_dirs:
        with open(created_dir + 'all/tweets', 'r') as tweet_file:
            tweets = tweet_file.readlines()
            n = len(tweets)
            for i in range(0, n, 1000):
                chunk = tweets[i: min(i + 1000, n)]
                output_file = created_dir + str(i / n) + '/tweets'
                create_file_if_not_exist(output_file)
                with open(output_file, 'w') as output_f:
                    output_f.writelines(chunk)
