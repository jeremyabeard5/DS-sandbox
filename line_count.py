# line_count.py
import sys

count = 0
#print(f"line_count.py: sys.stdin is {sys.stdin}")
for line in sys.stdin:
    print(f"line_count.py: line in sys.stdin is {line}")
    count += 1
    
# print goes to sys.stdout
print(count)