print("Welcome to the Disney Park")
height = int(input("What's your height in cm? "))
bill = 0

if height > 150:
  print("You can get into this park!")
  age = int(input("What's your age? "))
  if age < 12:
    bill = 3
    print("Child ticket is 3$")
  elif age < 18:
    bill = 5
    print("Youth tickets are 5$")
  else:
    bill = 7
    print("Adult tickets are 7$")
  print("The photo is 3$")
  want_photo = input("Do you wanna photo to memorise? Type Y or N")
  if want_photo == "Y":
    bill += 3
    print(f"Your total bill is {bill}")
else:
  print("Sorry, we can't to access you")
