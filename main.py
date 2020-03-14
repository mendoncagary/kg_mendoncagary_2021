import sys

map = {}

x = list(sys.argv)[1]
y = list(sys.argv)[2]


for i in range(len(x)):
    if x[i] in map:
        if map[x[i]] != y[i]:
            print(False)
            sys.exit()
    map[x[i]] = y[i]

print(True)