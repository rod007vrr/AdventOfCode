from test import REQUIRED_ENTRIES


with open(r"04\data.txt", 'r') as file:
    data = [line.removesuffix("\n") for line in file]
data.append("")

last = -1
spaces = []

for x in range(len(data)):
    if data[x] == "":
        spaces.append((last+1,x-1))
        last = x

people = []
       
for n in spaces:
    person = []
    for x in range(n[0], n[1]+1):
        for attribute in data[x].split(" "):
            person.append(attribute)
    people.append(person)

total = 0

for n in people:
    count = len(n)
    for x in n:
        if "cid" in x:
            count -=1
    if count >6:
        total += 1
        
print(total)
