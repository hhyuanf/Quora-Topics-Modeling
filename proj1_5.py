from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os
import csv
from sets import Set

b = open('user.csv', 'wb')
a = csv.writer(b, delimiter=',')

text_file = open("user_list", "r")
lines = text_file.readlines()

chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

for url in lines:
    #url = "http://www.quora.com/Domhnall-OHuigin\n"
    url_str = str(url)[:-1]+"?share=1"
    browser.get(url_str)
    html_source = browser.page_source
    user_id = str(url)[:-1]
    html_soup = BeautifulSoup(html_source)
    topic_url = url_str[20:-1].split('?')[0]+"/topics"
    try:
        topics_num = html_soup.find('a', href=topic_url).get_text()[7:]
    except:
        topics_num = str(0)
    blog_url = url_str[20:-1].split('?')[0]+"/blogs"
    try:
        blogs_num = html_soup.find('a', href=blog_url).get_text()[6:]
    except:
        blogs_num = str(0)
    question_url = url_str[20:-1].split('?')[0]+"/questions"
    try:
        questions_num = html_soup.find('a', href=question_url).get_text()[10:]
    except:
        questions_num = str(0)
    answer_url = url_str[20:-1].split('?')[0]+"/answers"
    try:
        answers_num = html_soup.find('a', href=answer_url).get_text()[8:]
    except:
        answers_num = str(0)
    edit_url = url_str[20:-1].split('?')[0]+"/log"
    try:
        edits_num = html_soup.find('a', href=edit_url).get_text()[6:]
    except:
        edits_num = str(0)
    follower_url = url_str[20:-1].split('?')[0]+"/followers"
    try:
        followers_num = html_soup.find('a', href=follower_url).get_text()[8:]
    except:
        followers_num = str(0)
    following_url = url_str[20:-1].split('?')[0]+"/following"
    try:
        following_num = html_soup.find('a', href=following_url).get_text()[8:]
    except:
        following_num = str(0)
    fr_url = url_str[:-8]+"/followers?share=1"
    fg_url = url_str[:-8]+"/following?share=1"
    follower_list = []
    following_list = []
    for i in range(0,2):
        if i == 0 and followers_num != str(0):
            browser.get(fr_url)
        elif  i == 0 and followers_num == str(0):
            continue
        elif i != 0 and following_num != str(0):
            browser.get(fg_url)
        elif i != 0 and following_num == str(0):
            continue
        src_updated = browser.page_source
        src = ""
        while src != src_updated:
            time.sleep(1)
            src = src_updated
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            src_updated = browser.page_source
        f_source = browser.page_source
        f_soup = BeautifulSoup(f_source)
        f_items = f_soup.find_all(attrs={"class":"pagedlist_item"})
        for l in range (0, len(f_items) - 1):
            for link in f_items[l].find_all('a', attrs={"class":"user"}, href= True):
                user_list = "http://www.quora.com" + link['href'].encode('utf8')
                if i == 0:
                    follower_list.append(user_list)
                else:
                    following_list.append(user_list)
    index = [user_id, topics_num, blogs_num, questions_num, answers_num, edits_num, "{{{"+",".join(follower_list)+"}}}", "{{{"+",".join(following_list)+"}}}"]
    a.writerow(index)

b.close()