from MatchOutcome import playGame
import csv

playIns = ['North Dakota St','NC Central','Belmont','Temple', \
          'Fairleigh Dickinson','Prairie View','Arizona St','St John\'s (NY)']
playIn = []
for game in range(0,8,2):
    team1 = playIns[game]
    team2 = playIns[game+1]
    # with open('APNewRankFilter.csv','r') as file:
    with open('APNewRankFilter.csv','r') as file:
        filereader = csv.reader(file, delimiter=',', quotechar='|')
        for row in filereader:
            if len(row) > 0:
                # print(row[2])
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
    playIn.append(playGame(Ateam,Bteam))
# print('Play In Round Winners')
# print(playIn)

Tournament = ['Duke','North Dakota St','VCU','UCF','Mississippi St','Liberty','Virginia Tech',\
'Saint Louis','Maryland','Belmont','LSU','Yale','Louisville','Minnesota','Michigan St',\
'Bradley','Gonzaga','Fairleigh Dickinson','Syracuse','Baylor','Marquette','Murray St','Florida St',\
'Vermont','Buffalo','Arizona St','Texas Tech','Northern Ky','Nevada','Florida','Michigan',\
'Montana','Virginia','Gardner-Webb','Ole Miss','Oklahoma','Wisconsin','Oregon', \
'Kansas St','UC Irvine','Villanova','Saint Mary\'s (CA)','Purdue','Old Dominion',\
'Cincinnati','Iowa','Tennessee','Colgate','North Carolina','Iona','Utah St',\
'Washington','Auburn','New Mexico St','Kansas','Northeastern','Iowa St','Ohio St',\
'Houston','Georgia St','Wofford','Seton Hall','Kentucky','Abilene Christian',]
#
Round1 = []
for game in range(0,64,2):
    team1 = Tournament[game]
    team2 = Tournament[game+1]
    with open('APNewRankFilter.csv','r') as file:
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
    Round1.append(playGame(Ateam,Bteam))
print('-----------------------------------------------------------------------')
print('Round 1 Winners')
print(Round1)

Round2 = []
for game in range(0,32,2):
    team1 = Round1[game]
    team2 = Round1[game+1]
    with open('APNewRankFilter.csv','r') as file:
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
    Round2.append(playGame(Ateam,Bteam))
print('-----------------------------------------------------------------------')
print('Sweet 16')
print(Round2)

Round3 = []
for game in range(0,16,2):
    team1 = Round2[game]
    team2 = Round2[game+1]
    with open('APNewRankFilter.csv','r') as file:
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
    Round3.append(playGame(Ateam,Bteam))
print('-----------------------------------------------------------------------')
print('Elite 8')
print(Round3)

Round4 = []
for game in range(0,8,2):
    team1 = Round3[game]
    team2 = Round3[game+1]
    with open('APNewRankFilter.csv','r') as file:
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
    won = playGame(Ateam,Bteam)
    Round4.append(won)
print('-----------------------------------------------------------------------')
print('Final Four')
print(Round4)

Round5 = []
for game in range(0,4,2):
    team1 = Round4[game]
    team2 = Round4[game+1]
    with open('APNewRankFilter.csv','r') as file:
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
    Round5.append(playGame(Ateam,Bteam))
print('-----------------------------------------------------------------------')
print('Championship')
print(Round5)

team1 = Round5[0]
team2 = Round5[1]
with open('APNewRankFilter.csv','r') as file:
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
Champ = playGame(Ateam,Bteam)
print('-----------------------------------------------------------------------')
print('Champion')
print(Champ)
