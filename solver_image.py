# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 01:36:08 2018

@author: Sharif
"""
      
from selenium import webdriver
import random
from PIL import Image 
import time


US=['w','w','w','w','w','w','w','w','w']
FS=['w','w','w','w','g','w','w','w','w']
LS=['w','w','w','w','o','w','w','w','w']
RS=['w','w','w','w','r','w','w','w','w']
BS=['w','w','w','w','b','w','w','w','w']
DS=['w','w','w','w','y','w','w','w','w']


C=['w','r','o','b','g','y']
imp={'up_red.jpg':(1,1),'face_red.jpg':(1,2),'right_red.jpg':(1,3),'bottom_red.jpg':(1,4),'left_red.jpg':(1,5),'down_red.jpg':(1,6),
     'up_orange.jpg':(2,1),'face_orange.jpg':(2,2),'right_orange.jpg':(2,3),'bottom_orange.jpg':(2,4),'left_orange.jpg':(2,5),'down_orange.jpg':(2,6),
     'up_blue.jpg':(3,1),'face_blue.jpg':(3,2),'right_blue.jpg':(3,3),'bottom_blue.jpg':(3,4),'left_blue.jpg':(3,5),'down_blue.jpg':(3,6),
     'up_green.jpg':(4,1),'face_green.jpg':(4,2),'right_green.jpg':(4,3),'bottom_green.jpg':(4,4),'left_green.jpg':(4,5),'down_green.jpg':(4,6),
     'up_yellow.jpg':(5,1),'face_yellow.jpg':(5,2),'right_yellow.jpg':(5,3),'bottom_yellow.jpg':(5,4),'left_yellow.jpg':(5,5),'down_yellow.jpg':(5,6)
     }


def side(c,s,n):
    if s==1:US[n]=C[c]
    if s==2:FS[n]=C[c]
    if s==3:RS[n]=C[c]
    if s==4:BS[n]=C[c]
    if s==5:LS[n]=C[c]
    if s==6:DS[n]=C[c]      


for a,(c,s) in imp.items():#1        
    count=0
    check=0
    bw=Image.open(a).load()
    while count<100:
        x=random.randint(20,150)
        y=random.randint(20,150)
        count=count+1        
        if bw[x,y]==255:
            check=check+1
    if check>70:
        n=0
        side(c,s,n)

for a,(c,s) in imp.items():#2       
    count=0
    check=0
    bw=Image.open(a).load()
    while count<100:
        x=random.randint(180,320)
        y=random.randint(20,150)
        count=count+1
        if bw[x,y]==255:
            check=check+1
    if check>70:
        n=1
        side(c,s,n)
        
for a,(c,s) in imp.items():#3       
    count=0
    check=0
    bw=Image.open(a).load()
    while count<100:
        x=random.randint(350,480)
        y=random.randint(20,150)
        count=count+1
        if bw[x,y]==255:
            check=check+1
    if check>70:
        n=2
        side(c,s,n)
        
for a,(c,s) in imp.items():#4        
    count=0
    check=0
    bw=Image.open(a).load()
    while count<100:
        x=random.randint(20,150)
        y=random.randint(180,320)
        count=count+1
        if bw[x,y]==255:
            check=check+1
    if check>70:
        n=3
        side(c,s,n)

#5 default centre peice

for a,(c,s) in imp.items():#6        
    count=0
    check=0
    bw=Image.open(a).load()
    while count<100:
        x=random.randint(350,480)
        y=random.randint(180,320)
        count=count+1
        if bw[x,y]==255:
            check=check+1
    if check>70:
        n=5
        side(c,s,n)
        
for a,(c,s) in imp.items():#7        
    count=0
    check=0
    bw=Image.open(a).load()
    while count<100:
        x=random.randint(20,150)
        y=random.randint(350,480)
        count=count+1
        if bw[x,y]==255:
            check=check+1
    if check>70:
        n=6
        side(c,s,n)

for a,(c,s) in imp.items():#8
    count=0
    check=0
    bw=Image.open(a).load()
    while count<100:
        x=random.randint(180,320)
        y=random.randint(350,480)
        count=count+1
        if bw[x,y]==255:
            check=check+1
    if check>70:
        n=7
        side(c,s,n)
        
for a,(c,s) in imp.items():#9        
    count=0
    check=0
    bw=Image.open(a).load()
    while count<100:
        x=random.randint(350,480)
        y=random.randint(350,480)
        count=count+1
        if bw[x,y]==255:
            check=check+1
    if check>70:
        n=8
        side(c,s,n)

        
print("US: ",US)
print("LS: ",LS)
print("FS: ",FS)
print("RS: ",RS)
print("BS: ",BS)
print("DS: ",DS)
        
browser=webdriver.Chrome("chromedriver")
browser.get("https://rubiks-cube-solver.com/")
mode=browser.find_element_by_id("toflatView")
mode.click()


color='color6' #assign

sk=1

for j in range (0,9):
    sk=str(sk)
    element = browser.find_element_by_id('sticker'+sk)
    if US[j]=='w':color='color1'
    if US[j]=='o':color='color2'
    if US[j]=='g':color='color3'
    if US[j]=='r':color='color4'
    if US[j]=='b':color='color5'
    if US[j]=='y':color='color6'
    browser.execute_script("arguments[0].setAttribute('class',arguments[1])", element,color)
    sk=int(sk)
    sk=sk+1
    
for j in range (0,9):
    sk=str(sk)
    element = browser.find_element_by_id('sticker'+sk)
    if LS[j]=='w':color='color1'
    if LS[j]=='o':color='color2'
    if LS[j]=='g':color='color3'
    if LS[j]=='r':color='color4'
    if LS[j]=='b':color='color5'
    if LS[j]=='y':color='color6'
    browser.execute_script("arguments[0].setAttribute('class',arguments[1])", element,color)
    sk=int(sk)
    sk=sk+1
    
for j in range (0,9):
    sk=str(sk)
    element = browser.find_element_by_id('sticker'+sk)
    if FS[j]=='w':color='color1'
    if FS[j]=='o':color='color2'
    if FS[j]=='g':color='color3'
    if FS[j]=='r':color='color4'
    if FS[j]=='b':color='color5'
    if FS[j]=='y':color='color6'
    browser.execute_script("arguments[0].setAttribute('class',arguments[1])", element,color)
    sk=int(sk)
    sk=sk+1
    
for j in range (0,9):
    sk=str(sk)
    element = browser.find_element_by_id('sticker'+sk)
    if RS[j]=='w':color='color1'
    if RS[j]=='o':color='color2'
    if RS[j]=='g':color='color3'
    if RS[j]=='r':color='color4'
    if RS[j]=='b':color='color5'
    if RS[j]=='y':color='color6'
    browser.execute_script("arguments[0].setAttribute('class',arguments[1])", element,color)
    sk=int(sk)
    sk=sk+1
    
for j in range (0,9):
    sk=str(sk)
    element = browser.find_element_by_id('sticker'+sk)
    if BS[j]=='w':color='color1'
    if BS[j]=='o':color='color2'
    if BS[j]=='g':color='color3'
    if BS[j]=='r':color='color4'
    if BS[j]=='b':color='color5'
    if BS[j]=='y':color='color6'
    browser.execute_script("arguments[0].setAttribute('class',arguments[1])", element,color)
    sk=int(sk)
    sk=sk+1
    
for j in range (0,9):
    sk=str(sk)
    element = browser.find_element_by_id('sticker'+sk)
    if DS[j]=='w':color='color1'
    if DS[j]=='o':color='color2'
    if DS[j]=='g':color='color3'
    if DS[j]=='r':color='color4'
    if DS[j]=='b':color='color5'
    if DS[j]=='y':color='color6'
    browser.execute_script("arguments[0].setAttribute('class',arguments[1])", element,color)
    sk=int(sk)
    sk=sk+1

time.sleep(.5)
url = browser.find_element_by_id("solveCube").get_attribute("href")
print (url)
browser.get(url)
mode=browser.find_element_by_id("toflatView")
mode.click()
key=input("Press any key to start:")
print("Starting...")
end=browser.find_element_by_class_name("hanysztep").text
end=end.split()
limit=end[0]
limit=int(limit)

for h in range(1,limit+1):
    h=str(h)
    id="algoritmusHanyadik"+h
    html=browser.find_element_by_id(id)
    code=html.text
    print(code)
    
h=int(h)
h+1
print("Solved")


