import getpass
import pg8000
import csv
user = input("Username: ")
secret = getpass.getpass()
db = pg8000.connect(user=user, password=secret, host='bartik.mines.edu', database='csci403')
db.autocommit = True
cursor = db.cursor()
var = 'Virginia'
# get rank, record, home_record, away_record, tournament_record where name = [variable] from team

query = "SELECT rank, record, home_record, away_record, tournament_record FROM team WHERE id = %s"
team = input("Enter team name: ")
cursor.execute(query,  (team,))
results = cursor.fetchall()

for row in results:
    rank, record, home_record, away_record, tournament_record = row
    print(rank, record, home_record, away_record, tournament_record)


# get name from the round table based on id = [variable]

query = "SELECT name FROM round WHERE id = %s"
round_no = input("Enter round number: ")
cursor.execute(query,  (round_no,))
results = cursor.fetchall()

for row in results:
    name = row
    print(name)

# get the rank_id from xref based on team name (might need to get team_id with a subquery)
query = "SELECT round_id FROM round_team_xref WHERE team_id = (SELECT id FROM team WHERE name = %s);"
team_name = input("Enter team name: ")
cursor.execute(query,  (team_name,))
results = cursor.fetchall()

for row in results:
    round_id = row
    print(round_id)