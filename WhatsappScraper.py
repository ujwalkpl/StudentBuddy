from selenium import webdriver
import time
import configparser
import time
from selenium.webdriver.common.keys import Keys

import pickle
from selenium.common.exceptions import NoSuchElementException
path="C:\\Users\\Ujwal\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver=webdriver.Chrome(path)


driver.get('https://web.whatsapp.com/')

LAST_MESSAGES = 10000
extracted  = []
top_messages = []


message_dic = {}




def chats():
    name = driver.find_element_by_xpath("//div[@class='_19vo_']/span").text
    m_arg = '//div[@class="_1ays2"]/div'
    messages = driver.find_elements_by_xpath(m_arg)  
    top_messages = messages[-1*globals.LAST_MESSAGES:]
    message_dic[name] = [m.text for m in top_messages]
    extracted = message_dic[name]
    print(message_dic[name])


name = "ISE 6C🤟"
input('Enter anything after scanning QR code')




user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

ho = driver.find_element_by_xpath("//div[@class='_1_q7u']")
ho.click()

for i in range(100):
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    time.sleep(4)            
chats()


with open("test1.txt", "wb") as fp:
    pickle.dump(extracted, fp)

