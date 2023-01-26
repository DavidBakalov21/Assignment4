import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
