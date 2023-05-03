import requests
from bs4 import BeautifulSoup
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\Chrome/55.0.2883.87 Safari/537.36'}

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
        url="https://wiki.biligame.com/ys/"+name
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
    
def downloadpic(itemslist):#download the pictures of upgrade materials
    if(folderexist('D:\\GenshinCalendar\\pictures\\'+itemslist[3])==0):#if already exisited, don't need to download again
        pic_url=itemslist[0]
        #item_url=itemslist[1]
        item_name=itemslist[2]
        name=itemslist[3]
        os.makedirs('D:\\GenshinCalendar\\pictures\\'+name)
        for i in range(0,5):
            pic_file=open('D:\\GenshinCalendar\\pictures\\'+name+'./%d'%(i+1)+item_name[i]+'.png', 'wb')
            pic_file.write(requests.get(pic_url[i]).content)
        pic_file.close()
        
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