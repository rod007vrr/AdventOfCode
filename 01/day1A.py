
with open(r"01\data.txt", 'r') as file:
    data = [int(line) for line in file]
    
for n in data:
    for x in data:
        if n + x == 2020:
            print(n*x)