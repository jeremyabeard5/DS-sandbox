# egrep.py
import sys, re

# sys.argv is list of command-line arguments
# [0] is name of program itself
# [1] is regex specified at command-line
regex = sys.argv[1]

# for every line passed into the script
for line in sys.stdin:
    # if it matches regex, write it to stdout
    if re.search(regex, line):
        sys.stdout.write(line)
        