print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percent = int(input("What percentage tip would you like to give? 10,12 or 15? "))
people = int(input("How many people to split the bill? "))

formula = (bill * (percent / 100 + 1)) / people

final = "{:.2f}".format(formula)

print(f"Each person should pay: $ {final}")
