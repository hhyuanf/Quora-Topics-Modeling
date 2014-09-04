from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os
from sets import Set

url=[]
set = Set([])
text_file = open("topic_urls", "r")
lines = text_file.readlines()
fw_links = open("question_urls" , mode='w')

chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

for i in range(0,len(lines)):
    set = Set([])
    url.append(lines[i].split('\t')[-1].split('\n')[0])
    fw_links.write(url[i][21:].split('?')[0]+'\n')
#links_file_name = url[21:].split('?')[0]
    browser.get(url[i])
    src_updated = browser.page_source
    src = ""
    while src != src_updated:
        time.sleep(1)
        src = src_updated
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        src_updated = browser.page_source
        html_source = browser.page_source
        split_html = html_source.split("<h3>")
    for i in range(1,len(split_html)):
        part = split_html[i].split('</h3>')[0]
        part_soup = BeautifulSoup(part)
        if ("<div") in part:
                #print part_soup.get_text()
            for link in part_soup.find_all('a' , href=True):
                link_url = "http://www.quora.com" + link['href'] + "?share=1"
                len1 = len(set)
                set.add(link_url)
                len2 = len(set)
                if len1 != len2:
                    fw_links.write((link_url + '\n').encode('utf-8'))

fw_links.close()