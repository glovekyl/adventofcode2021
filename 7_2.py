from collections import Counter
from utils import *

txt = read_string(day=7)

example = ("16,1,2,0,4,2,7,1,2,14")

def main(data):
  data = ints(data)
  positions = set(data)
  
  T = lambda n: (n * (n + 1)) // 2 # info: Triangle Numbers
  fn = lambda x: sum([T(abs(x - p)) for p in data])

  minimum = float('inf')
  for i in range(min(positions), max(positions)):
    minimum = min(minimum, fn(i))
  print(minimum)
  
if __name__ == "__main__":
  main(txt) # answer: 95167302