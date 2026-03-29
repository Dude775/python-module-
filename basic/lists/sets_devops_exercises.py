# Exercise 1 – Create required_packages from a list
# יוצרים set מתוך list — הכפילות של "pip" תיעלם אוטומטית
required_packages = set(["python3", "pip", "requests", "boto3", "pip"])

# Exercise 2 – Print the set
print(required_packages)

# Exercise 3 – Check if "requests" is in the set
# in מחזיר True כי requests קיים ב-set
print("requests" in required_packages)

# Exercise 4 – Check if "ansible" is in the set
# in מחזיר False כי ansible לא קיים
print("ansible" in required_packages)

# Exercise 5 – F-string membership check
print(f"Is 'requests' required? {'requests' in required_packages}")

# Exercise 6 – F-string membership check
print(f"Is 'ansible' required? {'ansible' in required_packages}")

# Exercise 7 – Add a package
# add() מוסיף איבר ל-set — שים לב: add ולא append
required_packages.add("paramiko")

# Exercise 8 – Safe remove with discard
# discard() מסיר בלי לזרוק שגיאה אם הערך לא קיים
required_packages.discard("pip")

# Exercise 9 – Print after changes
print(required_packages)

# Exercise 10 – Create installed_packages
installed_packages = {"docker", "python3", "pip"}

# Exercise 11 – Missing packages
# מה שנדרש אבל לא מותקן — minus מחזיר מה שב-required ולא ב-installed
missing_packages = required_packages - installed_packages

# Exercise 12 – Extra packages
# מה שמותקן אבל לא נדרש — אולי אפשר למחוק
extra_packages = installed_packages - required_packages

# Exercise 13 – Common packages
# מה שגם נדרש וגם מותקן — & זה intersection
common_packages = required_packages & installed_packages

# Exercise 14 – Print results with f-strings
print(f"\nMissing packages: {missing_packages}")
print(f"Extra packages: {extra_packages}")
print(f"Common packages: {common_packages}")

# Exercise 15 – Summary
# סיכום מלא — תמונת מצב של החבילות על השרת
print(f"\n--- Package Audit Summary ---")
print(f"Missing packages: {missing_packages}")
print(f"Extra packages: {extra_packages}")
print(f"Common packages: {common_packages}")