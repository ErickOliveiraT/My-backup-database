import mysql.connector
import secrets
import os

main_dir = 'D:\\Backups'

mydb = mysql.connector.connect(
  host = secrets.host,
  user = secrets.user,
  passwd = secrets.password,
  database = secrets.database
)

mycursor = mydb.cursor()

def bytesToMB(_bytes):
	return _bytes/pow(1024,2)

def get_size(folder):
    total_size = 0
    start_path = main_dir+'\\'+folder
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return round(bytesToMB(total_size),2)

def insertCloud(name, quota, server, username):
	sql = "INSERT INTO clouds (name, quota, server, username) VALUES (%s,%s,%s,%s)"
	cloud_data = (name,quota,server,username)
	mycursor.execute(sql, cloud_data)
	mydb.commit()

def insertDir(name,size,dvd_burned,cloud_id):
	sql = "INSERT INTO backup_dirs (dir,size,dvd_burned,cloud_id) VALUES (%s,%s,%s,%s)"
	dir_data = (name,size,dvd_burned,cloud_id)
	mycursor.execute(sql, dir_data)
	mydb.commit()

for folder in os.listdir(main_dir):
    #folders.append(folder)
    size = get_size(folder)
    print("{} - {}".format(folder,size))
    insertDir(folder,size,'true',1)