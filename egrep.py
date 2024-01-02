# egrep.py
import sys, re

# sys.argv is list of command-line arguments
# [0] is name of program itself
# [1] is regex specified at command-line
#print(f"egrep.py: sys.argv[0] is {sys.argv[0]}, sys.argv[1] is {sys.argv[1]}")
regex = sys.argv[1]

# for every line passed into the script
#print(f"egrep.py: sys.stdin is: {sys.stdin}")
for line in sys.stdin:
    # if it matches regex, write it to stdout
    if re.search(regex, line):
        sys.stdout.write(line)