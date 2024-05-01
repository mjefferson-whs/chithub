import secret

print("HiiiiiiiiiIIIII")
user_pass = input("Please enter your password\n> ")

if user_pass == secret.PASSWORD:
  print("Welcome!")
else:
  print("F")