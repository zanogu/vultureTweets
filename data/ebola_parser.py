import glob
import csv
import time
import datetime
import random

prevCas = 0
prevDate = " "
casNow = 0
dateNow = " "

alist, blist = [], []
d= 0


with open('ebola_cas_parsed.csv', 'w') as resultcsvfile:
    csvwriter1 = csv.DictWriter(resultcsvfile, delimiter=",", lineterminator='\n', fieldnames = ["a", "b"])
    with open('ebola_cas1.csv', 'r') as csvfile:
        csvreader1 = csv.reader(csvfile, delimiter=',')

        for row in csvreader1:
            alist.append(row)
        print(len(alist))

        for i in range(1,len(alist)):
            k = len(alist) - i 
            #print(k)
            alist[k][1] = int(alist[k][1]) - int(alist[k-1][1])

        delRows = []

        print(len(alist))
        for i in alist:
            
            for j in alist:
                
                if (i[0] == j[0] and i != j ):
                    print(i[0] + "   " + j[0])
                    i[1] = i[1] + j[1]
                    alist.remove(j)
                    

             
        print(len(alist))

        for i,j in zip(alist, alist[1:]):
           
            dateI = datetime.datetime.strptime(i[0], "%d/%m/%Y")
            dateJ = datetime.datetime.strptime(j[0], "%d/%m/%Y")
            a = dateJ - dateI
            #print (i,j,a.days)
            for k in range(0,int(a.days)):
                myDate = dateI + datetime.timedelta(days=k)
               
                deaths = int(i[1])/a.days
                myDate2 = myDate.strftime('%d/%m/%Y')
                #print (myDate2, deaths)
                row = [myDate2, deaths]
                blist.append(row)

        for row in blist:
            print(row)
            csvwriter1.writerow({'a':row[0], 'b': row[1]})
            
                
                
           
        #print(blist)

       
        '''

        
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
                
                
                 
                  
