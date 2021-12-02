from utils import *

lines = read_lines(day=2)
example = ("forward 5","down 5","forward 8","up 3","down 8","forward 2")

horizon, depth, aim = 0, 0, 0
for commands in lines:
  action, units = commands.split()
  units = int(units)
  if action == "forward":
    horizon += units
    depth += aim * units
  elif action == "down":
    aim += units
  elif action == "up":
    aim -= units
print(horizon*depth) # answer: 1840311528