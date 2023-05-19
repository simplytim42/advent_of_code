def is_valid(passport):
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    keys = [key.split(':')[0] for key in passport]

    for req in required_fields:
        if req not in keys:
            return False
    return True

data = open('input.txt').read().strip().split('\n\n')
data = [passport.split() for passport in data]

count = 0
for passport in data:
    if is_valid(passport):
        count += 1
print(count)