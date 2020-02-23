# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 23:12:34 2020

@author: Microsoft
"""

import numpy
import pandas as pd
import matplotlib.pyplot as plt
import math

V = 0
a = -9.8
posisiawal = input("Masukkan posisi awal : ")
pendekatannumerik = input("Masukkan Pendekatan numerik : ")
Yo = float(posisiawal)
delt = float(pendekatannumerik)
posanalitik = float(pendekatannumerik)
yanalitik = float(posisiawal)
yoanalitik = float(posisiawal)
t = 0
tanalitik = 0
i = 0
posisi = []
waktu = []
posisianalitik = []
waktuanalitik = []
print("Hasil Numerik")
while (Yo >= 0) :
    V = V + a*delt
    Yo = Yo + (V * delt)
    t = t + delt
    print("Nilai Posisi Numerik",round(Yo,3))
    print("Nilai Waktu Numerik",round(t,3))
    posisi.append(round(Yo,2))
    waktu.append(round(t,2))

print("Hasil Analitik")
while (yanalitik >= 0) :
    yanalitik = 0.5*a*(posanalitik*posanalitik)+yoanalitik
    i = i + 1 
    print("Nilai Waktu Analitik",round(posanalitik,3))
    print("Nilai Posisi",round(yanalitik,3))
    posisianalitik.append(round(yanalitik,2))
    waktuanalitik.append(round(posanalitik,2))
    posanalitik = posanalitik + delt
        
plt.plot(waktuanalitik,posisianalitik)
plt.plot(waktu,posisi)
plt.xlabel("waktu")
plt.ylabel("posisi")
plt.title("Posisi vs Waktu")
plt.legend(["Numerik","Analitik"])
plt.show()