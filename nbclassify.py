import os,string,json,math,sys
stopword=[]

def createStopwords():
    with open("stopwords.txt","r") as file:
        stopwords= file.readlines(1)
    stopwords=[word.strip('\n') for word in stopwords]
    return stopwords

def getScore(index,common_dict,key,dict):
    score1=0
    if key in common_dict:
        value=float(dict[key])
        prob=common_dict[key][index-1]
        prob=math.log(prob,10)
        return prob*value
    return score1

def getDict(file,dict):
    with open(file,'r') as f:
        for line in f:
            line=line.translate(None, string.punctuation)
            querywords = line.split()

            resultwords  = [word for word in querywords if word.lower() not in stopword]
            result = ' '.join(resultwords)
            result = ''.join([i for i in result if not i.isdigit()])
            for word in result.split():
                word=word.lower()
                word=word.strip()
                if word in dict and bool(word):
                    count=dict[word]
                    count+=1
                    dict[word]=count
                elif bool(word):
                    dict[word]=1


    return dict
f=open("nbmodel.txt",'r')
f1=open("nboutput.txt",'w')
common_dict=json.load(f)
pathname=sys.argv[1]
count=0

for root, dirs, files in os.walk(pathname):
    for file in files:

        if file.endswith(".txt") and file!='README.txt':
            file_path=str(root)+'/'+file
            dict={}
            dict=getDict(file_path,dict)
            score1=0
            score2=0
            score3=0
            score4=0
            for key in dict:
                score1+=getScore(1,common_dict,key,dict)
                score2+=getScore(2,common_dict,key,dict)
                score3+=getScore(3,common_dict,key,dict)
                score4+=getScore(4,common_dict,key,dict)
            list=[score1,score2,score3,score4]

            i=max(list)
            i = list.index(i)

            if i== 0:

                f1.write('deceptive negative ')

            elif i== 1:

                f1.write('truthful negative ')

            elif i== 2:

                f1.write('deceptive positive ')

            elif i== 3:

                f1.write('truthful positive ')
            f1.write(str(file_path))
            f1.write('\n')
