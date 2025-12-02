import pandas as pd
data={
    "name":["sampreeti","tania","john"],
    "marks":[99,90,45],
    "City":["kolkata","mumbai","bangalore"]
}
df=pd.DataFrame(data)
#write csv
df.to_csv("students.csv",index=False)
print("csv file created")
#ex 2
import pandas as pd
df=pd.read_csv("students.csv")
print("csv file read successfully")
print(df)
