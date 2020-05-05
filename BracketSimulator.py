from MatchOutcome import playGame
import csv

Tournament = ['Duke','North Dakota St','VCU','UCF','Mississippi St','Liberty','Virginia Tech',\
'Saint Louis','Maryland','Belmont','LSU','Yale','Louisville','Minnesota','Michigan St',\
'Bradley','Gonzaga','Fairleigh Dickinson','Syracuse','Baylor','Marquette','Murray St','Florida St',\
'Vermont','Buffalo','Arizona St','Texas Tech','Northern Ky','Nevada','Florida','Michigan',\
'Montana','Virginia','Gardner-Webb','Ole Miss','Oklahoma','Wisconsin','Oregon', \
'Kansas St','UC Irvine','Villanova','Saint Mary\'s (CA)','Purdue','Old Dominion',\
'Cincinnati','Iowa','Tennessee','Colgate','North Carolina','Iona','Utah St',\
'Washington','Auburn','New Mexico St','Kansas','Northeastern','Iowa St','Ohio St',\
'Houston','Georgia St','Wofford','Seton Hall','Kentucky','Abilene Christian',]

#######################
Round = Tournament
x = 64
for i in range(6):
    print('Round of ',x)
    while True:
        print("""
Which statistic would you use to predict the outcome of this round?
    (1) rank
    (2) record
    (3) home record
    (4) away record
    (5) tournament record
    (6) % season games won as the favorite
    (7) % season games won as the underdog
        """)
        e = input("Input the number of your choice: ")
        try: 
            e = int(e)
            if e < 8 and e > 0:
                break
            print('Pleas input a valid character')
        except:
            print('Please input a valid character')   
    NewRound = []
    for game in range(0,x,2):
        team1 = Round[game]
        team2 = Round[game+1]
        with open('APRankOnlyFilteredStats.csv','r') as file:
            filereader = csv.reader(file, delimiter=',', quotechar='|')
            for row in filereader:
                if len(row) > 0:
                    if row[1] == team1:
                        rank1 = int(row[0])
                    if row[1] == team2:
                        rank2 = int(row[0])
        if rank1 > rank2:
            Ateam = team2
            Bteam = team1
        else:
            Ateam = team1
            Bteam = team2
        NewRound.append(playGame(Ateam,Bteam))
    print('Round Winners')
    print(NewRound)
    print('-----------------------------------------------------------------------')
    Round = NewRound
    x = int(x/2)