import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


def choose():
    # url = "https://hot.ziroom.com/zrk_rent_cn/pages/list/main?product=1"
    url = "https://www.ziroom.com/z/"

    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_argument('--headless')  # 无头浏览器，不弹出浏览器，在后台爬取
    # web = Chrome(options=chrome_options)
    web = Chrome()
    web.get(url)

    # 地段
    web.find_element("xpath", '/html/body/section/div[2]/ul/li[1]/div/div[1]/span').click()
    web.find_element("xpath", '/html/body/section/div[2]/ul/li[1]/div/div[1]/div/div/a[2]').click()
    # web.find_element("xpath", '/html/body/section/div[2]/ul/li[1]/div/div[1]/div[2]/span[12]/span[2]/a[5]').click()

    # 类型 合租
    web.find_element("xpath", '/html/body/section/div[2]/ul/li[2]/div/a[2]').click()

    # 租金
    web.find_element(By.NAME, value="low").send_keys('100')
    web.find_element(By.NAME, value="high").send_keys('3500')
    web.find_element(By.CLASS_NAME, value="confirm").click()

    # 户型
    web.find_element("xpath", "/html/body/section/div[2]/ul/li[4]/div/a[1]").click()

    # 点击展开
    web.find_element("xpath", "/html/body/section/div[2]/div[1]/div").click()

    # 房源面积
    web.find_element("xpath", "/html/body/section/div[2]/ul/div/li[3]/div/a[2]").click()
    web.find_element("xpath", "/html/body/section/div[2]/ul/div/li[3]/div/a[3]").click()
    web.find_element("xpath", "/html/body/section/div[2]/ul/div/li[3]/div/a[4]").click()
    web.find_element("xpath", "/html/body/section/div[2]/ul/div/li[3]/div/a[5]").click()

    # 朝向：南、东、西
    web.find_element("xpath", "/html/body/section/div[2]/ul/div/li[4]/div/a[1]").click()
    web.find_element("xpath", "/html/body/section/div[2]/ul/div/li[4]/div/a[3]").click()
    web.find_element("xpath", "/html/body/section/div[2]/ul/div/li[4]/div/a[4]").click()

    # 供暖方式
    web.find_element("xpath", "/html/body/section/div[2]/ul/div/li[6]/div/a[1]").click()
    time.sleep(20)


def getXiChengInfo():
    url = 'https://www.ziroom.com/z/z1-d23008626-u9-r0/?p=b3-g2|1|3-a1|2|3|4&cp=100TO3500&isOpen=1'
    chrome_options = Options()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_argument('--headless')  # 无头浏览器，不弹出浏览器，在后台爬取
    web = Chrome(options=chrome_options)
    web.get(url)

    link_list = list()
    house_info_list = list()
    # 爬取链接
    pic_box = web.find_elements(By.CSS_SELECTOR, '.pic-box')
    for house0 in pic_box:
        if isSaleHouse(house0, 'tip'):
            continue
        link = house0.find_element(By.CLASS_NAME, 'pic-wrap').get_attribute("href")
        link_list.append(link)

    # 爬取房子信息
    info_box = web.find_elements(By.CSS_SELECTOR, '.info-box')
    for house in info_box:
        if isSaleHouse(house, 'label'):
            continue
        title = house.find_element(By.CLASS_NAME, 'title').text
        desc = house.find_element(By.CLASS_NAME, 'desc').text
        tag = house.find_element(By.CLASS_NAME, 'tag').text
        house_info_list.append(title + desc + tag)

    # 数据整合
    ans = merge(link_list, house_info_list)
    for i in ans:
        print(i)


def merge(link_list, house_info_list):
    ans = list()
    i = 0
    j = 0
    while i < len(link_list) and j < len(house_info_list):
        ans.append(link_list[i])
        ans.append(house_info_list[j])
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


if __name__ == '__main__':
    getXiChengInfo()
