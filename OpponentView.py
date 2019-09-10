import csv

team = str(input('Team:'))

teamFile = 'Team Data\\' + team + '.csv'

with open('APfullstats.csv','r') as second:
    filegreader = csv.reader(second,delimiter=',')
    for grow in filegreader:
        if len(grow) > 0:
            if grow[2] == team:
                rank = grow[0]
                print(grow[0],team)
with open(teamFile,'r') as original:
    filereader = csv.reader(original,delimiter=',')
    for row in filereader:
        if len(row) > 0:
            opponent = row[1]
            outcome = row[2][0]
            if opponent[0] == '@':
                opponent = opponent[2:len(opponent)-1]
                away = True
            else:
                opponent = opponent[1:len(opponent)-1]
            opponent = opponent.replace('.','')
            opponentRank = 0
            with open('APfullstats.csv','r') as second:
                filegreader = csv.reader(second,delimiter=',')
                for grow in filegreader:
                    if len(grow) > 0:
                        if grow[2] == opponent:
                            opponentRank = grow[0]
            if  int(opponentRank) < 50 and opponentRank != 0:
                print(opponent,opponentRank,outcome)
                pass

            # print(opponent,opponentRank,outcome)
