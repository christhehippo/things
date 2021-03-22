# Script to check the last upload of a youtube channel
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Set up the chrome web driver 
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path='D:\MiscProgrammingThings\chromedriver.exe', options=options)

# channel url string
channelurl = 'https://www.youtube.com/user/'

# Users can enter channel name as argument or enter it via prompt
if len(sys.argv) > 1:
    channelurl += sys.argv[1]
else:
    channelurl += input('Enter channel name: ')

print('Checking last upload of ' + "\"" + channelurl.rpartition("/")[2] + "\"")
driver.get(channelurl)

driver.close()
quit()