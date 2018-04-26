#coding=utf-8

import urllib
import urllib2
import re
from selenium import webdriver

# url = "https://c.open.163.com/mob/video.htm?plid=ADBC5LMDJ&mid=ADBC5LMD3#share-mob"
url = "https://c.open.163.com/mob/audio.htm?plid=ADERF24NJ&mid=ADERF24NF"
driver = webdriver.PhantomJS()
driver.get(url)
# data=driver.page_source
data = driver.find_elements_by_tag_name("video")
print(type(data))
if data:
    data = data
else:
    data = driver.find_element_by_tag_name("audio")
if data:
    data = data
else:
    print("There is no video or audio")
data = data.get_attribute("src")
print data
driver.quit()

# url = "https://c.open.163.com/mob/video.htm?plid=MD8VG7QS8&mid=MD8VHFF15#share-mob"
# res = urllib2.urlopen(url)
# html = res.read()
# r = re.compile('<video.*?></video>')
# # print(html)
# news = re.findall(r,html)
# print(html)
# print(news)
# for i in news:
#      print(i[0])
#
# print(res.read())