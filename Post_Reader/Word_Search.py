import csv
import numpy as np
import pandas as pd
import os

class word_search(object):

    #creates instance of the class with proper time and words
    def __init__(self,word_file,time_file):
        with open(word_file,mode='r',encoding='UTF-8') as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        if content.__contains__(' '):
            content.remove(' ')
        word_dict = {i: 0 for i in content}

        # creates a numpy array of the words to search for
        self.word_np = np.array(content)

        time_df = pd.read_csv(time_file)
        time_str = []
        # I had spaces on either side here and I'm not sure why
        for ele in time_df['time']:
            time_str.append(str(ele))

        # creates an array of 0 with the shape of the words and times
        place_holer = np.zeros(shape=(len(time_str), len(self.word_np)))

        self.matrix = pd.DataFrame(data=place_holer, index=time_str, columns=self.word_np)


    def search(self,posts_file):
        dates = []
        texts = []

        csvfile = open(posts_file, 'rt')
        output = csv.reader(csvfile)
        dates = next(output)
        texts = next(output)

        post_num = 0
        for index in range(len(dates)):
            time = dates[index]
            day = 1231459200
            while int(float(time)) > day:
                day = day + 86400
            day = day - 86400

            # loops through every key word
            for key in self.word_np:
                wrd_loc = 0
                wrd_count = 0
                sample = texts[index]
                # loops through the post finding key word until the post does not contain the key word
                # (shrinks the post from back of key word every time)
                while wrd_loc is not -1:
                    # works only in uppercase to count all instances
                    wrd_loc = sample.upper().find(key)
                    # find returns -1 when it is not contained and moves on to next word
                    if (wrd_loc == -1):
                        break
                    # checks the key is part of another word by checking if there is another letter in
                    # front or behind it, if not adds the word to the word count
                    if not (sample[wrd_loc - 1:wrd_loc].isalpha() or sample[wrd_loc + len(key):wrd_loc + len(
                            key) + 1].isalpha()):
                        wrd_count = wrd_count + 1
                    # shrinks the post to everything after the instance of the first key word
                    sample = sample[wrd_loc + len(key):]
                # adds the num of instances of key word to matrix
                self.matrix.loc[str(day), key] = self.matrix.loc[str(day), key] + wrd_count
            post_num = post_num + 1

    #saves file to inputed location
    def save(self,save_file):
        self.matrix.to_csv(save_file)