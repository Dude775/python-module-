# Lab 4.5 - For Loop Practice

# === חלק 1: תרגילי בסיס ===

# תרגיל 1 - הדפס 1 עד 5
for i in range(1, 6):
    print(i)

# תרגיל 2 - הדפס 5 עד 1
for i in range(5, 0, -1):
    print(i)

# תרגיל 3 - זוגיים בין 1 ל-10
for i in range(2, 11, 2):
    print(i)

# תרגיל 4 - כל המספרים 1 עד 10
for i in range(1, 11):
    print(i)

# תרגיל 5 - כפולות 3 מתחת ל-20
for i in range(3, 20, 3):
    print(i)

# === חלק 2: עבודה עם range ===

# תרגיל 6 - הדפס Hello חמש פעמים
for _ in range(5):
    print("Hello")

# תרגיל 7 - הדפס 0 עד 9
for i in range(10):
    print(i)

# תרגיל 8 - 2 עד 20 בקפיצות של 2
for i in range(2, 21, 2):
    print(i)

# תרגיל 9 - 10 עד 0
for i in range(10, -1, -1):
    print(i)

# תרגיל 10 - סכום 1 עד 100
total = 0
for i in range(1, 101):
    total += i
print(f"Sum: {total}")

# === חלק 3: עבודה עם רשימות ===

# תרגיל 11 - הדפס שמות מרשימה
names = ["Alice", "Bob", "Charlie", "Diana"]
for name in names:
    print(name)

# תרגיל 12 - ספור פריטים ברשימה
items = ["apple", "banana", "cherry", "date", "elderberry"]
count = 0
for item in items:
    count += 1
print(f"Items: {count}")

# תרגיל 13 - סכום מספרים מרשימה
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
print(f"Sum: {total}")

# תרגיל 14 - מספר גדול ביותר ברשימה
numbers = [3, 17, 8, 42, 11, 5]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"Max: {max_num}")

# תרגיל 15 - שמות שמתחילים ב-A
names = ["Alice", "Bob", "Anna", "Charlie", "Alex"]
for name in names:
    if name.startswith("A"):
        print(name)

# === חלק 4: תנאים בתוך לולאה ===

# תרגיל 16 - זוגיים מרשימה
numbers = [1, 4, 7, 8, 11, 14, 19, 20]
for num in numbers:
    if num % 2 == 0:
        print(num)

# תרגיל 17 - ספור מספרים גדולים מ-10
numbers = [3, 15, 8, 22, 7, 11, 2]
count = 0
for num in numbers:
    if num > 10:
        count += 1
print(f"Greater than 10: {count}")

# תרגיל 18 - מתחלקים גם ב-2 וגם ב-3
for i in range(1, 31):
    if i % 2 == 0 and i % 3 == 0:
        print(i)

# תרגיל 19 - ריבוע של כל מספר
numbers = [2, 5, 8, 3, 10]
for num in numbers:
    print(f"{num}² = {num ** 2}")

# תרגיל 20 - רשימה חדשה עם חיוביים בלבד
numbers = [-5, 3, -1, 8, -2, 7, 0, -4, 12]
positives = []
for num in numbers:
    if num > 0:
        positives.append(num)
print(f"Positives: {positives}")
