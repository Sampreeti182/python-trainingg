import pandas as pd
df = pd.DataFrame({
    "name":["sampreeti","tania","john"],
    "marks":[99,90,45],
    "City":["kolkata","mumbai","bangalore"],
    "Age":[22,34,45],
})
print(df)
print(df.head(2))
print(df.tail(2))
print(df.shape)
print(df.columns)
print(df.describe())
#ex2
import pandas as pd
df = pd.DataFrame({
    "name":["sampreeti","tania","john"],
    "marks":[99,90,45],
    "City":["kolkata","mumbai","bangalore"],
    "Age":[22,34,45],
})
print(df)
print(df["name"])
print(df[["name","marks"]])
high_scores=df[df["marks"]>70]
print(high_scores)
filtered=df[(df["marks"]>70) & (df["Age"]>22)]
print(filtered)
#ex3
import pandas as pd
df = pd.DataFrame({
    "name":["sampreeti","tania","john"],
    "marks":[99,90,45],
    "City":["kolkata","mumbai","bangalore"],
    "Age":[22,34,45],
})
print(df)
df["result"]=df["Marks"].apply(lambda x: "pass" if x>=60 else "fail")
print(df)
sorted_df=df.sort_values(by="marks",ascending=False)
print(sorted_df)

#ex4
import pandas as pd
df = pd.DataFrame({
    "name":["sampreeti","tania","john"],
    "marks":[99,90,45],
    "City":["kolkata","mumbai","bangalore"],
    "Age":[22,34,45],
})
#print(df)
df2=df.copy()
df2.loc[2,"City"]="none"
print(df2)
print(df2.isnull().sum())
df2_filled=df2.fillna("Unknown")
print(df2_filled)
#ex5
import pandas as pd
df = pd.DataFrame({
    "name":["sampreeti","tania","john"],
    "Marks":[99,90,45],
    "City":["kolkata","mumbai","bangalore"],
    "Age":[22,34,45]
})
city_count=df.groupby("City")["Name"].count()
print(city_count)
avg_marks=df.groupby("City")["Marks"].mean()
print(avg_marks)
