with open(r"03\data.txt", 'r') as file:
    data = [line for line in file]


size = len(data[0])-1
travels = [(1,1),(3,1),(5,1),(7,1),(1,2)]

def checkRoute(path):
    x = 0
    y = 0
    count = 0
    while y<len(data):
        if data[y][x] == "#":
            count+=1
        y += path[1]
        x = (x + path[0])%size
    return count

prod = 1

for route in travels:
    prod*=checkRoute(route)
    
print(prod)