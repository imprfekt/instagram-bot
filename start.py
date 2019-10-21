from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint, shuffle
from helpers import *


# import pandas as pd


def get_comment_box():
    return web.find_element_by_css_selector('textarea')


# chromedriver_path = 'C:\\chromedriver.exe' # Change this to your own chromedriver path!
chromedriver_path = '/usr/local/bin/chromedriver'  # Change this to your own chromedriver path!
web = webdriver.Chrome(executable_path=chromedriver_path)

web.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

sleep(2)
username = web.find_element_by_name('username')
username.send_keys('dusanjaukovic')
password = web.find_element_by_name('password')
password.send_keys('Solaris011')
password.send_keys(Keys.ENTER)

# button_login = web.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > button')
# button_login.click()
sleep(randint(2, 7))

# notnow = web.find_element_by_css_selector("[role='dialog']")
# notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications

hashtags = ['fashionvideos', 'modeling', 'gaymodel', 'malemodel', 'malemodels', 'fashion', 'fashionbeauty',
            'fashionphotography', 'belgrade', 'fashionvideos', 'fashionmovies', 'visualart', 'portrait', 'people',
            'model', 'fashionmodel', 'gayvid', 'gaymovie', 'fashionbeauty']
shuffle(hashtags)
# prev_user_list = []  # - if it's the first time you run it, use this line and comment the two below
# prev_user_list = pd.read_csv('20181203-224633_users_followed_list.csv', delimiter=',').iloc[:,1:2]
# useful to build a user log
# prev_user_list = list(prev_user_list['0'])

# new_followed = []
# tag = -1
# followed = 0
# likes = 0
# comments = 0
for hashtag in hashtags:
    web.get('https://www.instagram.com/explore/tags/' + hashtag)
    sleep(randint(2, 4))
    first_thumbnail = web.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
    # first_thumbnail = web.find_elements_by_css_selector('img[alt]')[1]

    first_thumbnail.click()
    sleep(randint(1, 4))

    for x in range(1, randint(15, 50)):
        comment = get_comment()
        get_comment_box().click()
        sleep(randint(2, 4))
        get_comment_box().send_keys(comment)
        sleep(randint(2, 5))
        # comment_box.send_keys(Keys.ENTER)
        web.find_element_by_css_selector('button[type="submit"]').click()
        sleep(randint(1, 4))

        # Liking the picture
        empty_hearts = web.find_elements_by_css_selector('[aria-label="Like"]')

        for btn in empty_hearts:
            if randint(1, 100) <= 45:
                btn.click()
                sleep(randint(1, 6))

        web.find_element_by_xpath('/html/body').send_keys(Keys.RIGHT)
        sleep(randint(2, 4))

        # username = web.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[1]/h2/a').text
        # if username not in prev_user_list:
        #     # If we already follow, do not unfollow
        #     if web.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':

        #         web.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()

        #         #new_followed.append(username)
        #         followed += 1
        #         sleep(randint(1,3))
        #         # Liking the picture
        #         button_like = web.find_element_by_css_selectors('[aria-label="Like"]')

        #         for btn in button_like:
        #         	if randint(1,100) < 75:
        #         		btn.click()
        #         		sleep(randint(2,7))

        #         # button_like.click()
        #         # likes += 1
        #         # sleep(randint(4,12))
        #         # Comments and tracker
        #         attributes = ["cool", "kool", "nice", "GREAT", "awesome", "gorgeous", "good", "super"]
        #         photos = ["photo", "pic", "photoghraphy", "picture", "work", "job"]
        #         suffixes = ["", ":)", ":)))", ":D", "hehe", "!!!", "!", "...", ".", "lol"]
        #         pronouns = ["that's", "this is", "it's", "that is", "it is"]
        #         prefixes = ["", "Wow", "hey", "oh", "oooh", "wooow", "BRAVO!"]
        #         comments += 1
        #         web.find_element_by_xpath('/html/body/div[2]/div[2]/div/article/div[2]/section[3]/div/form/textarea').click()
        #         comment_box = web.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[3]/div/form/textarea')

        #         prefix = prefixes[randint(0, len(prefixes) - 1)]
        #         pronoun = pronouns[randint(0, len(pronouns) - 1)]
        #         attribute = attributes[randint(0, len(attributes) - 1)]
        #         photo = photos[randint(0, len(photos) - 1)]
        #         suffix = suffixes[randint(0, len(suffixes) - 1)]

        #         comment = "{} {} a {} {} {}".format(prefix, pronoun, attribute, photo, suffix)
        #         sleep(randint(2,8))
        #         # Enter to post comment
        #         comment_box.send_keys(Keys.ENTER)

        #     # Next picture
        #     web.find_element_by_xpath('/html/body').send_keys(Keys.RIGHT)
        #     #web.find_element_by_css_selector(".coreSpriteRightPaginationArrow").click()
        #     sleep(randint(12,22))
        # else:
        # 	#web.find_element_by_css_selector(".coreSpriteRightPaginationArrow").click()
        #     web.find_element_by_xpath('/html/body').send_keys(Keys.RIGHT)
        #   # sleep(randint(14,24))
    # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
    # except:
    #    continue

# for n in range(0,len(new_followed)):
#     prev_user_list.append(new_followed[n])

# updated_user_df = pd.DataFrame(prev_user_list)
# updated_user_df.to_csv('{}_users_followed_list.csv'.format(strftime("%Y%m%d-%H%M%S")))
# print('Liked {} photos.'.format(likes))
# print('Commented {} photos.'.format(comments))
# print('Followed {} new people.'.format(followed))
