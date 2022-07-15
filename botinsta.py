# __________________________________# PYTHON
try:
    from selenium import webdriver
except:
    print("""\n Please Install selenium\n
    pip install selenium (on CMD)
        """)


class instagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def Login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)
        user_name = self.driver.find_element_by_xpath("//input[@name='username']")
        user_name.clear()
        user_name.send_keys(self.username)
        time.sleep(2)
        pass_word = self.driver.find_element_by_xpath("//input[@name='password']")
        pass_word.clear()
        pass_word.send_keys(self.password)
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{self.username}/")

    def Comment(self, hsh):
        hashtag = hsh.split(",")
        for i in range(len(hashtag)):
            self.driver.get(f"https://www.instagram.com/explore/tags/{hashtag[i]}/")
            time.sleep(5)
            link_2 = []
            for l in range(20):
                link = self.driver.find_elements_by_tag_name('a')
                link_2 = [l.get_attribute('href') for l in link if '/p/' in l.get_attribute('href')]
                time.sleep(2)
                self.driver.execute_script("window.scroll(0, document.body.scrollHeight);")
                for ele in range(len(link_2)):
                    try:
                        time.sleep(1)
                        self.driver.get(link_2[ele])
                        time.sleep(1)
                        self.driver.execute_script("scroll(0,400)")
                        entry = lambda: self.driver.find_element_by_css_selector('textarea.Ypffh')
                        entry().click()
                        time.sleep(0.5)
                        entry().send_keys(com + Keys.ENTER)
                        print(f"\n {ele} \n")
                        time.sleep(randint(200, 240) / 2)
                    except:
                        self.driver.get(link_2[ele + 1])
                        time.sleep(1)
                        self.driver.execute_script("scroll(0,400)")
                        entry = lambda: self.driver.find_element_by_css_selector('textarea.Ypffh')
                        entry().click()
                        time.sleep(0.5)
                        entry().send_keys(com + Keys.ENTER)
                        print(f"\n {ele} \n")
                        time.sleep(randint(200, 240) / 2)


user = "username"

passs = "password"

com = "Best language for programming"

hashtaghs = "python"


test = instagramBot(user, passs)
test.Login()
time.sleep(2)
test.Comment(hashtaghs)
