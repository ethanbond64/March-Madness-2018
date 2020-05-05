import csv

infile = open('fullstats.csv','r')
reader = csv.DictReader(infile)

outfile = open('dbStats.csv','w')
head = ['rank','name','conference','record','away_record','tournament_record','home_record']
outwriter = csv.DictWriter(outfile,fieldnames=head)
outwriter.writeheader()

for row in reader:
    print(row['name'])
    del row['index'], row['ot_record']

    record = [int(i) for i in row['record'].split('-')]
    record = (record[0]-record[1])/sum(record)
    row['record'] = record
    
    away_record = [int(i) for i in row['away_record'].split('-')]
    away_record = (away_record[0]-away_record[1])/sum(away_record)
    row['away_record'] = away_record
    
    tournament_record = [int(i) for i in row['tournament_record'].split('-')]
    if sum(tournament_record) == 0:
        row["tournament_record"] = 0
    else:
        tournament_record = (tournament_record[0]-tournament_record[1])/sum(tournament_record)
        row['tournament_record'] = tournament_record

    home_record = [int(i) for i in row['home_record'].split('-')]
    home_record = (home_record[0]-home_record[1])/sum(home_record)
    row['home_record'] = home_record
    
    outwriter.writerow(row)