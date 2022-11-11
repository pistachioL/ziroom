from util import *


def getChaoYangInfo():
    # url = 'https://www.ziroom.com/z/z1-d23008613-u9-r0/?p=b3-g2|1|3-a1|2|3|4&cp=100TO3500&isOpen=1'
    url = 'https://www.ziroom.com/z/z1-d23008613-b611100323%7C18335647%7C18335622%7C611100448%7C18335644%7C611100324%7C18335641%7C18335734%7C18335779%7C18335736%7C18335666%7C1100006187%7C611100316%7C611100698%7C18335707%7C18335709%7C18335706%7C18335711%7C18335740%7C611100321%7C18335704-u9-r0/?p=b3-g2|1|3-a1|2|3|4&cp=100TO3500&isOpen=1'
    web.get(url)

    cy_house_info_list = list()
    cy_link_list = list()
    if isPageTurn(web, '.Z_pages .next'):
        while True:
            for inf in getHouseInfo():
                cy_house_info_list.append(inf)

            for li in getLink():
                cy_link_list.append(li)

            if isPageTurn(web, '.Z_pages .next'):
                web.find_element(By.XPATH, '//*[@id="page"]/a[last()]').click()
            else:
                break
    else:
        cy_house_info_list = getHouseInfo()
        cy_link_list = getLink()

    houseList = merge(cy_house_info_list, cy_link_list)

    print("======= 朝阳区区房子详情：", str(len(cy_house_info_list)) + '个房源 =======')
    for i in houseList:
        print(i)
    print('\n')
