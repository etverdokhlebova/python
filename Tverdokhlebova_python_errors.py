seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is ', seasons[3])

message = ""
for number in range(10):
  # use a if the number is a multiple of 3, otherwise use b
  if (number % 3) == 0:
    message = message + "a"
  else:
    message = message + "b"
print(message)


name = input("What is your name: ")

if any(char.isdigit() for char in name): #nerozumiem tomuto, to ma byť, že ked najde hociaké čislo na miesto pismena v mene, tak ma urobiť vynimku, ale stale mi ukazuje chybu NameError: name 'mik1' is not defined 
  raise Exception("Name cannot contain numbers.")
if " " in name:
  raise Exception("Name cannot contain spaces.")
if not name[0].isupper():
  raise Exception("Name must start with an uppercase letter.")
  

def divide_integers():
  while True:
    try:
      num1 = int(input("Enter the first integer: "))
      num2 = int(input("Enter the second integer: "))
      if num2 == 0:
        print("The second number cannot be zero. Please try again.")
      else:
        result = num1 / num2
        print(f"The result of the division is {result}.")
        break
    except ValueError:
      print("Both numbers must be integers. Please try again.")
     
divide_integers()
Enter the first integer: 2
Enter the second integer: 0
The second number cannot be zero. Please try again.
Enter the first integer: 4
Enter the second integer: 2
The result of the division is 2.0.  


year = int(input("Greetings! What is your year of origin?"))
if year <= 1900:
 print ("Woah, that's the past!")
elif year > 1900 and year < 2020:
 print ("That's totally the present!")
elif year >= 2020:
 print ("Far out, that's the future!!")
 
Greetings! What is your year of origin? 2018
That's totally the present!