with open(r"09\data.txt", 'r') as file:
    data = [int(line.removesuffix("\n")) for line in file]

size = 25

def verify(dataset ,start, number):
    for n in range(size):
        for x in range(size):
            if dataset[start:start+size][n] + dataset[start:start+size][x] == number and n != x:
                return True
            
    return False
    
for n in range(size,len(data)):
    if not verify(data, n-size, data[n]):
        print(data[n])