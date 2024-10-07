from pathlib import Path
import csv

path = Path('/Users/o.bogachenko/PycharmProjects/aqa4/Data_for_test/')

csv1_set = set()
csv2_set = set()

with open(path / 'random.csv', 'r') as f:
    csv1 = csv.reader(f)
    for row1 in csv1:
        clear_row1 = (i.rstrip(',') for i in row1)
        csv1_set.add(tuple(clear_row1))

with open(path / 'random-michaels.csv', 'r') as g:
    csv2 = csv.reader(g)
    for row2 in csv2:
        clear_row2 = (i.rstrip(',') for i in row1)
        csv2_set.add(tuple(clear_row2))

result = csv1_set | csv2_set

with open(path / 'result_Bogachenko.csv', 'w', newline='') as h:
    writer = csv.writer(h)
    writer.writerows(result)
