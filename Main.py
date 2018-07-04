from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import datetime
import random
import numpy as np
# from selenium.webdriver.common.keys import Keys


# open chrome driver and navigate to web.whatsapp site
driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")
driver.get("https://web.whatsapp.com")
# Uncomment the input line in front of the name var to enable contact input on run
name = "Bot"  # input('Enter the name of user or group : ')
# Uncomment the msg var to write custom messages
#msg = input('Enter your message : ')
count = int(input('Enter the count : '))
# make sure to do not start until QR been scanded
input('Scan the QR code and then press enter')
# find the contact box and click on it
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

# select the text box to start writting
msg_box = driver.find_element_by_class_name('_2S1VP')
msg_box.click()

for i in range(count):
    # time.sleep(20)
    latest_msg = driver.find_elements_by_css_selector("span.XELVh")[-1]
    latest_sender = driver.find_elements_by_css_selector("span._2a1Yw")[-1]
    #now = datetime.datetime.now()
    if latest_msg.text == latest_msg.text:
        for i in range(100):
            replay_indexing = i
        replay_list = [
            "البوت يرحب بكم أرسلوا لكي يتم الرد عليكم",
            "أهلاً بكم في المجموعة ",
            "تفاعلوا فالمجموعة مجموعتكم",
            "الرجاء على الأعضاء الجدد التعريف بأنفسهم ",
            "سيتم أضافة خواص جديدة في المجموعة قريباً , انتظرونا",
            "أكثروا من الصلاة على حبيبنا محمد صلى الله عليه وسلم",
            "أكثروا من ذكر الله الا بذكر الله تطمئن القلوب ",
            "الصبر مفتاح الفرج ",
            "كلمتان خفيفتان على اللسان ثقيلتان في الميزان عزيزتان على الرحمن سبحان الله وبحمده سبحان الله العظيم",
            "أرسلوا لكي يتم الرد عليكم , شكراً",
        ]
        msg_box.send_keys(replay_list[replay_indexing] + Keys.ENTER +  "-Bot")
        button = driver.find_element_by_class_name('_2lkdt')
        button.click()
    else:
        msg_box.send_keys("وعليكم السلام ," + latest_sender.text)
        button = driver.find_element_by_class_name('_2lkdt')
        button.click()
# msg_box.send_keys("لقد قرأ البوت رسالتكم .")
# button = driver.find_element_by_class_name('_2lkdt')
# button.click()
