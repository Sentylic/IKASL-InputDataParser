import json
import utils

class ScrapedTweetJsonParser:
    def __init__(self, out_dir, input_file):
        self.out_dir = out_dir
        self.input_file = input_file

    def parse(self, group_by_1000s=False):
        with open(self.input_file, 'r') as input_f:
            tweets = input_f.readlines()
            created_dirs = set()
            for data_json_str in tweets:
                data_json = json.loads(data_json_str)
                tweet = data_json['content']
                date = data_json['date']
                out_dir = self._dir_name(date)
                created_dirs.add(out_dir)
                output_file = out_dir + 'all/tweets'
                utils.create_file_if_not_exist(output_file)
                with open(output_file, 'a') as output_f:
                    output_f.write(tweet.encode('utf-8') + '\n')
            if group_by_1000s:
                utils.group_by_1000s(created_dirs)
            return created_dirs

    def _dir_name(self, date_str):
        return '{}daily/{}/'.format(self.out_dir, date_str)

if __name__ == '__main__':
    input_dir = '/home/isura/Downloads/facebook/'
    output_dir = '/home/isura/Downloads/facebook/'
    created_dirs = set()
    for input_file in utils.get_all_files_in_dir(input_dir):
        print 'Processing', input_file
        parser = ScrapedTweetJsonParser(output_dir, input_file)
        created_dirs.update(parser.parse())
    utils.group_by_1000s(created_dirs)
