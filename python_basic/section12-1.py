# Section 12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime
from sqlite3.dbapi2 import connect

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now : ', now)

nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDateTime : ', nowDateTime)

# sqlite3 버전
print('sqlite3.version : ', sqlite3.version)
print('sqlite3.sqlite_version : ', sqlite3.sqlite_version)

# DB 생성 및 Auto Commit(Rollback)
conn = sqlite3.connect('/Users/yoonseo/Desktop/python/python_basic/resource/database.db', isolation_level=None)

# Cursor
c = conn.cursor()
print('Cursor Type : ', type(c))

# 테이블 생성(Data Type : TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, \
    username text, email text, phone text, website text, regdate text)")

# 데이터 삽입
c.execute("INSERT INTO users VALUES(1, 'Kim', 'Kim@naver.com', '010-2222-2222',\
    'kim.com', ?)", (nowDateTime,))
c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", (2, 'Park', 'park@mgail.com', '010-1341-3214', 'park.ac.kr', nowDateTime))

# Many 삽입(튜플, 리스트)
userList = (
    (3, 'Lee', 'Lee@nav.com', '010-3154-3155', 'Lee.com', nowDateTime),
    (4, 'Cho', 'Cho@dav.com', '010-3999-3155', 'Cho.com', nowDateTime),
    (5, 'PPP', 'PPP@qav.com', '010-7774-1155', 'PPP.com', nowDateTime),
)

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", userList)

# 테이블 데이터 삭제
# conn.execute("DELETE FROM users")
# print("users db deleted : ", conn.execute("DELETE FROM users").rowcount)

# 커밋 : isolation_level = None 일 경우 자동 반영(으로 커밋) -> Auto Commit
# conn.commit()
# conn.rollback()

# 접속 해제
conn.close()