import random

class Movie_Suggestion():
    def randomizer(self, kl, dic):
        dd = random.choice(kl)
        op = dic[dd]
        return (op)
    def dic_out(self, i, q):
        ok=q[i]
        return (ok)
    def category(self):
        ga_ip=input('Give your input : ')
        if ga_ip == 'y' or ga_ip == 'Y':
            op = obj.randomizer(gl,gd)
            print(f'''Are u ok with this {op}''')
            o = input('Give your input : ')
            if o == 'y' or 0 == 'Y':
                obj.movies(op)
            else:
                obj.welcom()

        elif ga_ip in gl:
            op = obj.dic_out(ga_ip, gd)
            print(f'''Are u ok with this {op}''')
            o = input('Give your input : ')
            if o == 'y' or o == 'Y':
                obj.movies(op)

            else:
                obj.category()

        else:
             quit(print('Y boss wrong input ??'))
    def movies(self, gd):
        lis=obj.dic_out(gd,gdl)
        print(f'''movie list {lis}''')
        i=input('give your input : ')
        if i=='y':
            kk=(list(lis.keys()))
            obj.final(kk)

        elif i in list(l.keys()) or list(l2.keys()) or list(l3.keys()) or list(l4.keys()):
            print('hi')
            obj.dic_out(i,l)

        else:
            print('dic keys')
            l[i]
            print('ok pa')

    def dic_val(self, dic, key):
        ot=dic[key]
        print(ot)
    def final(self,i):
        o = random.choice(i)
        print(f'''I get this movie for you {o}
                    press "y" to continue "n" to pick other one ''')
        m=input('give your input : ')
        if m=='y':
            print('Enjoy your movie :) ')
            print(o)
        elif m=='n':
            obj.final(i)
        else:
            obj.movies()

    def welcom(self):
        print(f'''
                   Hello user!!
                   here I will help you suggest a movie to watch 
                   movie genrs are = {mg}
                   You can choose your own or do you need suggestion press y
                   ''')
        quit(obj.category())

gl = ['Action', 'Comedy', 'Drama', 'general']
gd = {"Action": 'ACTION', "Comedy": 'COMEDY', "Drama": 'DRAMA', "general": 'GENERAL'}
gdl = {'ACTION':None,'COMEDY': None,'DRAMA': None,'GENERAL': None}
l = {"mo1": 'link1', "mo2": 'link2', "mo3": 'link 3'}
l2 = {"move1": 'link1', "mov2": 'link2', "mov3": 'link 3'}
l3 = {"movi1": 'link1', "movi2": 'link2', "movi3": 'link 3'}
l4 = {"movie1": 'link1', "movie2": 'link2', "movie3": 'link 3'}

gdl['ACTION'] =l
gdl['COMEDY'] =l2
gdl['DRAMA'] =l3
gdl['GENERAL'] =l4

obj = Movie_Suggestion()
l="movie list"
d="f"
mg ='movie cat'
while True:
    obj.welcom()