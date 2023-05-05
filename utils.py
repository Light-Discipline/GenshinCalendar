import requests
from bs4 import BeautifulSoup
import os
import time
import csv
from datetime import datetime
import random

headers_list = [
        {'User-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'},
        {'User-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36'},
        {'User-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36'},
        {'User-agent': 'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1'}, 
        {'User-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'},
        {'User-agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666'},
        {'User-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320'},
        {'User-agent': 'Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/10.0.9.2372 Mobile Safari/537.10+'},
        {'User-agent': 'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/7.2.1.0 Safari/536.2+'},
        {'User-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'},
        {'User-agent': 'Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'},
        {'User-agent': 'Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'},
        {'User-agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G950U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'},
        {'User-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G965U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36'},
        {'User-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; SM-T837A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Safari/537.36'},
        {'User-agent': 'Mozilla/5.0 (Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true'},
        {'User-agent': 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LGMS323 Build/KOT49I.MS32310c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.0.0 Mobile Safari/537.36'},
        {'User-agent': 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 550) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/14.14263'},
        {'User-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'},
        {'User-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 10 Build/MOB31T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'},
        {'User-agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'},
        {'User-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'},
        {'User-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'},
        {'User-agent': 'Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6 Build/N6F26U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'},
        {'User-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'},
        {'User-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 7 Build/MOB30X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'},
        {'User-agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)'},
        {'User-agent': 'Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13'},
        {'User-agent': 'Mozilla/5.0 (Linux; Android 9; Pixel 3 Build/PQ1A.181105.017.A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36'},
        {'User-agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'},
        {'User-agent': 'Mozilla/5.0 (Linux; Android 11; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36'},
        {'User-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'},
        {'User-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'},
        {'User-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'},
        {'User-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'},
        {'User-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'},
        {'User-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'}
]

headers = random.choice(headers_list)


def folderexist(path):#create folder
    folder=os.path.exists(path)
    if not folder:
        return 0
    else:
        return 1

def search_items(name):#search character's upgrade materials
    pic_url=[]
    item_url=[]
    item_name=[]
    if(folderexist('D:\\GenshinCalendar\\pictures\\'+name)==0):#if already exisited, don't need to download again
        print("downloading materials...")
        url="https://wiki.biligame.com/ys/"+name
        headers = random.choice(headers_list)
        bs=BeautifulSoup(requests.get(url,headers=headers).content,"lxml")
        print("request successfully")
        i=0
        for divs in bs.find_all('div',class_='visible-md visible-sm visible-lg'):
            for tds in divs.find_all('td'):
                if(i>0):
                    i=i+1
                    for pic_link in tds.find_all('img'):
                        pic_url_before_replace=pic_link.get('src')
                        pic_url_after_replace=pic_url_before_replace.replace("70px-","140px-")
                        pic_url.append(pic_url_after_replace)
                    for divs_2 in tds.find_all('div',style="position: absolute;bottom: 0px;left:0px;font-size:10px;color:#fff;font-weight: bolder;text-shadow: #000 -1px 0 0,#763c12 0 -1px 0,#5d2b08 1px 0 0,#1d1515 0 1px 0;width: 68px;display: inline-block;overflow: hidden;white-space: nowrap;text-overflow: ellipsis;text-align:left;background: linear-gradient(rgb(0 0 0 / 0%), rgb(37 37 37 / 90%));width: 100%;;padding-left:2px"):
                        for a_s in divs_2.find_all('a'):
                            item_url.append("https://wiki.biligame.com"+a_s.get('href'))
                            item_name.append(a_s.get('title'))
                if(tds.string=="9→10\n"):
                    i=1
                    print("found!")
                if(i>1):
                    break
            if(i>1):
                break
        pic_url[4]=pic_url[4].replace("thumb","")
        pic_url[4]=pic_url[4].split("/140px-")[0]
        print("materials got successfully")
        return [pic_url,item_url,item_name,name]
    else:
        return [0,0,0,name]

def getnamelist():#get the list of character's name
    print('downloading namelist...')
    time.sleep(1.5)
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
    print("namelist got successfully")
    return(star_5,star_4,star_all)
    
def downloadpic(itemslist):#download the pictures of upgrade materials & get the time available
    requests.adapters.DEFAULT_RETRIES = 7
    if(folderexist('D:\\GenshinCalendar\\pictures\\'+itemslist[3])==0):#if already exisited, don't need to download again
        pic_url=itemslist[0]
        item_url=itemslist[1]
        item_name=itemslist[2]
        name=itemslist[3]
        os.makedirs('D:\\GenshinCalendar\\pictures\\'+name)
        print("pictures downloading...")
        for i in range(0,5):
            if(i==1):#get the time that materials are available
                time.sleep(1.5)
                j=0
                bs=BeautifulSoup(requests.get(item_url[1],headers=headers).content,"lxml")#get when you can find the upgrade materials
                print('request successfully')
                for tables in bs.find_all('table',class_='wikitable'):
                    print('table found')
                    for trs in tables.find_all('tr'):
                        for ths in trs.find_all('th'):
                            if(ths.string=='来源\n'):
                                print("th found")
                                j=1
                                for tds in trs.find_all('td'):
                                    tds=str(tds)
                                    tds=tds.split("时间：")[1]
                                    tds=tds.replace("/","")
                                    tds=tds.replace("\n<td>","")
                                    break
                                break
                            if(j==1):
                                break
                        if(j==1):
                            break
                with open('D:\\GenshinCalendar\\pictures\\'+name+'./%d'%(i+1)+item_name[i]+';'+tds+'.png', 'wb') as pic_file:
                    print("download%d/5:  "%(i+1)+pic_url[i])
                    time.sleep(1.5)
                    headers = random.choice(headers_list)
                    pic_file.write(requests.get(pic_url[i],headers=headers).content)
            else:
                with open('D:\\GenshinCalendar\\pictures\\'+name+'./%d'%(i+1)+item_name[i]+'.png', 'wb') as pic_file:
                    print("download%d/5:  "%(i+1)+pic_url[i])
                    time.sleep(1.5)
                    headers = random.choice(headers_list)
                    pic_file.write(requests.get(pic_url[i],headers=headers).content)
        print("pictures downloaded successfully")
        #with open('D:\\GenshinCalendar\\data.csv', "w", encoding="utf-8", newline="") as f:
        
def filenamelist(path):
    filenamelist=os.listdir(path)
    origin_namelist=[]
    namelist=[]
    i=1
    for name in filenamelist:
        origin_namelist.append(name)
        name=name.split(".")[0]
        name=name.split("%d"%(i))[1]
        namelist.append(name)
        i=i+1
    return [origin_namelist,namelist]

def readcsv(path):
    developlist1=[]
    if(folderexist(path)==0):
        print("Not found")
        with open(path, "w", encoding="utf-8", newline="") as f:
            csv_writer = csv.writer(f)
            name=['name','material','days']
            csv_writer.writerow(name)
    else:
        with open(path,'r', encoding='UTF-8') as f:
            next(f)
            for row in f:
                developlist1.append(row)
    return developlist1

def writecsv(path,developlist1):
    with open(path, "w", encoding="utf-8", newline="") as f:
        csv_writer = csv.writer(f)
        name=['name','material','days']
        csv_writer.writerow(name)
        csv_writer.writerows(developlist1)
        
def weekday(Qcal):
    today=str(Qcal)
    today=today.split('QDate(')[1]
    today=today.replace(')','')
    today1=datetime.strptime(today,"%Y, %m, %d")
    weekday=datetime.date(today1).weekday()+1
    return weekday

def showdeveloplist(dlist,wdtype):
    dlistshow=[]
    for character in dlist:
        if ((wdtype==1 and character[2]=='周一周四周日') or (wdtype==2 and character[2]=='周二周五周日') or (wdtype==3 and character[2]=='周三周六周日') or wdtype==4):
            dlistshow.append(character[0]+'----'+character[1])
    return dlistshow