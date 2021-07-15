import re

text = "Kama\nKamil Klemsa\nZádvoří 253\nKonice"

print(text)

dotStar = re.compile(r".*")

print(dotStar.search(text))
print(dotStar.findall(text))