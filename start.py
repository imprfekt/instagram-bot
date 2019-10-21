from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint, shuffle
from helpers import *
from constants import user, pwd

# import pandas as pd


def get_comment_box():
    return web.find_element_by_css_selector('textarea')


# chromedriver_path = 'C:\\chromedriver.exe' # Change this to your own chromedriver path!
chromedriver_path = '/usr/local/bin/chromedriver'  # Change this to your own chromedriver path!
web = webdriver.Chrome(executable_path=chromedriver_path)

web.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

sleep(2)
username = web.find_element_by_name('username')
username.send_keys(user)
password = web.find_element_by_name('password')
password.send_keys(pwd)
password.send_keys(Keys.ENTER)

sleep(randint(3, 6))

# comment these 2 lines out, if you don't get a pop up asking about notifications
# notnow = web.find_element_by_css_selector("[role='dialog']")
# notnow.click()

hashtags = ['fashionvideos', 'modeling', 'gaymodel', 'malemodel', 'malemodels', 'fashion', 'fashionbeauty',
            'fashionphotography', 'belgrade', 'fashionvideos', 'fashionmovies', 'visualart', 'portrait', 'people',
            'model', 'fashionmodel', 'gayvid', 'gaymovie', 'fashionbeauty']
shuffle(hashtags)

for hashtag in hashtags:
    web.get('https://www.instagram.com/explore/tags/' + hashtag)
    sleep(randint(2, 5))
    first_thumbnail = web.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')

    first_thumbnail.click()
    sleep(randint(2, 5))

    # How many photos for this hashtag you want to interact with?
    for x in range(1, randint(12, 50)):
        if randint(1, 2) < 2:
            # Liking the picture
            empty_hearts = web.find_elements_by_css_selector('article [aria-label="Like"]')

            for btn in empty_hearts:
                if randint(1, 100) <= 40:
                    btn.click()
                    sleep(randint(2, 5))
        else:
            if randint(1, 100) < 40:
                comment = get_comment()
                get_comment_box().click()
                sleep(randint(2, 4))
                get_comment_box().send_keys(comment)
                sleep(randint(2, 5))
                web.find_element_by_css_selector('button[type="submit"]').click()
                sleep(randint(3, 5))

        web.find_element_by_xpath('/html/body').send_keys(Keys.RIGHT)
        sleep(randint(2, 6))
