# thompson sampling : thompson örneklemesi
# veri eksikse veya belirsizlik varsa ve sistemin performansı hakkında tahminde bulunman gerekiyorsa kullanılır

# 1. her aksiyon için iki sayı hesaplanır
# Ni1(n) : o ana kadar ödül olarak 1 gelme sayısı
# Ni0(n) : o ana kadar ödül olarak 0 gelme sayısı
# 2. her seçenek için beta dağılımında rastgele bir sayı üretilir
# en yüksek beta değerine sahip olan seçenek seçilir

# her makinenin farklı bir dağılımı (beta dağılımı) vardır, amacı bu dağılıma lineer yaklaşarak orta değeri bulmaktır



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Ads_CTR_Optimisation.csv')

# random Selection (Rasgele Seçim)
import random

N = 10000
d = 10 
toplam = 0
secilenler = []
for n in range(0,N):
    ad = random.randrange(d)
    secilenler.append(ad)
    odul = data.values[n,ad] # verilerdeki n. satır = 1 ise odul 1
    toplam = toplam + odul
    
    
plt.hist(secilenler)
plt.show()


import random
#UCB
N = 10000 # 10.000 tıklama
d = 10  # toplam 10 ilan var
#Ri(
#Ni(n)
toplam = 0 # toplam odul
secilenler = []
# tıklamalar
birler = [0] * d
sifirlar = [0] * d
for n in range(1,N):
    ad = 0 #seçilen ilan
    max_th = 0
    for i in range(0,d):
        # beta dağılımı
        rasbeta = random.betavariate ( birler[i] + 1 , sifirlar[i] +1)
        if rasbeta > max_th:
            max_th = rasbeta
            ad = i
    secilenler.append(ad)
    odul = data.values[n,ad] # verilerdeki n. satır = 1 ise odul 1
    if odul == 1:
        birler[ad] = birler[ad]+1
    else :
        sifirlar[ad] = sifirlar[ad] + 1
    toplam = toplam + odul
print('Toplam Odul:')   
print(toplam)

plt.hist(secilenler)
plt.show()
