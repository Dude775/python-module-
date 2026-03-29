# Exercise 1 – Create two sets
# קבוצת חברים וקבוצת חברים בחו"ל
friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

# Exercise 2 – Print both sets
print(f"Friends: {friends}")
print(f"Abroad: {abroad}")

# Exercise 3 – difference: who is local?
# מי נמצא ב-friends אבל לא ב-abroad — כלומר מי נשאר בארץ
local = friends.difference(abroad)
print(f"\nLocal friends: {local}")

# Exercise 4 – Reverse difference
# מי ב-abroad אבל לא ב-friends — אף אחד, כי כולם ב-abroad גם ב-friends
print(f"Abroad but not friends: {abroad.difference(friends)}")

# Exercise 5 – Create an empty set
# שים לב: {} יוצר dict ריק, לא set. חייבים set()
empty = set()
print(f"\nEmpty set: {empty}")

# Exercise 6 – Create new sets
local = {"Rolf"}
abroad = {"Bob", "Anne"}

# Exercise 7 – Union with method
# מאחד את שתי הקבוצות — כל החברים ביחד
friends = local.union(abroad)
print(f"\nAll friends (union): {friends}")

# Exercise 8 – Union with operator
# | עושה בדיוק אותו דבר כמו union()
print(f"All friends (|): {local | abroad}")

# Exercise 9 – Create new sets for intersection
art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

# Exercise 10 – Intersection with method
# מי לומד גם אומנות וגם מדעים — רק המשותפים
both = art.intersection(science)
print(f"\nCommon students (intersection): {both}")

# Exercise 11 – Intersection with operator
# & עושה בדיוק אותו דבר כמו intersection()
print(f"Common students (&): {art & science}")

# Exercise 12 – Membership check (True)
print(f"\nIs Bob in art? {'Bob' in art}")

# Exercise 13 – Membership check (False)
print(f"Is Anne in art? {'Anne' in art}")

# Exercise 14 – F-string with intersection result
print(f"\nCommon elements: {both}")

# Exercise 15 – Summary: all three operations in sequence
print(f"\n--- Summary ---")
print(f"Local friends: {friends.difference(abroad)}")
print(f"All friends: {local.union(abroad)}")
print(f"Common interests: {art & science}")
