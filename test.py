import regex as re

note = "b#7"

r = re.match(r"[A-Ga-g]+[#b]*\d+", note)

print(r)
