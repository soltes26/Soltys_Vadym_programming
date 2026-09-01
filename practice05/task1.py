birth_year = 2009  
height = 1.78  
full_name = "Vadym Soltys"  
has_scholarship = True  

print(f"birth_year = {birth_year}, type: {type(birth_year)}")
print(f"height = {height}, type: {type(height)}")
print(f"full_name = {full_name}, type: {type(full_name)}")
print(f"has_scholarship = {has_scholarship}, type: {type(has_scholarship)}")

print("--- До зміни типу ---")
print(f"birth_year = {birth_year}, type: {type(birth_year)}")
print(f"has_scholarship = {has_scholarship}, type: {type(has_scholarship)}")

birth_year = "two thousand nine"  
has_scholarship = 1.78 

print("--- Після зміни типу ---")
print(f"birth_year = {birth_year}, type: {type(birth_year)}")
print(f"has_scholarship = {has_scholarship}, type: {type(has_scholarship)}")

birth_year = birth_year + 1