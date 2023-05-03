import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\Chrome/55.0.2883.87 Safari/537.36'}

def test(name):
    url="https://wiki.biligame.com/ys/"+name
    bs=BeautifulSoup(requests.get(url,headers=headers).content,"lxml")
    print("request successfully")
    i=0
    for divs in bs.find_all('div',class_='visible-md visible-sm visible-lg'):
        for tds in divs.find_all('td'):
            if(i>0):
                i=i+1
                for divs_2 in tds.find_all('div',style="position: absolute;bottom: 0px;left:0px;font-size:10px;color:#fff;font-weight: bolder;text-shadow: #000 -1px 0 0,#763c12 0 -1px 0,#5d2b08 1px 0 0,#1d1515 0 1px 0;width: 68px;display: inline-block;overflow: hidden;white-space: nowrap;text-overflow: ellipsis;text-align:left;background: linear-gradient(rgb(0 0 0 / 0%), rgb(37 37 37 / 90%));width: 100%;;padding-left:2px"):
                    for a_s in divs_2.find_all('a'):
                        url_1=a_s.get('href')
                        item=a_s.get('title')
                        print(item+": "+"https://wiki.biligame.com"+url_1)
            if(tds.string=="9→10\n"):
                i=1
                print("found!")
            if(i>1):
                break
        if(i>1):
            break
def getnamelist():
    url="https://wiki.biligame.com/ys/角色"
    bs=BeautifulSoup(requests.get(url,headers=headers).content,"lxml")
    star_5=[]
    star_4=[]
    star_all=[]
    for divs in bs.find_all('div',class_='resp-tab-content',style="display:block;"):
        for star_five in divs.find_all('div',class_='g C5星'):
            for star_five_name in star_five.find_all('div',class_='L'):
                star_5.append(star_five_name.string)
                star_all.append(star_five_name.string)
        for star_four in divs.find_all('div',class_='g C4星'):
            for star_four_name in star_four.find_all('div',class_='L'):
                star_4.append(star_four_name.string)
                star_all.append(star_four_name.string)
    print("done")
    return(star_5,star_4,star_all)