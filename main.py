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

def third():
    DateData=file[file["release_year"]>=2000].dropna()
    DateDataRate=DateData[DateData["imdb_score"]>=8.0].dropna()

    #DateDataRateSorted=DateDataRate.sort_values("release_year")
    g =DateDataRate.groupby('release_year')["imdb_score"].count()
    gd =DateData.groupby('release_year')["type"].count()
    gg=g.reset_index()
    ggg=gd.reset_index()
    gg1=gg.sort_values("release_year")
    ggg1=ggg.sort_values("release_year")
    print(gg1)

    merged_df=pd.merge(gg1, ggg1, how="outer", on="release_year").sort_values("release_year")
    merged_df=merged_df.fillna(0)
    YData=merged_df["imdb_score"]/merged_df["type"]
    #gg1["release_year"]
    XData=merged_df["release_year"]

    plt.plot(XData, YData)
    plt.show()
