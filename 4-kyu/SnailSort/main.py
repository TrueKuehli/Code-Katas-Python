xPlus = [1, 0, -1, 0]
yPlus = [0, 1, 0, -1]

def snail(array):
  direction = 0 # R, D, L, U
  x, y = (0, 0)
  restraints = [0, 0, 0, 0] # R, B, L, T

  out = []

  if len(array[0]) == 0:
    return out

  while True:
    if (direction == 0) and (x > (len(array[0]) - restraints[0])):
      break
    if (direction == 1) and (y > (len(array) - restraints[1])):
      break
    if (direction == 2) and (x < restraints[2]):
      break
    if (direction == 0) and (y < restraints[3]):
      break

    out.append(array[y][x])
    x += xPlus[direction]
    y += yPlus[direction]

    if (direction == 0):
      if x == (len(array[0]) - restraints[0]):
        x-=1
        y+=yPlus[(direction+1)%4]
        restraints[3] += 1
        direction += 1
        direction %= 4
    elif (direction == 1):
      if y == (len(array) - restraints[1]):
        x+=xPlus[(direction+1)%4]
        y-=1
        restraints[0] += 1
        direction += 1
        direction %= 4
    elif (direction == 2):
      if x == (restraints[2]):
        restraints[1] += 1
        direction += 1
        direction %= 4
    else:
      if y == (restraints[3]):
        restraints[2] += 1
        direction += 1
        direction %= 4

    if (restraints[1] + restraints[3]) == len(array):
      break
    if (restraints[0] + restraints[2]) == len(array[0]):
      break
  return out

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
print(snail(array), expected)


array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
expected = [1,2,3,4,5,6,7,8,9]
print(snail(array), expected)

array = [[1, 2, 3, 4, 5, 6], [20, 21, 22, 23, 24, 7], [19, 32, 33, 34, 25, 8], [18, 31, 36, 35, 26, 9], [17, 30, 29, 28, 27, 10], [16, 15, 14, 13, 12, 11]]
expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
print(snail(array), expected)
