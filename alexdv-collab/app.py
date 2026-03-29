from utils import add_entry, read_entries

add_entry("Project initialized by A")
add_entry("B: first change")
add_entry("C: first change")

for line in read_entries():
    print(line)
add_entry("A-Master: second change")
add_entry("C-Daniel: second change")
add_entry("B-David: second change")
print("Executed by A")
print("Executed by B")
print("Executed by C")
print("GOOD WEEK")