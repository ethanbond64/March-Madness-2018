import getpass
import pg8000
import csv
user = input("Username: ")
secret = getpass.getpass()
db = pg8000.connect(user=user, password=secret, host='bartik.mines.edu', database='csci403')
db.autocommit = True
cursor = db.cursor()

# TABLE TEAM
cursor.execute("DROP TABLE team;")
db.commit()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS team (id INTEGER PRIMARY KEY, rank INTEGER, name TEXT, conference TEXT, record FLOAT(24), away_record FLOAT(24), tournament_record FLOAT(24), home_record FLOAT(24));")
db.commit()

with open('dbStats.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    columns = next(reader)
    for row in reader:
        if "'" in str(row[1]):
            temp = str(row[1])
            temp = temp.replace("'", "")
            cursor.execute("INSERT INTO team (id, rank, name, conference, record, away_record, tournament_record, "
                           "home_record) VALUES ({}, {}, \'{}\', \'{}\', {}, {}, {}, {});".format(row[0], row[0], temp,
                                                                                              str(row[2]), row[3],
                                                                                              row[4], row[5], row[6]))
        else:
            cursor.execute("INSERT INTO team (id, rank, name, conference, record, away_record, tournament_record, "
                       "home_record) VALUES ({}, {}, \'{}\', \'{}\', {}, {}, {}, {});".format(row[0], row[0],str(row[1]), str(row[2]), row[3],
                                                                                  row[4], row[5], row[6]))
    db.commit()
    csvfile.close()

# TABLE ROUND
cursor.execute("DROP TABLE round;")
db.commit()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS round (id INTEGER PRIMARY KEY, name TEXT);")
db.commit()

with open('dbRounds.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    columns = next(reader)
    for row in reader:
        cursor.execute("INSERT INTO round (id, name) VALUES ({}, \'{}\');".format(row[0], str(row[1])))
    db.commit()
    csvfile.close()

# TABLE ROUND TEAM XREF
cursor.execute("DROP TABLE round_team_xref;")
db.commit()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS round_team_xref (round_id INTEGER REFERENCES round(id), team_id INTEGER REFERENCES team(id));")
db.commit()

with open('dbXref.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    columns = next(reader)
    for row in reader:
        if "'" in str(row[1]):
            temp = str(row[1])
            temp = temp.replace("'", "")
            cursor.execute("INSERT INTO round_team_xref (round_id, team_id) SELECT {}, id FROM team WHERE name = \'{}\';".format(row[0], temp))

        else:
            cursor.execute("INSERT INTO round_team_xref (round_id, team_id) SELECT {}, id FROM team WHERE name = \'{}\';".format(row[0], str(row[1])))
    db.commit()
    csvfile.close()