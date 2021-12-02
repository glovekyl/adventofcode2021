from utils import *

reports = read_lines(day=1)
example = [199,200,208,210,200,207,240,269,260,263]

count = 0
for a, b in zip(ints(reports), ints(reports)[1:]):
  if b > a:
    count += 1
print(count) # answer: 1446