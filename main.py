# importing built-in module, or code library, for returning a list with a random selection from the given sequence
import random

# welcome banner for user
print("""---------------------------------
Welcome to the Password Generator
---------------------------------
""")

# listing out all possible characters for a password
rand_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*().,0123456789"

def password_func():
  # asking user for number of passwords
  while True:
    try:
      num_passwords = int(input("How many passwords do you need? "))
    except ValueError:
      print("\n*Please enter a number.")
      continue
    else:
      break

  # asking user for length of password(s)
  while True:
    try:
      length_password = int(input("Enter password length: "))
    except ValueError:
      print("\n*Please enter a number.")
      continue
    else:
      break

  # message on new line for user
  print("\nSee password(s) below:")

  # nested for loops to generate random password based on number of passwords needed and character length
  for pwd in range(num_passwords):
    passwords = ""
    for char in range(length_password):
      passwords += random.choice(rand_chars)
    print(passwords)

password_func()

# asking user if more passwords are needed 
while True:
  next_round = str(input("\nDo you need more passwords? Yes or No: "))
  if next_round == "Yes":
    # print("Okay!")
    password_func()
    continue
  elif next_round == "No":
    print("Bye then!")
    break
  else:
    print("Please enter either Yes or No: ")
    continue
  
"""
Future Enhancements:
- Remove case sensitivity for Yes/No options
- Also modify Yes/No question to accept Y, y, N, and n
"""