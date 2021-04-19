with open(r"08\data.txt", 'r') as file:
    data = [line.removesuffix("\n") for line in file]
    
accumulator = 0

currentLine = 0
        
callStack = []

def runLine(line):
    global accumulator
    global currentLine
    instruction = data[line].split(" ")
    if instruction[0] == "nop":
        currentLine += 1
    elif instruction[0] == "acc":
        accumulator += int(instruction[1])
        currentLine += 1
    elif instruction[0] == "jmp":
        currentLine += int(instruction[1])

def noDuplicatess(obj):
    if len(obj) == len(set(obj)):
        return True
    else:
        return False

while noDuplicatess(callStack):
    runLine(currentLine)
    callStack.append(currentLine)
    