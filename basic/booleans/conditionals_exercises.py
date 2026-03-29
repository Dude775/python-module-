# ============================================
# Lab 3.1 - Conditional Logic with if, elif, else
# ============================================

day_of_week = input("What day of the week is it today? ")
print('1+2')
print(day_of_week)

# === Part 2 - בדיקת תנאי עם Boolean ===
print(day_of_week == "Monday")

# === Part 3 - שימוש ב-if ===
# Exercise 5+6+7 - תנאי בסיסי

if day_of_week == "Monday":
    print("Have a great start of the week!")

# === Part 4 - קוד מחוץ ל-if ===

# Exercise 8+9 - שורה שרצה תמיד

print("This always runs")

# === Part 5 - שימוש ב-else ===

# Exercise 10+11 - טיפול בכל שאר המקרים

if day_of_week == "Monday":
    print("Have a great start of the week!")
else:
    print("Full speed ahead!")

# === Part 6 - שימוש ב-elif ===

# Exercise 12+13 - תנאי נוסף

if day_of_week == "Monday":
    print("Have a great start of the week!")
elif day_of_week == "Tuesday":
    print("It's a productive Tuesday!")
else:
    print("Full speed ahead!")

# === Part 7 - טיפול ב-Case Sensitivity ===

# Exercise 14+15 - נרמול קלט

day_of_week = input("What day of the week is it today? ").lower()

if day_of_week == "monday":
    print("Have a great start of the week!")
elif day_of_week == "tuesday":
    print("It's a productive Tuesday!")
else:
    print("Full speed ahead!")