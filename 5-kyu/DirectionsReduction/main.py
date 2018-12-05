opposing = {
  "NORTH": "SOUTH",
  "SOUTH": "NORTH",
  "WEST": "EAST",
  "EAST": "WEST"
}

def dirReduc(dirs):
  length = len(dirs) - 1
  pos = 0
  while pos < length:
    if opposing[dirs[pos]] == dirs[pos+1]:
      del dirs[pos + 1]
      del dirs[pos]

      if pos != 0:
        pos -= 1

      length -= 2
    else:
      pos+=1


  return dirs


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a), ['WEST'])
u = ["NORTH", "WEST", "SOUTH", "EAST"]
print(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])
