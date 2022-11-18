import time

from util import *


# 通过搜索关键字找房
def searchHouse():
    url = 'https://www.ziroom.com/z/'
    web.get(url)

    areas = ['亚运村', '惠新西街', '西单', '车公庄', '官园', '西直门', '安德里', '广安门', '军博', '公主坟', '甘家口', '紫竹桥',
             '白石桥', '苏州桥', '双榆树', '五道口', '德胜门', '六铺炕', '知春路', '牡丹园', '二里庄', '南沙滩'
             '马甸桥', '安华桥', '健翔桥', '黄寺大街安定门', '安贞', '雍和官', '交道口', '地安门', '东四',
             '宣武门', '长椿街', '月坛', '金融街', '阜成门']

    for area in areas:
        house_info_list = list()
        link_list = list()
        print('正在爬取：' + area + '的房源......')
        web.find_element(By.CLASS_NAME, 'Z_search_input').clear()
        web.find_element(By.CLASS_NAME, 'Z_search_input').send_keys(area)
        web.find_element(By.CLASS_NAME, 'Z_search_btn').click()
        web.find_element(By.LINK_TEXT, '合租').click()
        time.sleep(1)
        web.find_element(By.CLASS_NAME, 'low').send_keys('1000')
        web.find_element(By.CLASS_NAME, 'high').send_keys('3500')
        web.find_element(By.CLASS_NAME, 'confirm').click()
        time.sleep(1)
        web.find_element(By.LINK_TEXT, '2户合住').click()
        time.sleep(1)
        web.find_element(By.CLASS_NAME, 'more').click()
        time.sleep(1)
        web.find_element(By.LINK_TEXT, '12-15㎡').click()
        web.find_element(By.LINK_TEXT, '15-20㎡').click()
        web.find_element(By.LINK_TEXT, '20㎡以上').click()
        time.sleep(1)
        web.find_element(By.LINK_TEXT, '南').click()
        web.find_element(By.LINK_TEXT, '东').click()
        web.find_element(By.LINK_TEXT, '西').click()
        time.sleep(1)
        web.find_element(By.LINK_TEXT, '长租1年').click()
        time.sleep(1)
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

        if len(house_info_list) == 0 or len(link_list) == 0:
            print("暂无对应房源")
            continue

        print("======= 搜索房子详情：", str(len(link_list)) + '个房源 =======')
        houseList = [x for y in zip(house_info_list, link_list) for x in y]
        hostListSet = set(houseList)
        for i in range(len(hostListSet)):
            print(houseList[i])
            print()
        print()
