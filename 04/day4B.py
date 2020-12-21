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
    try:
        byr = 1920 <= int(passport["byr"]) <= 2002
        iyr = 2010 <= int(passport["iyr"]) <= 2020
        eyr = 2020 <= int(passport["eyr"]) <= 2030
        hgt = ((passport["hgt"].endswith("cm") and (150 <= int(passport["hgt"].removesuffix("cm")) <= 193)) or (passport["hgt"].endswith("in") and (59 <= int(passport["hgt"].removesuffix("in")) <= 76)))
        hcl = passport["hcl"].startswith("#") and len(passport["hcl"]) == 7 and int(passport["hcl"][1:], 16) % 1 == 0
        ecl = passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        pid = len(passport["pid"]) == 9 and int(passport["pid"])%1 == 0
        if all([byr, iyr, eyr, hgt, hcl, ecl, pid]):
            count += 1
    except KeyError:
        pass
            
print(count)