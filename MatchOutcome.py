import csv


# This Csv doesn't account for the difference in rank. Just above or below
# This CSV does
def playGame(Ateam,Bteam):
    # with open('APRankOnlyFilteredStats.csv', 'r') as stats:
    with open('APRankOnlyFilteredStats.csv', 'r') as stats:
        filereader = csv.reader(stats, delimiter=',', quotechar='|')
        for row in filereader:

            if len(row) > 0:
                # print(row)
                # print(r
                if row[1] == Ateam:
                    Astats = [row[2],row[3],row[4],row[5]]
                if row[1] == Bteam:
                    Bstats = [row[2],row[3],row[4],row[5]]

  
    Afavor = (float(Astats[0]) + float(Bstats[1]))/1.285551625751775
    Bfavor = (float(Bstats[2]) + float(Astats[3]))/0.19998530707843082

    if Afavor > Bfavor:
        winner = Ateam
        print(Afavor/Bfavor)
    if Afavor < Bfavor:
        winner = Bteam
        print(Bfavor/Afavor)

    return winner
