#! /usr/bin/python3.7

import openpyxl

wb = openpyxl.load_workbook('xlsx/produceSales.xlsx')
ws = wb.active

update_list ={'Celery': 1.19, 'Garlic': 3.07, 'Lemon': 1.27}

for row in ws.rows:
    produce_c, price_c = row[0:2]
    if produce_c.value in update_list:
        price_c.value = update_list[produce_c.value]

wb.save('produceSales_updated.xlsx')

