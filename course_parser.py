import re

pattern = "^([ A-Z]+) - ([0-9]*) - ([A-Z]+) ([0-9]+) - ([0-9]+)$"

# uses the `course_file` object to read the contents of the file as a string
# and then splits the string on '\n', creating a list `courses`
# The file will close automatically when we exit the `with` block.
with open("./courses.txt") as course_file:
    courses_input = course_file.read().split('\n')

# iterates through the `courses` list and uses the `match` function in the `re`
# package to parse each string in the list.
# `re.match` returns a Match object. The member function groups() returns a
# tuple containing all the subgroups of the match.
# If the regex `pattern` wasn't present in the string being parsed, `re.match`
# returns the None object. We have to check for that before calling `groups()`.
courses_parsed = list()
for i in range(len(courses_input)):
    matches = re.match(pattern, courses_input[i])
    if matches:
        courses_parsed.append(matches.groups())

# `courses_parsed` is now a list of tuples
# try `print(courses_parsed)` to see how the parsing worked out.

# We want to find all the departments represented in our file
depts = set()
for i in range(len(courses_parsed)):
    depts.add(courses_parsed[i][2])

print(depts)
