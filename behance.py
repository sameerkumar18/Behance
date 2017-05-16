from my_randomizer import randomizer
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import csv


def csvv(name,link,likes,views):
    f = open('profiles.csv', 'a')
    writer = csv.writer(f, dialect='excel')
    writer.writerow([name + " , " + link + " , " + likes + " , " + views])

def main():
    driver = webdriver.Chrome()


    url = "https://www.behance.net/search?field=63&content=users&sort=appreciations&time=all&location_id=16173236-en&country=IN&city=New%20Delhi"
    driver.get(url)
    time.sleep(5)
    x=1
    t=2.5
    for i in range(0,100):
        for z in range(1,8):

            #loop x for next profile //*[@id="content"]/div[2]/div[x]//div[1]/a[1]
            try:
                name =  driver.find_element_by_xpath('//*[@id="content"]/div[2]/div['+str(x)+']//div[1]/a[1]').text
                link = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div['+str(x)+']//div[1]/a[1]').get_attribute('href')

                likes = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div['+str(x)+']//div[1]/div[3]/div[2]/span[1]').text
                views = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div['+str(x)+']//div[1]/div[3]/div[2]/span[2]').text

                print str(str(name) + "  " + str(link) + "  " + str(likes) + "  " + str(views))

                csvv(name,link,likes,views)
            except:
                pass
            x = x + 1

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(t)
        t = t + 0.1

main()