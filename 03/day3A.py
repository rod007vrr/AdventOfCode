with open(r"03\data.txt", 'r') as file:
    data = [line for line in file]

count = 0
x = 0
size = len(data[0])
for n in data:
    if n[x] == "#":
        count += 1
    if x  > len(n):
        x = x+3 - len(n)
    else:
        x = x+3

print(count)