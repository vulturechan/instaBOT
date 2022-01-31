from time import sleep
from random import randint as rd
from selenium.webdriver.common.keys import Keys

class bot:
    def __init__(self, webdriver, hashtags=[], following=[], accont_new=[], followed_new=[], followed=0, likes=0, pub_open=0, comments=0):
        self.following = following
        self.hashtags = hashtags
        self.webdriver = webdriver
        self.accont_new = accont_new
        self.followed_new = followed_new
        self.hashtags_pass =[]
        # estatisticas
        # self.likes = likes
        # self.comments = comments
        # self.followed = followed
        # self.pub_open = pub_open


    def main(self):
        bot.open_hashtag(self)
        bot.data_scraping(self)
        bot.process(self)
            
            
    def process(self):
        for i in range(len(self.accont_new)):
            if not (self.accont_new[i] in self.following):
                user = self.accont_new[i]
                self.webdriver.get('https://www.instagram.com/'+str(user)+'/')
                sleep(2)
                print(i, user, bot.new_fallowed(self,user))
                # bot.open_firstpub(self)
                # prob = rd(1,20)
                # if prob < 10:
                #     bot.like(self)
                #     sleep(rd(1,20))

            
    def open_hashtag(self):
        for i in self.hashtags:
            self.webdriver.get('https://www.instagram.com/explore/tags/'+i+'/')
            self.hashtags.remove(i)
            self.hashtags_pass.append(i)


    def data_scraping(self):
        self.webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div').click()
        sleep(2)
        bot.add_new_user(self)
        for i in range(0,10):
            bot.next(self,i)
            bot.add_new_user(self)


    def open_firstpub(self):
        self.webdriver.element_find_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div').click()

    
    def add_new_user(self):
        self.accont_new.append(self.webdriver.find_element_by_xpath('/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/span/a').text)


    def next(self, value):
        if value == 0:
            self.webdriver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/button').click()
            sleep(2)
        else:
            self.webdriver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div[2]/button').click()
            sleep(2)


# ____ comments, Likes and Fallowed ________        
    def like(self):
        self.webdriver.find_element_by_xpath('/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button').click()


    def comment(self, value):
        bot.like(self)
        comment_line = self.webdriver.element_find_by_xpath('/html/body/div[5]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')
        if (value < 7):
            comment_line.send_keys('a decidir')
            sleep(1)
        elif (value > 6) and (value < 9):
            comment_line.send_keys('a decidir')
            sleep(1)
        elif value == 9:
            comment_line.send_keys('a decidir')
            sleep(1)
        elif value == 10:
            comment_line.send_keys('a decidir')
            sleep(1)
        comment_line.send_keys(Keys.ENTER)


    def new_fallowed(self, user):
        pub = int(self.webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span/span').text.replace('.', ''))
        followers = int(self.webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').get_attribute('title').replace('.', ''))
        if followers > 2000 and pub > 20:
            self.webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button').click()
            self.followed_new.append(user)
            return f'Publication: {pub}\r Followers: {followers} S'
        else:
            return f'Publication: {pub}\r Followers: {followers} N'
# ____________________________________________________

    def data_update(self):
        with open('DATA/botData', 'x') as file:
            file.write(self.hashtags)
            file.write(self.hashtag_pass)
            file.write(self.following)
            file.write(self.fallowed_new)
            print(file.read())
        
        return self.webdriver.close()
        

if __name__ == "__main__":
    with open('bot/README.md', 'r') as file:
        print(file.read())
