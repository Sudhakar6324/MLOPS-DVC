import pandas as pd    
import os
data={"name":["a","b","c"],
      "age":[20,30,40],
      "city":["d","f","g"]}
df=pd.DataFrame(data)
# n_c1={"name":"i","age":9,"city":"o"}
# df.loc[len(df)]=n_c1
# n_c2={"name":"ut","age":10,"city":"oojo"}
# df.loc[len(df)]=n_c2

#create data floder
if not os.path.exists('data'):
    os.makedirs('data')
#save data as csv file
df.to_csv('data/sample_data.csv',index=False)

