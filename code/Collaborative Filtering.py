# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:03:11 2019

Collaborative Filtering System

@author: jae woong Han
"""


import pandas as pd
from math import sqrt

# 파일불러오기
preference = pd.read_csv('journey csv file', encoding='utf-8')

# 분포도
preference.describe()

# 딕셔너리 리스트로 만들기 (리스트 목록)
import csv

f = open('./journey5.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

result = {}
Changdeokgung_Palace = ''
Gyeongbokgung_Palace = ''
Gwangmyeong_Cave = ''
Namhansanseong_Fortress = ''
Songdo_Central_Park = ''
Hwaseong_Fortress = ''
Ikseon_dong_Hanok_Street = ''
Daegwallyeong_Yangtte_Farm = ''
Vivaldi_Park = ''
Namiseom_Island = ''
Gamcheon_Village = ''
Jagalchi_Market = ''
Bulguksa_Temple = ''
Oedo_Isaland = ''
Taejongdae_Park = ''
Haeundae = ''
Yeosu = ''
Jeonju_Hanok_Village = ''
Boseong_Green_Tea_Village = ''
Daecheon_Beach = ''
Nakhwaam_Rock = ''
Anmyeondo_Island = ''
Seongsan_Ilchulbong_Tuff_Cone = ''
Udo_Isaland = ''
Hallasan_Dulegil = ''

for line in rdr:
    Changdeokgung_Palace = line[1]
    Gyeongbokgung_Palace = line[2]
    Gwangmyeong_Cave = line[3]
    Namhansanseong_Fortress = line[4]
    Songdo_Central_Park = line[5]
    Hwaseong_Fortress = line[6]
    Ikseon_dong_Hanok_Street = line[7]
    Daegwallyeong_Yangtte_Farm = line[8]
    Vivaldi_Park = line[9]
    Namiseom_Island = line[10]
    Gamcheon_Village = line[11]
    Jagalchi_Market = line[12]
    Bulguksa_Temple = line[13]
    Oedo_Isaland = line[14]
    Taejongdae_Park = line[15]
    Haeundae = line[16]
    Yeosu = line[17]
    Jeonju_Hanok_Village = line[18]
    Boseong_Green_Tea_Village = line[19]
    Daecheon_Beach = line[20]
    Nakhwaam_Rock = line[21]
    Anmyeondo_Island = line[22]
    Seongsan_Ilchulbong_Tuff_Cone = line[23]
    Udo_Isaland = line[24]
    Hallasan_Dulegil = line[25]
    break
            
for line in rdr:
    if 'NAME' in line[0] :
        continue
    result[line[0]] = {Changdeokgung_Palace: int(line[1]), Gyeongbokgung_Palace: int(line[2]), Gwangmyeong_Cave: int(line[3]), 
                       Namhansanseong_Fortress: int(line[4]), Songdo_Central_Park: int(line[5]), Hwaseong_Fortress: int(line[6]),
                       Ikseon_dong_Hanok_Street: int(line[7]), Daegwallyeong_Yangtte_Farm: int(line[8]), Vivaldi_Park: int(line[9]), 
                       Namiseom_Island: int(line[10]), Gamcheon_Village: int(line[11]), Jagalchi_Market: int(line[12]),
                       Bulguksa_Temple: int(line[13]), Oedo_Isaland: int(line[14]), Taejongdae_Park: int(line[15]),
                       Haeundae: int(line[16]), Yeosu: int(line[17]), Jeonju_Hanok_Village: int(line[18])
                      , Boseong_Green_Tea_Village: int(line[19]), Daecheon_Beach: int(line[20]), Nakhwaam_Rock: int(line[21]),
                       Anmyeondo_Island: int(line[22]), Seongsan_Ilchulbong_Tuff_Cone: int(line[23]), Udo_Isaland: int(line[24])
                      , Hallasan_Dulegil: int(line[25])}

result

# 0인 것은 평점이 아니기 때문에 딕셔너리에서 삭제

for outerKey in result:
    innerDict = result[outerKey]
    removingCandidates = []
    for innerKey in innerDict:
        if innerDict[innerKey] == 0:
            removingCandidates.append(innerKey)
    for candidate in removingCandidates:
        del innerDict[candidate]

print(result)


# 피어슨 상관계수 구하기
def sim_pearson(data, name1, name2):
    sumX=0 # X의 합
    sumY=0 # Y의 합
    sumPowX=0 # X 제곱의 합
    sumPowY=0 # Y 제곱의 합
    sumXY=0 # X*Y의 합
    count=0 #여행지 개수
    
    for i in data[name1]: 
        if i in data[name2]: # 같은 여행지를 평가했을때만
            sumX+=data[name1][i]
            sumY+=data[name2][i]
            sumPowX+=pow(data[name1][i],2)
            sumPowY+=pow(data[name2][i],2)
            sumXY+=data[name1][i]*data[name2][i]
            count+=1
    
    return ( sumXY- ((sumX*sumY)/count) )/ sqrt( (sumPowX - (pow(sumX,2) / count)) * (sumPowY - (pow(sumY,2)/count)))


# example
# 응답자 1번과 6번의 상관관계
sim_pearson(result,'1','6')


# 딕셔너리 돌면서 상관계수순으로 정렬
def top_match(data, name, index=3, sim_function=sim_pearson):
    li=[]
    for i in data: #딕셔너리를 돌고
        if name!=i: #자기 자신이 아닐때만
            try:
                li.append((sim_function(data,name,i),i)) #sim_function()을 통해 상관계수를 구하고 li[]에 추가
            except ZeroDivisionError:
                print("")
    li.sort() #오름차순
    li.reverse() #내림차순
    return li[:index]


# example
# 63번째의 응답자와 비슷한 상관관계를 가지는 유형자들의 내림차순
top_match(result, '63', 6)

# 여행지에 대한 추천 시스템
def getRecommendation (data,person,sim_function=sim_pearson):
    results = top_match(result, person ,len(data))
    
    simSum=0 # 유사도 합을 위한 변수
    score=0 # 평점 합을 위한 변수
    li=[] # 리턴을 위한 리스트
    score_dic={} # 유사도 총합을 위한 dic
    sim_dic={} # 평점 총합을 위한 dic
 
    for sim,name in results: # 튜플이므로 한번에 
        if sim<0 : continue #유사도가 양수인 사용자만
        for movie in data[name]: 
            if movie not in data[person]: #name이 평가를 내리지 않은 여행지
                score+=sim*data[name][movie] # 그사람의 여행평점 * 유사도
                score_dic.setdefault(movie,0) # 기본값 설정
                score_dic[movie]+=score # 합계 구함
 
                # 조건에 맞는 사람의 유사도의 누적합을 구한다
                sim_dic.setdefault(movie,0) 
                sim_dic[movie]+=sim
 
            score=0  #여행지가 바뀌었으니 초기화
    
    for key in score_dic: 
        score_dic[key]=score_dic[key]/sim_dic[key] # 평점 총합/ 유사도 총합
        li.append((score_dic[key],key)) # list((tuple))의 리턴을 위해서.
    li.sort() #오름차순
    li.reverse() #내림차순
    return li

# example
# 63번째 사용자가 가보지 않은 여행지에 대한 예상 평점
getRecommendation(result, '63')

