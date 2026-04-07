from database1 import conn,pool

def show_all_users():
    try:
        query = "SELECT * FROM users"
        pool.execute(query)

        result = pool.fetchall()

        for row in result:
            print(row)

    except Exception as err:
        print("Error is:", err)

