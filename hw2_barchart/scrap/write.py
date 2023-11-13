import csv

def write(filename, xlabel, data):
    with open(filename, 'w', newline='') as wf:
        wri = csv.writer(wf)
        wri.writerow(xlabel)        
        #wri.writerow(['2020_revenue', '2020_net_income', '2020_Capital Expenditure', '2021_revenue', '2021_net_income', '2021_Capital Expenditure'])
        for i in range(len(data)):
            wri.writerow(data[i])
    