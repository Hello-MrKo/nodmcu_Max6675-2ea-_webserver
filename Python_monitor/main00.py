
 # 2023-07-27
 # ESP8266 node MCU  webserver 온도 데이터 불러오기 
 # 온도 센서 : Max6675  
 # 데이터 TXT 저장 
 

import time
from urllib.request import urlopen
from bs4 import BeautifulSoup


# No. 변수 
add=0      
Webaddress="http://192.168.137.202/"                  # node MCU IP 주소                                   

# 첫번째 Line 출력 
firstline='No.''\t''--date & time --''\t''temp1(cel)''\t''temp2(cel)''\n'
print(firstline)

# 데이터 저장 
TT=time.strftime('%Y-%m-%d-%H-%M-%S')
filename='./data/'+TT+'.txt'                          # 폴더 및 파일명 지정 
f=open(filename,'w')
f.write(firstline)


# Data 읽기 
for i in range(1,30):                              # 측정 Data 길이 
    
    add=add+1                                        
    time.sleep(1)                                  # 기다리기 
    num=str(add)                                   # 번호 달기  
    SS='\t'
    TT=time.strftime('%Y-%m-%d %H:%M:%S')          # 일시     

    html = urlopen(Webaddress)                     # 웹 주소 Data 불러오기 
    soup = BeautifulSoup(html, "html.parser") 
    tem1 = soup.find(id='temperature1')
    Temp1=tem1.string[13:18]                         # 온도 데이터 추출    

    tem2 = soup.find(id='temperature2')
    Temp2=tem2.string[13:18]                         # 온도 데이터 추출    

    SUM=num+SS+TT+SS+Temp1+SS+Temp2+'\n'
  
    print(SUM)                                    # 데이터 출력 

    f=open(filename,'a')                          # 데이터 저장   
    f.write(SUM)                                  
    f.close()
