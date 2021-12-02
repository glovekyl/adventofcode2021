from utils import *

reports = read_lines(day=1)
example = [199,200,208,210,200,207,240,269,260,263]

count = 0
for a, b, c, d in zip(ints(reports), ints(reports)[1:], ints(reports)[2:], ints(reports)[3:]):
  if b + c + d > a + b + c:
    count += 1
print(count) # answer: 1486