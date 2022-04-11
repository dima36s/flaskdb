from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///CGF.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CREATE TABLE
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.TEXT)
    wrs_name = db.Column(db.TEXT)
    MAC = db.Column(db.TEXT)
    user = db.Column(db.TEXT)
    departments = db.Column(db.TEXT)
    mthb = db.Column(db.TEXT)
    cpu = db.Column(db.TEXT)
    ram = db.Column(db.TEXT)
    video = db.Column(db.TEXT)
    displays = db.Column(db.TEXT)
    hhd = db.Column(db.INTEGER)
    os_version = db.Column(db.TEXT)
    nomachine = db.Column(db.TEXT)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    additional_info = db.Column(db.TEXT)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


db.create_all()

# CREATE USERS
new_user = Users(id=1, ip_address="192.168.45.101", wrs_name="WRSWIN5101", MAC="2C:4D:54:50:2B:A6", user='a.mishenin',
                 departments="shots", mthb="Asustekcomputer", cpu="Intel(R)", ram="32 GB", video="GeForceGTX10603G",
                 displays="unknown",
                 hhd=72, os_version='Windows 10.0.17763', nomachine="not used", date="2022.04.06", additional_info=""
                 )
db.session.add(new_user)
db.session.commit()


class DDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()  # создаем класс курсора
        self.__db.sqlite3.connect("CGF.db")
        self.__cur.fetchall()

    # def create_db(self):
    #     self.__cur.execute('''CREATE TABLE IF NOT EXISTS user(
    #    wrs_user TEXT,
    #    user TEXT,
    #    departments TEXT,
    #    mtnb TEXT,
    #    cpu TEXT,
    #    ram TEXT,
    #    video TEXT,
    #    date DATETIME,
    #    changes INT,
    #    ip_address INT,
    #    MAC INT ,
    #    displays TEXT,
    #    disk_usage INT,
    #    additional_info TEXT,
    #    os_version TEXT,
    #    nomachine TEXT
    #    )
    #
    #     ''')
    #     self.__db.commit()
    #     self.__db.close()

    def insert(self, wrs_user, user, departments, mtnb, cpu, ram, video, date, changes, ip_address, MAC, display,
               disk_usage,
               additional_info, os_version, nomachine):
        self.__cur.cursor()
        # the NULL parameter is for the auto-incremented id
        self.__cur.execute("INSERT INTO CGF VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                           (
                               wrs_user, user, departments, mtnb, cpu, ram, video, date, changes, ip_address, MAC,
                               display,
                               disk_usage,
                               additional_info, os_version, nomachine))
        self.__db.commit()
        self.__db.close()

    def view(self):
        self.__db.sqlite3.connect("CGF.db")
        self.__cur.cursor()
        self.__cur.execute("SELECT * FROM CGF")
        self.__cur.fetchall()
        self.__db.close()
        return self.__cur.fetchall()

    def search(self, wrs_user="", user="", departments="", mtnb="", cpu="", ram="", video="", date="", changes="",
               ip_address="",
               MAC="", display="", disk_usage="",
               additional_info="", os_version="", nomachine=""):
        self.__db.sqlite3.connect("CGF.db")
        self.__cur.cursor()
        self.__cur.execute(
            "SELECT * FROM CGF WHERE wrs_user = ? OR user = ? OR departments = ? OR mtnb=? OR cpu=? OR ram=? OR video=? OR data=? OR changes=?OR ip_address = ? OR MAC=?"
            "OR display=? OR disk_usage=? OR additional_info=? OR os_version=? OR nomachine=?",
            (wrs_user, user, departments, mtnb, cpu, ram, video, date, changes, ip_address, MAC, display, disk_usage,
             additional_info, os_version, nomachine))
        self.__cur.fetchall()
        self.__db.close()
        return self.__cur.fetchall()

    def delete(self, id):
        self.__db.sqlite3.connect("CGF.db")
        self.__cur.cursor()
        self.__cur.execute("DELETE FROM CGF WHERE id = ?", (id,))
        self.__db.commit()
        self.__db.close()

    def update(self, id, wrs_user, user, departments, mtnb, cpu, ram, video, date, changes, ip_address, MAC, display,
               disk_usage,
               additional_info, os_version, nomachine):
        self.__db.sqlite3.connect("CGF.db")
        self.__cur.cursor()
        self.__cur.execute(
            "UPDATE CGF SET wrs_user = ?, user = ?, departments = ?, mtnb=?,cpu=?,ram=?,video=?,date=?,changes=?,ip_address=?,MAC=?,display=?,"
            "disk_usage=?,additional_info=?,os_version=?,nomachine=? WHERE id = ?",
            (
                wrs_user, user, departments, mtnb, cpu, ram, video, date, changes, ip_address, MAC, display,
                disk_usage,
                additional_info, os_version, nomachine, id))
        self.__db.commit()
        self.__db.close()
