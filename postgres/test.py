import psycopg2
def table():
    conn = psycopg2.connect(dbname='student', user="postgres", password='password', host="localhost", port=5432)

    cursor = conn.cursor()
    cursor.execute('''create table employees(name text, id int, age int);''')
    print('Table created succesfully')

    conn.commit()
    conn.close()

def data():
    conn = psycopg2.connect(dbname='student', user="postgres", password='password', host="localhost", port=5432)
    cursor = conn.cursor()

    name = input('Enter name: ')
    id = input('Enter id: ')
    age = input('Enter age: ')

    query = ''' insert into employees(name, id, age) values(%s, %s, %s);'''
    cursor.execute(query, (name, id, age))
    print('Data added successfully')

    conn.commit()
    conn.close()

def extract(): 
    conn = psycopg2.connect(dbname='student', user="postgres", password='password', host="localhost", port=5432)
    cursor = conn.cursor()
    cursor.execute(''' select * from employees;''')
    show = list(cursor.fetchall())
    print('Data fetched successfully', show)

    conn.commit()
    conn.close()


data()
