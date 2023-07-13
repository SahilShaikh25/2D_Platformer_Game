import sqlite3

def connect():
    con = sqlite3.connect('MyDb.db')
    cursor = con.cursor()
    return con, cursor

def create_table():
    con , cursor = connect()
    cursor.execute('''CREATE TABLE IF NOT EXISTS User(
                Name TEXT,
                Highscore INT)''')
    con.commit()
    insert_data()
    con.commit()
    con.close()

def drop_table():
    con, cursor = connect()
    cursor.execute("drop table User")
    con.commit()
    con.close()

def check_score(score):
    score_bool = False
    con, cursor = connect()
    # score check
    cursor.execute("SELECT Highscore from User")
    db_score = cursor.fetchone()[0]
    if score > db_score:
        score_bool = True
    con.commit()
    con.close()
    return score_bool

def insert_data():
    con, cursor = connect()
    cursor.execute("INSERT INTO User VALUES ('Echo', 0)")
    con.commit()
    con.close()

def update_data(score):
    score_bool= check_score(score)
    con, cursor = connect()
    if score_bool:
        cursor.execute(f"UPDATE User SET Highscore = {score}")
        cursor.execute("SELECT Highscore from User")
        x = cursor.fetchone()[0]
        print(f"update_type : {x}")

    con.commit()
    con.close()

def get_highscore():
    con, cursor = connect()
    cursor.execute("SELECT Highscore from User")
    highscore = cursor.fetchone()[0]
    con.commit()
    con.close()
    return highscore

# con = sqlite3.connect('MyDb.db')
# cursor = con.cursor()
# # cursor.execute("UPDATE User SET Highscore = 0")
# cursor.execute("SELECT * from User")
# x = cursor.fetchone()
# con.commit()
# con.close()