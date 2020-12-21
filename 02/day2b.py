
with open(r"02\data.txt", 'r') as file:
    data = [line for line in file]

def checkValidity(sample):

    locations = [int(n)-1 for n in sample.split(" ")[0].split("-")]
    letter = sample.split(" ")[1][0]
    password = sample.split(" ")[2]

    if (letter == password[locations[0]]) ^ (letter == password[locations[1]]):
        return True
    else:
        return False
        
count = 0

for n in data:
    if checkValidity(n):
        count += 1

print(count)

