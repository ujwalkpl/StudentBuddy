from selenium import webdriver
import time
import configparser
import time
from selenium.webdriver.common.keys import Keys
import re
from selenium.common.exceptions import NoSuchElementException
from dateparser.search import search_dates

path="C:\\Users\\HOME\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver=webdriver.Chrome(path)


driver.get('https://web.whatsapp.com/')

LAST_MESSAGES = 10000
WAIT_FOR_CHAT_TO_LOAD = 2 # in secs

message_dic = {}
def read_last_in_message(driver):
    """
    Reading the last message that you got in from the chatter
    """
    for messages in driver.find_elements_by_xpath(
            "//div[contains(@class,'message-in')]"):
        try:
            message = ""
            emojis = []

            message_container = messages.find_element_by_xpath(
                ".//div[@class='copyable-text']")

            message = message_container.find_element_by_xpath(
                ".//span[contains(@class,'selectable-text invisible-space copyable-text')]"
            ).text

            for emoji in message_container.find_elements_by_xpath(
                    ".//img[contains(@class,'selectable-text invisible-space copyable-text')]"
            ):
                emojis.append(emoji.get_attribute("data-plain-text"))

        except NoSuchElementException:  # In case there are only emojis in the message
            try:
                message = ""
                emojis = []
                message_container = messages.find_element_by_xpath(
                    ".//div[@class='copyable-text']")

                for emoji in message_container.find_elements_by_xpath(
                        ".//img[contains(@class,'selectable-text invisible-space copyable-text')]"
                ):
                    emojis.append(emoji.get_attribute("data-plain-text"))
            except NoSuchElementException:
                pass

    return message, emojis




name = "ISE 6C🤟"
# msg = input('Enter message')
# count = int(input('Enter the count'))
input('Enter anything after scanning QR code')




user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))

# driver.find_element_by_xpath("//div[@class='_10V4p _1jxtm']/div").send_keys(Keys.CONTROL + Keys.HOME)

user.click()
ho = driver.find_element_by_xpath("//div[@class='_1_q7u']")
ho.click()

for i in range(0,50):
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    time.sleep(4)

def chats():
    
    
    name = driver.find_element_by_xpath("//div[@class='_19vo_']/span").text
    m_arg = '//span[@class="_F7Vk selectable-text invisible-space copyable-text"]/span'
    messages = driver.find_elements_by_xpath(m_arg)  
    top_messages = messages[-1*LAST_MESSAGES:]
    message_dic[name] = [m.text for m in top_messages]
    print(message_dic[name])
    # image = driver.find_element_by_xpath("//*[@id="main"]/header/div[1]/div/img")
    # message_dic[name].append(image.get_attribute('src'))
    #print(message_dic[name])
    for s in message_dic[name]:
        event = re.findall(r'lab test|lab internal|fee payment|fees',s.lower())
        sub = re.findall(r'SS|Java|OOADP|java|ss|ooadp|ml|payment',s.lower())
        dates = search_dates(s.lower())
        if len(event) and len(sub) and dates is not None:
            print("Event:",event[0])
            print("Subject",sub[0])
            #print("Dates:",dates)
            for f in dates:
                time = re.findall(r'am|pm',f[0].lower())
                day = re.findall(r'mon|tue|wed|thur|fri|sat|sun|jan|feb|mar|apr|may|jun|july|aug|sept|oct|nov|dec',f[0].lower())
                if time != '' or day !='':
                    print("When:",f[0])
                    print()
                print()    
    # msg_box = driver.find_element_by_class_name('_13mgZ')


chats()
# subject = [('Java','J2EE'),('OOADP','Object Oriented Design Pattersn'),('System Software','SS'),('Machine Learning','ML')]
# test = ['test','internals','lab test']
# # for messages in message_dic[name]:

# for i in range(count):
#     msg_box.send_keys(msg)
#     driver.find_element_by_class_name('_3M-N-').click()





