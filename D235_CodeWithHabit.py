# Formatting string litterals: f-string
# advantages compared format() method: you can bring variables directly into strings (no need to pass them
# as arguments)
# documentation

name = "kamil"
print(f"His name is: {name}")

print(f"His name is: {name!r}")

num = 23.52685
# padding using formatting from .function() method
print(f"My 10 character, four decimals number is: {num:10.4f}")
# padding using f-strings (note if you want to have 4 decimals, you must involve the integer as well)
print(f"My 10 character, four decimals number is: {num:{10}.{6}}")