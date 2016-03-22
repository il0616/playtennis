import math

def getEntropy(data):
    sum = 0
    for tuple in data.values():
        sum += tuple

    result = 0.0
    for tuple in data.values():
        result -= (tuple/sum) * math.log2(tuple/sum)

    return result




inputFile = open("agaricus-lepiota.data.txt", 'r')
namesFile = open("names.txt", 'w')
lines = inputFile.readlines()

n = len(lines[0].split(','))
cols = list()
for i in range(0, n):
    cols.append(dict())
for line in lines:
    data = line.rstrip('\n').split(',')
    for i, a in enumerate(data):
        if a in cols[i]:
            cols[i][a] += 1
        else:
            cols[i][a] = 1

print(getEntropy(cols[0]))
for i in cols:
    print(i)

# for i in range(0, n):
#     print(attr[i])
#     attr[i]
#
#     for d in attr[i]:
#         namesFile.write(d)
#         namesFile.write(',')
#
#     namesFile.write('\n')

