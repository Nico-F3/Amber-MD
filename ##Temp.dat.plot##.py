##rsmd.plot##
import pandas as pd
import numpy
import matplotlib.pyplot as plt

data_p_1 = pd.read_csv('temp.dat', sep=" ", header=None)
# print(data_p_1)
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
d_p_1 = {'time':data_p_1[0],'T.K':data_p_1[1]}# make a dictionary from the data 
df_p_1 = pd.DataFrame(data=d_p_1)#make a dataframe for the dictionary
for i in range(len(df_p_1)):
    for j in range(i+1,len(df_p_1)):
        if df_p_1['T.K'][j]<df_p_1['T.K'][i]:
            df_p_1=df_p_1.drop(df_p_1.index[j])

data_p_2 = pd.read_csv('temp_water.dat', sep=" ", header=None)
d_p_2 = {'time':data_p_2[0],'T.K':data_p_2[1]}
df_p_2 = pd.DataFrame(data=d_p_2)

for i in range(len(df_p_2)):
    for j in range(i+1,len(df_p_2)):
        if df_p_2['T.K'][j]<df_p_2['T.K'][i]:
            df_p_2=df_p_2.drop(df_p_2.index[j])           

data_p_3 = pd.read_csv('tempdoble.dat', sep=" ", header=None)
d_p_3 = {'time':data_p_3[0],'T.K':data_p_3[1]}
df_p_3 = pd.DataFrame(data=d_p_3)


df_p_3=df_p_3.drop(df_p_3.index[-1]) 

frames = [df_p_1, df_p_2, df_p_3]

result = pd.concat(frames)

print(result)

plt.plot(result['time'],result['T.K'],label='wm1mg')
plt.xlabel('time(ps)')
plt.ylabel('T.K')
plt.legend()
plt.savefig('newtemptotal.png')