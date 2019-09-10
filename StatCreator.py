import csv
def StatCreator(teamName):
    teamcsv = str(teamName)+'.csv'
    print(teamcsv)
    rows = 0
    wins = 0
    with open(teamcsv, 'r') as csvfile:
        # filewriter = csv.writer(csvfile, delimiter=',')
        # for pp in csvfile:
        #     print(pp)
        filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
        # print(len(filereader))
        for row in filereader:
            if len(row) > 0:
                rows += 1
                if row[2][0] == 'W':
                    wins += 1
    with open(teamcsv,'a') as f:
        writer=csv.writer(f)
        writer.writerow([])
        writer.writerow(['Wins ',' Games ',' Win %'])
        writer.writerow([wins,rows,(wins/rows)])
        return wins,rows,(wins/rows)
print(StatCreator('North Carolina'))
