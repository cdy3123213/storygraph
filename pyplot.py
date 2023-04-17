from matplotlib import pyplot
import datetime
import matplotlib as mpl
import numpy as np
fig,ax= pyplot.subplots()
pyplot.rcParams['font.sans-serif']=['SimHei']
#x = range(1,31,1)
start=datetime.datetime(2023,1,1)
stop=datetime.datetime(2023,1,31)
delta=datetime.timedelta(1)
dates=mpl.dates.drange(start,stop,delta)

y = [1,1,2.5,7,10,12,13,17,24,30,35,40,41,42,44,46,49,50,46,42,36,32,24,16,8,4,3,2,1,1]
pyplot.plot(dates, y)
#pyplot.xticks(dates)
#pyplot.xticks(range(min(dates), max(dates) + 1))
ax=pyplot.gca()
date_format=mpl.dates.DateFormatter('%Y-%m-%d')
ax.xaxis.set_major_formatter(date_format)#设定x轴主要格式
ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(2))#设定坐标轴的显示的刻度间隔
fig.autofmt_xdate()
pyplot.ylabel("事件热度")
pyplot.xlabel("日期")
#对图表注释
pyplot.annotate('舆情起始',xy=(dates[1],1),xytext=(dates[0], 8),arrowprops=dict( alpha=0.6,arrowstyle='-|>',color='r'))
pyplot.annotate('民间讨论',xy=(dates[4],10),xytext=(dates[6], 6),arrowprops=dict( alpha=0.6,arrowstyle='-|>',color='r'))
pyplot.annotate('官媒介入',xy=(dates[11],40),xytext=(dates[12], 35),arrowprops=dict( alpha=0.6,arrowstyle='-|>',color='r'))
pyplot.annotate('民间讨论',xy=(dates[20],36),xytext=(dates[17], 28),arrowprops=dict( alpha=0.6,arrowstyle='-|>',color='r'))
pyplot.annotate('舆情消退',xy=(dates[25],4),xytext=(dates[26], 8),arrowprops=dict( alpha=0.6,arrowstyle='-|>',color='r'))
#标记被注释的点
pyplot.scatter(dates[1],1,c='b')
pyplot.scatter(dates[4],10,c='b')
pyplot.scatter(dates[11],40,c='b')
pyplot.scatter(dates[20],36,c='b')
pyplot.scatter(dates[25],4,c='b')
#划分生命周期并注明
pyplot.text(dates[1],20,'萌芽期',fontsize=15,bbox=dict(boxstyle='round'))
pyplot.text(dates[13],20,'成熟期',fontsize=15,bbox=dict(boxstyle='round'))
pyplot.text(dates[24],20,'消退期',fontsize=15,bbox=dict(boxstyle='round'))
n1=[dates[7],dates[7]]
m1=[-5,50]
pyplot.plot(n1,m1,linestyle = '-.',markerfacecolor='r')
n2=[dates[21],dates[21]]
m2=[-5,50]
pyplot.plot(n2,m2,linestyle = '-.',markerfacecolor='r')
pyplot.show()
