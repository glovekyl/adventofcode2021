from utils import *

txt = read_string(day=6)

example = ("3,4,3,1,2")

def simulate(data: list[int]) -> list[int]:
  for i in range(len(data)):
    data[i] -= 1
    if data[i] < 0:
      data[i] = 6
      data.append(8)

def main(data, days=80):
  lanternfish = list(ints(data))
  for _ in range(days):
    simulate(lanternfish)
  print(len(lanternfish))

if __name__ == "__main__":
  main(txt, days=80) # answer: 358214