# Exercise 1 – קלט בסיסי
# input() עוצר את התוכנית ומחכה שהמשתמש יקליד משהו
# מה שהמשתמש מקליד נשמר במשתנה כ-string
name = input("Enter your name: ")
print(name)

# Exercise 2 – שימוש ב-Prompt
# הטקסט שבתוך input() מוצג למשתמש כהודעה לפני שהוא מקליד
city = input("Which city do you live in? ")
print(city)

# Exercise 3 – קלט מספרי ללא המרה
# input() תמיד מחזיר string, אז "20" + 5 זה שגיאה
# אי אפשר לחבר string עם מספר — Python לא מנחש מה התכוונת
try:
    age = input("Enter your age: ")
    print(age + 5)
except TypeError as e:
    print(e)
    
# Exercise 4 – המרה ל-int
# עוטפים את input() עם int() כדי להפוך את הstring למספר שלם
age = int(input("Enter your age: "))
print(age)

# Exercise 5 – חישוב גיל בעתיד
# עכשיו שזה מספר אמיתי, אפשר לעשות חשבון רגיל
age_future = age + 10
print(age_future)

# Exercise 6 – קלט float
# float() במקום int() כשצריך מספר עם נקודה עשרונית
price = float(input("Enter price: "))
print(price)

# Exercise 7 – חישוב מחיר כולל מס
# מכפילים ב-1.17 כדי להוסיף 17% מס
price = float(input("Enter price: "))
total = price * 1.17
print(total)

# Exercise 8 – שימוש ב-F-String
# f-string מאפשר לשתול את המשתנה בתוך הודעה קריאה
print(f"The final price is {total}")

# Exercise 9 – פורמט שתי ספרות עשרוניות
# :.2f בתוך הסוגריים המסולסלים אומר "הצג 2 ספרות אחרי הנקודה"
print(f"The final price is {total:.2f}")

# Exercise 10 – חיבור שני מספרים
# קולטים שני מספרים, ממירים ל-int, ומחברים
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(num1 + num2)

# Exercise 11 – חישוב ממוצע
# סוכמים את שלושת המספרים ומחלקים ב-3
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
average = (a + b + c) / 3
print(average)

# Exercise 12 – המרה ל-square meters
# 1 square foot = 0.09259259 square meters (חלקי 10.764)
sqft = float(input("Enter house size in square feet: "))
sqm = sqft / 10.764
print(sqm)

# Exercise 13 – שימוש ב-F-String לחישוב שטח
# מציגים את שני הערכים בהודעה אחת ברורה
print(f"{sqft} square feet is equal to {sqm} square meters")

# Exercise 14 – פורמט תוצאה
# :.2f שוב — מסדר את המספר לשתי ספרות אחרי הנקודה
print(f"{sqft:.0f} square feet is equal to {sqm:.2f} square meters")

# Exercise 15 – שילוב מלא
# הכל ביחד: קלט > המרה > חישוב > הצגה מפורמטת
sqft = float(input("Enter house size in square feet: "))
sqm = sqft / 10.764
print(f"{sqft:.0f} square feet is equal to {sqm:.2f} square meters")
