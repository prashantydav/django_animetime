from bs4 import BeautifulSoup
import requests
import sys
import datetime
# scraped data of my anime list
class ScrapedData:
    
   
    def get_title():
         
        tlist = []
        page = requests.get("https://myanimelist.net/anime/season")
        soup = BeautifulSoup(page.text,"lxml")
        anime_detail = soup.find_all('div',class_="seasonal-anime js-seasonal-anime")
        for detail in anime_detail:
            tlist.append(str(detail.find('a',class_="link-title").text.encode("utf-8")).split("'")[-2])
        return tlist

    def get_genre():
        glist = []
        page = requests.get("https://myanimelist.net/anime/season")
        soup = BeautifulSoup(page.text,"lxml")
        anime_detail = soup.find_all('div',class_="seasonal-anime js-seasonal-anime")
        for detail in anime_detail:
            inner = detail.find(class_="genres-inner js-genre-inner")
            glist.append(inner.get_text().replace("\n"," "))
        return glist


    def get_production():
        plist = []
        page = requests.get("https://myanimelist.net/anime/season")
        soup = BeautifulSoup(page.text,"lxml")
        anime_detail = soup.find_all('div',class_="seasonal-anime js-seasonal-anime")
        for detail in anime_detail:
            plist.append(str(detail.find('span',class_="producer").text.encode("utf-8")).split("'")[-2])
        return plist

    def get_image():
        ilist = []
        page = requests.get("https://myanimelist.net/anime/season")
        soup = BeautifulSoup(page.text,"lxml")
        anime_detail = soup.find_all('div',class_="seasonal-anime js-seasonal-anime")
        for detail in anime_detail:
            sub = detail.find("div",class_="image")
            im = str(sub.a.img.encode("utf-8")).split(" ")[-3]
            ilist.append(im)
        return ilist

    def get_discription():
        dlist = []
        page = requests.get("https://myanimelist.net/anime/season")
        soup = BeautifulSoup(page.text,"lxml")
        anime_detail = soup.find_all('div',class_="seasonal-anime js-seasonal-anime")
        for detail in anime_detail:
            inner = str(detail.find(class_="preline").get_text().encode("utf-8"))
            dlist.append(inner)
        return dlist

    def get_release_date():
        rlist = []
        page = requests.get("https://myanimelist.net/anime/season")
        soup = BeautifulSoup(page.text,"lxml")
        anime_detail = soup.find_all('div',class_="seasonal-anime js-seasonal-anime")
        for detail in anime_detail:
            inner = detail.find(class_="remain-time").text.strip().replace(",","")
            # print(inner)'
            if len(inner) <= 11:
                inner = inner + " 00:00:00"
            if len(inner) > 11:
                inner = inner[:18]
            rlist.append(inner)
        
        return rlist

    def get_season():
        rlist = []
        page = requests.get("https://myanimelist.net/anime/season")
        soup = BeautifulSoup(page.text,"lxml")
        anime_detail = soup.find('div',class_="navi-seasonal js-navi-seasonal")
        season = anime_detail.find("h1",class_="season_nav").text.strip()
        
        return season

    
        

    def get_image():
            ilist = []
            page = requests.get("https://myanimelist.net/anime/season")
            soup = BeautifulSoup(page.text,"lxml")
            anime_detail = soup.find_all('div',class_="seasonal-anime js-seasonal-anime")
            for detail in anime_detail:
                sub = detail.find("div",class_="image")
                im = str(sub.a.img.encode("utf-8")).split(" ")[-3]
                ilist.append(im)
            return ilist

    def get_news():
        ilist=[]
        tlist = []
        hlist =[]
        page = requests.get("https://myanimelist.net/news")
        soup = BeautifulSoup(page.text,"lxml")
        titles= soup.find_all("p",class_="title")
        for title in titles:
            anime_title = title.text.split("\n")[1]
            title_link = title.a.get("href")
            tlist.append(anime_title)
            hlist.append(title_link)
        for i in range(20):
            inf = f'{tlist[i]} more info: {hlist[i]}'
            ilist.append(inf) 
        
        return tlist

    def get_episodes():
        plist = []
        page = requests.get("https://myanimelist.net/anime/season")
        soup = BeautifulSoup(page.text,"lxml")
        anime_detail = soup.find_all('div',class_="seasonal-anime js-seasonal-anime")
        for detail in anime_detail:
            epi = ((detail.find('div',class_="eps").text)[1:3]).strip()
            if epi == "?":
                epi = "12"
            plist.append((int(epi)))
        return plist


            


p = ScrapedData
# print((p.get_release_date()))
# print(len(p.get_release_date()[-1]))
# print(len(p.get_release_date()[57]))
print((p.get_episodes()))