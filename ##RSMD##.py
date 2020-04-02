##rsmd.plot##
import pandas as pd
import numpy
import matplotlib.pyplot as plt

data_p_1 = pd.read_csv('RSMD.csv', sep=",", header=0)
print(data_p_1)
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
d_p_1 = {'time':data_p_1['Time'],'RSMD':data_p_1['RMSD']}# make a dictionary from the data 
df_p_1 = pd.DataFrame(data=d_p_1)#make a dataframe for the dictionary



plt.plot(df_p_1['time'],df_p_1['RSMD'],label='wm1mg')
plt.xlabel('time(ps)')
plt.ylabel('RMSD')
plt.legend()
plt.savefig('RMSD.png')

