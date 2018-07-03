import cx_Oracle

con = cx_Oracle.connect('ngc438/pass123@localhost/orcl')

cur = con.cursor()
cur.execute("SELECT * FROM MEMBERS")

for result in cur:
    print(result)

cur.close()
con.close()
