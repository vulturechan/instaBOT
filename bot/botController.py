from sys import stdout
from time import sleep
from random import randint as rd
from selenium.webdriver.common.keys import Keys

class bot:
    def __init__(self, webdriver, hashtags=[], following=[],hashtag_quant=0,comments=0,followed=0,pub_open=0,likes=0,mark=0):
        self.hashtags_pass =[]
        self.hashtags = hashtags
        self.following = following
        self.webdriver = webdriver
        # estatisticas
        self.mark = mark
        self.likes = likes
        self.comments = comments
        self.followed = followed
        self.pub_open = pub_open
        self.hashtag_quant = hashtag_quant


    def main(self):
        bot.open_hashtag(self)
        while len(self.hashtags) != 0:
            bot.open_pub(self)
            for i in range(1,100):
                bot.time(rd(5,100))
                user = self.webdriver.find_element_by_css_selector('body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.UE9AK > div > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.e1e1d > span > a').text
                march = f' \n{user}, {bot.follow(self)}, Like: {self.likes},  Followeds: {self.followed}, Comments: {self.comments}, Open: {self.pub_open}'
                prob = rd(1,50)
                if prob < 10:
                    bot.comment(self,prob)
                elif prob > 10 and prob < 20:
                    bot.mark(self)
                elif (prob > 31 and prob < 40) and not (user in self.following):
                    march = f' \n{user}, {bot.follow(self, follow=True)}, Followeds: {self.followed}, Like: {self.likes}, Comments: {self.comments}, Open: {self.pub_open}'
                elif prob > 40:
                    bot.like(self)
                else:
                    march = march + 'pulo do gato'
                print(march)
                bot.next(self)  
        
        bot.data_update(self)
        return self.webdriver.close()
                

    def open_pub(self):
        self.pub_open += 1
        self.webdriver.find_element_by_css_selector('#react-root > section > main > article > div.EZdmt > div > div > div:nth-child(1) > div:nth-child(1) > a > div > div._9AhH0').click()


    def open_hashtag(self):
        for first in self.hashtags:
            self.webdriver.get('https://www.instagram.com/explore/tags/'+first+'/')
            self.hashtags.remove(first)
        
    
    def time(value):
        symbol = '.'
        for i in range(0, value):
            sleep(1)
            stdout.write(f'\r{value}/{i} $%-¬__>> {i*symbol}')
            stdout.flush()
           

    def next(self):
        self.pub_open += 1
        try:
            pass
        except:
            self.webdriver('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm').click()
        self.webdriver.find_element_by_css_selector('body > div.RnEpo._Yhr4 > div.Z2Inc._7c9RR > div > div.l8mY4.feth3 > button').click()
        sleep(2)


# ____ comments, Likes and Fallowed ________        
    def like(self):
        self.likes += 1
        try:
            self.webdriver.find_element_by_css_selector('body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button').click()
        except:
            return

    
    def mark(self):
        self.mark += 1
        try:
            self.webdriver.find_element_by_css_selector('body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.ltpMr.Slqrh > span.wmtNn > div > div > button').click()
        except:
            return


    def comment(self, value):
        bot.like(self)
        self.comments += 1
        self.webdriver.find_element_by_css_selector('body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.ltpMr.Slqrh > span._15y0l > button').click()
        comment_line = self.webdriver.find_element_by_css_selector('body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.eo2As > section.sH9wk._JgwE > div > form > textarea')
        if (value == 2):
            comment_line.send_keys('Very Cool!!')
            sleep(1)
        elif (value == 1) or (value == 4):
            comment_line.send_keys('Nice!')
            sleep(1)
        elif value == 9:
            comment_line.send_keys('I like its!')
            sleep(1)
        elif value == 10:
            comment_line.send_keys('wow, its very nice!')
            sleep(1)
        elif value == 3:
            comment_line.send_keys('OMG')
            sleep(1)
        else:
            comment_line.send_keys('LMAO!!')
            sleep(1)
        comment_line.send_keys(Keys.ENTER)
        sleep(rd(1,20))

    
    def follow(self,follow=False):
        self.followed += 1
        if follow == True:
            self.webdriver.find_element_by_css_selector('body > div.RnEpo._Yhr4 > div.pbNvD.QZZGH.bW6vo > div > article > div > div.HP0qD > div > div > div.UE9AK > div > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.bY2yH > button').click()
            return f'Followed: S'
        else:
            return f'Followwed: N'
# ____________________________________________________


    def data_update(self):
        bot.following_update(self)
        with open('DATA/botData', 'x') as file:
            file.write(self.hashtags)
            file.write(self.following)
            print(file.read())
        

if __name__ == "__main__":
    with open('bot/README.md', 'r') as file:
        print(file.read())
