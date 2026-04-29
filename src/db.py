import sqlite3, os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data.db')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def find_person(name):
    conn = get_db()
    cur = conn.cursor()
    query = """
    SELECT p.name, r.ho, r.floor
    FROM people p
    JOIN room_people rp ON p.id = rp.person_id
    JOIN rooms r ON rp.room_id = r.id
    WHERE p.name LIKE ?
    """
    cur.execute(query, (f"%{name}%",))
    rows = cur.fetchall()
    conn.close()
    return [{"name": row["name"], "ho": row["ho"], "floor": row["floor"]} for row in rows]

    