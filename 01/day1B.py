with open(r"01\data.txt", 'r') as file:
    data = [int(line) for line in file]



def check():
    count = 0
    prod = 0
    dataS = {"count" : count, 
            "product": prod}
    for n in data:
        for x in data:
            for i in data:
                count +=1
                if n+x+i == 2020:
                    prod = n*x*i
                    return dataS
                
print(check())