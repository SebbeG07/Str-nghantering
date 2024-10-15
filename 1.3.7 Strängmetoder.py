text = "  python programming is fun sometimes  "

print("Center:".center(30, "-"))
print(text.center(50, '-'))


print("\nCount 'p':", text.count('p'))
print("Count 'is':", text.count('is'))


print("\nRjust:".rjust(30, "-"))
print(text.rjust(60))


print("\nLjust:".ljust(30, "-"))
print(text.ljust(60))


print("\nUpper:".upper())
print(text.upper())


print("\nLower:".lower())
print(text.lower())


print("\nCapitalize:".capitalize())
print(text.capitalize())


print("\nTitle:".title())
print(text.title())


print("\nStrip:".strip())
print(text.strip())


print("\nReplace 'python' with 'Java':".replace(' ', '-'))
print(text.replace('python', 'Java'))

