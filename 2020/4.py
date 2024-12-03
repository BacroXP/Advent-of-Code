import re


def is_valid_height(hgt):
    if hgt.endswith("cm"):
        height_cm = int(hgt[:-2])
        return 150 <= height_cm <= 193
    elif hgt.endswith("in"):
        height_in = int(hgt[:-2])
        return 59 <= height_in <= 76
    return False


def is_valid_hair_color(hcl):
    return re.match(r"^#[0-9a-f]{6}$", hcl) is not None


def is_valid_eye_color(ecl):
    return ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


def is_valid_passport_id(pid):
    return re.match(r"^\d{9}$", pid) is not None


def is_valid_passport(passport, required_fields):
    for data_string in passport.split():
        data_type, data = data_string.split(":")

        if data_type == "byr" and not (1920 <= int(data) <= 2002):
            return False
        elif data_type == "iyr" and not (2010 <= int(data) <= 2020):
            return False
        elif data_type == "eyr" and not (2020 <= int(data) <= 2030):
            return False
        elif data_type == "hgt" and not is_valid_height(data):
            return False
        elif data_type == "hcl" and not is_valid_hair_color(data):
            return False
        elif data_type == "ecl" and not is_valid_eye_color(data):
            return False
        elif data_type == "pid" and not is_valid_passport_id(data):
            return False

    return set(required_fields).issubset(set(data.split(":")[0] for data in passport.split()))


passwords = open("input.txt").read().strip().split("\n\n")
required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

valid_passports_part_1 = 0
valid_passports_part_2 = 0

for passport in passwords:
    passport = passport.replace("\n", " ")

    data_types = set(data.split(":")[0] for data in passport.split())
    if required_fields.issubset(data_types):
        valid_passports_part_1 += 1

    if is_valid_passport(passport, required_fields):
        valid_passports_part_2 += 1

print(valid_passports_part_1)
print(valid_passports_part_2)
