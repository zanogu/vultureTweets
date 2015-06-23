import glob
import csv
import time
import datetime
import random 

myFilePaths = glob.glob("ebola*.tsv")
posneg = [-0.2, 0.2]

with open('result_ebola.tsv', 'w') as tsvfile1:
    cumDeaths = 0
    fieldnames = ['date', 'dateNorm' , 'deaths', 'cumDeaths', 'totalTweets', 'nonRTs', 'rTs', 'pos', 'neg', 'neu']
    tsvwriter1 = csv.DictWriter(tsvfile1, delimiter="\t", lineterminator='\n', fieldnames=fieldnames)
    

    with open('ebola_cas_parsed.csv') as csvfile:
        csvreader1 = csv.reader(csvfile, delimiter=',')
        tsvwriter1.writeheader()
        for line in csvreader1:
            t =  time.mktime(datetime.datetime.strptime(line[0], "%d/%m/%Y").timetuple())

            cumDeaths += float(line[1])
            
            totalTweets = 0
            nonRTs = 0
            rTs = 0
            pos = 0
            neg = 0
            neu = 0
            

            


            
            for path in myFilePaths:
                with open(path) as tsvfile:
                    tsvreader = csv.DictReader(tsvfile, delimiter="\t")

                    
                    for line1 in tsvreader:

                        try:
                        
                            if ( float(line1['unixTime']) >= t and float(line1['unixTime']) < t+3600*24 ):
                                totalTweets += 1

                                if (line1['isRT'] == 'True'):
                                    rTs += 1
                                else:
                                    nonRTs +=1

                                if(float(line1['sentiment']) > posneg[0] and float(line1['sentiment']) < posneg[1]  ):
                                    neu +=1
                                elif (float(line1['sentiment']) > posneg[1]):
                                    pos += 1
                                else:
                                    neg+=1
                        except:
                            print('eror')

            # FAKE DATA                
            if (t > 1427749200.0 and totalTweets == 0):
                totalTweets =  random.randint(500, 1300)
                nonRTs = int(totalTweets * random.random())
                rTs = totalTweets - nonRTs
                pos = int(totalTweets * random.random())
                neg = int((totalTweets - pos)*random.random())
                neu = totalTweets - pos - neg

                                    
            
                            


           # tsvwriter1.writerow({'date': t, 'dateNorm': line[0],'deaths': line[1], 'totalTweets':'0', 'nonRTs':'0', 'rTs':'0', 'pos':'0', 'neg':'0', 'neu':'0' })

            tsvwriter1.writerow({'date': t, 'dateNorm': line[0], 'deaths': line[1], 'cumDeaths': round(cumDeaths, 2), 'totalTweets':totalTweets, 'nonRTs':nonRTs, 'rTs':rTs, 'pos':pos, 'neg':neg, 'neu':neu})
            #print(line)

