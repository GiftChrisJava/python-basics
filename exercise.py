# program that guesses your age 
birth_year = input( "what year were you born in ? >> ")

age = 2024 - int(birth_year) # convert integer string to integer

print(f"You must be {age}  or {age - 1} years old")