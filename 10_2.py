from utils import *

lines = read_lines(day=10)

example = (
  "[({(<(())[]>[[{[]{<()<>>",
  "[(()[<>])]({[<{<<[]>>(",
  "{([(<{}[<>[]}>{[]{[(<()>",
  "(((({<>}<{<{<>}{[]{[]{}",
  "[[<[([]))<([[{}[[()]]]",
  "[{[{({}]{}}([{[{{{}}([]",
  "{<[[]]>}<{[{[{[]{()[[[]",
  "[<(<(<(<{}))><([]([]()",
  "<{([([[(<>()){}]>(<<{{",
  "<{([{{}}[<[[[<>{}]]]>[]]"
)

points = {
  "(": 1,
  "[": 2,
  "{": 3,
  "<": 4
}
score = lambda total, val: (total * 5) + points[val]

LOOKUP = {
  "[": "]",
  "(": ")",
  "{": "}",
  "<": ">"
}
OPENERS = set(("(", "[", "{", "<"))
CLOSERS = set((")", "]", "}", ">"))


def syntax_errors(data) -> set:
  corrupted = set()
  for line in data:
    stack = []
    for char in line:
      if char in OPENERS:
        stack.append(char)
        continue
      if len(char) == 0: # invalid
        corrupted.add(line)
        break
      if char in CLOSERS:
        head = stack.pop()
        if char == LOOKUP[head]: continue # valid
        corrupted.add(line)
        break
  return corrupted


def main(data):
  data = set(data)
  data -= syntax_errors(data)
  
  scores = []
  for line in data:
    stack = []
    for char in line:
      if char in OPENERS:
        stack.append(char)
      elif char in CLOSERS:
        stack.pop()
    
    total = 0
    while stack:
      total = score(total, stack.pop())
    scores.append(total)
  
  scores.sort()
  print(scores[len(scores) // 2])
  

if __name__ == "__main__":
  main(lines) # answer: 1685293086