import pymysql

def save_to_database(file_name, lines):
    connection = pymysql.connect(
        host='your-database-host',
        user='your-username',
        password='your-password',
        database='your-database'
    )
    cursor = connection.cursor()
    try:
        query = "INSERT INTO files (file_name, lines) VALUES (%s, %s)"
        cursor.execute(query, (file_name, lines))
        connection.commit()
        print(f"Saved {file_name} with {lines} lines to database.")
    except Exception as e:
        print(f"Error saving to database: {e}")
    finally:
        cursor.close()
        connection.close()
