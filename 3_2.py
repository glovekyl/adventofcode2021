from utils import *

lines = read_lines(day=3)
example = ("00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010")

## - UTILITY LAMBDAs -
lambda_one = lambda a, b: a[b] == '1'
lambda_zero = lambda a: a == '0'
getFirstSetElement = lambda x: next(iter(x))

## - CRITERIA -
most_common = lambda a, b: a if len(a) >= len(b) else b
least_common = lambda a, b: a if len(a) < len(b) else b

def get_rating(data: set[str], func=most_common):
  binsize = len(getFirstSetElement(data))
  for i in range(binsize):
    if len(data) == 1:
      break
    ones = set(filter(lambda x: x[i] == '1', data))
    zeros = data-ones
    data = func(ones, zeros)
  return '0b%s' % getFirstSetElement(data)


def main(data=None):
  oxygen_genr = int(get_rating(set(data), most_common), 2)
  co2_scrubber = int(get_rating(set(data), least_common), 2)
  print(oxygen_genr*co2_scrubber) # answer: 3832770

if __name__ == "__main__":
  main(lines)