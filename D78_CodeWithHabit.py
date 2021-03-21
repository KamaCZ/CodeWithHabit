# Lambda expression for grabbing the first character of a string:

first_letter = lambda word: word[0]
print(first_letter("Kamil"))



# Lambda expression for reversing a string:

reverse = lambda word: word[:2-1]
print(reverse("Kamil"))


def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

print(reverse("kamil"))

def reverse(s):
    return s[::-1]

print(reverse("Lubos"))

print(list(reversed("Kamil")))
print("".join(list(reversed("Kamil"[0:4]))))


