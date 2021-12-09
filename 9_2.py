from utils import *

lines = read_lines(day=9)

example = (
  "2199943210",
  "3987894921",
  "9856789892",
  "8767896789",
  "9899965678"
)

def dirs(x, y, w, h):
  if x - 1 >= 0:
    yield x - 1, y
  if x + 1 < w:
    yield x + 1, y
  if y - 1 >= 0:
    yield x, y - 1
  if y + 1 < h:
    yield x, y + 1

def get_lows(grid):
  lows = set()
  h, w = len(grid), len(grid[0])
  for x in range(w):
    for y in range(h):
      z = grid[y][x]

      lowest = True
      for a, b in dirs(x, y, w, h):
        if grid[b][a] <= z:
          lowest = False
          break
      if lowest:
        lows.add((x, y))
  return lows

def dfs(grid: tuple, visited: set, x, y):
  stack = [(x, y,)]
  h, w = len(grid), len(grid[0])
  while len(stack):
    x, y = stack.pop()
    if (x, y) in visited:
      continue

    visited.add((x, y))
    for dx, dy in dirs(x, y, w, h):
      if (val := grid[dy][dx]) > grid[y][x] and val != 9:
        stack.append((dx, dy))

def main(data):
  grid = [tuple(map(int, x)) for x in data]
  lows = get_lows(grid)

  basins = []
  for x, y in lows:
    dfs(grid, (visited := set()), x, y)
    basins.append(len(visited))
  basins.sort()
  print(basins[-3] * basins[-2] * basins[-1])

if __name__ == "__main__":
  main(lines) # answer: 899392