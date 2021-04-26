with open(r"09\data.txt", 'r') as file:
    data = [int(line.removesuffix("\n")) for line in file]

number = 105950735

tempSum = []

def sumElem(arr):
    s = 0
    for n in arr:
        s+=n
    return s

for n in range(len(data)):
    for x in range(n, len(data)):
        tempSum.append(data[x])
        if sumElem(tempSum) >= number:
            
            break
    if sumElem(tempSum) == number:
        print(min(tempSum) + max(tempSum))
        break
    else:
        tempSum = [] 