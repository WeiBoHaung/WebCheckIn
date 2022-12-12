
import os,sys
import time
from datetime import date, datetime


from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.command import Command
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests


url={
    'lollipop168':'http://www.lollipop168.com/thread-24918-1-4.html',
    'bhmtsff':'https://bhmtsff.com/thread-7242-1-1.html',
    'kafra-mart':'https://kafra-mart.com/bbs/forum.php?mod=viewthread&tid=521',
}

class WebBrowser(webdriver.Chrome):
    def __init__(self, 
            id,
            pw,
        ):
        super(WebBrowser,self).__init__(ChromeDriverManager().install())
        self.id=id
        self.pw=pw
        # self.driver = webdriver.Chrome(self.chromePath,chrome_options=options)
        # self.driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
        # self.driver.minimize_window()

    def loginTest(self):
        print()
    
if __name__=='__main__':
    b=WebBrowser()
    b.close()
    print('555')