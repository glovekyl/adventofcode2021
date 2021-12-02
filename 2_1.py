from utils import *

lines = read_lines(day=2)
example = ("forward 5","down 5","forward 8","up 3","down 8","forward 2")

horizon, depth = 0, 0
for commands in lines:
  action, units = commands.split()
  units = int(units)
  if action == "forward":
    horizon += units
  elif action == "down":
    depth += units
  elif action == "up":
    depth -= units
print(horizon*depth) # answer: 2073315
