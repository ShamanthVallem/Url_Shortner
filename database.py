import sqlite3

def create_connection():
    con = sqlite3.connect("urlShortnerdatabse.db")
    return con

def create_table():
    con = create_connection()
    cursor = con.cursor()

    tableCreationQuerey = """
    CREATE TABLE IF NOT EXISTS  websites(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mainUrl TEXT NOT NULL,
    shortTokenage Text NOT NULL
    );
    """

    cursor.execute(tableCreationQuerey)
    con.commit()
    con.close()

def insert_url(mainUrl, shortToken):
    con = create_connection()
    cursor = con.cursor()
    insertQuery = """
    INSERT INTO websites (mainUrl, shortTokenage) VALUES (?, ?);
    """
    cursor.execute(insertQuery, (mainUrl, shortToken))
    con.commit()
    con.close()

def fetch_long_url(shortToken):
    con = create_connection()
    cursor = con.cursor()
    cursor.execute("SELECT mainUrl FROM websites WHERE shortTokenage=?", (shortToken,))
    result = cursor.fetchone()
    con.close()
    return result[0] if result else None
    
