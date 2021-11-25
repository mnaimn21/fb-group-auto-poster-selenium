from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import re
import os
import time
from dotenv import dotenv_values
import random


env = dotenv_values(".env")

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(options=chrome_options, executable_path="/usr/lib/chromium-browser/chromedriver")
driver.get('https://www.facebook.com/')


def randomTime() :
        randomTime = random.randint(10,20)
        time.sleep(randomTime)


try :
    email = driver.find_element_by_name('email')
    password = driver.find_element_by_name('pass')
    email.send_keys(env['USER'])
    password.send_keys(env['PASSWORD'])
    password.send_keys(Keys.RETURN)
    print("Successfully Login")
    time.sleep(5)
    f = open("groud_id_list.txt", "r")
    
    for line in f :
        group_address = 'https://www.facebook.com/groups/{}/buy_sell_discussion'.format(line)
        driver.get(group_address)
        time.sleep(3)

        post_class = 'oajrlxb2 b3i9ofy5 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x cxgpxx05 d1544ag0 sj5x9vvc tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn orhb3f3m czkt41v7 fmqxjp7s emzo65vh btwxx1t3 buofh1pr idiwt2bm jifvfom9 kbf60n1y'
        post_class = post_class.replace(' ', '.')
        click_post = driver.find_element_by_class_name(post_class)
        click_post.click()
        randomTime()
        
        post_content = driver.find_element_by_class_name('notranslate._5rpu')
        post_content = driver.switch_to_active_element()
        post_content.send_keys("POST YOUR TEXT HERE")
        randomTime()


        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_pc = soup.find_all('div', attrs={'id': re.compile("^mount_0_0_")})
        id_ = str(all_pc[0].get('id'))
        xpath = '//*[@id="' + id_ + '"]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div/div[3]/div[2]/div[1]/div'
        post = driver.find_element_by_xpath(xpath)
        post.click()
        randomTime()
    f.close()

except NoSuchElementException as e :
    print(e)
    
driver.close()
