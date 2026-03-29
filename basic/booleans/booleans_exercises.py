# ============================================
# Lab 3.0 - Working with Booleans and Comparisons
# ============================================

# תרגיל 1 
print(1)
print(10 == 10) # true
print(10 == 5)# false

# תרגיל 2
print(2)
print(10 != 5)
print(10 != 10)

# תרגיל 3
print(3)
print(10 < 3) #false
print(10 > 5) #true

# תרגיל 4
print(4)
print(5 < 10) #true
print(10 < 3) #false

# תרגיל 5 
print(5)
print(10 >= 10)#true
print(10 >= 5)#true

# 6
print(6)
print(5 <= 10)#true
print(5 <= 5)#true

#7 
print(7)
print("DAVID" != "david") #true
print("DAVID" !="DAVID") #false

# ! ============================
#חלק 3 — שימוש ב־Boolean עם משתנים

#8

is_equal = (100 == 100)
print(8)
print(is_equal)
print(type(is_equal))

#9
is_greater = (50 > 100)
print(9)
print(is_greater)

# ! === Part 4 - השוואת מבני נתונים ===

#10
list_a = [1, 2, 3]
list_b = [1, 2, 3]
print(10)
print(list_a == list_b)

# ! === Part 5 - שימוש ב-is ===
#11
print(11)
print(list_a is list_b)

#12
list_c = list_a
print(12)
print(list_c is list_a)

# !  === Part 6 - == מול is ביחד ===
#13
print(13)
print(list_a == list_b)
print(list_a is list_b)
print(list_a == list_c)
print(list_a is list_c)

# ! === Part 8 - שגיאה נפוצה ===
# 15
x = 5
print(15)
print(x == 5)