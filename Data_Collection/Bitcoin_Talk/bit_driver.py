from scrape_tools import scrape_tools
import time
import datetime

class bit_driver(scrape_tools):

    base_url ='https://bitcointalk.org/index.php?topic='

    #topic where you would like to start scraping from
    topic = 510879
    sec = 78
    sub_sec = 8
    file_num = 5
    while (topic < 5030294 ):

        current_url = base_url + str(topic) + '.'
        print(str(topic))
        save_indicator =scrape_tools.scrape_topic(current_url,sec,sub_sec,file_num)

        #determines what to save the file as
        if save_indicator:
            print('saving...')
            print(datetime.datetime.now())
            file_num = file_num + 1
        if file_num > 50:
            sub_sec = sub_sec + 1
            file_num = 1
            if sub_sec > 50:
                sec = sec+ 1
                sub_sec = 1
        topic = topic + 1
        time.sleep(1)
