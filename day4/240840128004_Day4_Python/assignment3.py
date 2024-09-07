# assignment 3
# implement a classic algorithm using list comprehension

l = [x for x in range(0,21)]

l1 = ['FizzBuzz' if x % 3 == 0 and x % 5 == 0 else ('Fizz' if x % 3 == 0 else('Buzz' if x % 5 == 0 else x)) for x in l]

print(l1)