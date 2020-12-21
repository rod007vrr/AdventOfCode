
with open(r"02\data.txt", 'r') as file:
    data = [line for line in file]

def checkValidity(sample):


    span = [int(n) for n in sample.split(" ")[0].split("-")]
    letter = sample.split(" ")[1][0]
    password = sample.split(" ")[2]

    letterCount = 0
    for n in password:
        if n == letter:
            letterCount+=1

    if letterCount >= span[0] and letterCount <= span[1]:
        return True
    else:
        return False
        
count = 0

for n in data:
    if checkValidity(n):
        count += 1

print(count)

