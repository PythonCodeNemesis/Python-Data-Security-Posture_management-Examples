import sqlite3
# Example of an insecure query
def insecure_query(user_input):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + user_input + "'"
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows
# Example of a secure query with parameterized queries
def secure_query(user_input):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (user_input,))
    rows = cursor.fetchall()
    conn.close()
    return rows
# Usage example
username = input("Enter a username: ")
insecure_result = insecure_query(username)
secure_result = secure_query(username)
print("Insecure query result:", insecure_result)
print("Secure query result:", secure_result)
