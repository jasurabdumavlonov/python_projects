
print("Welcome to Treasure Island Game!!!")
left_right = input("Choose left or right: ")
if left_right == "left":
  swim_wait = input("Choose swim or wait: ")
  if swim_wait == "wait":
    door = input("Which door? red, yellow, blue ")
    if door == "red":
      print("Game Over")
    elif door == "yellow":
      print("You Win!")
    elif door == "blue":
      print("Game Over")
  else:
    print("Game Over")
else:
  print("Game Over")
