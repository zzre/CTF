with open("check_flag.vokram", 'r') as f:
    data = f.read()

from collections import Counter

counter = Counter(data)
print(counter)