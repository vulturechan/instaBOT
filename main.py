from time import sleep
from login import login
from selenium import webdriver
from bot.botController import bot
from selenium.webdriver.common.keys import Keys

with open('bot/DATA/botData.txt') as file:
    hashtags = file.readline().split(',')
    following = file.readline().split(',')

chromedriver = webdriver.Chrome(executable_path='chrome/driver.exe')
chromedriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(2)
user = login(chromedriver,'user.txt')
user.initialize()
sleep(2)
libot = bot(chromedriver, hashtags, following)
libot.main()
