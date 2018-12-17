#tools in scraping the bittalk forum


import requests
from bs4 import BeautifulSoup
import csv
import time
import datetime
import unicodedata
import os

class scrape_tools(object):


    base_url ='https://bitcointalk.org/index.php?topic='

    #scrapes a topic
    @staticmethod
    def scrape_topic(url,sec,sub_sec,file_num):
        all_dates = []
        all_texts = []
        page = 0
        page_turner = True

        while (page_turner):
            #adds the page number to
            data = scrape_tools.scrape_single_page(url + str(page))
            #if page comes back as non type or has no results it get skipped over
            if data == None or len(data[0])==0:
                break;
            page = page + 20
            #checks to see if the page has already been scraped, if it has it will save what it already has
            if len(all_dates) > 0 and all_dates[len(all_dates) - 1] == data[0][len(data[0]) - 1]:
                file_name = 'bit_' + str(sec) + '_' + str(sub_sec)+ '_' + str(file_num)
                scrape_tools.save_as_csv(all_dates, all_texts, 'sec_' + str(sec), 'sub_sec_' + str(sub_sec),file_name )
                #used to see if the results got saved
                return True;
            #appends the new page into the topic array
            for index in range(len(data[0])):
                all_dates.append(data[0][index])
                all_texts.append(data[1][index])



    @staticmethod
    def scrape_single_page(url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        posts = soup.find_all(class_='td_headerandpost')

        dates = []
        texts = []
        try:
            for post in posts:

                date = post.find(class_= 'smalltext').get_text()

                #weeds out the results which were not dates
                if date[0].isalpha():
                    unix_date = scrape_tools.string_to_unix_time(date)
                    #checks to see if the date could be read
                    if isinstance(unix_date,int):
                        print('Unreadable data')
                        return None
                    dates.append(unix_date)
                    sample = post.find(class_='post')
                    if sample.find(class_='quote') == None:
                        texts.append(post.find(class_='post').get_text())
                    else:
                        all_string = post.find(class_='post').get_text()
                        header = post.find(class_='post').find(class_='quoteheader').get_text()
                        reply = post.find(class_='post').find(class_='quote').get_text()
                        cut = len(header) + len(reply)
                        new_string = all_string[cut:]
                        texts.append(new_string)
        except AttributeError:
            return None
        data = dates,texts
        return data
    #these turns the format of the bittalk date to unix time. May not work with other strings
    @staticmethod
    def string_to_unix_time(input):
        month_dict = {"January": 1,
                      'February' :2,
                      'March' :3,
                      'April' :4,
                      'May' :5,
                      'June' :6,
                      'July' :7,
                      'August' :8,
                      'September' :9,
                      'October' :10,
                      'November' :11,
                      'December' :12
                      }
        month_num = 0
        for key,value in month_dict.items():
            if key in input:
                month_num = value
        if month_num == 0:
            print('Month Could Not Be Read!')
            return 0

        day_and_year = ''
        for character in input:
            if not character.isalpha():
                day_and_year = day_and_year + character

        day_and_year = day_and_year.lstrip()
        day = int(day_and_year[:2])
        year = int(day_and_year[4:-11])
        hour = int(day_and_year[10:-7])

        unix_time = time.mktime(datetime.datetime(year,month_num,day,hour).timetuple())
        return unix_time

    # trying to get rid of the unicode characters
    @staticmethod
    def clean_results(texts):
        str_texts = []
        for x in range(len(texts)):
            if isinstance(texts[x], str):
                raw_text = texts[x]
                convert_text = unicodedata.normalize('NFKD', raw_text).encode('ascii', 'ignore')
                str_texts.append(convert_text)

        data = str_texts

        return data

    def save_as_csv(dates, texts,sec, folder, topic):
        clean_text = scrape_tools.clean_results(texts)

        file_loc = '//home//ugrads//runyan//Summer-2018//Bittalk_3//output//' + sec + '//' + folder
        if not os.path.exists(file_loc):
            os.makedirs(file_loc)
        file_name = file_loc + '//' + topic + '.csv'
        with open(file_name, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(dates)
            writer.writerow(clean_text)
