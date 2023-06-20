import zipfile
import json
import sqlite3
from pathlib import Path
connection = sqlite3.connect('C:\DB_sqlite\hw1.db')
cursor = connection.cursor()
create_table = """
CREATE TABLE IF NOT EXISTS okved(
    code TEXT,
    parent_code TEXT, 
    section TEXT, 
    name TEXT, 
    comment TEXT
 )
"""
cursor.execute(create_table)
connection.commit()
with zipfile.ZipFile('C:\Python\dz1\okved_2.json.zip', 'r') as zipobj:
    file_names = zipobj.namelist()
    for name in file_names:
        zipobj.extract(name)
        with open(name, 'r',encoding='utf-8') as f:
            val = json.loads(f.read())
            print(type(val))
    path = Path(name)
    path.unlink()
insert_rows = """
INSERT INTO okved (code, parent_code, section, name, comment)
VALUES (:code, :parent_code, :section, :name, :comment)
"""
cursor.executemany(insert_rows, val)
connection.commit()
cursor.close()
connection.close()

