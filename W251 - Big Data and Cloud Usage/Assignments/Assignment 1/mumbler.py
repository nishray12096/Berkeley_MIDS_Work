import pandas as pd
import sys as sys
import paramiko
from StringIO import StringIO
import numpy as np
from numpy.random import choice
import time

def selectword(df1, df2, df3):
        df1.columns = df2.columns = df3.columns = ['word','matches']
#add data from three nodes together
        data = pd.concat([df1,df2,df3],ignore_index=True)
#strip strings and filter set to only alphanumeric tokens
        data.word = data.word.str.strip()
        data = data[data.word.str.isalnum()]
#ensure that the count is numeric: may not be numeric if a \t was present in the token itself
        data.matches = data.matches.apply(pd.to_numeric,errors='coerce')
#just impute 0 counts for nonvalid tokens
        data.matches.fillna(0,inplace=True)
        total = data.matches.sum()
        if((len(data) == 0) | (total == 0)):
                print "stop returned"
                return "STOP TOKEN"

#calculate total occurrences of each word and subsequent probability
        results = data.groupby('word')['matches'].sum()

        probs = results / total
#draw one word based on the probability of each word
        draw = choice(probs.index, 1, p=probs.values)
        return draw[0]

#checking if an SSH'd command is complete
def channelReady(channel):
        return (channel.closed | channel.recv_ready() | channel.recv_stderr_ready())

maximum = int(sys.argv[1])
currentWord = str(sys.argv[2])

phrase = ""
phrase = phrase + currentWord

counter = 1

while counter < maximum:
        print(currentWord)
#boilerplate to SSH into each of the nodes
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh2 = paramiko.SSHClient()
        ssh2.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh3 = paramiko.SSHClient()
        ssh3.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect('50.23.102.141')
        ssh2.connect('50.23.102.142')
        ssh3.connect('50.23.102.138')
#search each node, capture output
        stdin,stdout,stderr = ssh.exec_command('sh /gpfs/gpfsfpo/mumbler/SearchNode1.sh ' + currentWord)
        stdin2,stdout2,stderr2 = ssh2.exec_command('sh /gpfs/gpfsfpo/mumbler/SearchNode2.sh ' + currentWord)
        stdin3,stdout3,stderr3 = ssh3.exec_command('sh /gpfs/gpfsfpo/mumbler/SearchNode3.sh ' + currentWord)

#set a manual timeout, the paramiko timeout doesn't work and can hang
        timeout = 7

        t0 = time.time()
#wait until all three commands are finished, or if timeout is exceeded
        while (~channelReady(stdout.channel) | ~channelReady(stdout2.channel) | ~channelReady(stdout3.channel)) & (time.time() - t0 < timeout):
                time.sleep(1)

        DFstr1 = StringIO(stdout.read())
        DFstr2 = StringIO(stdout2.read())
        DFstr3 = StringIO(stdout3.read())

        ssh.close()
        ssh2.close()
		ssh3.close()
#try to load the results. If failures, note the failure and just return and empty DF (as if the node had no data on this word)
        try:
                DF1 = pd.read_csv(DFstr1,sep='\t')
        except:
                print("load failure: node 1")
                DF1 = pd.DataFrame(columns=['foo','bar'])
        try:
                DF2 = pd.read_csv(DFstr2,sep='\t')
        except:
                print("load failure: node 2")
                DF2 = pd.DataFrame(columns=['foo','bar'])
        try:
                DF3 = pd.read_csv(DFstr3,sep='\t')
        except:
                print("load failure: node 3")
                DF3 = pd.DataFrame(columns=['foo','bar'])
#function to select a new word based on ngram counts
        currentWord = selectword(DF1,DF2,DF3)

        if(currentWord == "STOP TOKEN"):
                print ("word not found")
                break

        phrase = phrase + " " + currentWord
        counter += 1

print(phrase)