import re

zx = "12"

ptr = "\d{2}"

qw = re.match(ptr, zx)

print(qw)

if re.match(ptr, zx):
    print("hey")