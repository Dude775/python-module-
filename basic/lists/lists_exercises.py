# 1. Create a list of servers

my_servers = [
    "cache01",
    "api01",
    "db01"
]

# 2. Print the list
print(my_servers)


# 3. Print the first server
print(my_servers[0])

# 4. Print the second server
print(my_servers[1])

# 5. Print the last server using negative index
print(my_servers[-1])

# 6. Print the second from the end
print(my_servers[-2])

# # 7. servee not in list
# print(my_servers[5])

# 8. Add a new server (5) to the list
servers_five = [
    "cache01",
    "api01",
    "db01",
    "web01",
    "proxy01"
]
print(servers_five)

# Exercise 9 - Basic Slicing
print(servers_five[0:2])

# Exercise 10 - Slicing from the middle
print(servers_five[1:])

# Exercise 11 - Slicing with negative indexes
print(servers_five[-2:])

# Exercise 12 - Step
print(servers_five[0:5:2])

# # Exercise 12 - Step - new option
print(servers_five[::2])

# Exercise 13 - Different step 
print(servers_five[::3])

# Exercise 14 - Mixed types list
mixed_list = [
    "cache01",
    42,
    3.14,
    True,
    None
]
print(mixed_list)

# Exercise 15 - Slicing doesn't change the original

mixed_list = [
    "cache01",
    42,
    3.14,
    True,
    None
]
new_list = mixed_list[:2]
print("New list:", new_list)
print("Original list:", mixed_list)