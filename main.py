from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_argument('--headless')  # 无头浏览器，不弹出浏览器，在后台爬取
web = Chrome(options=chrome_options)


# 爬取房子信息
def getHouseInfo():
    house_info_list = list()
    info_box = web.find_elements(By.CSS_SELECTOR, '.info-box')
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
    pic_box = web.find_elements(By.CSS_SELECTOR, '.pic-box')
    for house in pic_box:
        if isSaleHouse(house, 'tip'):
            continue
        link = house.find_element(By.CLASS_NAME, 'pic-wrap').get_attribute("href")
        link_list.append(link)

    return link_list


def merge(link_list, house_info_list):
    ans = list()
    i = 0
    j = 0
    while i < len(link_list) and j < len(house_info_list):
        ans.append(house_info_list[j])
        ans.append(link_list[i])
        i += 1
        j += 1
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


def getXiChengInfo():
    url = 'https://www.ziroom.com/z/z1-d23008626-u9-r0/?p=b3-g2|1|3-a1|2|3|4&cp=100TO3500&isOpen=1'
    web.get(url)
    xc_house_info_list = list()
    xc_link_list = list()

    if isPageTurn(web, '.Z_pages .next'):
        for page in range(0, 3):
            for inf in getHouseInfo():
                xc_house_info_list.append(inf)

            for li in getLink():
                xc_link_list.append(li)

            web.find_element(By.XPATH, '//*[@id="page"]/a[last()]').click()
    else:
        xc_house_info_list = getLink()
        xc_link_list = getHouseInfo()

    # 数据整合
    ans = merge(xc_house_info_list, xc_link_list)
    print("==================================西城区房子详情：", str(len(xc_house_info_list)) + '个房源==================================')
    for i in ans:
        print(i)


def getChaoYangInfo():
   #url = 'https://www.ziroom.com/z/z1-d23008613-u9-r0/?p=b3-g2|1|3-a1|2|3|4&cp=100TO3500&isOpen=1'
    url = 'https://www.ziroom.com/z/z1-d23008613-b18335706%7C18335709%7C18335711%7C18335740%7C18335647%7C18335704%7C611100324%7C18335736%7C611100448%7C18335622%7C18335707%7C611100698%7C611100316%7C18335641%7C611100323%7C611100330%7C611100602%7C1100006187%7C18335728%7C611100446-u9-r0/?p=b3-g2|1|3-a1|2|3|4&cp=100TO3500&isOpen=0'
    web.get(url)

    cy_house_info_list = list()
    cy_link_list = list()
    if isPageTurn(web, '.Z_pages .next'):
        for page in range(0, 3):
            for inf in getHouseInfo():
                cy_house_info_list.append(inf)

            for li in getLink():
                cy_link_list.append(li)

            web.find_element(By.XPATH, '//*[@id="page"]/a[last()]').click()
    else:
        cy_house_info_list = getHouseInfo()
        cy_link_list = getLink()

    houseList = merge(cy_house_info_list, cy_link_list)

    print("==================================朝阳区区房子详情：", str(len(cy_house_info_list)) + '个房源==================================')
    for i in houseList:
        print(i)


if __name__ == '__main__':
    getXiChengInfo()
    getChaoYangInfo()
