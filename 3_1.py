from utils import *

lines = read_lines(day=3)
example = ("00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010")

get_rating = lambda a, b: '0b%s' % ''.join(b(x) for x in a)
most_common = lambda a:'1' if a >= len(lines) // 2 else '0'
least_common = lambda a: '1' if a < len(lines) // 2 else '0'

counter = None
for bits in lines:
  if counter is None:
    counter = (0,) * len(bits)
  counter = [i + int(char) for i, char in zip(counter, bits)]

gamma_rate = int(get_rating(counter, most_common), base=2) # Most common bits
epsilon_rate = int(get_rating(counter, least_common), base=2) # Least common bits
print(gamma_rate*epsilon_rate) # answer: 4118544