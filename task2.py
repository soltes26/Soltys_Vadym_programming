name = "Vadym"
surname = "Soltys"
group = "IT-32"
 
print(f"{name} {surname}, {group}")

letters = list(surname.lower())
c = len(letters)
print("Letters:", letters)
print("Length:", c)

print("First:", letters[0])
print("Middle:", letters[c // 2])
print("Last (index -1):", letters[-1])
print("Last (index len-1):", letters[len(letters) - 1])

print("First three:", letters[:3])
print("All except first three:", letters[3:])
print("Every second:", letters[::2])
print("Reversed:", letters[::-1])
print("Last two:", letters[-2:])
print("Slice of length 5 from position c:", letters[c:c + 5])
 
unique = []
for ch in letters:
    if ch not in unique:
        unique.append(ch)
print("Unique:", unique)
 
has_repeats = False
for ch in unique:
    count = letters.count(ch)
    if count > 1:
        print(f"{ch}: {count}")
        has_repeats = True
if not has_repeats:
    print("No repeated letters")

print("Alphabetical:", sorted(letters))