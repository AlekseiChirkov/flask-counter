import psycopg2


conn = psycopg2.connect(
    host="127.0.0.1",
    port="5432",
    database="counter_db",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS counter
    (
     id serial PRIMARY KEY,
     counter integer,
     client_info varchar(255),
     created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
)

conn.commit()


def insert_into(data: dict):
    cur.execute(
        f"""
        INSERT INTO counter
        (counter, client_info)
        VALUES (%s, %s)
        """,
        (data["counter"], data["user_agent"])
    )
    conn.commit()


def select_from():
    cur.execute(
        f"""
        SELECT * FROM counter
        ORDER BY id DESC
        LIMIT 1
        """
    )
    records = cur.fetchall()
    return records
