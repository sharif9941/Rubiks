# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 01:36:08 2018

@author: Sharif
"""
      
from selenium import webdriver
import time

#S=[1,2,3,4,centre_piece=default,6,7,8,9]
#'w':color=white
#'o':color=orange
#'g':color=greeen
#'r':color=red
#'b':color=blue
#'y':color=yellow
#change text in US,FS,LS,RS,BS and DS  list

US=['w','w','w','w','w','w','w','w','w']
FS=['w','w','w','w','g','w','w','w','w']
LS=['w','w','w','w','o','w','w','w','w']
RS=['w','w','w','w','r','w','w','w','w']
BS=['w','w','w','w','b','w','w','w','w']
DS=['w','w','w','w','y','w','w','w','w']

        
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


color='color6' 
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


