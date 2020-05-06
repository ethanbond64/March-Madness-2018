import csv
import getpass
import pg8000

user = input("Username: ")
secret = getpass.getpass()
db = pg8000.connect(user=user, password=secret, host='bartik.mines.edu', database='csci403')
db.autocommit = True
cursor = db.cursor()

def playGame(t1,t2,selection):
    query = "SELECT name, rank, record, home_record, away_record, tournament_record FROM team WHERE id = %s"
    
    cursor.execute(query,  (str(t1),))
    results = cursor.fetchall()
    team1_data = results[0]

    cursor.execute(query,  (str(t2),))
    results = cursor.fetchall()
    team2_data = results[0]


    if selection == 1:
        if team1_data[1] < team2_data[1]:
            return t1, team1_data[0]
        else:
            return t2, team2_data[0]

    else:
        if team1_data[selection] > team2_data[selection]:
            return t1, team1_data[0]
        else:
            return t2, team2_data[0]


def printPretty(lst):
    if len(lst) > 8:
        for i in range(0, int(len(lst)/8)):
            for j in range(8):
                print(lst[8*i +j],end='    ')
            print()
    else:
        for i in lst:
            print(i,end='    ')

# order based on the ncaa bracket 
Tournament = ['Duke','North Dakota St','VCU','UCF','Mississippi St','Liberty','Virginia Tech',\
'Saint Louis','Maryland','Belmont','LSU','Yale','Louisville','Minnesota','Michigan St',\
'Bradley','Gonzaga','Fairleigh Dickinson','Syracuse','Baylor','Marquette','Murray St','Florida St',\
'Vermont','Buffalo','Arizona St','Texas Tech','Northern Ky','Nevada','Florida','Michigan',\
'Montana','Virginia','Gardner-Webb','Ole Miss','Oklahoma','Wisconsin','Oregon', \
'Kansas St','UC Irvine','Villanova','Saint Marys (CA)','Purdue','Old Dominion',\
'Cincinnati','Iowa','Tennessee','Colgate','North Carolina','Iona','Utah St',\
'Washington','Auburn','New Mexico St','Kansas','Northeastern','Iowa St','Ohio St',\
'Houston','Georgia St','Wofford','Seton Hall','Kentucky','Abilene Christian']

# convert list of names to list of id's
Round = []
for t in Tournament:
    query = "SELECT id FROM team WHERE name = %s"
    cursor.execute(query,  (t,))
    results = cursor.fetchall()
    Round.append(results[0][0])

#######################
x = 64
for round_no in range(1,8):

    # get name of the round
    query = "SELECT name FROM round WHERE id = %s"
    cursor.execute(query,  (round_no,))
    results = cursor.fetchall()
    print(results[0][0])
    print()
    if round_no == 7:
        print('The winner you chose is',toPrint[0])
        break

    print('Teams Still Alive:')
    if round_no == 1:
        printPretty(Tournament)
    else:
        printPretty(toPrint)

    print()

    while True:
        print("""
Which statistic would you use to predict the outcome of this round?
    (1) rank
    (2) record
    (3) home record
    (4) away record
    (5) tournament record
        """)
        e = input("Input the number of your choice: ")
        try: 
            e = int(e)
            if e < 8 and e > 0:
                break
            print('Pleas input a valid character')
        except:
            print('Please input a valid character')   
  
    NextRound = []
    toPrint = []
    for game in range(0,x,2):
        team1 = Round[game]
        team2 = Round[game+1]
        winner_id, winner_name = playGame(team1,team2,e)
        NextRound.append(winner_id)
        toPrint.append(winner_name)

    print('Your accuracy this round: ')
    print('-----------------------------------------------------------------------')
    Round = NextRound
    x = int(x/2)