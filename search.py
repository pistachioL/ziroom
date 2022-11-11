from util import *


# 通过搜索关键字找房
def searchHouse():
    url = 'https://www.ziroom.com/z/'
    web.get(url)

    house_info_list = list()
    link_list = list()
    areas = ['广安门', '西直门', '和平里', '复兴路']
    for area in areas:
        print('正在爬取：' + area + '的房源......')
        web.find_element(By.CLASS_NAME, 'Z_search_input').clear()
        web.find_element(By.CLASS_NAME, 'Z_search_input').send_keys(area)
        web.find_element(By.CLASS_NAME, 'Z_search_btn').click()
        web.find_element(By.LINK_TEXT, '合租').click()
        web.find_element(By.CLASS_NAME, 'low').send_keys('100')
        web.find_element(By.CLASS_NAME, 'high').send_keys('3500')
        web.find_element(By.CLASS_NAME, 'confirm').click()
        web.find_element(By.LINK_TEXT, '2户合住').click()
        web.find_element(By.CLASS_NAME, 'more').click()
        web.find_element(By.LINK_TEXT, '10-12㎡').click()
        web.find_element(By.LINK_TEXT, '12-15㎡').click()
        web.find_element(By.LINK_TEXT, '15-20㎡').click()
        web.find_element(By.LINK_TEXT, '20㎡以上').click()
        web.find_element(By.LINK_TEXT, '南').click()
        web.find_element(By.LINK_TEXT, '东').click()
        web.find_element(By.LINK_TEXT, '西').click()
        web.find_element(By.LINK_TEXT, '长租1年').click()

        if isPageTurn(web, '.Z_pages .next'):
            while True:
                for inf in getHouseInfo():
                    house_info_list.append(inf)

                for li in getLink():
                    link_list.append(li)

                if isPageTurn(web, '.Z_pages .next'):
                    web.find_element(By.XPATH, '//*[@id="page"]/a[last()]').click()
                else:
                    break
        else:
            house_info_list = getHouseInfo()
            link_list = getLink()

        houseList = merge(house_info_list, link_list)
        print("======= 搜索房子详情：", str(len(house_info_list)) + '个房源 =======')
        for house in houseList:
            print(house)
        print('\n')

