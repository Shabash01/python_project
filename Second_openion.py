import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv
import random
movie_rating = movie_year = movie_rank = movie_name = []
class Movie_Suggstion():
    def Scrapy(self, url, cc):
        try:
            source = requests.get(url)
            source.raise_for_status()
            soup = BeautifulSoup(source.text, 'html.parser')
            movies = soup.find_all('div', class_="lister-item mode-advanced")
            for movie in movies:
                name = movie.h3.a.text
                movie_name.append(name)
                rank = movie.find('div', class_='lister-item-content').span.text
                movie_rank.append(rank)
                year = movie.find('span', class_='lister-item-year').text.strip('()')
                movie_year.append(year)
                rating = movie.find('span', class_='lister-item-year text-muted unbold').text
                movie_rating.append(rating)
        except Exception as e:
            print("Something wrong with Url :( !!!\n and make sure your connection is good ", e)
            obj.new_URL()
        movie_DF = pd.DataFrame({'Name of movie': movie_name, 'Year of release': movie_year, 'Watch time': movie_rank,
                                 'Movie rating': movie_rating})
        print(movie_DF)
        movie_DF.to_csv(cc)
        return
    def random(self, cc):
        with open(cc) as f:
            r = csv.reader(f)
            header, l = next(r), list(r)
            r = random.choice(l)
        print(f'''{r}
Are you not satisfied with this movie press "R" to re-pick another one. 
or do you want to pic a movie by your own press "N"
to continue press "Y" ''')
        i = input('Give Your Input ')
        if i == 'y' or i == 'Y':
            print(f'''{r}\n Enjoy your movie''')
        elif i == 'r' or i == 'R':
            obj.random(cc)
        elif i == 'n' or i == 'N':
            print("Give a Number I'll get that movie for you")
            obj.reader(cc)
            ip = input('Give your Input : ')
            obj.my_decision(ip, n, cc)
        else:
            print('Wrong Input User !! ')
            obj.operation(cc)
    def welcome(self):
        print('''Welcome User !
         I'm here to help you for pick a movie 
         By default I prefer Action garner  
         Do you want to Change the link press " C "
         And It will take only a valid "imdb" address
         or do yo like to continue in this garner
         Press "y" to Continue press "E" to exit from the loops''')
        first = input('Enter Your Input : ')
        if first == 'y' or first == 'Y':
            cc = 'Movie_Data_pd.csv'
            obj.operation(cc)
        elif first == 'c' or first == 'C':
            obj.new_URL()
        elif first == 'E' or first == 'e':
            quit()
        else:
            print('Check your Input User !!! ')
            obj.welcome()
    def new_URL(self):
        print(f'''Before Giving Your Valid Url check once if it is valid or not.
                    than You have to give a name to perform \n You can use this links to perform \n {mod} ''')
        url_name = input('Give Your Valid Url : ')
        name = input('Give a Name for your file without .extension : ')
        f_name = name + '.csv'
        obj.Scrapy(url_name, f_name)
        obj.operation(f_name)
    def get_movie(self, n, cc):
        with open(cc) as f:
            d = csv.reader(f)
            header, l = next(d), list(d)
        print(l[n])
    def reader(self, cc):
        dd = open(cc)
        for data in dd:
            print(data)
    def operation(self,cc):
        results = pd.read_csv(cc)
        global n
        n = len(results)
        if n >= 0:
            print(f'''Here I listed {n} number of movies for you give "SI.number" for the movie
                    {obj.reader(cc)}
            I'll get that movie for you or do you like to pic a random one Press " R "''')
            ip = input('Give your Input : ')
            if ip == 'r' or ip == 'R':
                obj.random(cc)
            elif not None:
                obj.my_decision(ip, n, cc)
            else:
                obj.welcome()
        else:
            print("Sorry user Your Url Doesn't valid Try somthing new :) ")
            obj.welcome()
    def my_decision(self,ip, n, cc):
        try:
            d = int(ip)
            if d <= n:
                od = obj.get_movie(d, cc)
                print(f'''{od}
                        Are ok with you desertion press "Y" to continue
                        press "N" to No or 
                         do you need movie picker press "R" are ''')
                dc = input('Give your Input : ')
                if dc == 'Y' or dc == 'y':
                    print('Enjoy Your Movie')
                    od
                elif dc == 'r' or dc == 'R':
                    obj.random(cc)
                elif dc == 'n' or dc == 'N':
                    obj.operation(cc)
            elif d>=n:
                print('You Enter incorrect value', d)
                obj.my_decision(ip,n,cc)
        except Exception:
            print('Check Your Input User !! ')
            obj.welcome()

obj = Movie_Suggstion()
mod = (
    '"https://www.imdb.com/search/title/?genres=Comedy&ref_=nv_sr_srsg_0_tt_6_nm_1_q_come"\n "https://www.imdb.com/find/?q=drama&ref_=nv_sr_sm"')
while True:
    obj.welcome()
    break