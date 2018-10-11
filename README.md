## Parsing strings with regular expressions in Python

In this repo is a text file containing a list of courses at Portland
State University in a fixed-width format used by the Univeristy's
student information system.

The course ID format is as follows:

`[course title, all caps] - [university course num] - [department] [dept course num] - [section]`

eg.  `INTRODUCTION TO PLANT BIOLOGY - 10447 - BI 330 - 001`

---

The python program `course_parser.py` reads this file and prints the set
of departments represented in the file.

