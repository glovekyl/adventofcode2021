import numpy as np

from utils import *

lines = read_lines(day=13)
txt = read_string(day=13)

example = """
  6,10
  0,14
  9,10
  0,3
  10,4
  4,11
  6,0
  6,12
  4,1
  0,13
  10,12
  3,4
  3,0
  8,4
  1,10
  2,14
  8,10
  9,0

  fold along y=7
  fold along x=5
"""

RE_DOTS = re.compile(r'(\d+)\,(\d+)')
RE_FOLDS = re.compile(r'\w\=\d+')

def foldfn(dots: set[tuple], fold: tuple[str, int]):
  fx, fy = fold
  if fx:
    keep = {d for d in dots if d[0] < fx}
    fold = (d for d in dots if d[0] > fx)
    keep.update((2 * fx - x, y) for x, y in fold)
    return keep
  else:
    keep = {d for d in dots if d[1] < fy}
    fold = (d for d in dots if d[1] > fy)
    keep.update((x, 2 * fy - y) for x, y in fold)
    return keep


def main(data: str):
  dots = iter(zip(*RE_DOTS.findall(data)))
  dots = tuple(zip(map(int, next(dots)), map(int, next(dots))))
  
  axis = lambda ax, n: (n,0) if ax == 'x' else (0,n)
  folds = tuple(axis(ax, int(n)) for ax,n in map(lambda x: x.split('='), RE_FOLDS.findall(data)))

  dots = foldfn(set(dots), folds[0])
  # for fold in folds[1:]:
  #   dots = foldfn(dots, fold)
  print(len(dots))

  
if __name__ == "__main__":
  main(txt) # answer: 693