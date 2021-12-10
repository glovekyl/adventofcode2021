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

score = {
  ")": 3,
  "]": 57,
  "}": 1197,
  ">": 25137
}

lookup = {
  "(": set((")", "(", "[", "{", "<")),
  "[": set(("]", "(", "[", "{", "<")),
  "{": set(("}", "(", "[", "{", "<")),
  "<": set((">", "(", "[", "{", "<"))
}

openers = set(("(", "[", "{", "<"))
closers = set((")", "]", "}", ">"))

def main(data):
  total = 0
  for _, line in enumerate(data):
    stack = []
    for i, char in enumerate(line):
      if char in openers:
        stack.append(char)
        continue

      if len(char) == 0:
        # invalid
        total += score[char]
        break

      peek = stack[-1]
      if char in closers:
        head = stack.pop()
        if char in lookup[head]: continue # valid
        total += score[char]
        break
  print(total)

if __name__ == "__main__":
  main(lines)