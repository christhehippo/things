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
    user = sys.argv[1]
    channelurl += sys.argv[1]
else:
    user = input('Enter channel name: ')
    channelurl += user
channelurl += '/videos'

print('Checking last upload of ' + "\"" + user + "\"")
# Attempt to open the channel url
try:
    driver.get(channelurl)
except Exception as e:
        print(e)

#Check if the channel exists
if (driver.title == '404 Not Found'):
    # Youtube has some weird stuff going on with their url formats, try this one second '*\c\*user*
    channelurl = 'https://www.youtube.com/c/'
    channelurl += user
    channelurl += '/videos/'
    
    try:
        driver.get(channelurl)
    except Exception as e:
        print(e)

    if (driver.title == '404 Not Found'):
        print('Channel does not exist!')
        driver.close()
        quit()

# Get the page source to scan through
src = driver.page_source
# Now do some matching to find the video that was last uploaded
if (('by ' + user)  in src):
    # Do this in two parts based on the position of the author tag in the page source
    # First we seperate the massive string at the first occurence of the video author, i.e. "by MaxMoeFoe"
    # We are looking for this type of string: ("SHOCK COLLAR COOKING by maxmoefoe 4 years ago 17 minutes 5,946,074 views")
    # lstr is ALL the text the the left of "by MaxMoeFoe", '"SHOCK COLLAR COOKING '
    lstr = src.partition('by ' + user)[0]
    # The data we are looking for is enclosed within quotation marks, so find the LAST occurence of
    # a quotation mark in our big slab of text, which will isolate the video title
    lstr = lstr.rpartition("\"")[2]

    # Now we do the second part of the massive string we cut in two
    # This other string will BEGIN win the data we want
    # i.e ("SHOCK COLLAR COOKING by maxmoefoe 4 years ago 17 minutes 5,946,074 views") --- WHAT WE WANT IN TOTAL
    # The second piece of the string will start at ' 4 years ago 17 minutes 5,946,074 views"' and have a some garbage following
    # So now split the page source again but grab the other part
    rstr = src.partition('by ' + user)[2]
    rstr = rstr.partition("\"")[0]  

    # Now lets clean the extra white space off the strings and make things look pretty
    lstr = lstr[:-1]
    lstr = lstr + ': '
    rstr = rstr[1:]
    
    print()
    print(user + " last uploaded video:", )
    print(lstr + rstr)
else:
    print('User has no uploads!')


driver.close()
quit()