with open(r"07\data.txt", 'r') as file:
    data = [line.removesuffix("\n") for line in file]


bags = {}
for line in data:
    color_of_main = line[0:line.find("bags")-1]
    subs = line.split("contain")[1].split(",")
    subs = [n[3:n.find("bag")-1] for n in subs]
    for n in range(len(subs)):
        if subs[n] == " other":
            subs[n] = None
    bags[color_of_main] = subs

colors_containing = set()
        
def checkContainment(color):
    for bag in bags:
        subs = bags[bag]
        if color in subs:
            colors_containing.add(bag)
            checkContainment(bag)

checkContainment("shiny gold")

print(len(colors_containing))