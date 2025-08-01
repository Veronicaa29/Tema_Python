# Currency Conversion with Unpacking and f-Strings

data = [
    (100, 'USD', 'EUR', 0.83),
    (100, 'USD', 'CAD', 1.27),
    (100, 'CAD', 'EUR', 0.65)
]

for amount, currency, target_currency, exchange_rate in data:
    converted = amount * exchange_rate
    print(f"{amount} {currency} = {converted:.2f} {target_currency}")



# Sum of Odd Numbers

total = 0
for num in range(1, 101):
    if num % 2 != 0:
        total += num

print("Sum of odd numbers from 1 to 100:", total)



# Number Guessing Game

secret_number = 7
attempts = 3

while attempts > 0:
    guess = int(input("Guess the number (1-10): "))
    
    if guess == secret_number:
        print("Congratulations! You guessed the number!")
        break
    else:
        print("Wrong guess.")
        attempts -= 1

if attempts == 0:
    print("Sorry, you've run out of attempts. The number was 7.")




# Enumerate List Items with Index

fruits = ['apple', 'banana', 'cherry', 'date']

for index, fruit in enumerate(fruits, start=1):
    length = len(fruit)
    print(f"{index}: {fruit} ({length} letters)")



# Mutate the Data and Find Max Difference

data = [
    ['2021-01-01', 20, 10],
    ['2021-01-02', 20, 18],
    ['2021-01-03', 10, 10],
    ['2021-01-04', 102, 100],
    ['2021-01-05', 45, 25]
]

for row in data:
    stop = row[1]
    start = row[2]
    difference = stop - start
    row.insert(1, difference)

max_diff = -1
max_date = ""

for row in data:
    difference = row[1]
    date = row[0]
    if difference > max_diff:
        max_diff = difference
        max_date = date

print(f"The largest difference was on {max_date} with a value of {max_diff}.")