from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def login(self):
        self.driver.get('http://tinder.com')

    def dislike(self):
        dislike = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[2]/button')
        dislike.click()

    def auto_swipe(self):
        while True:
            sleep(0.5)
            try:
                self.dislike()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self)