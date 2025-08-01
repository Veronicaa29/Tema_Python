# Are Two Words Anagrams?

word1 = "listen"
word2 = "silent"

def count_letters(word):
    freq = {}
    for letter in word:
        freq[letter] = freq.get(letter, 0) + 1
    return freq

dict1 = count_letters(word1)
dict2 = count_letters(word2)

print("Original dictionaries:")
print("Word 1:", dict1)
print("Word 2:", dict2)

print("Are anagrams:", dict1 == dict2)

del dict2['t']

print("\nAfter deleting one letter from word2:")
print("Word 1:", dict1)
print("Word 2:", dict2)



# Invert a Dictionary with Duplicates in Values

grades = {"Alice": "A", "Bob": "B", "Charlie": "A", "Diana": "C"}

inverted = {}

for student, grade in grades.items():
    if grade not in inverted:
        inverted[grade] = []
    inverted[grade].append(student)

print("Inverted dictionary:")
print(inverted)



# Set Analysis for Conference Attendees

testing = {"Ana", "Bob", "Charlie", "Diana"}
development = {"Charlie", "Eve", "Frank", "Ana"}
devops = {"George", "Ana", "Bob", "Eve"}

all_three = testing & development & devops
print("Attended all three:", all_three)

only_testing = testing - (development | devops)
only_development = development - (testing | devops)
only_devops = devops - (testing | development)
only_one = only_testing | only_development | only_devops
print("Attended only one session:", only_one)

print("All testing in devops:", testing.issubset(devops))

all_attendees = testing | development | devops
sorted_attendees = sorted(all_attendees)
print("All unique attendees (sorted):", sorted_attendees)

development_copy = development.copy()
development.clear()
print("Copied development:", development_copy)
print("Cleared original development:", development)



#  Create Data with Comprehensions

squares = [x**2 for x in range(1, 11)]
print("Squares 1 to 10:", squares)

# Set of Numbers Divisible by 7
divisible_by_7 = {x for x in range(1, 51) if x % 7 == 0}
print("Numbers divisible by 7 (1-50):", divisible_by_7)

# Dictionary of Students Who Passed
score = {"Alice": 85, "Bob": 59, "Charlie": 92}
passed = {name: mark for name, mark in score.items() if mark >= 60}
print("Students who passed:", passed)

# Nested Dictionary: Weekly Attendance Log
students = ["Michael", "David", "Liza"]
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]

attendance_log = {
    student: {day: (day in ["Mon", "Wed"]) for day in weekdays}
    for student in students
}

print("Weekly attendance log:")
for student, days in attendance_log.items():
    print(f"{student}: {days}")