# Lab 4.2 - Enumerate & Zip Practice

# === חלק 1: enumerate ===

# תרגיל 1 - הדפס כל שם עם אינדקס
names = ["Alice", "Bob", "Charlie"]
for idx, name in enumerate(names):
    print(f"{idx}: {name}")
# enumerate(names) - עוטפת רשימה ומחזירה זוג (מספר סידורי, ערך) בכל סיבוב
# for idx, name - מפרקים את הזוג: idx = מספר, name = שם

# תרגיל 2 - הדפס שרתים עם אינדקס מ-1
servers = ["app-01", "app-02", "app-03"]
for idx, server in enumerate(servers, start=1):
    print(f"{idx}: {server}")
# start=1 - אומר לenumerate להתחיל לספור מ-1 במקום מ-0

# תרגיל 3 - הדפס רק שגיאות באינדקס זוגי
errors = ["disk full", "timeout", "connection lost"]
for idx, error in enumerate(errors):
    if idx % 2 == 0:
        print(f"{idx}: {error}")
# idx % 2 == 0 - בודק אם האינדקס מתחלק ב-2 בלי שארית = זוגי

# תרגיל 4 - הדפס פורטים עם אינדקס גדול מ-1
ports = [22, 80, 443, 8080]
for idx, port in enumerate(ports):
    if idx > 1:
        print(f"{idx}: {port}")
# idx > 1 - מדלג על אינדקסים 0 ו-1, מדפיס רק מ-2 והלאה

# תרגיל 5 - הדפס User #index: name
users = ["admin", "dev", "ops"]
for idx, user in enumerate(users):
    print(f"User #{idx}: {user}")
# פשוט מוסיפים טקסט קבוע "User #" לפני האינדקס ב-f-string

# תרגיל 6 - הדפס רק את הקובץ האחרון
files = ["log1.txt", "log2.txt", "log3.txt"]
for idx, file in enumerate(files):
    if idx == len(files) - 1:
        print(f"{idx}: {file}")
# len(files) - 1 = האינדקס האחרון ברשימה (3 פריטים = אינדקס 2)

# תרגיל 7 - הדפס הכל מלבד הראשון
regions = ["us-east-1", "eu-west-1", "ap-south-1"]
for idx, region in enumerate(regions):
    if idx != 0:
        print(f"{idx}: {region}")
# idx != 0 - מדלג על האיבר הראשון (אינדקס 0)

# תרגיל 8 - הדפס שירותים עם אינדקס מ-1
services = ["nginx", "redis", "postgres"]
for idx, service in enumerate(services, start=1):
    print(f"{idx}: {service}")
# זהה לתרגיל 2 - start=1 מתחיל ספירה מ-1

# תרגיל 9 - הדפס משימות באינדקס אי-זוגי
tasks = ["backup", "cleanup", "monitoring"]
for idx, task in enumerate(tasks):
    if idx % 2 != 0:
        print(f"{idx}: {task}")
# idx % 2 != 0 - שארית מחילוק ב-2 לא אפס = אי-זוגי

# תרגיל 10 - עצור כשאינדקס מגיע ל-2
containers = ["c1", "c2", "c3", "c4"]
for idx, container in enumerate(containers):
    if idx == 2:
        break
    print(f"{idx}: {container}")
# break - שובר את הלולאה לגמרי כשהתנאי מתקיים

# === חלק 2: zip ===

# תרגיל 11 - הדפס host עם IP
hosts = ["host1", "host2", "host3"]
ips = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]
for host, ip in zip(hosts, ips):
    print(f"{host} -> {ip}")
# zip(hosts, ips) - לוקחת איבר ראשון מכל רשימה ויוצרת זוג, אז שני, וכו'

# תרגיל 12 - הדפס User <name> has ID <id>
users = ["alice", "bob", "charlie"]
ids = [101, 102, 103]
for user, id in zip(users, ids):
    print(f"User {user} has ID {id}")
# אותו zip - מחבר שם למספר מזהה

# תרגיל 13 - התאמה בין service לport
services = ["nginx", "redis", "postgres"]
ports = [80, 6379, 5432]
for service, port in zip(services, ports):
    print(f"{service} -> port {port}")
# zip מחבר כל שירות לפורט שלו לפי סדר

# תרגיל 14 - חבר region+zone
regions = ["us-east-1", "eu-west-1"]
zones = ["a", "b"]
for region, zone in zip(regions, zones):
    print(f"{region}{zone}")
# פשוט מדביקים את שני הערכים ביחד ב-f-string

# תרגיל 15 - הדפס רק containers שרצים
containers = ["c1", "c2", "c3"]
statuses = ["running", "stopped", "paused"]
for container, status in zip(containers, statuses):
    if status == "running":
        print(f"{container}: {status}")
# אחרי ה-zip מוסיפים if שבודק רק סטטוס מסוים

# תרגיל 16 - הדפס שלושה ערכים יחד
files = ["file1", "file2"]
sizes = [100, 200]
types = ["txt", "log"]
for file, size, type in zip(files, sizes, types):
    print(f"{file} | {size}KB | {type}")
# zip עובד גם עם 3 רשימות - מפרקים ל-3 משתנים

# תרגיל 17 - כמה איברים יודפסו
names = ["serviceA", "serviceB", "serviceC"]
versions = ["1.0", "2.0"]
count = 0
for name, version in zip(names, versions):
    print(f"{name}: v{version}")
    count += 1
print(f"Total: {count}")
# zip עוצרת ברשימה הקצרה ביותר! 3 שמות + 2 גרסאות = 2 תוצאות בלבד

# תרגיל 18 - הדפס שלישיית DB
dbs = ["mysql", "postgres", "mongo"]
ports = [3306, 5432, 27017]
hosts = ["db1", "db2", "db3"]
for db, port, host in zip(dbs, ports, hosts):
    print(f"{db} on {host}:{port}")
# zip עם 3 רשימות - כל סיבוב מפרק שלישייה

# תרגיל 19 - הדפס רק משימות שנכשלו
tasks = ["build", "test", "deploy"]
durations = [5, 10, 3]
statuses = ["ok", "ok", "failed"]
for task, duration, status in zip(tasks, durations, statuses):
    if status == "failed":
        print(f"FAILED: {task} (took {duration}s)")
# zip עם 3 רשימות + if שמסנן רק סטטוס "failed"

# תרגיל 20 - הדפס הכל בשורה אחת
users = ["admin", "dev"]
roles = ["full-access", "read-only"]
regions = ["us", "eu"]
for user, role, region in zip(users, roles, regions):
    print(f"{user} | {role} | {region}")
# zip עם 3 רשימות - מדפיס כל שלישייה בשורה עם מפריד |
