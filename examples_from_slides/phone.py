import re
ph_nums = list()

input_strs = ["503-725-3000", "503-725-ABCD", "800-547-8887",
              "503-75-3000", "503-725--3000"]

pattern = "[0-9]{3}-[0-9]{3}-[0-9]{4}"

for input_str in input_strs:
    if re.match(pattern, input_str):
        ph_nums.append(input_str)
    else:
        ph_nums.append("NOPE")

print(ph_nums)

