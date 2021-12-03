import re

from pathlib import Path

RE_INT   = re.compile(r"\d+")
RE_FLOAT = re.compile(r"\d?\.\d+")

def ints(o: object) -> list[int]:
  return list(map(int, RE_INT.findall(o) if type(o) is str else o))

def floats(o: object) -> list[float]:
  return list(map(float, RE_FLOAT.findall(o) if type(o) is str else o))

def resolve_path(**kwargs) -> Path:
  for folder in kwargs.get("folders", ["data/{day}", "."]):
    path = Path(folder.format(**kwargs)) / "input"
    if path.exists():
      return path

def read_string(**kwargs):
  with open(resolve_path(**kwargs)) as f:
    return f.read()

def read_lines(**kwargs):
  with open(resolve_path(**kwargs)) as f:
    return tuple(map(str.strip, f))