from todo import add_task, list_tasks

add_task("Initial task by A")
add_task("B: test push")

tasks = list_tasks()
for t in tasks:
    print(t)

print("Hi there!!!!!!!!!")
print("Run by A")

def update_first_task(new_task):
    with open("tasks.txt", "r") as f:
        lines = f.readlines()
    lines[0] = new_task + "\n"
    with open("tasks.txt", "w") as f:
        f.writelines(lines)


def count_tasks():
    with open("tasks.txt", "r") as f:
        return len(f.readlines())
    
    print("Total tasks:", count_tasks())
add_task("A iteration task")

from todo import list_tasks

for task in list_tasks():
    print(task)