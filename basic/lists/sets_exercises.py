# 1- port lists

ports_list = [80, 443, 8080, 22, 21]    

# 2- convert list to set + 3 print

unique_ports = set(ports_list)
print(ports_list,"type:",type(ports_list)) 
print(unique_ports,"type:",type(unique_ports))

# 4 Create another Set "server_names"
server_names = {"web01", "web02", "web03"}
print(server_names)

# 5  Membership_cheak  
print(22 in unique_ports)

# 6  server names
print(22 in server_names)

# Exercise 7 – Add an element

unique_ports.add(3000)
print(unique_ports)


# Exercise 8 – הדפסת ה-Set לאחר הוספה

# Exercise 9 – הסרת איבר + 10 

unique_ports.remove(22)


# Exercise 10 – Try to remove again (will fail)
try:
    unique_ports.remove(22)
except KeyError as e:
    print(f"KeyError: {e}")
    
# Exercise 11 – Discard (safe remove)
unique_ports.discard(22)

# 12

valid_set = {(1, 2), (3, 4)}
print(valid_set)

#13Exercise 13 – ניסיון Set לא חוקי

try:
    invalid_set = {[1, 2], [3, 4]}
except TypeError as e:
    print(e)

# Exercise 14 – Remove duplicates from a list

duplicated = [1, 2, 3, 4, 5, 1, 2]
noduplicate = set(duplicated)
print(duplicated)
print(noduplicate)

