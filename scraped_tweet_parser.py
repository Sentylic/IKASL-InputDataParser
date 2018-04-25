import utils

class ScrapedTweetParser:
    def __init__(self, out_dir, input_file):
        self.out_dir = out_dir
        self.input_file = input_file

    def parse_daily(self, group_by_1000s=False):
        with open(self.input_file, 'r') as input_f:
            tweets = input_f.readlines()
            created_dirs = set()
            for data in tweets:
                info = data.split('> ', 1)
                tweet = info[1][:-1]
                date = utils.get_date_from_raw(info[0])
                out_dir = self.out_dir + 'daily/' + date + '/'
                created_dirs.add(out_dir)
                output_file = out_dir + 'all/tweets'
                utils.create_file_if_not_exist(output_file)
                with open(output_file, 'a') as output_f:
                    output_f.write(tweet + '\n')
            if group_by_1000s:
                utils.group_by_1000s(created_dirs)
            return created_dirs
    
    def parse_weekly(self):
        pass

if __name__ == '__main__':
    input_dir = '/home/isura/Downloads/SL-racism-violence-tweets~2600-tweets/'
    output_dir = '/home/isura/Downloads/SL-racism-violence-tweets~2600-tweets/'
    created_dirs = set()
    for input_file in utils.get_all_files_in_dir(input_dir):
        print 'Processing', input_file
        parser = ScrapedTweetParser(output_dir, input_file)
        created_dirs.update(parser.parse_daily())
    utils.group_by_1000s(created_dirs)
