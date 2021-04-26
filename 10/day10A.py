with open(r"10\data.txt", 'r') as file:
    data = [int(line.removesuffix("\n")) for line in file]