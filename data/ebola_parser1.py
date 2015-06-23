import glob
import csv
import time
import datetime
import random

prevCas = 0
prevDate = " "
casNow = 0
dateNow = " "

with open('ebola_cas_parsed.csv', 'w') as resultcsvfile:
    csvwriter1 = csv.DictWriter(resultcsvfile, delimiter=",", lineterminator='\n', fieldnames = ["a", "b"])

    with open('ebola_cas1.csv', 'r') as csvfile:
         csvreader1 = csv.reader(csvfile, delimiter=',')
         prevDate = time.mktime(datetime.datetime.strptime("25/03/2014", "%d/%m/%Y").timetuple())
         #print(prevDate)
         #print(datetime.datetime.fromtimestamp( prevDate).strftime("%d/%m/%Y %H %M %S "))
         for line in csvreader1:
             dateNow = time.mktime(datetime.datetime.strptime(line[0], "%d/%m/%Y").timetuple())
             
             cas = -prevCas + int(line[1])
             prevCas = int(line[1])
             l = {"a":line[0], "b":cas}
             #print(l)
             csvwriter1.writerow(l)
             
             
             '''
             if (dateNow - prevDate > 3600*4):
                
                #print (int(dateNow)/(3600*24))
                days = round((dateNow - prevDate)/(3600*24)) + 1
                print(days)
                cas = (int(line[1]) - prevCas) / days
                for x in range(1,int(days)):
                    date = datetime.datetime.fromtimestamp( prevDate + x*3600*24+3600).strftime("%d/%m/%Y") 
                    csvwriter1.writerow([date, cas])
                prevCas = int(line[1])
                prevDate = dateNow
            '''
                
                
                 
                  
