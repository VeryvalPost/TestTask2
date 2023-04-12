import psycopg2
import datetime
import random
import time


while True:

    # Connecting to DB
    connection = psycopg2.connect(dbname="postgres",
                                  host="db",
                                  user="postgres",
                                  password="password",
                                  port="5432"
                                )
    cursor = connection.cursor()

    # Data from random
    def generate_data():
        return ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for i in range(10))


    # Check if values is exist
    def check_count_row():
        global cursor
        sql = """SELECT COUNT(*) FROM public.recordings"""
        cursor.execute(sql)
        count = cursor.fetchone()[0]
        if count > 29:
            cursor.execute("""DELETE FROM public.recordings""")

    # Check values for indexing
    def check_index():
        global cursor
        sql = """SELECT COUNT(*) FROM public.recordings"""
        cursor.execute(sql)
        index = cursor.fetchone()[0]
        return index+1

    # Write to database
    def insert_data():
        global cursor
        data = generate_data()
        timestamp = datetime.datetime.now()
        check_count_row()
        id = check_index()
        cursor.execute("""INSERT INTO public.recordings (id, data, date) VALUES (%s,%s, %s)""", (id, data, timestamp))
        connection.commit()
        print('Data written to table:')
        print('Id:', id)
        print('Data:', data)
        print('Date:', timestamp)


    insert_data()
    cursor.execute('commit')
    cursor.close()
    connection.close()
    # wait for 60 seconds
    time.sleep(60)
