import pandas as pd
df=pd.read_csv("height-weight.csv")
height=df["Height(Inches)"].tolist()

sum=0
for eachdata in height: 
    sum=float(eachdata)+sum
mean=sum/len(height)
print(mean)