# First version

total = 0

for i in range(0,101,2):
  total += i
print(total)


# Second version
total2 = 0

for number in range(1,101):
  if number % 2 == 0:
    total2 += number
print(total2)