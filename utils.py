def test(name):
    import requests
    from bs4 import BeautifulSoup
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\Chrome/55.0.2883.87 Safari/537.36'}
    url="https://wiki.biligame.com/ys/"+name
    #print(url)
    bs=BeautifulSoup(requests.get(url,headers=headers).content,"lxml")
    #print(bs.prettify)
    i=0
    for divs in bs.find_all('div',class_='visible-md visible-sm visible-lg'):
        for tds in divs.find_all('td'):
            if(i>0):
                i=i+1
                for divs_2 in tds.find_all('div',style="position: absolute;bottom: 0px;left:0px;font-size:10px;color:#fff;font-weight: bolder;text-shadow: #000 -1px 0 0,#763c12 0 -1px 0,#5d2b08 1px 0 0,#1d1515 0 1px 0;width: 68px;display: inline-block;overflow: hidden;white-space: nowrap;text-overflow: ellipsis;text-align:left;background: linear-gradient(rgb(0 0 0 / 0%), rgb(37 37 37 / 90%));width: 100%;;padding-left:2px"):
                    for a_s in divs_2.find_all('a'):
                        url=a_s.get('href')
                        print("https://wiki.biligame.com"+url)
            if(tds.string=="9→10\n"):
                i=1
                print("found!")
            if(i>1):
                break
        if(i>1):
            break
    #print("Done2")
    #for link in tds:
        #print(link)
    print("Done")