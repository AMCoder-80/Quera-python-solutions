import csv

# 0-esm 1-famil 2-keshvar 3-rang 4-ashia 5-ghaza
fields = ['esm', 'famil', 'keshvar', 'rang', 'ashia', 'ghaza']
output = dict()

with open('esm_famil_data.csv', 'r') as f:
    content = csv.reader(f)
    next(content)
    content = list(content)
    for i in fields:
        output[i] = [content[n][fields.index(i)] for n in range(len(content)) \
            if content[n][fields.index(i)]!= '']

print(output)