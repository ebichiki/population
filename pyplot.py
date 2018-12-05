import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'IPAPGothic'

df =  pd.read_csv('population.csv',index_col=0,encoding="utf_8")
man = df['人口男']
wom = df['人口女']

fig, ax = plt.subplots(ncols=2, figsize=(8,6))

# 男性人口
ax[0].barh(df.index, man, color='teal', height=0.5, label='Male')
ax[0].yaxis.tick_right() # 軸を右に
ax[0].set_yticks(np.array(range(0,111,10))) #　10歳刻み
ax[0].set_yticklabels([]) # こちらの軸ラベルは非表示
ax[0].set_xlim([5000,0]) # x軸反転
#　女性人口
ax[1].barh(df.index, wom, color='tomato', height=0.5, label='Famale')
ax[1].set_yticks(np.array(range(0,111,10)))
ax[1].set_xlim([0,5000])
ax[1].set_xlabel('Population')

fig.legend(loc='upper right')
plt.show()