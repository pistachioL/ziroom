from util import *


def getHaiDianInfo():
    url = 'https://www.ziroom.com/z/z1-d23008618-u9-r0/?p=b3-g2|1|3-a1|2|3|4&cp=100TO3500&isOpen=1'
    web.get(url)

    hd_house_info_list = list()
    hd_link_list = list()
    if isPageTurn(web, '.Z_pages .next'):
        for page in range(0, 2):
            for inf in getHouseInfo():
                hd_house_info_list.append(inf)

            for li in getLink():
                hd_link_list.append(li)

            web.find_element(By.XPATH, '//*[@id="page"]/a[last()]').click()
    else:
        hd_house_info_list = getHouseInfo()
        hd_link_list = getLink()

    houseList = merge(hd_house_info_list, hd_link_list)

    print("==================================海淀区房子详情：", str(len(hd_house_info_list)) + '个房源==================================')
    for i in houseList:
        print(i)