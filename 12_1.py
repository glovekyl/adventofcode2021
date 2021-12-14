from utils import *

lines = read_lines(day=12)

example_small = ( # 10 paths
  "start-A",
  "start-b",
  "A-c",
  "A-b",
  "b-d",
  "A-end",
  "b-end"
)

example_med = ( # 19 paths
  "dc-end",
  "HN-start",
  "start-kj",
  "dc-start",
  "dc-HN",
  "LN-dc",
  "HN-end",
  "kj-sa",
  "kj-HN",
  "kj-dc",
)

example_large = ( # 226 paths
  "fs-end",
  "he-DX",
  "fs-he",
  "start-DX",
  "pj-DX",
  "end-zg",
  "zg-sl",
  "zg-pj",
  "pj-he",
  "RW-he",
  "fs-DX",
  "pj-RW",
  "zg-RW",
  "start-pj",
  "he-WI",
  "zg-he",
  "pj-fs",
  "start-RW"
)

class NodeObject(object):
  pass

class Node(NodeObject):
  def __init__(self, key: str):
    super().__init__()
    self._key = key
    self._edges: list[NodeObject] = []
    self._visited_count = 0
  
  def __repr__(self) -> str:
    return self.key
  
  def __str__(self) -> str:
    return "{}: {}".format(self.key, [e.key for e in self._edges])
  
  def add_edge(self, node: object) -> list[NodeObject]:
    self._edges.append(node)
    return self.edges
  
  @property
  def key(self) -> str:
    return self._key

  @property
  def edges(self) -> list[NodeObject]:
    return self._edges
  
  @property
  def count(self) -> int:
    return self._visited_count
  
  @count.setter
  def count(self, i) -> int:
    self._visited_count = i
    return self._visited_count

def dfs(known: list[str], node: Node, visited: set[Node]=set(), path: list=list()):
  if node.key == 'end':
    known.append(','.join(path + ['end',]))
    return

  if node not in visited:
    path.append(node.key)
    if node.key.islower():
      visited.add(node)
    for edge in node.edges:
      dfs(known, edge, visited.copy(), path.copy())

def main(data):
  data = tuple(line.split('-') for line in data)
  
  cave: dict[str: Node] = dict()
  for a, b in data:
    if a not in cave: cave[a] = Node(a)
    if b not in cave: cave[b] = Node(b)
    a: Node = cave[a]
    b: Node = cave[b]
    a.add_edge(b)
    b.add_edge(a)
  
  dfs(paths := [], cave['start'])
  print(len(paths))
  
if __name__ == "__main__":
  main(lines) # answer: 3410