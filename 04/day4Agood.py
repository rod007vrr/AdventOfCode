with open(r"04\data.txt", 'r') as file:
    data = [line.removesuffix("\n") for line in file]
data.append("")

passports, passport = [], {}

REQUIRED_ENTRIES = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

for line in data:
    if line == "":
        passports.append(passport)
        passport = {}

    else:
        fields = line.split()

        for field in fields:
            field = field.split(":")
            passport[field[0]] = field[1]
        
count = 0
            
for passport in passports:
    if all(val in passport for val in REQUIRED_ENTRIES):
         count += 1
print(count)
