# Reinforced Learning: takviyeli öğrenme : pekiştirmeli öğrenme
# bir ajanın(etmenin) belirli bir çevrede eylemler gerçekleştirerek ödül kazanmayı öğrenmesini sağlar
# amacı uzun vadeli en yüksek ödülü elde etmek için en iyi eylem stratejisini öğrenmektir

# UCB : upper confidence bound : üst güven sınırı

# One-Armed Bandit Problem (Tek Kollu Haydut Problemi): 
# Slot makinelerine benzer
# farklı seçeneklerden (makinelerden) hangisinin en yüksek ödülü verdiğini öğrenmeye çalışır
# objectif olarak seçilemeyen kararlarda kullanılır
# amacı zamanla en karlı seçeneği keşfetmek ve onu seçmektir
# reklam seçimi gibi karar alma süreçlerinde kullanılır.

# A/B Testi
# farklı seçeneklerin hangisinin daha başarılı olduğunu bulmak için faydalıdır

# greedy decisions : aç gözlü kararlar
# UCB Upper Confidence Bound : Üst Güven Sınırı 
# keşif ve sömürü arasında denge kurar
# bir yandan en iyi seçeneği sömürmek isterken diğer yandan yeni seçenekleri keşfetmeye devam eder
# keşif için seçilmemiş seçeneklere daha fazla şans tanır

# Reward - ödül
# bir eylemin sonucunda elde edilen geri bildirimdir
# ajanın belirli bir eylemi gerçekleştirdikten sonra aldığı sayısal değerdir
# ajanın o eylemi doğru yapıp yapmadığını gösterir
# Ajan bu ödülleri toplayarak en iyi eylemleri seçmeye ve uzun vadede en yüksek toplam ödülü kazanmaya çalışır

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Ads_CTR_Optimisation.csv')

# random sampling
# ramdom selection
# rastgele dağılması
import random

N = 10000 # reklamın kaç defa seçileceği
d = 10    # reklam sayısı
total_reward = 0 # toplam ödül miktarı
ads_selected = [] # seçilen reklamların listesi

for n in range(0, N):
    ad = random.randrange(d)
    ads_selected.append(ad)
    reward = data.values[n, ad] # verilerdeki n. satır ve ad sütunu 1 ise ödül 1
    total_reward += reward
    
plt.hist(ads_selected)
plt.show()

# Üst Güven Sınırı (UCB)
import math

N = 10000 # 10.000 tıklama
d = 10    # Toplam 10 reklam
# Ri(n)
rewards = [0] * d # başlangıçta tüm reklamların ödülü 0
# Ni(n)
clicks = [0] * d  # o ana kadar ki tıklamalar
total_reward = 0  # toplam ödül
ads_selected = []

for n in range(1, N):
    ad = 0  # seçilen reklam
    max_ucb = 0
    for i in range(0, d):
        if clicks[i] > 0:
            avg_reward = rewards[i] / clicks[i]
            delta_i = math.sqrt(3/2 * math.log(n) / clicks[i])
            ucb = avg_reward + delta_i
        else:
            ucb = N * 10
        # upper confidence bound Üst güven sınırı değeri en büyük olan reklamı bul
        if max_ucb < ucb:  # daha büyük bir UCB değeri bulundu
            max_ucb = ucb
            ad = i
    ads_selected.append(ad)
    clicks[ad] += 1
    reward = data.values[n, ad]  # verilerdeki n. satır ve ad sütunu 1 ise ödül 1
    rewards[ad] += reward
    total_reward += reward

print('Toplam Ödül:')   
print(total_reward)

plt.hist(ads_selected)
plt.show()


# ödül, reklam seçiminin ne kadar başarılı olduğunu (kullanıcı tarafından tıklanma durumu) ifade eder
# ajan, en çok ödül getiren (yani tıklanma oranı en yüksek) reklamı öğrenmeye çalışır.

# ucb algoritması 
# 1. her turda (tur sayısı n) her reklam alternatifi (i) için aşağıdaki sayılar tutulur
# Ni(n): i sayılı reklamın o ana kadarki tıklanma sayısı
# Ri(n): o ana kadar ki i reklamından gelen toplam ödül
# 2. değerler hesaplanır
# o ana kadar ki her reklamın ortalama ödülü = Ri(n) / Ni(n)
# güven aralığı için aşağı ve yukarı oynama potansiyeli di(n) * sqrt( 3/2 * ( log(n) / Ni(n) ))
# en yüksek ucb değerine sahip olan reklam seçilir