import csv
import numpy as np
data = []
Afavors = []
Bfavors = []
with open('APNewRankFilter.csv', 'r') as stats:
    filereader = csv.reader(stats, delimiter=',', quotechar='|')
    for row in filereader:
        if len(row) > 0:
            data.append(row)
for team1 in range(len(data)):
    for team2 in range((team1+1),len(data)):
        Ateam = data[team1]
        Bteam = data[team2]
        Astats = [Ateam[2],Ateam[3],Ateam[4],Ateam[5]]
        Bstats = [Bteam[2],Bteam[3],Bteam[4],Bteam[5]]
        #note
        Afavor = (float(Astats[0]) + float(Bstats[1]))
        Bfavor = (float(Bstats[2]) + float(Astats[3]))
        Afavors.append(Afavor)

        Bfavors.append(Bfavor)
print('medians')
print(np.median(Afavors))
print(np.median(Bfavors))
print('Averages')
print(np.mean(Afavors))
print(np.mean(Bfavors))
