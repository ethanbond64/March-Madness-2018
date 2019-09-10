import csv
Ateam = str(input('Higher Ranked Team:'))
Bteam = str(input('Lower Ranked Team:'))

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

    ## New Medians V1 (V5 using data from V3 and V4)
    # Afavor = (float(Astats[0]) + float(Bstats[1]))/0.8235294117647058
    # Bfavor = (float(Bstats[2]) + float(Astats[3]))/0.20588235294117646
    ##Means V2
    # Afavor = (float(Astats[0]) + float(Bstats[1]))/0.8117149890930305
    # Bfavor = (float(Bstats[2]) + float(Astats[3]))/0.21310015892561643
    ##Filtered Rank Medians V3
    # Afavor = (float(Astats[0]) + float(Bstats[1]))/0.9178592028389427
    # Bfavor = (float(Bstats[2]) + float(Astats[3]))/0.1624898955488932
    ##Filtered Rank Means V4
    # Afavor = (float(Astats[0]) + float(Bstats[1]))/2.420274497319837
    # Bfavor = (float(Bstats[2]) + float(Astats[3]))/0.319103867133289
    ##AP Filtered Rank Medians V6
    Afavor = (float(Astats[0]) + float(Bstats[1]))/1.285551625751775
    Bfavor = (float(Bstats[2]) + float(Astats[3]))/0.19998530707843082
    ##AP Filtered Rank Means V7
    # Afavor = (float(Astats[0]) + float(Bstats[1]))/2.96591400308395
    # Bfavor = (float(Bstats[2]) + float(Astats[3]))/0.3908430026413479
    ## New AP Filtered Medians V8
    # Afavor = (float(Astats[0]) + float(Bstats[1]))/21.13333511650999
    # Bfavor = (float(Bstats[2]) + float(Astats[3]))/3.2977470517354632

    #Better AP medians?
    # Afavor = (float(Astats[0]) + float(Bstats[1]))/21.036429658399705
    # Bfavor = (float(Bstats[2]) + float(Astats[3]))/3.3043628764043023

    #Better AP Means?
    # Afavor = (float(Astats[0]) + float(Bstats[1]))/20.56486703989248
    # Bfavor = (float(Bstats[2]) + float(Astats[3]))/3.4569561140680984

    # print(Afavor)
    # # print(Bstats)
    # print(Bfavor)
    if Afavor > Bfavor:
        winner = Ateam
        print(Afavor/Bfavor)
    if Afavor < Bfavor:
        winner = Bteam
        print(Bfavor/Afavor)

    return winner
print(playGame(Ateam,Bteam))
