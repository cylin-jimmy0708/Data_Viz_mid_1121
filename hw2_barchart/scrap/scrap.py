import os

os.chdir("C://Users//user//Desktop//林啓揚//大四//資料視覺化//hw2_barchart//scrap")
import write as wr


def scrap_rainfall(form_command, year, tile_command):
    import requests
    from bs4 import BeautifulSoup
    url_head = "https://e-service.cwb.gov.tw/HistoryDataQuery/YearDataController.do?"
    url = url_head+form_command+str(year)+tile_command
    response = requests.get(url)
    year_rainfall = []

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
            precption = cols[18].text.strip()
            print(precption)
            year_rainfall.append(precption)
            # 將溫度資料印出來
            #print(temperature)
    return year_rainfall


def average_monthly_rainfall(form_command, tile_command):
    import numpy as np
    all_precption = [[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(1998, 2023):
        one_year_rainfall = scrap_rainfall(form_command, i, tile_command)
        for j in range(12):
            try:
                all_precption[j].append(float(one_year_rainfall[j]))
            except:
                continue
    
    average = []
    for month in range(1, 13):
        average.append(np.mean(all_precption[month-1]))
    return average


tpe_form = "command=viewMain&station=466920&stname=%25E8%2587%25BA%25E5%258C%2597&datepicker="
tile_command = "&altitude=5.3m"
tyc_form = "command=viewMain&station=467490&stname=%25E8%2587%25BA%25E4%25B8%25AD&datepicker="
tyc_tile = "&altitude=84.04m"
tan_form = "command=viewMain&station=467420&stname=%25E6%25B0%25B8%25E5%25BA%25B7&datepicker="
tan_tile = "&altitude=8.1m"


tpe_year_rainfall = average_monthly_rainfall(tpe_form, tile_command)
tyc_year_rainfall = average_monthly_rainfall(tyc_form, tyc_tile)
tan_year_rainfall = average_monthly_rainfall(tan_form, tan_tile)    #tan
print(tpe_year_rainfall, tyc_year_rainfall, tan_year_rainfall)

month = ["Site", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
#title = ["month", "TPE", "TYC", "TAN"]

'''w_data = []
for i in range(12):
    w_data.append([month[i], tpe_year_rainfall[i], tyc_year_rainfall[i], tan_year_rainfall[i]])
'''
w_data = [["TPE"]+tpe_year_rainfall, ["TXG"]+tyc_year_rainfall, ["TNN"]+tan_year_rainfall]

os.chdir("C://Users//user//Desktop//林啓揚//大四//資料視覺化//hw2_barchart")
wr.write("Avg_monthly_rainfall_(trans).csv", month, w_data)
