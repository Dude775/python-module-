def add_entry(text):
    with open("data.txt", "a") as f:
        f.write(text + "\n")

def read_entries():
   with open("data.txt", "r") as f:
       return f.readlines()
