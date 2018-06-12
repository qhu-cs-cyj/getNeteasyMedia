#coding=utf-8
from selenium import webdriver

url = "https://c.open.163.com/mob/video.htm?plid=MBRIIOOUT&mid=MBRIT2144"
driver = webdriver.PhantomJS()
driver.get(url)
# data=driver.page_source
data = driver.find_elements_by_tag_name("video")
driver.quit()
if data:
    data = data
else:
    data = driver.find_element_by_tag_name("audio")
if data:
    data = data
else:
    print("There is no video or audio")
data = data[0].get_attribute("src")

