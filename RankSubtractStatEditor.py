import csv
import os
rankReference = []
Bests = []
with open('APfullstats2.csv','r') as filegreader:
    filegreader = csv.reader(filegreader, delimiter=',', quotechar='|')
    for grow in filegreader:
        if len(grow) > 0:
            rankReference.append(grow)
# print(rankReference)

with open('APfullstats.csv', 'r') as original:

    filereader = csv.reader(original, delimiter=',', quotechar='|')

    for row in filereader:
        if len(row) > 0:
            rank = int(row[0])

            name = row[2]

            # home = row[7]
            # homeFirst = ''
            # homeSecond = ''
            # for ii in range(len(home)):
            #     if home[ii] == '-':
            #         for kk in range(ii+1,len(home)):
            #             homeSecond += home[kk]
            #         break
            #     homeFirst += home[ii]
            # #Loss Unexpected Home
            # LUH = int(homeSecond) / (int(homeSecond)+int(homeFirst))
            # WEH = int(homeFirst) / (int(homeSecond)+int(homeFirst))
            #
            # road = row[5]
            # roadFirst = ''
            # roadSecond = ''
            # for ii in range(len(road)):
            #     if road[ii] == '-':
            #         for kk in range(ii+1,len(road)):
            #             roadSecond += road[kk]
            #         break
            #     roadFirst += road[ii]
            #
            # neutral = row[6]
            # neutralFirst = neutral[0]
            # neutralSecond = neutral[2]
            # #Win Unexpected Road
            # WUR = (int(roadFirst)+int(neutralFirst))/(int(roadFirst)+int(neutralFirst)+int(roadSecond)+int(neutralSecond))
            # LER = (int(roadSecond)+int(neutralSecond))/(int(roadFirst)+int(neutralFirst)+int(roadSecond)+int(neutralSecond))

            bigOffense = 0
            bigDefense = 0
            gamesPlayed = 0
            WinEX = 0
            LoseEX = 0
            WinU = 0
            LoseU = 0
            teamcsv = 'Team Data\\' + name + '.csv'
            #Use other files to calculate when an upset occurs in favor out out of favor
            if os.path.isfile(teamcsv) == True:
                with open(teamcsv,'r') as readme:
                    filereading = csv.reader(readme, delimiter=',', quotechar='|')
                    for game in filereading:
                        away = False
                        if len(game) > 0:
                            gamesPlayed += 1
                            opponent = game[1]
                            outcome = game[2][0]
                            if opponent[0] == '@':
                                opponent = opponent[2:len(opponent)-1]
                                away = True
                            else:
                                opponent = opponent[1:len(opponent)-1]
                            opponent = opponent.replace('.','')
                            opponentRank = 0
                            for dd in rankReference:
                                if dd[2] == opponent:
                                    opponentRank = int(dd[0])
                                    break
                                else:
                                    opponentRank = 400

                            #########################
                            if opponentRank > rank and rank != 400:#away == False
                                if outcome == 'W':
                                    WinEX += (1/rank) - (1/opponentRank)
                                else:
                                    LoseU += (1/rank) - (1/opponentRank)
                            elif  opponentRank < rank and rank != 400:# away == True and
                                if outcome == 'W':
                                    WinU += (1/opponentRank) - (1/rank)
                                else:
                                    LoseEX +=    (1/opponentRank) - (1/rank)
                            else:
                                pass

            newstats = [rank,name,WinEX,LoseEX,WinU,LoseU]

            with open('APRankOnlyFilteredStats.csv','a') as latest:
                filewriter = csv.writer(latest, delimiter=',')
                if newstats[2] != 0 or newstats[3] != 0 or newstats[4] != 0 or newstats[5] != 0 :
                    filewriter.writerow(newstats)

            if LoseU != 0 and LoseEX != 0:
                myRank = (WinEX+WinU)/(LoseEX+LoseU)
            print(rank,name)
