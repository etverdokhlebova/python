def divide(num1, num2):
  result = num1/num2
  return result
  
result = divide(10, 5)
print(result)
2.0


def print_sum(numbers):
  total = 0
  for number in numbers:
    total += number
  print(total)
  
print_sum([1, 2, 3, 4, 5])
15


compare_list = lambda x: print("big list") if len(x) > 5 else print("small list")

result = compare_list([1, 2, 3, 4, 5, 6])
big list

result = compare_list([1, 2, 3])
small list


def get_string_info(string):
  upper_count = 0
  lower_count = 0
  for letter in string:
    if letter.isupper():
      upper_count += 1
    elif letter.islower():
      lower_count += 1
  return string, upper_count, lower_count
  

result = get_string_info("I just want to have a good salary and then go to Marocco, but I think my brain will explode because of these things")
print(result)
('I just want to have a good salary and then go to Marocco, but I think my brain will explode because of these things', 3, 88)


def compute_payment(lunch_cost, voucher_value):
  voucher_payment = min(lunch_cost, voucher_value)
  cash_payment = lunch_cost - voucher_payment
  voucher_count = voucher_payment // voucher_value
  return "Lunch cost: {} euro\nPay in cash: {} euro\nPay in meal vouchers: {} pcs, {} euro each".format(lunch_cost, cash_payment, voucher_count, voucher_value)
  
result = compute_payment(6, 3)
print(result)
Lunch cost: 6 euro
Pay in cash: 3 euro
Pay in meal vouchers: 1 pcs, 3 euro each