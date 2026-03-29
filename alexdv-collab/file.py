def delete_last_entry():
    with open("data.txt", "r") as f:
        lines = f.readlines()
    with open("data.txt", "w") as f:
        f.writelines(lines[:-1])
print("Hi Daniel")
