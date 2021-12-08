from utils import *

lines = read_lines(day=8)

example = (
  # "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf", # Unused example
  "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
  "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
  "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
  "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
  "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
  "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
  "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
  "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
  "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
  "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"
)

DIGITS = (6,2,5,5,4,5,6,3,7,6) # Section counts for digital numbers
NUMS = {
  2: (1,),
  3: (7,),
  4: (4,),
  5: (2, 3, 5),
  6: (0, 6, 9),
  7: (8,)
}

DIGITS_RE = re.compile(r'\w+')

def main(data):
  count = 0
  for line in data:
    seqs = tuple(map(frozenset, DIGITS_RE.findall(line)))
    one, seven, four, *_, eight = sorted(set(seqs), key=len)
    count += sum(x in {one, seven, four, eight} for x in seqs[-4:])
  print(count)

if __name__ == "__main__":
  main(lines) # asnwer: 409