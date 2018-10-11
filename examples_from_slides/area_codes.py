
import re
area_codes = list()

input_strs = ["503-725-3000", "503-725-ABCD", "800-547-8887",
              "503-75-3000", "503-725--3000"]

pattern = "([0-9]{3})-([0-9]{3}-[0-9]{4})"

for input_str in input_strs:
    match_result = re.match(pattern, input_str)
    if match_result:
        area_codes.append(match_result.groups()[0])
    else:
        area_codes.append("NOPE")

print(area_codes)
