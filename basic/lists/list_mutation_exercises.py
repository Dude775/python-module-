# Exercise 1 – יצירת רשימה

# Exercise 1 – Create a deployment targets list
# יוצרים רשימה עם סוגריים מרובעים [] ושמים בפנים 3 שרתים
# כל איבר מופרד בפסיק
deployment_targets = ["us-east-1", "eu-west-1", "ap-southeast-1"]

# Exercise 2 – Print the list
# print על רשימה מדפיס את כל האיברים כולל הסוגריים
print(deployment_targets)

# Exercise 3 – Access the first element by index
# אינדקס מתחיל מ-0, אז [0] זה האיבר הראשון
print(deployment_targets[0])

# Exercise 4 – Access the second element
# [1] זה האיבר השני — תמיד מספר המיקום פחות 1
print(deployment_targets[1])

# Exercise 5 – Append a new target
# append() תמיד מוסיף לסוף — אין בחירה לאן
deployment_targets.append("us-west-2")

# Exercise 6 – Print after append
# עכשיו יש 4 איברים — us-west-2 נוסף בסוף
print(deployment_targets)

# Exercise 7 – Append another target
# מוסיפים עוד יעד — שוב נכנס לסוף הרשימה
deployment_targets.append("af-south-1")

# Exercise 8 – Modify an existing value by index
# List היא mutable — אפשר לגשת לאינדקס ולדרוס את הערך
# מחליפים את eu-west-1 (אינדקס 1) ב-eu-central-1
deployment_targets[1] = "eu-central-1"

# Exercise 9 – Print after modification
# הרשימה השתנתה במקום — לא נוצרה רשימה חדשה
print(deployment_targets)

# Exercise 10 – Negative index — last element
# [-1] תמיד מצביע על האיבר האחרון, לא משנה כמה יש ברשימה
print(deployment_targets[-1])

# Exercise 11 – Negative index — second from the end
# [-2] זה אחד לפני האחרון
print(deployment_targets[-2])

# Exercise 12 – Change the first element
# דורסים את הערך באינדקס 0 — הערך הישן נעלם
deployment_targets[0] = "us-east-2"

# Exercise 13 – List length with len()
# len() סופר כמה איברים יש ברשימה — לא אינדקס, אלא כמות
print(len(deployment_targets))

# Exercise 14 – Full print after all changes
# הרשימה עברה append פעמיים ושינוי ערך פעמיים
print(deployment_targets)

# Exercise 15 – Summary: append + modify + print
# מוסיפים ערך חדש
deployment_targets.append("sa-east-1")
# משנים ערך קיים
deployment_targets[2] = "ap-northeast-1"
# מדפיסים את התוצאה הסופית
print(deployment_targets)
