from utils import *

lines = read_lines(day=8)

example = (
  # "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf", # Unused example
  # "abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg | agbfce agced adgfeb acgfd", # Simple 0263
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

DIGITS_RE = re.compile(r'\w+')

NUMS = {
  2: (1,),
  3: (7,),
  4: (4,),
  5: (2, 3, 5),
  6: (0, 6, 9),
  7: (8,)
}

_filter = lambda fn, x: next(filter(fn, x))

def main(data):
  total = 0
  for line in data:
    seqs = tuple(map(frozenset, DIGITS_RE.findall(line)))
    one, seven, four, *pending, eight = sorted(set(seqs), key=len)
    six   = _filter(lambda x: len(eight - x) == 1 and len(x & one) == 1, pending)
    three = _filter(lambda x: len(x) == 5 and seven.issubset(x), pending)
    five  = _filter(lambda x: len(x) == 5 and not seven.issubset(x) and len(x & four) == 3, pending)
    two   = _filter(lambda x: len(x) == 5 and not seven.issubset(x) and len(x & four) != 3, pending)
    nine  = _filter(lambda x: len(x) == 6 and three | four == x, pending)
    zero  = _filter(lambda x: len(x) == 6 and not four.issubset(x) and seven.issubset(x), pending)
    six   = _filter(lambda x: len(x) == 6 and not four.issubset(x) and not seven.issubset(x), pending)

    lookup = {
      zero: '0',
      one: '1',
      two: '2',
      three: '3',
      four: '4',
      five: '5',
      six: '6',
      seven: '7',
      eight: '8',
      nine: '9'
    }
    total += int(seq := ''.join([lookup[x] for x in seqs[-4:]]))
    # print(seq)
  print(total)
  
if __name__ == "__main__":
  main(lines) # answer: 1024649