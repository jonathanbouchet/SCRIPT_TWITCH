import json
import pandas as pd
import glob

list = ['Destiny','Overwatch','League','Street','Tom','World','Evolve','Pok']
for name in list:
    print name
    col = ['datetime','channels','game','_links','time','date','viewers']
    index = range(0)
    df = pd.DataFrame(index=index, columns=col)
    selection = 'JSON/' + str(name)+ '*.json'
    print selection
    counter=0
    for filename in glob.glob(selection):
        #print filename
        with open(filename) as data_file:    
            data = json.load(data_file)
            #print data
            df.loc[counter] = data
            counter=counter+1
    print ('total files : %d' % counter)
    str1=df.iloc[2,2]
    str2=df.iloc[1,5]
    str3='.csv'
    name = str1+str2+str3
    print name
    df.to_csv(name.encode("utf8"), sep='\t',encoding='utf-8')



