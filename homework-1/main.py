"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="i1485563"
)

with open("north_data/customers_data.csv", encoding="UTF-8", newline='') as f:

    reader = csv.DictReader(f)

    for row in reader:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (row["customer_id"], row["company_name"], row["contact_name"]))
            conn.commit()

with open("north_data/employees_data.csv", encoding="UTF-8", newline='') as f:

    reader = csv.DictReader(f)

    for row in reader:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", (row["employee_id"],
                                                                                  row["first_name"],
                                                                                  row["last_name"],
                                                                                  row["title"],
                                                                                  row["birth_date"],
                                                                                  row["notes"],
                                                                                  ))
            conn.commit()

with open("north_data/orders_data.csv", encoding="UTF-8", newline='') as f:

    reader = csv.DictReader(f)

    for row in reader:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (row["order_id"],
                                                                                  row["customer_id"],
                                                                                  row["employee_id"],
                                                                                  row["order_date"],
                                                                                  row["ship_city"],
                                                                               ))

            conn.commit()
