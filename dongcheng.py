from util import *


def getDongChengInfo():
    url = 'https://www.ziroom.com/z/z1-d23008614-u9-r0/?p=b3-g2|1|3-a1|2|3|4&cp=100TO3500&isOpen=1'
    web.get(url)
    dc_house_info_list = list()
    dc_link_list = list()

    if isPageTurn(web, '.Z_pages .next'):
        while True:
            for inf in getHouseInfo():
                dc_house_info_list.append(inf)

            for li in getLink():
                dc_link_list.append(li)

            if isPageTurn(web, '.Z_pages .next'):
                web.find_element(By.XPATH, '//*[@id="page"]/a[last()]').click()
            else:
                break
    else:
        dc_house_info_list = getLink()
        dc_link_list = getHouseInfo()

    # 数据整合
    houseList = merge(dc_house_info_list, dc_link_list)
    print("======= 东城区房子详情：", str(len(dc_house_info_list)) + '个房源 =======')
    for i in houseList:
        print(i)
    print('\n')
