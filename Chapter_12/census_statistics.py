#! /usr/bin/python3.7


import openpyxl
import pprint

wb = openpyxl.load_workbook('xlsx/censuspopdata.xlsx')
ws = wb.active

dict_total_pop={}

for row in ws.rows:
    census_tract, state, country, pop = row

    census_tract = census_tract.value
    state = state.value
    country = country.value
    pop = pop.value

    if state not in dict_total_pop:
        dict_total_pop[state] = {country: {'pop': pop, 'ct_counter': 1}}
    elif country not in dict_total_pop[state]:
        dict_total_pop[state][country] = {'pop': pop, 'ct_counter': 1}
    else:
        dict_total_pop[state][country]['pop'] += pop
        dict_total_pop[state][country]['ct_counter'] += 1

with open('census_statistics.txt', 'w') as file:
    file.write(pprint.pformat(dict_total_pop))