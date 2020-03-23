from selenium import webdriver
from getpass import getpass


class facebooKAutomation:
    def fetch(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        return driver

    def parse(self, html):
        pass

    def run(self):
        usr = input("Enter User Name: ")
        pwd = getpass("Enter Password")
        response = self.fetch('https://www.facebook.com/')
        username_box = response.find_element_by_id("email")
        userpas_box = response.find_element_by_id('pass')
        username_box.send_keys(usr)
        userpas_box.send_keys(pwd)
        login_btn = response.find_element_by_id(
            "u_0_b")
        print(login_btn)
        login_btn.submit()
        print(response)


if __name__ == '__main__':
    scraper = facebooKAutomation()
    scraper.run()
