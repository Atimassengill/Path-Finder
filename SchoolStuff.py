# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:39:58 2020

@author: David
"""
import threading 
from threading import Thread
import pyautogui
import time
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
class SchoolStuff:
    
    def __init__(self):
        self.t = time.sleep(4)
        
       
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.ChromeUrl = "http://www.google.com"
        
        self.GmailURl = "http://www.google.com/gmail"
        self.DocsUrl = "http://www.google.com/docs"
        self.DriveUrl = "http://www.google.com/drive"
        self.CanvasUrl = 'https://www.hopkinsschools.org/canvas'
        self.sign_in = "//*[@id='gb_70']"
        self.Username_promt = "//*[@id='identifierId']"
        self.Username = 'Username'
        self.Next_promt = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]"
        self.Password_promt = '//*[@id="password"]/div[1]/div/div[1]/input'
        self.Password = 'Password'
        self.click_signin = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]"
    def get_signed_in(self):
            
        self.driver.get(self.ChromeUrl)
        self.driver.find_element_by_xpath(self.sign_in).click()
    
        self.driver.find_element_by_xpath(self.Username_promt).click()
        pyautogui.typewrite(self.Username)
        self.t
    
        self.driver.find_element_by_xpath(self.Next_promt).click()
        self.t
        
        time.sleep(4)
        self.driver.find_element_by_xpath(self.Password_promt).click()
        pyautogui.typewrite(self.Password)
        
    
    
        self.driver.find_element_by_xpath(self.click_signin).click()
        
    
    def get_Gmail(self):
    
        self.driver.execute_script("window.open('http://www.google.com/gmail');")
        self.t
    # Switch to the new window
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(self.GmailURl)
        self.t
        
    
  
    
    
    def get_Docs(self):
        self.driver.execute_script("window.open('http://www.google.com/docs');")
        self.t
        
    
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.driver.get(self.DocsUrl) 
        
    
    
    
    
    
    def get_drive(self):
        self.driver.execute_script("window.open('http://www.google.com/drive');")
        self.t
    
        self.driver.switch_to.window(self.driver.window_handles[3])
        self.driver.get(self.DriveUrl)
        self.t
    
        self.driver.find_element_by_xpath('/html/body/header/div[1]/div/div[3]/div/a[1]').click()
        self.t
    
        self.driver.switch_to.window(self.driver.window_handles[3])
        self.driver.close()
   
    def get_classlink(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get(self.CanvasUrl)
        self.driver.find_element_by_xpath('//*[@id="node-66324"]/div/div[2]/div/div/div/div/div/p[2]/a').click()
    def login_classlink(self):    
        self.t
        #driver.find_element_by_xpath('//*[@id="username"]').click()
        

        self.driver.find_element_by_xpath("//*[@id='username']")
        pyautogui.typewrite('Username')
        self.t
        #driver.find_element_by_xpath('//*[@id="password"]').click()
        
        self.driver.find_element_by_xpath("//*[@id='password']")
        pyautogui.typewrite('Password')
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="signin"]').click()
    def runall(self):
        if __name__ == '__main__':
            Thread(target = self.get_signed_in).start()
            time.sleep(20)
           
            Thread(target = self.get_Gmail).start()
            time.sleep(10)
            Thread(target = self.get_Docs).start()
            time.sleep(10)
            Thread(target = self.get_drive).start()
            time.sleep(15)
            
            
            Thread(target = self.get_classlink).start()
            time.sleep(10)
         
            Thread(target = self.login_classlink).start()
   
        
SchoolStuff().runall()
input('Press ENTER to exit')
