from time import sleep
from login import login
from selenium import webdriver
from bot.botController import bot
from selenium.webdriver.common.keys import Keys

chromedriver = webdriver.Chrome(executable_path='chrome/driver.exe')
chromedriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(2)
user = login(chromedriver,'user.txt')
user.initialize()
sleep(2)
libot = bot(chromedriver, ['programming', 'coding'])
libot.main()
