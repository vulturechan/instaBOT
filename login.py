from time import sleep

class login:
    def __init__(self, webdriver, path_file):
        self.webdriver =  webdriver
        self.path_file = path_file

    
    def initialize(self):
        login.open_user_file(self)
        login.login(self)

    
    def open_user_file(self):
        with open(str(self.path_file), 'r') as file:
            self.__email_user = file.readline()
            self.__password_user = file.readline()

    
    def login(self):
        self.webdriver.find_element_by_name('username').send_keys(self.__email_user)
        self.webdriver.find_element_by_name('password').send_keys(self.__password_user)
        sleep(4)
        self.webdriver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button').click()
        sleep(4)
        self.webdriver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button').click()
        sleep(4)
        self.webdriver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm').click()
        sleep(4)