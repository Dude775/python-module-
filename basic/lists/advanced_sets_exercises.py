# Exercise 1 – Try to create a Set with Lists (will fail)
# list הוא mutable ולכן לא hashable — אי אפשר לשים אותו ב-set
try:
    set([[1, 2], [3, 4]])
except TypeError as e:
    print(f"Exercise 1: {e}")
    
    # Exercise 2 – Try to create a Set with Sets (will fail)
# set בתוך set גם לא חוקי — מאותה סיבה, set הוא mutable
try:
    eval("{{1, 2}, {3, 4}}")
except TypeError as e:
    print(f"Exercise 2: {e}")
    
# Exercise 3 – Create a Set with Tuples (valid)
# tuple הוא immutable ולכן hashable — מותר לשים אותו ב-set
set_of_tuples = {(1, 2), (3, 4)}
print(f"\nExercise 3: {set_of_tuples}")

# Exercise 4 – Membership check with Tuple
# בודקים אם tuple שלם קיים ב-set — לא איבר בודד
print(f"Exercise 4a: (1, 2) in set? {(1, 2) in set_of_tuples}")
print(f"Exercise 4b: (1, 3) in set? {(1, 3) in set_of_tuples}")

# Exercise 5 – Create two Sets
developers = {"Alice", "Bob", "Charlie"}
admins = {"Alice", "David"}

# Exercise 6 – Check membership
print(f"\nExercise 6a: Alice in developers? {'Alice' in developers}")
print(f"Exercise 6b: Alice in admins? {'Alice' in admins}")

# Exercise 7 – Union with method
# union מחזיר set חדש עם כל האיברים משניהם, בלי כפילויות
print(f"\nExercise 7 - union(): {developers.union(admins)}")

# Exercise 8 – Union with operator
# | עושה בדיוק אותו דבר כמו union() — סינטקס מקוצר
print(f"Exercise 8 - |: {developers | admins}")

# Exercise 9 – Intersection with method
# intersection מחזיר רק מה שמשותף לשניהם
print(f"\nExercise 9 - intersection(): {developers.intersection(admins)}")


# Exercise 10 – Intersection with operator
# & עושה בדיוק אותו דבר כמו intersection()
print(f"Exercise 10 - &: {developers & admins}")


# Exercise 11 – Difference with method
# difference מחזיר מה שב-developers ולא ב-admins
print(f"\nExercise 11 - difference(): {developers.difference(admins)}")


# Exercise 12 – Difference with operator
# - עושה בדיוק אותו דבר כמו difference()
print(f"Exercise 12 - minus: {developers - admins}")


# Exercise 13 – intersection_update (MUTATES the original)
# שים לב: זה משנה את developers במקום! לא מחזיר set חדש
# אחרי זה developers יכיל רק את מה שמשותף עם admins
developers.intersection_update(admins)
print(f"\nExercise 13 - developers after intersection_update: {developers}")


# Exercise 14 – Compare: intersection does NOT mutate
# יוצרים מחדש כי intersection_update שינה את developers
developers = {"Alice", "Bob", "Charlie"}
result = developers.intersection(admins)
print(f"\nExercise 14 - intersection result: {result}")
print(f"Exercise 14 - developers unchanged: {developers}")

# Exercise 15 – Summary with custom Sets
ports = {80, 443, 8080, 3000}
secure_ports = {443, 8443}
print(f"\nExercise 15 - Union: {ports | secure_ports}")
print(f"Exercise 15 - Intersection: {ports & secure_ports}")
print(f"Exercise 15 - Difference: {ports - secure_ports}")