names_list = ['Jiri', 'Jan', 'Marie', 'Petr', 'Jana', 'Josef', 'Pavel', 'Martin', 'Jaroslav', 'Tomas', 'Eva', 'Miroslav', 'Hana', 'Anna', 'Zdenek', 'Frantisek', 'Vaclav', 'Michal', 'Lenka', 'Katerina']
name = input("What is your name?")

What is your name? Mark

if name in names_list:
  print("Your name is on the list of top 20 names in the Czech Republic!")
else:
  print("Your name is not on the list of top 20 names in the Czech Republic.")
  
Your name is not on the list of top 20 names in the Czech Republic.


d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta','e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima', 'm':'mike','n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec','r':'romeo', 's':'sierra', 't':'tango', 'u':'uniform','v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee','z':'zulu'}
name = input("What is your name?")
What is your name? Daniel
for letter in name:
  letter = letter.lower()
  if letter in d:
    print(letter + ":" + d[letter])    
d:delta
a:alfa
n:november
i:india
e:echo
l:lima


shopping_list = ['wine', 'bread', 'cheese', 'apples']
while True:
  item = input('Enter item: ')
  for i in shopping_list:
    if i == item:
      print(f'{item} found in shopping list')
      break
  else:
    shopping_list.append(item)
    print(f'{item} added to shopping list')
        

numbers = [1, 2, 3, 4, 5]
new_numbers = [num**2 for num in numbers]
print(numbers)
print(new_numbers)
[1, 2, 3, 4, 5]
[1, 4, 9, 16, 25]
numbers = [1, 2, 3, 4, 5]
new_numbers = [str(num) + ' is my favorite number!' for num in numbers]
print(numbers)
print(new_numbers)
[1, 2, 3, 4, 5]
['1 is my favorite number!', '2 is my favorite number!', '3 is my favorite number!', '4 is my favorite number!', '5 is my favorite number!']


seq = 'ACTGCTCAAG'
new = [i for i, letter in enumerate(seq) if letter == 'A']
print(new)
[0, 7, 8]

seq = 'ACTGCTCAAG'
new = [i for i in range(len(seq)) if seq[i] == 'A']
print(new)
[0, 7, 8]

scores = {'John': 10, 'Emily': 35, 'Matthew': 50}
tripled_scores = {k: v * 3 for k, v in scores.items()}
print(tripled_scores)
{'John': 30, 'Emily': 105, 'Matthew': 150}