from utils import *

txt = read_string(day=7)

example = ("16,1,2,0,4,2,7,1,2,14")

def main(data):
  data = ints(data)
  positions = set(data)

  fn = lambda x: sum((abs(x - p) for p in data))
  
  minimum = float('inf')
  for i in range(min(positions), max(positions)):
    minimum = min(minimum, fn(i))
  print(minimum)
  
if __name__ == "__main__":
  main(txt) # answer: 336701