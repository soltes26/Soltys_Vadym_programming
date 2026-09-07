print("Vadym Soltys, IT-32")

name = "Vadym"
surname = "Soltys"
full_name = name + surname

vowels = "aeiouy"
vowel_count = 0
consonant_count = 0

for letter in full_name:
    if letter.lower() in vowels:
        vowel_count += 1
    else:
        consonant_count += 1

print(f"{name} {surname}")
print(f"Vowels: {vowel_count}, consonants: {consonant_count}")
print(f"Total letters: {len(full_name)}")