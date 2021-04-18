with open(r"07\data.txt", 'r') as file:
    data = [line.removesuffix("\n") for line in file]
    
bags = {}
for line in data:
    color_of_main = line[0:line.find("bags")-1]
    subs = line.split("contain")[1].split(",")
    #subs = [n[3:n.find("bag")-1] for n in subs]
    subs = [  (n[3:n.find("bag")-1], n[1])    for n in subs]
    for n in range(len(subs)):
        if subs[n][0] == " other":
            subs[n] = None
    bags[color_of_main] = subs

total = 0

def checkContain(color):
    for bag in bags[color]:
        global total
        
        if bag != None:
            total += int(bag[1])
            for n in range(int(bag[1])):
                checkContain(bag[0])
        
checkContain("shiny gold")

print(total)

