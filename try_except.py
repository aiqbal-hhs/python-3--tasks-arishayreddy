while True:
  try:
    number = int(input("Enter a number: "))
    break
  except ValueError:
    print("Please enter a number!")


while True:
  try:
    height = float(input("Enter your height in meters: "))
    break
  except ValueError:
    print("Please enter a valid height in meters eg. 1.65")
