with open(r"03\data.txt", 'r') as file:
    data = [line for line in file]

count = 0
x = 0
size = len(data[0])-1
for n in data:
    if n[x] == "#":
        count += 1
    x = (x+3) % size
    
    

print(count)