from utils import *

lines = read_lines(day=3)
example = ("00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010")

most_common = lambda a:'1' if a >= len(lines) // 2 else '0'
least_common = lambda a: '1' if a < len(lines) // 2 else '0'

counter = None
for bits in lines:
  if counter is None:
    counter = (0,) * len(bits)
  counter = [i + int(char) for i, char in zip(counter, bits)]

gamma = "".join(most_common(c) for c in counter) # Most common bits
epsilon = "".join(least_common(c) for c in counter) # Least common bits

gamma = int(gamma, base=2)
epsilon = int(epsilon, base=2)

print(gamma*epsilon) # answer: 4118544