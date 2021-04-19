with open(r"08\data.txt", 'r') as file:
    data = [line.removesuffix("\n") for line in file]
    for n in range(len(data)):
        data[n] = [data[n].split(" ")[0], int(data[n].split(" ")[1])]


def testIteration():
    
    accumulator = 0
    currentLine = 0
    callStack = []
   
    while True:
            
        try:
            instruction = data[currentLine]
        except IndexError:
            return accumulator        
        if instruction[0] == "nop":
            currentLine += 1
        elif instruction[0] == "acc":
            accumulator += instruction[1]
            currentLine += 1
        elif instruction[0] == "jmp":
            currentLine += instruction[1]
        
        callStack.append(currentLine)
        
        if not len(callStack) == len(set(callStack)):
            return "Failed" 

for n in range(len(data)):
    if data[n][0] == "jmp":
        data[n][0] = "nop"
        print(f"{n}: {testIteration()}")
        data[n][0] = "jmp"
    elif data[n][0] == "nop":
        data[n][0] = "jmp"
        print(f"{n}: {testIteration()}")
        data[n][0] = "nop"
