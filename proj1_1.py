from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os

def findSub(url,stack,i):
	#print i
    url_about = url.split('?')[0] + "/about?share=1"
    browser.get(url_about)
    html_source = browser.page_source
    child_source = html_source.split('Child Topics')
    for j in range(0,i):
        url_link = "http://www.quora.com/" + stack[j] + "?share=1"
        if j != i-1:
            fw_links.write((url_link + '\t').encode('utf-8'))
            fw.write((stack[j]+'\t').encode('utf-8'))
        else:
            fw_links.write((url_link + '\n').encode('utf-8'))
            fw.write((stack[j]+'\n').encode('utf-8'))
    if len(child_source) != 1:
        child = child_source[1]
        child_html = child.split("</html>")[0]
        c = child_html.split("</strong>")[1]
        soup = BeautifulSoup(c)
        for link in soup.find_all('a', attrs={"class":"topic_name"}):
            link_url = "http://www.quora.com" + link['href'] + "?share=1"
            stack.append(link['href'][1:])
            i = i+1
            findSub(link_url,stack,i)
    i=i-1
    stack.pop()
	

url_1 = 'http://www.quora.com/Cigars?share=1'
url_2 = 'http://www.quora.com/Quitting-Smoking?share=1'

fw_links = open("topic_urls.txt", mode='w')
fw = open("topic_names.txt", mode='w')

stack=[]

name_1 = url_1[21:].split('?')[0]
name_2 = url_2[21:].split('?')[0]

chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
browser.get(url_1)

stack.append(name_1)
findSub(url_1,stack,1)
browser.get(url_2)
stack.append(name_2)
findSub(url_2,stack,1)

#print stack

fw.close()
fw_links.close()

