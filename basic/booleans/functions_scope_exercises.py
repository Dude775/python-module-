# ============================================
# Lab 3.5 - Functions, Scope, and Execution Flow
# ============================================

# === Part 1 - הגדרת פונקציה בסיסית ===

# Exercise 1 - def יוצר פונקציה. הקוד בפנים לא רץ עד שקוראים לה
def hello():
    print("Hello")

# Exercise 2 - בלי לקרוא לפונקציה, לא יודפס כלום
# הפונקציה מוגדרת אבל "ישנה" עד שמפעילים אותה

# === Part 2 - קריאה לפונקציה ===

# Exercise 3 - סוגריים אחרי השם = הפעלה
hello()  # Hello

# === Part 3 - סדר ריצה ===

# Exercise 4 - פייתון רץ שורה אחרי שורה מלמעלה למטה
print("Start")
hello()  # קופץ לתוך הפונקציה, מבצע, חוזר
print("End")

# === Part 4 - פונקציה עם לוגיקה ===

# Exercise 5+6+7 - פונקציה שקולטת גיל וממירה לשניות
# שנה אחת = 365 ימים * 24 שעות * 60 דקות * 60 שניות
def user_age_in_seconds():
    age = int(input("Enter your age: "))
    age_seconds = age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is: {age_seconds}")

# === Part 5 - הפרדה בין הגדרה להרצה ===

# Exercise 8 - הפונקציה מוגדרת למעלה, הקריאה כאן
print("Welcome to the age in seconds program")
user_age_in_seconds()
print("Goodbye")

# === Part 6 - דריסת פונקציות מובנות (Shadowing) ===

# Exercise 9 - אם מגדירים פונקציה בשם print, דורסים את המובנית
# מרגע זה print() המקורי לא קיים - רק הפונקציה שלנו
# def print():
#     pass
# print("Hi")  # TypeError! הפונקציה שלנו לא מקבלת ארגומנטים
# הקוד מעלה בהערה כדי לא לשבור את שאר הקובץ

# === Part 7 - Scope ושגיאה ===

# Exercise 10+11 - משתנה גלובלי לא נגיש להשמה מתוך פונקציה
friends = ["John", "Jane"]

def add_friend_broken():
    # friends = friends + ["Rolf"]  # UnboundLocalError!
    # פייתון רואה השמה ל-friends אז מתייחס אליו כ-local
    # אבל בצד ימין מנסה לקרוא אותו לפני שהוגדר מקומית
    pass

# === Part 8 - פתרון בעיית scope ===

# Exercise 12 - פתרון: שם אחר למשתנה המקומי
def add_friend_fixed():
    friend_name = input("Enter your friend name: ")
    updated_friends = friends + [friend_name]
    print(updated_friends)

# === Part 9 - קריאה לפני הגדרה ===

# Exercise 13 - אי אפשר לקרוא לפונקציה לפני ש-def רץ
# say_hello()  # NameError: name 'say_hello' is not defined
# def say_hello():
#     print("Hi")

# === Part 10 - שימוש ב-append על משתנה גלובלי ===

# Exercise 14 - append עובד כי לא עושים השמה - משנים את האובייקט הקיים
# זה ההבדל: friends = ... יוצר local חדש, אבל friends.append() משנה את הגלובלי
global_friends = []

def add_rolf():
    global_friends.append("Rolf")

add_rolf()
print(global_friends)  # ['Rolf']

# === Part 11 - התנהגות מצטברת ===

# Exercise 15 - כל קריאה מוסיפה עוד איבר לאותה רשימה גלובלית
add_rolf()
add_rolf()
print(global_friends)  # ['Rolf', 'Rolf', 'Rolf']