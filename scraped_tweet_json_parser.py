import json
import utils

class ScrapedTweetJsonParser:
    def __init__(self, out_dir, input_file, tweet_frequency):
        self.out_dir = out_dir
        self.input_file = input_file
        self.tweet_frequency = tweet_frequency

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
                output_file = out_dir + '/all/tweets'
                utils.create_file_if_not_exist(output_file)
                with open(output_file, 'a') as output_f:
                    output_f.write(tweet.encode('utf-8') + '\n')
            if group_by_1000s:
                utils.group_by_1000s(created_dirs)
            return created_dirs

    def _dir_name(self, date_str):
        return '{}/{}/{}'.format(self.out_dir, self.tweet_frequency.value, utils.get_dir_name(date_str, self.tweet_frequency))

if __name__ == '__main__':
    input_dir = '/home/isura/Documents/FYP/datasets/deletefacebook'
    output_dir = '/home/isura/Documents/FYP/datasets/deletefacebook'
    created_dirs = set()
    for input_file in utils.get_all_files_in_dir(input_dir):
        print 'Processing', input_file
        parser = ScrapedTweetJsonParser(output_dir, input_file, utils.TweetFrequency.daily)
        created_dirs.update(parser.parse())
    utils.group_by_1000s(created_dirs)
