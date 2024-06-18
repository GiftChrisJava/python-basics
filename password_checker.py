#password checker

username = input("Enter username: ")
password = input("Enter password: ")

star_password = "*" * len(password)

print(f"{username} your password: {star_password} is {len(star_password)} letters long")