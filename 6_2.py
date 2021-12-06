from collections import Counter

from utils import *

txt = read_string(day=6)

example = ("3,4,3,1,2")

def main(data, days=80):
  # { # key=cycle N
  #   0: # of fish,
  #   1: # of fish,
  #   ...
  #   8: # of fish
  # }
  cycles = Counter(ints(data))
  del data

  for _ in range(days):
    zeros = cycles[0]
    for k in range(1, 10):
      cycles[k-1] = cycles[k]
    
    cycles[6] += zeros
    cycles[8] += zeros
  print(sum(cycles.values()))
  
if __name__ == "__main__":
  main(txt, days=256) # answer: 1622533344325