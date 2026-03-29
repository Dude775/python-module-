# === Part 1 - בדיקת שייכות ברשימה ===

# Exercise 1 - יצירת רשימת חברים
friends = ["Rolf", "Bob", "Jen"]

# Exercise 2 - בדיקה האם שם קיים ברשימה
# in עובר על כל איבר ברשימה ובודק האם יש התאמה
print("Jen" in friends)   # True

# Exercise 3 - בדיקת שם שלא קיים
print("Anne" in friends)  # False

# === Part 2 - שימוש ב-Set לבדיקת שייכות ===

# Exercise 4 - יצירת סט של סרטים
# Set במקום List כי לא צריכים סדר ולא רוצים כפילויות
movies = {"The Matrix", "Green Book", "Her"}

# Exercise 5 - קלט מהמשתמש
user_movie = input("Enter a movie you have watched recently: ")

# Exercise 6 - בדיקה האם הסרט בסט
print(user_movie in movies)

# === Part 3 - in עם מחרוזות ===

# Exercise 7 - בדיקת תת-מחרוזת
# in על string בודק האם רצף תווים מופיע בתוך מחרוזת
print("rix" in "The Matrix")   # True

# Exercise 8 - תת-מחרוזת שלא קיימת
print("xyz" in "The Matrix")   # False

# === Part 4 - שילוב in עם if ===

# Exercise 9+10 - תנאי על בדיקת שייכות
# משלבים את in בתוך if - במקום להשוות ערך אחד, בודקים שייכות לאוסף שלם
user_movie = input("Enter a movie you have watched recently: ")

if user_movie in movies:
    print("You've already watched this movie.")
else:
    print("You should watch this movie!")

# === Part 5 - התנהגות Set עם כפילויות ===

# Exercise 11+12 - Set מסיר כפילויות אוטומטית
# גם אם מכניסים את אותו ערך פעמיים, Set שומר רק עותק אחד
movies_with_dupes = {"The Matrix", "Her", "The Matrix", "Her"}
print(movies_with_dupes)  # רק שני ערכים - הכפילויות נעלמו

# === Part 7 - חיזוק הבנה ===

# Exercise 14 - בדיקה נוספת עם ערך קיים
print("Rolf" in friends)  # True

# Exercise 15 - בדיקה עם ערך שלא קיים
print("Charlie" in friends)  # False