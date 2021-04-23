from selenium import webdriver
import webbrowser
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import time


joinURL = input('\nWhat is the group link?\n :')
botnameprefix = input("\nWhat does the botname need to be?\n :")
botamount = input("\nHow many bots do you want?\n :")

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_experimental_option("detach", True)



driver = webdriver.Chrome(chrome_options=chrome_options)


#https://teams.microsoft.com/_#/l/meetup-join/19:af8e2dea432f4cf881a3017407654ded@thread.tacv2/1618577909488?context=%7B%22Tid%22:%2278ccc6ac-6d1b-4306-b160-96aaf239df61%22,%22Oid%22:%22d64c48a5-6ec3-4c93-b7cb-f37101ef56e2%22%7D&anon=true&deeplinkId=2adec10a-ce6a-41d4-9601-2068c1980dfa
tabs = 0

def firstbot():
    driver.get(joinURL)
    
    input("\nPress Enter if you denied mic access and if youre in the call")
   
    time.sleep(1)
    
    print('BOT COMPLETED')
    
def secondbot():
    
    global tabs 
    tabs = tabs + 1
    
    time.sleep(1)
    
    driver = webdriver.Chrome(chrome_options=chrome_options)
    #driver.execute_script("window.open('');")
    # Switch to the new window
    #driver.switch_to.window(driver.window_handles[tabs])
    
    driver.get(joinURL)

    time.sleep(7)
    driver.find_element_by_tag_name('input').send_keys(botnameprefix + " " + str(tabs))
    driver.find_element_by_tag_name('input').send_keys(Keys.ENTER)
    
    time.sleep(7)
    driver.find_element_by_tag_name('button').click()
    
    time.sleep(1)
    driver.find_element_by_tag_name('input').send_keys(Keys.ENTER)
    time.sleep(3)
    driver.find_element_by_css_selector('#microphone-button').click()
    
    print('BOT COMPLETED')


firstbot()
 
for x in range(int(botamount)):
    secondbot()
    
    
print('epic')




























































