#! /usr/bin/python3.6
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def print_table(list):
    width = [0] * len(list)  # will contain the largest length of each sub-list

    for i in range(len(list)):
        for j in range(len(list[i])):
            if width[i] < len(list[i][j]):
                width[i] = len(list[i][j])

    for length in range(len(list[0])):
        for i in range(len(list)):
            value = list[i][length]
            print(value.rjust(width[i]), end=' ')
        print('\n')






print_table(tableData)


