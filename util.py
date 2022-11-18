from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_argument('--headless')  # 无头浏览器，不弹出浏览器，在后台爬取
# web = Chrome(options=chrome_options)
web = Chrome()


# 爬取房子信息
def getHouseInfo():
    house_info_list = list()
    info_box = web.find_elements(By.CSS_SELECTOR, 'body > section > div.Z_list > div.Z_list-box > div > div.info-box')
    for house in info_box:
        if isSaleHouse(house, 'label'):
            continue
        title = house.find_element(By.CLASS_NAME, 'title').text
        desc = house.find_element(By.CLASS_NAME, 'desc').text
        tag = house.find_element(By.CLASS_NAME, 'tag').text
        house_info_list.append(title + desc + tag)

    return house_info_list


# 爬取链接信息
def getLink():
    link_list = list()
    pic_box = web.find_elements(By.CSS_SELECTOR, 'body > section > div.Z_list > div.Z_list-box > div > div.pic-box')
    for house in pic_box:
        if isSaleHouse(house, 'tip'):
            continue
        link = house.find_element(By.CLASS_NAME, 'pic-wrap').get_attribute("href")
        link_list.append(link)

    return link_list


def merge(link_list, house_info_list):
    ans = [x for y in zip(house_info_list, link_list) for x in y]
    return ans


# 判断是否特价房
def isSaleHouse(driver, tag):
    flag = True
    try:
        driver.find_element(By.CLASS_NAME, tag)
        return flag
    except:
        flag = False
        return flag


def isPageTurn(driver, class_name):
    flag = True
    try:
        driver.find_element(By.CSS_SELECTOR, class_name)
        return flag
    except:
        flag = False
        return flag
