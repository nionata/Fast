import pymysql
from app import app
from flaskext.mysql import MySQL
from env import isProd, getVar

mysql = MySQL(cursorclass=pymysql.cursors.DictCursor)

# MySQL configurations

user = 'root'
password = 'password'
host = 'db'
db = 'fast'
dbUrl = getVar('CLEARDB_DATABASE_URL')
if isProd() and dbUrl:
    user, password, host, db = re.match('mysql://(.*?):(.*?)@(.*?)/(.*)', dbUrl).groups()

app.config['MYSQL_DATABASE_USER'] = user
app.config['MYSQL_DATABASE_PASSWORD'] = password
app.config['MYSQL_DATABASE_DB'] = db
app.config['MYSQL_DATABASE_HOST'] = host

mysql.init_app(app)
# conn = mysql.connect()

# def getCursor():
#     return conn.cursor()

# def commit():
#     conn.commit()