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
cur.close()
conn.close()
kdfoersdjfghd
kasdjbs
sdjfksjdf
