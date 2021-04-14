
with open(r"05\data.txt", 'r') as file:
    data = [line.removesuffix("\n") for line in file]

IDs = []

for bPass in data:
    rowRange = [1,128]
    size = 128
    for char in bPass[:7]:
        if char == "F":
            rowRange[1] -= size/2
            size/=2
        elif char =="B":
            rowRange[0] += size/2
            size/=2
    row = int(rowRange[0]-1)
    colRange = [1,8]
    size = 8
    for char in bPass[7:]:
        if char == "L":
            colRange[1] -= size/2
            size/=2
        elif char =="R":
            colRange[0] += size/2
            size/=2
    col = int(colRange[0]-1)
    IDs.append((8*row) + col) 
    
print(max(IDs))

allID = []

for n in range(1, 127):
    for x in range(8):
        allID.append(8*n+x)
missing = []

for n in allID:
    if n not in IDs:
        missing.append(n)

print(missing)
