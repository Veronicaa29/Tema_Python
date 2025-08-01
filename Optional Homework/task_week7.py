# File Filtering with Context Manager

# Create students.txt file
with open("students.txt", "w") as file:
    file.write("Alice\nEve\nCharlie\nOscar\nUma\nBob\nIan\nZack")

vowels = ('A', 'E', 'I', 'O', 'U')

with open("students.txt", "r") as infile, open("filtered.txt", "w") as outfile:
    for line in infile:
        name = line.strip()
        if name.startswith(vowels):
            outfile.write(name + "\n")



# Reverse File Content

# Create log file
with open("log.txt", "w") as f:
    f.write("Line 1: Start\nLine 2: Load\nLine 3: Process\nLine 4: Save\nLine 5: Complete\n")

with open("log.txt", "r") as original_file:
    lines = original_file.readlines()

lines.reverse()

with open("reversed_log.txt", "w") as reversed_file:
    reversed_file.writelines(lines)



# Modularize Student Report Generator

from report import generate_report

student_data = {
    'Lisa': 85,
    'Bart': 72,
    'Homer': 91,
    'Maggie': 78,
    'Marge': 88
}

report = generate_report(student_data)
print(report)