from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.common.keys
import time
import schedule

x = 0


def dmer():
    global x

    usrnames = ['usernaame1', 'username2']  # add user names here

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    browser = webdriver.Chrome("chromedriver.exe")

    browser.get('https://www.instagram.com/accounts/login/')

    time.sleep(2)

    usrname_bar = browser.find_element_by_xpath(
        '//*[@id="loginForm"]/div/div[1]/div/label/input')
    passwrd_bar = browser.find_element_by_xpath(
        '//*[@id="loginForm"]/div/div[2]/div/label/input')
    username = 'username'  # Enter your username here
    password = 'password'  # Enter your password here

    usrname_bar.send_keys(username)
    passwrd_bar.send_keys(password + Keys.ENTER)
    time.sleep(5)

    urlrn = browser.current_url
    if urlrn == 'https://www.instagram.com/accounts/onetap/?next=%2F':
        notnow = browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/div/button')
        notnow.click()

        time.sleep(3)

    # action = webdriver.common.action_chains.ActionChains(browser)
    # action.move_to_element_with_offset(5, 5)
    # action.click()
    # action.perform()

# in case the "save info" pops up!

    def checkelement():
        try:
            browser.find_element_by_xpath(
                '/html/body/div[4]/div/div/div/div[3]/button[2]') or browser.find_element_by_class_name('aOOlW   HoLwm ')
        except NoSuchElementException:
            return False
        return True

    if checkelement() == True:
        notnowbtn = browser.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[3]/button[2]')
        notnowbtn.click()

    time.sleep(2)
   # no we land on the main page

    while(True):  # used a white method so that the broeser doesnt closes

        browser.get('https://www.instagram.com/direct/new/')

        time.sleep(5)

        tobtn = browser.find_element_by_name('queryBox')  # search box

        tobtn.send_keys(usrnames)

        time.sleep(3)

        checkbox = browser.find_element_by_class_name(
            'dCJp8')  # check the users
        checkbox.click()

        time.sleep(3)

        nextbluebutton = browser.find_element_by_xpath(
            '/html/body/div[2]/div/div/div[1]/div/div[2]/div/button/div')  # next button
        nextbluebutton.click()

        time.sleep(2)

        textbox = browser.find_element_by_tag_name('textarea')  # text area
        # Customize your message
        textbox.send_keys(
            f"Hi @{usrnames} ! What's up ?")  # Customize your message

        time.sleep(2)

        snd_btn = browser.find_elements_by_tag_name('button')
        snd_btnn = snd_btn[len(snd_btn)-1]
        snd_btnn.click()

        time.sleep(2)

        browser.quit()
        print(f'''successfully sent a dm to the user
        
        built by
         __           __       __
        |  |         |  |     |  |
        |  |         |  |_____|  |
        |  |         |   _____   |
        |  |_____    |  |     |  |
        |________| . |__|     |__|
   
        reference github: b3!ngD3v )

         folow me on Instagram: @harshithlaxman
        Github: harshithlaxman

        <3 <3 <3

        
        
        
        
        ''')


# if __name__ == "__main__":
#     try:
#         dmer()
#     except TypeError:
#         print('failed')
# time to send the message(sheduled)
sheduledtime = "00:07:00"

try:
    schedule.every().day.at(sheduledtime).do(dmer)
except TypeError:
    pass

try:
    while True and x != 1:
        schedule.run_pending()
        time.sleep(1)
except UnboundLocalError:
    pass
