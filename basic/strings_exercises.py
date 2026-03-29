#  🧪 [Python Basics] Hands-On Lab 1.4 – Working with Strings in Python

# 1) יצרת מחזורוזות עם גרשיים כפולים - "Hello, World!" 

lang = "Hello, World!"
print(lang)

# 2) יצרת מחרזות עם גרש בודד

field = 'Hello, World!'
print(field)

# 3) מחרוזת מרובת שורות

multi = """line one
line two"""
print(multi)

# 4)  f-strings עם משתנים
results = 7 / 2
print(f"Results: {results}")    

# 5) f-strings ביטוי בתוך  - ישירות אליו

print(f"Results: {7 / 2}")

# 6) strip מסיר רווחים משני הצדדים  | strip() מחזיר עותק חדש בלי הרווחים — לא משנה את המקור
course = "  Pthon For DevOps  "
print(course.strip())

# 7) upper הופך הכל לאותיות גדולות  | — מחזיר עותק חדש, המקור לא משתנה

course_title = "Python for DevOps"
print(course_title.upper())

# 8) – lower הופך הכל לאותיות קטנות | אותו עיקרון כמו upper, רק הפוך

print(course_title.lower())

# 9) – startswith בודק איך המחרוזת מתחילה | מחזיר True או False 
filename = "file.yaml"
print(filename.startswith("file"))

# 10) – endswith בודק איך המחרוזת נגמרת | שימושי לבדוק סיומות קבצים
print(filename.endswith(".yaml"))

# 11) – split חותך מחרוזת לרשימה  |  לפי איזה תו לחתוך  |  כל חתיכה נכנסת כאיבר ברשימה

path = "/user/local/bin"
parts = path.split("/")
print(parts)

# 12) join מחבר רשימה חזרה למחרוזת |  split לתווים שבחרנו
print("\\".join(parts))


# 13) – שרשור מחרוזות עם + פשוט מדביקים עוד טקסט בסוף עם סימן

path = "/user/local/bin"
path = path + "/python"
print(path)

# 14) – indexing — גישה לתו לפי מיקום (מתחיל מ - 0 )  -   לזכור: +  לזכור: מצגי תמיד את ה START | לא מציג END

print(path[0])

# 15) חיתוך חלקים לפי טווח במחרוזת:

path = "/user/local/bin"
print(path[3:10])

# 16) – len מחזיר את אורך המחרוזת  | 
#  בקיצור סופר את התווים שיש בשורה כולל אותיות, משפרים, רווחים, סימני פיסוק, סימנים מיוחדי

print(len(path))

# 17) "immutable" = מחרוזת לא ניתנת לשינוי ישיר

try: 
    path[0] = "X"
except TypeError as e:
    print(e)
    
    