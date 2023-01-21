import numpy as np
import pandas as pd
import  matplotlib as mtp
import matplotlib.pyplot as plt
#a = np.array([1, 2, 3, 4, 5, 6])


#ff=np.linspace(0, 11, num=6)
#print(ff)

#print(a.reshape(2,3))


file = pd.read_csv("titles.csv")

def first():
    markF=file[file["type"]== "MOVIE"]["imdb_score"].dropna()
    markS=file[file["type"]== "SHOW"]["imdb_score"].dropna()
    print(markS.mean())
    print(markF.mean())
    plt.hist(markF, bins=np.arange(0,10.2,0.2))
    plt.hist(markS, bins=np.arange(0,10.2,0.2))
    plt.xlabel("Score")
    plt.ylabel("titles")
    plt.show()
def second():
    AgeData=file[file["type"]=="SHOW"].dropna()
    readyData=AgeData.pivot_table(columns=['age_certification'], aggfunc='size')
    readyDataFrame=readyData.reset_index()
    LabelData=readyDataFrame["age_certification"]
    print(readyData)
    plt.pie(readyData, labels=LabelData)
    plt.show()


def third():
    DateData=file[file["release_year"]>=2000].dropna()
    DateDataRate=DateData[DateData["imdb_score"]>=8.0].dropna()
    XData=DateDataRate["release_year"]
    YData=DateDataRate["imdb_score"]
    #xpoints = np.array([0, 6])
    #ypoints = np.array([0, 250])
    print(XData.shape)
    print(YData.shape)
    plt.scatter(XData, YData)
    plt.show()


    #print(DateData)

#class_23 = titanic[titanic["it"].isin(["23"])]

#print(mL)
#third()
second()
#print(titanic.tail(10))
