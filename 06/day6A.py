with open(r"06\data.txt", 'r') as file:
    data = [line.removesuffix("\n") for line in file]
data.append("")

    
personDict = {
    "a" : False,
    "b" : False,
    "c" : False,
    "d" : False,
    "e" : False,
    "f" : False,
    "g" : False,
    "h" : False,
    "i" : False,
    "j" : False,
    "k" : False,
    "l" : False,
    "m" : False,
    "n" : False,
    "o" : False,
    "p" : False,
    "q" : False,
    "r" : False,
    "s" : False,
    "t" : False,
    "u" : False,
    "v" : False,
    "w" : False,
    "x" : False,
    "y" : False,
    "z" : False
}



totalSum = 0
currentGroupDicts = []
groupDict = dict.fromkeys(personDict,0)
for line in data:
    if line == "": #new group completely
        for question in range(26):
            for indiv in currentGroupDicts:
            
                if list(indiv.values())[question] == True:
                    groupDict[list(indiv.keys())[question]] = True
                else:
                    groupDict[list(indiv.keys())[question]] = False
                    break
        groupSum = sum(groupDict.values()) #sum all true
        totalSum += groupSum #sum group sum with total sum
        groupSum = 0 # reset group sum
        personDict = dict.fromkeys(personDict,0) #reset person dict
        currentGroupDicts = []#reset current dict
        groupDict = dict.fromkeys(personDict,0) #reset group dict
    else:
        currentPerson = dict.fromkeys(personDict,0)
        try:
            for char in line:
                currentPerson[char] = True
        except KeyError:
            pass
        currentGroupDicts.append(currentPerson)
        
print(totalSum)


#duplicate and check overlapping