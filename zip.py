x = [1, 2, 3]
y = [4, 5, 6]
print(list(zip(x, y)))
x2, y2 = zip(*zip(x, y))
if(x == list(x2) and y == list(y2)):
    print(x2)
    print(y2)
    