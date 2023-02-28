Import("env")

import os
import git
import time
import subprocess
import shutil
import json

try:
    import mysql.connector
except ImportError:
    env.Execute("$PYTHONEXE -m pip install mysql-connector-python")
    import mysql.connector
"""
try:
    import git
except ImportError:
    env.Execute("$PYTHONEXE -m pip install GitPython")
    import git
"""

BUILDNR = int(round(time.time()))
VERSION_FILE = "version.h"
CONFIG_FILE = "config.h"
BUILD_DIR = "build/"
GITVERSION = ""
BOARD = env['BOARD']
API_URL = ""
FILENAME = ""
cwd = os.path.abspath(os.getcwd())
print(cwd)
r = git.repo.Repo(cwd)
print(r)
GITVERSION = r.git.describe("--tag")
print(GITVERSION)
    

mydb = mysql.connector.connect(
  host="192.168.178.49",
  user="olaf",
  password="10o10s60",
  database="esp32"
)

mycursor = mydb.cursor()

sql = "INSERT INTO boards (IP_Address) VALUES (%s)"
val = ("192.168.178.200",)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

