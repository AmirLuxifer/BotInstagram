# __________________________________# PYTHON
try:
    from selenium import webdriver
except:
    print("""\n Please Install selenium\n
    pip install selenium (on CMD)
        """)

try:
    from selenium.webdriver.common.keys import Keys
except:
    print("""\n Please Install selenium\n
    pip install selenium (on CMD)
        """)

try:
    import time
except:
    print("""\n Please Install time\n
    pip install time (on CMD)
        """)

try:
    from random import randint, choice
except:
    print("""\n Please Install random\n
    pip install random (on CMD)
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


user = "_amir.luxifer_"

passs = "amir0211"

com = "Best language for programming"

hashtaghs = "python"

# arezow_645
# 	123159753
# bitaow_25965
# 	123159753
# bahar_946324
# 	123159753
# hanie_sa963
# 	123159753
# bahre_mag987
# 	123159753
# setareww35963
#   123159753

# anita.bavari
#     123159753
# sara.moradi942
#     123159753
# reyhane.habibi952
#     123159753
# bitaaww.81
#     123159753
# bahare.sajadi_82
#     123159753

# faeeze.hamidi_83
#     123159753

"""
هرچی درمورد عکاسی بخوای داخل این پیج میتونی پیدا کنی @_hossein.visiontik__ @_hossein.visiontik__ @_hossein.visiontik__
یکی از بهترین پیج های آموزش عکاسی @_hossein.visiontik__ @_hossein.visiontik__ @_hossein.visiontik__
آموزش ژست گرفتن و عکاسی رو میتونین داخل این پیج  ببینید @_hossein.visiontik__ @_hossein.visiontik__ @_hossein.visiontik__ 
با این پیج حرفه ای عکاسی کنید  @_hossein.visiontik__ @_hossein.visiontik__ @_hossein.visiontik__
یکی از بهترین و حرفه ای ترین پیج های آموزش عکاسی @_hossein.visiontik__ @_hossein.visiontik__ @_hossein.visiontik__
یکی از بهترین پیج های عکاسی با استوری های اموزشی و جذاب @_hossein.visiontik__ @_hossein.visiontik__ @_hossein.visiontik__
"""
# عکاسی
# عکاسی_هنری
# عکاسی_پرتره
# عکاسی_با_موبایل
# عکاسی_مدلینگ
# عکاسی_حرفه_ای
# مدلینگ
# مدلینگ_عکاسی
# مدلینگ_دختر
# مدلینگ_پسر


"""
با اجازه ادمین سلام عشقا هرکی یه هََکــر مطمعن میخواد به ایدی پایین پیام بده @morteza_help @morteza_help @morteza_help
خدایی کارش حرف نداره هکــر قدرتمند صادق و کااار درست دمش گرمه حقیقت میگه @morteza_help @morteza_help @morteza_help @morteza_help
دوستان عزیز هََکر مطمعن سراغ دارم ایدی اینستاشو میدم حتما بهش پیام بدید @morteza_help @morteza_help @morteza_help
سلام عزیزان هرکسی مشکلی در مورد اینستااا داشت حتما به ایشون مراجعه کنه @morteza_help @morteza_help @morteza_help
"""
# اینستاگرام_مارکتینگ
# هکر_اینستا
# هکر
# اخبار
# هک
# امنیت_پیج
# امنیت_اطلاعات
# امنیت_سایبری
# امنیت_اینستاگرام
# اختراع


test = instagramBot(user, passs)
test.Login()
time.sleep(2)
test.Comment(hashtaghs)
