import cx_Oracle

conn = cx_Oracle.connect('ngc438/pass123@localhost/orcl')

cur = conn.cursor()

cur.execute('''
BEGIN
   EXECUTE IMMEDIATE 'DROP TABLE counts';
EXCEPTION
   WHEN OTHERS THEN
      IF SQLCODE != -942 THEN
         RAISE;
      END IF;
END;''')

cur.execute('''
CREATE TABLE Counts (name VARCHAR2(20), count INTEGER)''')

fname = input('Enter file name :')
if(len(fname) < 1):
    fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = %s ', (1, email))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
conn.close()
