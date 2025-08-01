# Working with Lists

numbers = [10, 20, 30, 40, 50]

print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Middle element:", numbers[len(numbers) // 2])

numbers.append(60)

numbers.insert(1, 15)

numbers.pop()

print("Length of the list:", len(numbers))

numbers.sort()
print("Sorted list:", numbers)



# Change a Specific Word in a Sentence

sentence = "Python is fun because Python is powerful"
target_word = "Python"
new_word = "Programming"

words = sentence.split()

for i in range(len(words)):
    if words[i] == target_word:
        words[i] = new_word

new_sentence = " ".join(words)
print("Modified sentence:", new_sentence)



# Palindrome Check with Slicing

word = input("Enter a word to check if it's a palindrome: ")

if word == word[::-1]:
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")



# f-String Formatting

name = "Alice"
age = 30
balance = 1234.56789
membership_date = "2023-08-12"
status = True

print(f"My name is {name} and I am {age} years old.")

print(f"Account balance: ${balance:>10.2f}")

print(f"Member since: {membership_date}")

active_status = "Yes" if status else "No"
print(f"Active member: {active_status}")


