#encoding:utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import MySQLdb
import urllib
from BeautifulSoup import BeautifulSoup
import datetime
import re

def one_article(request):
    start_time = datetime.datetime(2013,4,29)
    phase = 204
    day = (datetime.datetime.now()-start_time).days
    if day > 1:
        phase += day
    else:
        phase += 1
    one_url = "http://hanhan.qq.com/hanhan/one/one%sm.htm#page1" % phase
    html = urllib.urlopen(one_url)
    text = html.read()
    
    soup = BeautifulSoup(text)
    soup_title = soup.findAll('h1',{'id':'onebd','class':'tit'})
    soup_text = soup.findAll('div',{'id':'picIdbd'})
    
    p = re.compile("<[^>]+>")
    title = p.sub("",str(soup_title))
    text = p.sub("",str(soup_text))
    
    db = MySQLdb.Connect(user='root',db='test',passwd='root',host='localhost',charset='utf8')
    cursor = db.cursor()
    cursor.execute("insert into oneisall_one_article (title,content) values ('%s','%s')" % (title,text,))
    db.commit()
    db.close()
    return HttpResponse("<html><body> %s <br><br> %s </body></html>" % (title,text,))

def one_img(request):
    start_time = datetime.datetime(2013,4,29)
    phase = 204
    day = (datetime.datetime.now()-start_time).days
    if day > 1:
        phase += day
    else:
        phase += 1
    one_url = "http://hanhan.qq.com/hanhan/one/one%sm.htm" % phase
    html = urllib.urlopen(one_url)
    text = html.read()
    
    soup = BeautifulSoup(text)
    img_addr = soup.findAll('img',{'id':'mypicOne'})
    path = r"E:\\pySublimeTest\\one\\template\\one_img\\%s.jpg" % phase
    f = file(path,'wb')
    data = img_addr[0]['src']
    url_img = urllib.urlopen(data).read()
    f.write(url_img)
    f.close()
    image_data = open(path,'rb').read()
    return HttpResponse(image_data,mimetype='image/png')
    