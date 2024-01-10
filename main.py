def welcome_the_user():
  print("hello I am Chatbot I am here to assit you today?")
  

def collect_data():
  name = str(input("What is your name?: "))
  age = int(input("What is your age?: "))
  print(f"Hello {name} nice to meet you it must be nice being {age} years old")

def services():
  print("1.option 1")
  print("2.option 2")
  print("3.option 3")
  print("4.Exit")
  print("These are the tasks that I can complete")
  choice = int(input("Enter your choice: "))
  if choice == 1:
    print("you have selected option 1")
  elif choice == 2:
    print("you have selected option 2")
  elif choice == 3:
    print("you have selected option 3")
  elif choice == 4:
    print("I hope I was able to help")
    exit()
  else:
    print("Please choose a valid option")


welcome_the_user()
collect_data()
services()