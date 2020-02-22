# from instapy_cli import client
#
#
# with client("texnorama.uz", "texnorama2019!") as cli:
#     cli.upload("sample.jpg", "Hello everyone!!!")
#
# from InstagramAPI import InstagramAPI
#
# InstagramAPI = InstagramAPI("texnorama.uz", "texnorama2019!")
# InstagramAPI.login()  # login
#
# photo_path = 'sample.jpg'
# caption = "Sample photo"
# InstagramAPI.uploadPhoto(photo_path, caption=caption)
from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
import autoit
import time


def upload_photo_to_instagram(image_path, text):
    """

    :param image_path: full path to image
    :param text: text under image
    """
    username = "texnorama.uz"
    passwd = "texnorama2019!"
    driverpth = "C:/Program Files/chromedriver_win32/chromedriver.exe"

    photopath = image_path
    phototext = text

    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--silent")
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-logging")
    options.add_argument("--mute-audio")
    # mobile_emulation = {"deviceName": "Nexus 5"}
    # options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_argument(
        '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
    driver = webdriver.Chrome(executable_path=driverpth, options=options)
    driver.get("https://www.instagram.com/accounts/login/?hl=tr")
    time.sleep(3)
    driver.find_element_by_xpath(
        "//*[@id='react-root']/section/main/article/div/div/div/form/div[4]/div/label/input").send_keys(username)
    time.sleep(0.5)
    driver.find_element_by_xpath(
        "//*[@id='react-root']/section/main/article/div/div/div/form/div[5]/div/label/input").send_keys(passwd)
    time.sleep(0.5)
    driver.find_element_by_xpath(
        "//*[@id='react-root']/section/main/article/div/div/div/form/div[7]/button/div").click()
    while 1:
        time.sleep(1)
        try:
            driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/button").click()
            break
        except:
            pass
    # while 1:
    #     time.sleep(1)
    #     try:
    #         driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]").click()
    #         break
    #     except:
    #         pass

    # Click on cancel button on dialog box
    while 1:
        time.sleep(1)
        try:
            driver.find_element_by_xpath("/html/body//*[@role='dialog']/div/div[3]/button[2]").click()
            break
        except:
            pass

    # click on + button to add image
    driver.find_element_by_xpath("//div[@role='menuitem']").click()
    time.sleep(1.5)
    autoit.win_active("Open")  # open can change by your os language if not open change that
    time.sleep(2)
    autoit.control_send("Open", "Edit1", photopath)
    time.sleep(1.5)
    autoit.control_send("Open", "Edit1", "{ENTER}")
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='react-root']/section/div[1]/header/div/div[2]/button").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='react-root']/section/div[2]/section[1]/div[1]/textarea").send_keys(phototext)
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='react-root']/section/div[1]/header/div/div[2]/button").click()
    time.sleep(4)
    driver.close()

upload_photo_to_instagram('D:\\raisense\\projects\\texnorama_bot_integration\\sample.png', "heellloooo")