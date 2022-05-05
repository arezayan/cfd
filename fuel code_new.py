#fuel code
import numpy as np
from matplotlib import pyplot

first_cap=0
full_cap=10E4
tanker_1=25000
tanker_2=32000
tanker_3=19000

evap_1=1.03
evap_2=1.015
buy=3*tanker_2
res=np.zeros(365)
buy_list=[]
for i in range(1,365):
    res[0]=first_cap + 3*tanker_2 - 50000
    res[0]=res[0]/evap_1
    
    if i in np.arange(5,365,7):
        res[i]=res[i-1] + buy - (50000*1.15)
        res[i]=res[i]/evap_1

    else:
        buy=32000*max((0.9*full_cap-res[i-1])//tanker_1 , (0.9*full_cap-res[i-1])//tanker_2)
        print('day of',i,'is',buy,res[i-1])
        res[i]=res[i-1] + buy -50000
        res[i]=res[i]/evap_1
    if res[i]>99000:
            buy=buy-2*tanker_1
            res[i]=res[i-1] + buy -50000
            res[i]=res[i]/evap_1

    if res[i]<50000:
        buy=buy+1*tanker_2 + 1*tanker_3
        res[i]=res[i-1] + buy -50000
        res[i]=res[i]/evap_1
    buy_list.append(buy)

for i in range(179,365):
    buy=32000*max((0.9*full_cap-res[i-1])//tanker_1 , (0.9*full_cap-res[i-1])//tanker_2)
    #print('day of',i,'is',buy,res[i-1])
    res[i]=res[i-1] + buy -50000
    res[i]=res[i]/evap_2
    if res[i]>99000:
            buy=buy-2*tanker_1
            res[i]=res[i-1] + buy -50000
            res[i]=res[i]/evap_2

    if res[i]<50000:
        buy=buy+1*tanker_2 + 1*tanker_3
        res[i]=res[i-1] + buy -50000
        res[i]=res[i]/evap_2

    


for i in range(365):
    print('day of',i,' the remain fuel in tanks is',res[i])

pyplot.figure(figsize=(9,7),dpi=100)
pyplot.plot(res,'k',marker= 's')
pyplot.xlabel('days')
pyplot.ylabel('Residual Fuel')
pyplot.xticks(range(0,365,5))

pyplot.show()