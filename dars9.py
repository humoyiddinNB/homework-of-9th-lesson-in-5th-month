import psycopg2

conn = psycopg2.connect(database = 'cars_db', user = 'defendereviver71', password = '571632571632', port = 5432)
cur = conn.cursor()


##### 1 - masala
def update_table(table_name):
    try:
        column = input("yangi qiymatni kiriting\n")
        value = input(f"{column} = ")
        column1  = input("qaysi columni ozgartirmoqchisiz?\n")
        value1 = input(f"{column1} = ")
        query = f"UPDATE {table_name} SET {column} = %s WHERE {column1} = %s"
        cur.execute(query, (value, value1))
        conn.commit()
        return "Qiymat o'zgartirildi"
    except Exception as a:
        print("xatolik bor" + str(a))

# print(update_table("cars_info"))




##### 2 - masala
def writing_olds(table_name):
    cur.execute(f"Select * from {table_name} where age > 60")

    with open("old_cars.txt", 'w') as file:
        for i in cur.fetchall():
            file.write(str(i) + "\n")

# writing_olds("cars_info")






#### 3 - masala
def alter_table(table_name, column_name, yangi_tip):
    try:
        cur.execute(f"alter table {table_name} alter column {column_name} type {yangi_tip} using {column_name}::{yangi_tip}")
        conn.commit()

    except Exception as a:
        print(a)

    else:
        print("Column o'zgaritrildi")

# alter_table("cars_info", "age", "numeric")






####4 -masala
def alter_table_name():
    table = input("Table nomini kiriting: ")
    column  = input("Ozgarsidgan column nomini litiring: ")
    nom  = input("Yangi nomini kiriting: ")
    try:
        cur.execute(f"alter table {table} rename column {column} to {nom}")
        conn.commit()
    except Exception as e:
        print("nimadir xato ketti" + str(e))

    else:
        print(f"{column} columni {nom} ga o'zgartirildi")

# alter_table_name()







####  5-masala
def printing_chippes():
    table = input("Table name: ")
    try:
        with open("chippest_cars.txt", "w") as chippes:
            cur.execute(f"select * from {table} order by price limit 10")
            for i in cur.fetchall():
                chippes.write(str(i) + "\n")
    except Exception as e:
        print("Nimadir hato ketti")
    else:
        print("Eng arzon 10 ta moshinalar qoshildi")

# printing_chippes()

cur.close()
conn.close()

