name = "Vadym"
surname = "Soltys"
group = "IT-32"
c = 6

print(f"{name} {surname}, {group}")

grades = [6, 5, 7, 6, 8, 7]

average = sum(grades) / len(grades)
print("Grades:", grades)
print("Count:", len(grades))
print("Sum:", sum(grades))
print("Best:", max(grades))
print("Worst:", min(grades))
print(f"Average: {average:.2f}")
print("Sorted (best to worst):", sorted(grades, reverse=True))
print("Original:", grades)
 
print("Top 3:", sorted(grades, reverse=True)[:3])
print("Bottom 3:", sorted(grades)[:3])
 
print("Worst grade position:", grades.index(min(grades)) + 1)
 
above_average = []
for g in grades:
    if g > average:
        above_average.append(g)
print("Above average:", above_average)
print("Above average count:", len(above_average))

print("Has 12:", 12 in grades)
print("Has 1:", 1 in grades)

grades.append(c % 12 + 1)
print("After append:", grades)
 
grades.insert(0, 12)
print("After insert:", grades)
 
grades.remove(min(grades))
print("After removing worst:", grades)
 
removed = grades.pop()
print("Removed last:", removed)
print("After pop:", grades)

print("Count of 12:", grades.count(12))
 
result = grades.sort()
print("sort() returned:", result)
print("Sorted list:", grades)