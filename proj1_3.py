from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os
import csv
from sets import Set

b = open('answers.csv', 'wb')
a = csv.writer(b, delimiter=',', dialect='excel')
c = open("user_list", 'w')
user = Set([])
chromedriver = "/usr/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

text_file = open("question_urls", "r")
lines = text_file.readlines()
for l in range(0,len(lines)):
    #print 1
    if lines[l][0:4] != 'http':
        # print 1
        main_name = str(lines[l]).split('\n')[0]
        continue
    else:
        url = str(lines[l]).split('\n')[0]
    browser.get(url)
    more_link = browser.find_elements_by_class_name('more_link')
    for more in more_link:
        try:
            more.click()
            time.sleep(1)
        except:
            time.sleep(1)
        more_link = browser.find_elements_by_class_name('more_link')

    html_source = browser.page_source
    html_soup = BeautifulSoup(html_source)
    question = html_soup.find(attrs={"class":"question_details_text inline_editor_content"}).string
    if not question:
        question_string = ""
    else:
        question_string = question.encode('utf8')
    list_items = html_soup.find_all(attrs={"class":"pagedlist_item"})
    #print len(list_items)
    topics = html_soup.find_all('div',attrs={"class":"topic_list_item"})
    topics_list=[]
    for k in range(0,len(topics)):
        topics_list.append(topics[k].get_text().encode('utf8'))
    floor = 0
    if len(list_items) > 1:
        for i in range(0,len(list_items)-1):
            j = 1
            counter = 0
            
            voters = []
            for link in list_items[i].find_all('a',attrs={"class":"user"}, href= True):
                if j == 1:
                    user_id = "http://www.quora.com" + link['href'].encode('utf8')
                    user.add(user_id)
                    floor = floor+1
                    j = 2
                else:
                    voter = "http://www.quora.com" + link['href'].encode('utf8')
                    voters.append(voter)
                    user.add(voter)
                    counter = counter + 1
                answer_test = list_items[i].find('div', attrs={"class":"answer_content"}).get_text()[:-11].encode('utf8')
                date = list_items[i].find('span', attrs={"class":"answer_permalink"}).get_text().replace(',', '')
        
            index = [user_id + "-" + url + "-" + str(floor), url , user_id ,date , str(counter) , "{{{"+",".join(voters) + "}}}","{{{"+",".join(topics_list) + "}}}", main_name , "{{{" + question_string + "}}}" ,"{{{" + answer_test + "}}}"]
            a.writerow(index)
    else:
        user_id = ""
        answer_test= ""
        date = []
        voters=[]
        counter = 0
        index = [user_id + "-" + url, url , user_id ,date , str(counter) , "{{{"+",".join(voters) + "}}}","{{{"+",".join(topics_list) + "}}}", main_name , "{{{" + question_string + "}}}" ,"{{{" + answer_test + "}}}"]
        a.writerow(index)

b.close()
for item in user:
    c.write("%s\n"%item)

c.close()

