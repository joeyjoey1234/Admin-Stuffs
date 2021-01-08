import os
import sqlite3
path = os.environ['USERPROFILE']

connection = sqlite3.connect('{}\Documents\Ps-wins.accdb'.format(path))
cursor = connection.cursor()
cursor.execute("SELECT * FROM Contents;")
results = cursor.fetchall()
for x in results:
    print(x)