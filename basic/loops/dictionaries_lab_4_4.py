# Lab 4.4 - Dictionaries Practice

# תרגיל 1 - גישה לערך
friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
print(friend_ages["Anne"])
# ניגשים לערך לפי שם המפתח בסוגריים מרובעים

# תרגיל 2 - הוספת ערך
friend_ages = {"Rolf": 24, "Adam": 30}
friend_ages["Bob"] = 20
print(friend_ages)
# מוסיפים key חדש פשוט על ידי השמה - אם המפתח לא קיים הוא נוצר

# תרגיל 3 - עדכון ערך
friend_ages = {"Rolf": 24, "Adam": 30}
friend_ages["Rolf"] = 40
print(friend_ages)
# אותו תחביר כמו הוספה - אם המפתח כבר קיים הערך מתעדכן

# תרגיל 4 - בדיקה עם in
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
if "Bob" in student_attendance:
    print("Bob attended")
# in בודק אם המפתח קיים במילון - מחזיר True או False

# תרגיל 5 - מעבר על מפתחות
student_attendance = {"Rolf": 96, "Bob": 80}
for name in student_attendance:
    print(name)
# for על dictionary עובר על המפתחות (keys) כברירת מחדל

# תרגיל 6 - הדפסת מפתח וערך
student_attendance = {"Rolf": 96, "Bob": 80}
for name in student_attendance:
    print(name, student_attendance[name])
# ניגשים לערך דרך המפתח בתוך הלולאה

# תרגיל 7 - שימוש ב-items
student_attendance = {"Rolf": 96, "Bob": 80}
for name, grade in student_attendance.items():
    print(name, grade)
# items() מחזיר זוגות (key, value) - מפרקים לשני משתנים כמו enumerate

# תרגיל 8 - עבודה עם values
student_attendance = {"Rolf": 100, "Bob": 80, "Anne": 60}
grades = student_attendance.values()
average = sum(grades) / len(student_attendance)
print(average)
# values() מחזיר את כל הערכים בלבד, sum סוכם, len סופר כמה יש

# תרגיל 9 - רשימה של dictionaries
friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30}
]
print(friends[1]["name"])
# friends[1] = dictionary השני ברשימה, ["name"] = הערך של המפתח name

# תרגיל 10 - סינון מתוך רשימת dictionaries
friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27}
]
result = []
for friend in friends:
    if friend["age"] > 25:
        result.append(friend)
print(result)
# עוברים על כל dictionary ברשימה, בודקים תנאי על ערך, מוסיפים לרשימה חדשה
