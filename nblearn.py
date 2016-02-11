import os,string,json,sys
stopword=[]

def createStopwords():
    with open("stopwords.txt","r") as file:
        stopwords= file.readlines(1)
    stopwords=[word.strip('\n') for word in stopwords]
    return stopwords

def getDict1(file,dict,index,common_dict):
    count=0
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
                    countx=dict[word]
                    countx+=1
                    dict[word]=countx
                    count+=1
                    common_dict[word][index-1]=countx
                elif bool(word):
                    dict[word]=1
                    count+=1
                    if word in common_dict:
                        common_dict[word][index-1]=1
                    else:
                        common_dict[word]=[0,0,0,0]
                        common_dict[word][index-1]=1

    return [dict,common_dict,count]


pathname=sys.argv[1]
common_dict=dict()
dict1=dict()
dict2=dict()
dict3=dict()
dict4=dict()
count1=0
count2=0
count3=0
count4=0

f_nbmodel=open("nbmodel.txt",'w')

#commondict


for root, dirs, files in os.walk(pathname):
    for file in files:
        file_name=root+'/'+file
        if file.endswith(".txt") and file!='README.txt' :

            if(file_name.find("deceptive")!=-1 and file_name.find("negative")!=-1):
                result=getDict1(file_name,dict1,1,common_dict)
                dict1=result[0]
                common_dict=result[1]
                count1+=result[2]
            if(file_name.find("truthful")!=-1 and file_name.find("negative")!=-1):
                result=getDict1(file_name,dict2,2,common_dict)
                dict2=result[0]
                common_dict=result[1]
                count2+=result[2]
            if(file_name.find("deceptive")!=-1 and file_name.find("positive")!=-1):
                result=getDict1(file_name,dict3,3,common_dict)
                dict3=result[0]
                common_dict=result[1]
                count3+=result[2]
            if(file_name.find("truthful")!=-1 and file_name.find("positive")!=-1):
                result=getDict1(file_name,dict4,4,common_dict)
                dict4=result[0]
                common_dict=result[1]
                count4+=result[2]


for key in common_dict:
    val1 = common_dict[key][0]+1
    val2 = common_dict[key][1]+1
    val3 = common_dict[key][2]+1
    val4 = common_dict[key][3]+1
    common_dict[key][0]=val1/float(len(dict1)+count1)
    common_dict[key][1]=val2/float(len(dict2)+count2)
    common_dict[key][2]=val3/float(len(dict3)+count3)
    common_dict[key][3]=val4/float(len(dict4)+count4)
    #f_nbmodel.write(key+" "+str(common_dict[key]))
    #f_nbmodel.write('\n')
json.dump(common_dict,f_nbmodel)
