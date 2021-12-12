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

def main(data):
  data = set(data)
  # data -= syntax_errors(data)
  
  scores = []
  for line in data:
    stack = []

    # Syntax Errors
    try:
      for char in line:
        if char in OPENERS:
          stack.append(char)
        if char == LOOKUP[stack.pop()]:
          continue # valid
        raise SyntaxError()
    except SyntaxError:
      continue

    # Incomplete Lines
    total = 0
    while stack:
      total = score(total, stack.pop())
    scores.append(total)
  
  scores.sort()
  print(scores[len(scores) // 2])
  
if __name__ == "__main__":
  main(lines) # answer: 1685293086