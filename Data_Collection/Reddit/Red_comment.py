# I named this class wrong


import requests
from bs4 import BeautifulSoup
from Red_parent import Red_parent

class push_shift_submission(Red_parent):
    search_time = 1489788935
    num_files = 1
    section = 1
    while int(search_time) > 1284163200:
        dates = []
        texts = []

        #change submissions to comments if you'd like to scrape comments
        url = Red_parent.base_url + 'submission/?subreddit=bitcoin&size=500&before=' + str(search_time)

        page = requests.get(url).json()

        for index in range(len(page['data'])):
            texts.append(page['data'][index]['title'])
            dates.append(page['data'][index]['created_utc'])

        Red_parent.save_as_csv(dates,texts,'submissions','sec_' + str(section) ,'sub_' + str(num_files))
        num_files = num_files + 1
        if num_files > 50:
            section = section+ 1
            num_files = 0

        search_time = dates[len(dates)-1]
        print (search_time)