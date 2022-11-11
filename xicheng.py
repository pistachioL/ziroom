from util import *


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
    print("======= 西城区房子详情：", str(len(xc_house_info_list)) + '个房源 =======')
    for i in ans:
        print(i)
