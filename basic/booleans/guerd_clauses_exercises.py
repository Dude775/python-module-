#Lab 3.4 - Guard Clauses and Input Validation

# 1 
def process_data_guarded(data):
    print(data)
# 2
process_data_guarded([])
process_data_guarded([1, 2, 3])

# 3+4+5
def process_data_guarded(data):
    print(f"processing {len(data)} items...")
    print("processing")
    
process_data_guarded([1, 2, 3])
# === Part 3 - Guard Clause בסיסי ===

# Exercise 6+7 - בדיקה מוקדמת לפני עיבוד
# Guard Clause = בדיקה בתחילת הפונקציה שעוצרת אם הקלט לא תקין
# not data מחזיר True עבור None, רשימה ריקה [], ו-False עבור כל דבר עם תוכן
# return עוצר את הפונקציה מיד - לא ממשיך לקוד מתחת
def process_data_guarded(data):
    if not data:
        print("no data provided")
        return
    print(f"processing {len(data)} items...")
    print("processed")

process_data_guarded(None)       # no data provided
process_data_guarded([])         # no data provided
process_data_guarded([1, 2, 3])  # processing 3 items...

# === Part 4+5 - בדיקת טיפוס עם isinstance ===

# Exercise 8+9+10+11+12 - הגנה על סוג הקלט
# isinstance(data, list) בודק האם data הוא מטיפוס list
# ככה מונעים מצב שמישהו שולח string או מספר במקום רשימה
# f-string עם type() מראה למשתמש מה הוא שלח ומה היה צריך
def process_data_guarded(data):
    if not data:
        print("no data provided")
        return
    if not isinstance(data, list):
        print(f"invalid value type for data provided {type(data)} required list")
        return
    print(f"processing {len(data)} items...")
    print("processed")

# === Part 6+7 - בדיקה מלאה ===

# Exercise 13+14+15 - בודקים את כל המקרים
process_data_guarded([])         # no data provided
process_data_guarded([1, 2, 3])  # processing 3 items... processed
process_data_guarded(None)       # no data provided
process_data_guarded("ABC")      # invalid value type... <class 'str'>
process_data_guarded(10)         # invalid value type... <class 'int'>