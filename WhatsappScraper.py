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

LAST_MESSAGES = 10
extracted  = []
top_messages = []
message_dic = {}




def chats():
    # name = driver.find_element_by_xpath("//div[@class='_1wjpf _3NFp9 _3FXB1']/span").text
    name = "Adi"
    m_arg = '//div[@class="_3zJZ2"]/div'
    messages = driver.find_elements_by_xpath(m_arg)  
    print(messages)
    top_messages = messages[-1*LAST_MESSAGES:]
    [print("hi me  "+m.text) for m in top_messages]

    message_dic[name] = [m.text for m in top_messages]
    extracted = message_dic[name]
    print(message_dic[name])


name = "Adi"
input('Enter anything after scanning QR code')


user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

ho = driver.find_element_by_tag_name('body')
ho.click()

for i in range(10):
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    time.sleep(4)            
chats()
chatbot = []

print()

print(extracted)
with open("test1.txt", "wb") as fp:
    pickle.dump(message_dic["Adi"], fp)

with open("test2.txt", "wb") as fp:
    pickle.dump(chatbot, fp)
