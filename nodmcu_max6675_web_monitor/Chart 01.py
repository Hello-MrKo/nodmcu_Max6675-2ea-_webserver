# 온습도 센서 2개 Chart 그리기
# 온도 chart, 습도 Chart  
# https://wikidocs.net/92071


import time
import matplotlib.pyplot as plt
import numpy as np
from random import *
 
# No. 변수 
add=0                                  
XL=[]
yL11=[]
yL12=[]
yL21=[]
yL22=[]

# Data 읽기 
# for i in range(1,50):                       # 측정 Data 길이 
while(True):  
 
    add=add+1
    i00 = randint(0, 40)                  #  40부터 100 사이의 임의의 정수
    i01 = randint(0, 40)
    i02 = randint(60, 100)                  #  60부터 100 사이의 임의의 정수
    i03 = randint(60, 100)

    num=str(add)
 
    SS='\t'
    TT=time.strftime('%Y-%m-%d %H:%M:%S')
    H1=str(i00)
    T1=str(i01)
    H2=str(i02)
    T2=str(i03)

    SUM00=num+SS+TT+SS+H1+SS+T1+SS+H2+SS+T2+'\n'     

    print(SUM00)                                              #  인쇄                    

    time.sleep(1)    


    # Chart 그리기 
    # Chat data 
    x=int(add)                                       # X 축 데이터 
    y11=float(T1)                                    # Y1 데이터       
    y12=float(T2)                                    # Y2 데이터    
    y21=float(H1)                                    # Y3 데이터    
    y22=float(H2)                                    # Y4 데이터    
  
    # list 데이터 만들기 
    XL.append(x) 
    yL11.append(y11)
    yL12.append(y12)
    yL21.append(y21)
    yL22.append(y22)


    # 온도 Chart 
    plt.subplot(211)  
    plt.ylabel('Temp.(℃)')
    plt.plot(XL, yL11, color='red', marker='None', linestyle='solid')
    plt.plot(XL, yL12, color='green', marker='None', linestyle='solid')
    # 습도 Chart 
    plt.subplot(212)  
    plt.xlabel('red :1,   green:2')
    plt.ylabel('Humi.(%)')
    plt.plot(XL, yL21, color='red', marker='None', linestyle='solid')
    plt.plot(XL, yL22, color='green', marker='None', linestyle='solid')
    plt.pause(1)


plt.show()
