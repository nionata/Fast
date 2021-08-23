import pymysql
from app import app
from flaskext.mysql import MySQL
from env import isProd, getVar

mysql = MySQL(cursorclass=pymysql.cursors.DictCursor)

# MySQL configurations

if isProd():
    # getVar('CLEARDB_DATABASE_URL')
    print(1)
else:
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
    app.config['MYSQL_DATABASE_DB'] = 'fast'
    app.config['MYSQL_DATABASE_HOST'] = 'db'

mysql.init_app(app)
# conn = mysql.connect()

# def getCursor():
#     return conn.cursor()

# def commit():
#     conn.commit()