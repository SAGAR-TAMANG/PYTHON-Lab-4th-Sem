# Take the gender from the user (male/female).
# If the gender is male, ask the age from the user.
    # If the age is <= 26, then the insurance percentage is 26.
    # If the age > 26, then insurance percentage is 8.
# If gender is female, then ask the car type = (Sports/Non-Sports).
  # If car type is Sports, then the insurance percentage is 18.
  # If car type is non-sports then insurance percentage is 9.
# Take the car price from the user.
# Insurance offer is car price * insurance percentage / 100.
# Print the insurance offer.


gen = input("Give the gender: ")

if gen == "male":
  age = int(input("Give the age: "))
  if age > 26:
    insurance = 26
  else:
    insurance = 8
elif gen == "female":
  car_type = input("Sports or Non-Sports")
  if car_type == "Sports":
    insurance = 18
  else:
    insurance = 9

price = int(input("What is the price of the car? :"))

print("The insurance offer is:", (price *  insurance / 100))