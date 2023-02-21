from datetime import datetime

from data.connection import db_connection


def get_data():
    conn = db_connection()
    cursor = conn.execute("SELECT * FROM apiDB")
    articles = [
        dict(creation_date=row[1], title=row[2], author=row[3], answered=row[4], link=row[5])
        for row in cursor.fetchall()
    ]
    return articles


def post_data(user):
    conn = db_connection()
    cursor = conn.cursor()
    for i in user:
        if i['is_answered'] == 1:
            i['is_answered'] = "Да"
        else:
            i['is_answered'] = "Нет"
        convert_date = datetime.fromtimestamp(i['creation_date'])
        cursor.execute(f"insert into apiDB (creation_date, title, author, answered, link) values (?, ?, ?, ?, ?);",
                       (convert_date, i['title'], i['owner']['display_name'], i['is_answered'], i['link']))
        conn.commit()
    conn.close()


def delete_data():
    conn = db_connection()
    conn.execute("DELETE FROM apiDB")
    conn.commit()
    conn.close()