def scrap(form_command, year, tile_command):
    temperature_list = []
    import requests
    from bs4 import BeautifulSoup
    import numpy as np
    url_head = "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?"
    url = url_head+form_command+str(year)+tile_command
    response = requests.get(url)

    # 將網頁資料轉換成 BeautifulSoup 物件，以便進行解析
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到表格中所有的列
    rows = soup.find_all("tr")

    # 迭代每一列，獲取溫度資料
    for row in rows:
        # 找到列中所有的欄位
        cols = row.find_all("td")
        
        # 如果欄位數量為 17，代表這是一列有效的資料
        if len(cols) == 35:
            # 取得溫度資料，欄位索引為 7
            temperature = cols[7].text.strip()
            temperature_list.append(float(temperature))

            # 將溫度資料印出來
            #print(temperature)

    return np.mean(temperature_list)

def scrap_highest(form_command, year, tile_command):
    import requests
    from bs4 import BeautifulSoup
    url_head = "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?"
    url = url_head+form_command+str(year)+tile_command
    response = requests.get(url)

    # 將網頁資料轉換成 BeautifulSoup 物件，以便進行解析
    soup = BeautifulSoup(response.content, "html.parser")

    # 找到表格中所有的列
    rows = soup.find_all("tr")

    # 迭代每一列，獲取溫度資料
    for row in rows:
        # 找到列中所有的欄位
        cols = row.find_all("td")
        
        # 如果欄位數量為 17，代表這是一列有效的資料
        if len(cols) == 35:
            if cols[0].text.strip() == '07':
                # 取得溫度資料，欄位索引為 7
                temperature = cols[7].text.strip()
                print(temperature)

            # 將溫度資料印出來
            #print(temperature)


tpe_form = "command=viewMain&station=466920&stname=%25E8%2587%25BA%25E5%258C%2597&datepicker="
tile_command = "&altitude=5.3m"
tyc_form = "command=viewMain&station=467490&stname=%25E8%2587%25BA%25E4%25B8%25AD&datepicker="
tyc_tile = "&altitude=84.04m"
tan_form = "command=viewMain&station=467420&stname=%25E6%25B0%25B8%25E5%25BA%25B7&datepicker="
tan_tile = "&altitude=8.1m"
all_temperature = []
for i in range(1998, 2023):
    #scrap_highest(tpe_form, i, tile_command)
    #year_temperature = scrap(tpe_form, i, tile_command)    #TPE
    #year_temperature = scrap(tyc_form, i, tyc_tile)     #TYC
    year_temperature = scrap(tan_form, i, tan_tile)    #tan
    all_temperature.append(year_temperature)

print(all_temperature)
for i in range(1998, 2023):
    print(f"{i}:{all_temperature[i-1998]}  degree C")
'''import requests
from bs4 import BeautifulSoup

# 指定要爬取的網頁 URL
url = "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?command=viewMain&station=466920&stname=%25E8%2587%25BA%25E5%258C%2597&datepicker=2001&altitude=5.3m"
# 使用 requests 模組發送 HTTP 請求，獲取網頁資料
response = requests.get(url)

# 將網頁資料轉換成 BeautifulSoup 物件，以便進行解析
soup = BeautifulSoup(response.content, "html.parser")

# 找到表格中所有的列
rows = soup.find_all("tr")

# 迭代每一列，獲取溫度資料
for row in rows:
    # 找到列中所有的欄位
    cols = row.find_all("td")
    
    # 如果欄位數量為 17，代表這是一列有效的資料
    if len(cols) == 35:
        # 取得溫度資料，欄位索引為 7
        temperature = cols[7].text.strip()

        # 將溫度資料印出來
        print(temperature)'''