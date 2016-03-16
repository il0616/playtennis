def getEntropy():


inputFile = open("agaricus-lepiota.data.txt", 'r')
namesFile = open("names.txt", 'w')
lines = inputFile.readlines()

n = len(lines[0].split(','))
attr = list()
cols = list()
for i in range(0, n):
    attr.append(set())
    cols.append(dict())
for line in lines:
    data = line.rstrip('\n').split(',')
    for i, a in enumerate(data):
        attr[i].add(a)
        if a in cols[i]:
            cols[i][a] += 1
        else:
            cols[i][a] = 1

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

