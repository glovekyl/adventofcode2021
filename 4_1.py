from utils import *
from functools import reduce
import math

txt = read_string(day=4)

example = (
# Draw
(7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1),
# Board 1
(22,13,17,11,0,
 8,2,23,4,24,
 21,9,14,16,7,
 6,10,3,18,5,
 1,12,20,15,19),
# Board 2
(3,15,0,2,22,
 9,18,13,17,5,
 19,8,7,25,23,
 20,11,10,24,4,
 14,21,16,12,6),
# Board 3
(14,21,17,24,4,
 10,16,15,9,19,
 18,8,23,26,20,
 22,11,13,6,5,
 2,0,12,3,7)
)

class Grid():
  _size: int
  _numbers: dict[str, tuple]
  _columns: dict[str, int]
  _rows: dict[str, int]
  
  def __init__(self, data: list[int]) -> None:
    self._size = int(math.sqrt(len(data)))
    self._columns = {x: 0 for x in range(self._size)}
    self._rows = {x: 0 for x in range(self._size)}
    self._numbers = {}

    x, y = 0, 0
    for i, n in enumerate(data):
      self._numbers[int(n)] = (x, y)
      if x == self._size - 1:
        x = 0
        y += 1
      else:
        x += 1
  
  def mark(self, n: int):
    x, y = self._numbers[n]
    self._columns[x] += 1
    self._rows[y] += 1
    return self._columns[x] == self._size or self._rows[y] == self._size

class Board():
  _grid: Grid
  _numbers: set[int]
  _marked: set[int]

  def __init__(self, data: list[int]) -> None:
    self._grid = Grid(data)
    self._numbers = set(data)
    self._marked = set({})
    pass

  @property
  def grid(self) -> Grid:
    return self._grid

  @property
  def unmarked(self) -> set[int]:
    return self._numbers - self._marked

  @property
  def marked(self) -> set[int]:
    return self._marked
  
  def mark(self, n: int) -> bool: # Returns true if win!
    if(n in self._numbers):
      self._marked.add(n)
      return self._grid.mark(n)

def main(data=None):
  if type(data) is str:
    # Raw input
    parts = txt.split("\n\n")
    draw = map(int, parts[0].split(','))
    boards = [reduce(lambda x,y: x+y, [tuple(map(int, line.split())) for line in part.splitlines()]) for part in parts[1:]]
  elif type(data) is tuple:
    draw = data[0]
    boards = data[1:]
  
  boards = tuple(map(Board, boards))
  for n in draw:
    for b in boards:
      if(b.mark(n)):
        print(sum(b.unmarked) * n) 
        return

if __name__ == "__main__":
  main(txt) # answer: 44088