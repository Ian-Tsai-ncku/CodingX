# encoding=utf-8

list_of_board=['Gossiping','C-Chat','Baseball','Stock','Sex','Others']
list_count=[0,0,0,0,0,0]
''' find(name)，抓取<a> '''
import requests as req
url='https://www.pttweb.cc/hot/news/today'
res=req.get(url)
res.encoding = 'utf-8'
from bs4 import BeautifulSoup
soup=BeautifulSoup(res.text, 'html.parser')
container=soup.find_all(name='div',attrs={'class': 'e7-container'})
# container2=soup.find_all(name='div',attrs={'class': 'e7-container'})
# print(container[0].prettify())
# for cell in container[0].findChildren(name='div', attrs={'class':'e7-container'}):
#     pushCount = cell.find(name='div',attrs={'class':'e7-recommendScore'})
#     print(cell.prettify())
#     print(pushCount.text[3:])
# container_push=container[0].find(name='div',attrs={'class': 'e7-left e7-left-xs'})
# print(container_push)
n=len(container)
print(n)
push_tag=container[0].findChildren(name='div',attrs={'class': 'e7-container'})
num=0
for i in range(1,n):
    pushpush=push_tag[i-1].find(name='div',attrs={'class':'e7-recommendScore'})
    article_tag=container[i].findChildren(name='a',attrs={'class':'e7-boardName'})
    article_tag=article_tag[0].findChildren(name='span',attrs={'class':'e7-link-to-article'})
    topic_tag=container[i].findChildren(name='div',attrs={'e7-right ml-2'})
    topic_tag=topic_tag[0].findChildren(name='span',attrs={'e7-title my-1 e7-link-to-article e7-article-default'})

    for k in range(5):
        if article_tag[0].text==list_of_board[k]:
            list_count[k]+=1            

    try:
        print(pushpush.text)
        print(article_tag[0].text)
        print(topic_tag[0].text)
    except:
        print('none')
for i in range(5):
    num+=list_count[i]
n=n-num
list_count[5]=n
# print(type(list_of_board[0]))        
# print(list_count)

import matplotlib.pyplot as plt
plt.bar(list_of_board,list_count)
