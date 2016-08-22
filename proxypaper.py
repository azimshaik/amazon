import urllib
import random
import datetime
import MySQLdb
import re
from urllib import urlopen
from bs4 import BeautifulSoup
#proxy = {"http":"http://54.208.223.68:8083"}

my_dict  = {
    'a':'http://212.47.239.185:9009',
    'b':'http://119.29.146.114:1080',
    'c':'http://122.147.24.103:8080',
    'd':'http://39.80.207.94:81',
    'e':'http://211.142.195.72:80',
    'f':'http://180.166.150.114:1080',
    'g':'http://186.194.47.186:3128',
    'h':'http://202.43.147.226:1080',
    'i':'http://119.6.136.122:83',
    'j':'http://60.221.50.69:8090',
    'k':'http://124.244.157.209:80',
    'l':'http://84.26.93.234:80',
    'm':'http://47.89.22.253:1080'
}



rand_ip =  random.choice(my_dict.values())

proxy = {"http":rand_ip}
print proxy

localurl = urllib.urlopen('https://www.amazon.com/Hyper-Changing-execute-business-intelligence/dp/0692423087?ie=UTF8&qid=1465237340&ref_=tmm_pap_swatch_0&sr=8-10',proxies=proxy)
#f = urllib.urlopen('http://www.humorhuman.com/stuff/amazon/kindle.html',proxies=proxy)
#contents = f.read()

#localurl = urlopen('http://www.humorhuman.com/stuff/amazon/kindle.html',proxies=proxy)
bsObj = BeautifulSoup(localurl.read(),"html.parser")
ranks = bsObj.findAll("li",{"id":"SalesRank"})
p_rank_array = []
for rank in ranks:
    print re.findall('#(\d+)',rank.get_text().replace(',',''))
    p_rank_array = re.findall('#(\d+)',rank.get_text().replace(',',''))

if not len(p_rank_array):
    print "ranks not retieved"
else:
    db = MySQLdb.connect("localhost","azim","Az09347108396*","amazon" )
    cursor = db.cursor()
    today = datetime.date.today()
    tstamp = format(datetime.datetime.now())
    sql = """INSERT INTO paperbackranks(amz_best_seller_rank, books_management_inf_systems, books_inf_management, books_processes_infra, date, tstamp) VALUES (%s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql,(p_rank_array[0],p_rank_array[1],p_rank_array[2],p_rank_array[3],today,tstamp))
    db.commit()
    print "ranks successfully inserted"
    db.close()
#print f.read()
#open('document1.html','w').write(contents)
#insert into kindleranks (amz_best_seller_rank,kin_inf_management,books_business,books_inf_management,date,tstamp) values (100001,01,02,03,'2013-05-20','2013-05-20 01:01:10');
