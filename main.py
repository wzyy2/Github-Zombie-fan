#!/usr/bin/python
#coding=utf-8
from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  
import time,sys
  

user_id = raw_input("your user_id: ")
zombie_id = raw_input("zombie_id: ")
zombie_email = raw_input("zombie_email: ")

num = 99
cnt = 0
browser = webdriver.Chrome() # Get local session of firefox  
while(num):
    cnt = cnt + 1;
    if(cnt == 6):
        browser.close()
        browser = webdriver.Chrome()
        cnt = 0;
    browser.get("https://github.com/join") # Load page  
    browser.implicitly_wait(2)
    browser.find_element_by_id("user_login").send_keys(zombie_id + str(num))
    browser.find_element_by_id("user_email").send_keys(str(num) + zombie_email)
    browser.find_element_by_id("user_password").send_keys("1q2w3e4r5t")
    browser.find_element_by_id("user_password_confirmation").send_keys("1q2w3e4r5t")
    browser.find_element_by_id("signup_button").click()  

    browser.get("https://github.com/" + user_id) # Load page 
    browser.find_element_by_css_selector("[aria-label=\"Follow this person\"]").click() 
    browser.find_element_by_css_selector("[aria-label=\"Sign out\"]").click() 
    num = num - 1;

browser.close()  