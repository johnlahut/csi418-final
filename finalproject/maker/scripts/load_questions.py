import csv

def parse(filename):

    bad = []

    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')



        for row in reader:
            if len(row) < 10 or len(row) > 11:
                bad.append(row)
                continue



            print(len(row))

parse('sample.csv')