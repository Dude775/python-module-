# === Part 1 - שימוש ב-in בתוך if ===

# Exercise 1 - סט של סרטים
movies = {"The Matrix", "Green Book", "Her"}

# Exercise 2 - קלט מהמשתמש
user_movie = input("Enter a movie you have watched recently: ")

# Exercise 3 - בדיקה האם הסרט בסט עם תנאי
# in בתוך if - במקום לבדוק כל סרט בנפרד, בודקים שייכות לאוסף שלם
if user_movie in movies:
    print(f"I've watched {user_movie} too!")
else:
    print("I haven't watched that yet.")

# === Part 2 - משחק מספר קסם ===

# Exercise 4 - מספר סודי קבוע
magic_number = 7

# Exercise 5+6 - שואלים את המשתמש אם רוצה לשחק
user_input = input("Enter Y if you would like to play: ")

# Exercise 7+8 - תנאי מקונן: if בתוך if
# קודם בודקים אם המשתמש רוצה לשחק, ורק אז מבקשים ניחוש
if user_input == "Y":
    # int() ממיר את הקלט ממחרוזת למספר - בלי זה אי אפשר להשוות מספרים
    guess = int(input("Guess our number: "))
    if guess == magic_number:
        print("You guessed correctly!")
    else:
        print("Sorry, it's wrong.")

# === Part 3 - קלט מרובה עם tuple ===

# Exercise 9+10 - מאפשרים גם y קטנה וגם Y גדולה
# tuple עם כל האפשרויות המותרות - in בודק את כולן בשורה אחת
# אפשרות חלופית: user_input.lower() == "y"
user_input = input("Enter Y if you would like to play: ")

if user_input in ("y", "Y"):
    guess = int(input("Guess our number: "))
    if guess == magic_number:
        print("You guessed correctly!")
    else:
        print("Sorry, it's wrong.")

# === Part 4+5 - בדיקת קרבה עם abs() ===

# Exercise 11+12+13 - הגרסה המלאה של המשחק
# abs() מחזיר ערך מוחלט - הופך מספר שלילי לחיובי
# ככה לא צריך לבדוק גם +1 וגם -1 בנפרד
user_input = input("Enter Y if you would like to play: ")

if user_input in ("y", "Y"):
    guess = int(input("Guess our number: "))
    if guess == magic_number:
        print("You guessed correctly!")
    elif abs(guess - magic_number) == 1:
        # אם ההפרש המוחלט בין הניחוש למספר הוא 1, המשתמש היה קרוב
        # למשל: ניחש 6 או 8 כשהמספר הוא 7
        print("You were off by one.")
    else:
        print("Sorry, it's wrong.")