from selenium import webdriver
from bs4 import BeautifulSoup
import smtplib
import requests
import subprocess
#from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
options = Options()
options.binary_location = "/usr/bin/chromedriver"
driver=webdriver.Chrome()
driver.get("http://placement.iitk.ac.in")

username = driver.find_element_by_id("id_username")
password = driver.find_element_by_id("id_password")
username.send_keys("username")
password.send_keys("password")
login = driver.find_element_by_xpath("//*[@type='Submit']")
login.submit()
url="http://placement.iitk.ac.in/dashboard/"

prev="randomstring"

while(1):
    try:

        driver.get(url)
        page_source=driver.page_source
        soup=BeautifulSoup(page_source,'html.parser')
        pres=soup.find("div",{"class":"col-sm-9"})
        pres=(pres.text).strip()
        if prev!=pres:
            subprocess.Popen(['notify-send',"UPDATE",pres])
            server=smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login("your_mailid","your_password")
            msg="\n**UPDATE**"+"\n "+pres
            server.sendmail("sender_mailid","receiver_mailid",msg)
            server.quit()


        prev=pres
        time.sleep(10)
    except:
        print("conn error")
