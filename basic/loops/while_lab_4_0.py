# Lab 4.0 - While Loop Practice

# === חלק 1: תרגילי בסיס ===

# תרגיל 1 - הדפס 1 עד 5
i = 1
while i <= 5:
    print(i)
    i += 1

# תרגיל 2 - הדפס 5 עד 1
i = 5
while i >= 1:
    print(i)
    i -= 1

# תרגיל 3 - זוגיים בין 1 ל-10
i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1

# תרגיל 4 - סכום 1 עד 5
i = 1
total = 0
while i <= 5:
    total += i
    i += 1
print(f"Sum: {total}")

# תרגיל 5 - כפולות 3 מתחת ל-10
i = 1
while i < 10:
    if i % 3 == 0:
        print(i)
    i += 1

# === חלק 2: עבודה עם קלט משתמש ===

# תרגיל 6 - הדפס מספר 5 פעמים
num = input("Enter a number: ")
i = 0
while i < 5:
    print(num)
    i += 1

# תרגיל 7 - הדפס 1 עד המספר שהוזן
target = int(input("Enter a number: "))
i = 1
while i <= target:
    print(i)
    i += 1

# תרגיל 8 - הזן מספרים עד 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    print(f"You entered: {num}")

# תרגיל 9 - סיסמה עד 1234
password = ""
while password != "1234":
    password = input("Enter password: ")
print("Access granted!")

# תרגיל 10 - y להמשיך, n לעצור
choice = "y"
while choice == "y":
    print("Running...")
    choice = input("Continue? (y/n): ")

# === חלק 3: תנאים בתוך לולאה ===

# תרגיל 11 - זוגיים מ-1 עד 10 (כמו 3 אבל עד 10)
i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1

# תרגיל 12 - ספור זוגיים בין 1 ל-20
i = 1
count = 0
while i <= 20:
    if i % 2 == 0:
        count += 1
    i += 1
print(f"Even count: {count}")

# תרגיל 13 - סכום אי-זוגיים בין 1 ל-10
i = 1
total = 0
while i <= 10:
    if i % 2 != 0:
        total += i
    i += 1
print(f"Odd sum: {total}")

# תרגיל 14 - זוגי/אי-זוגי בלולאה עד q
while True:
    val = input("Enter a number (q to quit): ")
    if val == "q":
        break
    num = int(val)
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

# תרגיל 15 - מספר גדול ביותר מ-5 קלטים
i = 0
max_num = float("-inf")
while i < 5:
    num = int(input("Enter a number: "))
    if num > max_num:
        max_num = num
    i += 1
print(f"Max: {max_num}")

# === חלק 4: שליטה בלולאה ===

# תרגיל 16 - לולאה עד exit
while True:
    text = input("Type something (exit to stop): ")
    if text == "exit":
        break
    print(f"You said: {text}")

# תרגיל 17 - הדפס 1-10, עצור ב-7
i = 1
while i <= 10:
    if i == 7:
        break
    print(i)
    i += 1

# תרגיל 18 - סכום עד מספר שלילי
total = 0
while True:
    num = int(input("Enter a number (negative to stop): "))
    if num < 0:
        break
    total += num
print(f"Total: {total}")

# תרגיל 19 - משחק ניחוש
secret = 7
while True:
    guess = int(input("Guess the number: "))
    if guess == secret:
        print("Correct!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")

# תרגיל 20 - ספור קלטים עד stop
count = 0
while True:
    text = input("Enter something (stop to end): ")
    if text == "stop":
        break
    count += 1
print(f"Total inputs: {count}")
