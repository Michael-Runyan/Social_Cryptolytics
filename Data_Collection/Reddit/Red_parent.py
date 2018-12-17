import csv
import os

class Red_parent(object):
    base_url = 'https://api.pushshift.io/reddit/search/'
    @staticmethod
    def save_as_csv(dates,texts,result_type,folder,topic):
        clean_text = Red_parent.clean_results(texts)
        file_loc = 'C:\\Users\\Michael\\Reddit_3\\output\\' + result_type + '\\' + folder
        if not os.path.exists(file_loc):
            os.makedirs(file_loc)
        file_name =  file_loc + '\\' + topic + '.csv'
        with open(file_name, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(dates)
            writer.writerow(clean_text)

            # trying to get rid of the unicode characters

    @staticmethod
    def clean_results(texts):
        str_texts = []
        for x in range(len(texts)):
            import unicodedata

            if isinstance(texts[x], str):
                raw_text = texts[x]
                convert_text = unicodedata.normalize('NFKD', raw_text).encode('ascii', 'ignore')
                str_texts.append(convert_text)

        data = str_texts

        return data