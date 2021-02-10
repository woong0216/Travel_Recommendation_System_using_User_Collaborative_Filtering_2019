# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 16:03:11 2019

Test Rating

@author: jae woong Han
"""

import pandas as pd
from math import sqrt

import csv

f = open('./distribution csv file', 'r', encoding='utf-8')
rdr = csv.reader(f)

result = {}
A = ''
B = ''
C = ''
D = ''
for line in rdr:
    A = line[1]
    B = line[2]
    C = line[3]
    D = line[4]
    break
            
for line in rdr:
    if 'NAME' in line[0]:
        continue
    
    result[line[0]] = {A: int(line[1]), B: int(line[2]), C: int(line[3]), D: int(line[4])}

result

print(result)

# font
from matplotlib import font_manager, rc
from matplotlib import pyplot as plt
font_name = font_manager.FontProperties(fname="malgun.ttf").get_name()
rc('font', family=font_name)



#각 축의 크기 설정
plt.figure(figsize=(14,8))
plt.axis([0,6,0,6]) # 그래프의 x축,y축 크기설정
plt.show()

def drawGraph(data, name1, name2):
    plt.figure(figsize=(14, 8))  # plot 크기설정

    # plot 좌표를 위한 list 선언
    li = []
    li2 = []
    for i in result[name1]:  # i = 키 값
        if i in data[name2]:  # 같은 여행지 평가
            li.append(result[name1][i])  # name1의 평점 li[]에 추가
            li2.append(result[name2][i])  # name2의 평점 li2[]에 추가
            plt.text(result[name1][i], result[name2][i], i)  # 여행지 일치된 text 넣기

    plt.plot(li, li2, 'ro')  # plot그리기

    # 각 축의 크기 설정 (0에서 6까지)
    plt.axis([0, 6, 0, 6])

    # x축과 y축 이름 설정
    plt.xlabel(name1)
    plt.ylabel(name2)

    # 그리기
    plt.show()
drawGraph(result,'journey 1','journey 2')


# 피어슨 상관계수 구하기
def sim_pearson(data, name1, name2):
    sumX=0 # X의 합
    sumY=0 # Y의 합
    sumPowX=0 # X 제곱의 합
    sumPowY=0 # Y 제곱의 합
    sumXY=0 # X*Y의 합
    count=0 #영화 개수
    
    for i in data[name1]: # i = key
        if i in data[name2]: # 같은 여행지 평가했을때만
            sumX+=data[name1][i]
            sumY+=data[name2][i]
            sumPowX+=pow(data[name1][i],2)
            sumPowY+=pow(data[name2][i],2)
            sumXY+=data[name1][i]*data[name2][i]
            count+=1
    
    return ( sumXY- ((sumX*sumY)/count) )/ sqrt( (sumPowX - (pow(sumX,2) / count)) * (sumPowY - (pow(sumY,2)/count)))




def getRecommendation (data,person,sim_function=sim_pearson):
    results = top_match(result, person ,len(data))
    
    simSum=0 # 유사도 합을 위한 변수
    score=0 # 평점 합을 위한 변수
    li=[] # 리턴을 위한 리스트
    score_dic={} # 유사도 총합을 위한 dic
    sim_dic={} # 평점 총합을 위한 dic
 
    for sim,name in results: # 튜플이므로 한번에 
        if sim<0 : continue #유사도가 양수인 사람만
        for movie in data[name]: 
            if movie in data[person]: #name이 평가를 내리지 않은 여행지
                score+=sim*data[name][movie] # 그사람의 여행지평점 * 유사도
                score_dic.setdefault(movie,0) # 기본값 설정
                score_dic[movie]+=score # 합계 구함
 
                # 조건에 맞는 사람의 유사도의 누적합을 구한다
                sim_dic.setdefault(movie,0) 
                sim_dic[movie]+=sim
 
            score=0  #여행지가 바뀌었으니 초기화함
    
    for key in score_dic: 
        score_dic[key]=score_dic[key]/sim_dic[key] # 평점 총합/ 유사도 총합
        li.append((score_dic[key],key)) # list((tuple))의 리턴을 위해서.
    li.sort() #오름차순
    li.reverse() #내림차순
    return li


getRecommendation(result, 'journey 1')
