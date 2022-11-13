import matplotlib.pyplot as plt
import random
import math
import time


fig2, gr2 = plt.subplots()
gr2.set_facecolor("black")
gr2.set_title("Функция random")
gr2.set_xlabel("N", fontsize=14, fontweight="normal")
gr2.set_ylabel("Псевдослучайное число", fontsize=14, fontweight="normal")

fig1, gr1 = plt.subplots()
gr1.set_facecolor("black")
gr1.set_xlabel("N", fontsize=14, fontweight="normal")
gr1.set_ylabel("Псевдослучайное число", fontsize=14, fontweight="normal")

figravn1, grravn = plt.subplots()
grravn.set_facecolor("white")
grravn.set_title("Тестирование равномерного распределения")
grravn.set_xlabel("Номер интервала", fontsize=14, fontweight="normal")
grravn.set_ylabel("Частота попадания в интервал", fontsize=14, fontweight="normal")

figravn2, grstat = plt.subplots()
grstat.set_facecolor("white")
grstat.set_title("Проверка статистической независимости")
grstat.set_xlabel("Длина последовательности", fontsize=14, fontweight="normal")
grstat.set_ylabel("Корреляция пар чисел", fontsize=14, fontweight="normal")

print("1 - метод серединных квадратов\n2 - метод серединных произведений\n3 - метод перемешивания\n4 - линейный конгруэнтный метод")
while True:
    num = int(input("Введите номер метода: "))
    if(0<num<5):
        break
    else:
        print("Введите другой номер")
    
n = int(input("Введите длину последовательности: "))

i=0
r = 0.24681012
ri2 = 0.12345678
m=99999999
a=12345676
b=12345
r1 = []
r2 = []
ri = 1
B = []
ix = []
iy = []
x1i = []
x2i = []
B1 = [1,2,3,4,5,6,7,8,9,10]
B2 = [0,0,0,0,0,0,0,0,0,0]
ai = 0
Br=[]
R = []
ki = 10

while ki<n:
    Br.append(ki)
    ki+=1

i=0

def ravn(r1, n): #проверка равномерного распределения
    i=0
    j=0
    while i<n: #цикл нахождения количества интервалов
        ai = 10*r1[i]
        ai = list(str(ai))
        ai = ai[0:1]
        ai = 1+int(''.join(ai))
        B2[ai-1]+=1
        i+=1
    while j<10: #их преобразование в дробное
        B2[j]/=n
        j+=1
    print("B = ", B2)
    grravn.scatter(B1, B2, c = "red", marker=".") #вывод графика
    
def MD(r1, n): #метод равномерного распределения с мат. ожиданием и дисперсией
    i=0
    s1=0
    s2=0
    while i<n: #цикл нахождения суммы
        s1 += r1[i]
        s2 += r1[i]**2
        i+=1
    M = s1/n #мат. ожидание
    D = s2/n - M**2 #дисперсия
    print("M = ", M)
    print("D = ", D)
    
def stat(r1, n): #проверка статистической независимости
    i=10
    sg=0
    while i<n: #цикл нахождения R
        g=0
        sg=0
        while g<i: #цикл нахождения суммы для мат. ожидания
            sg += r1[g]*r1[g+1]
            g+=1
        R.append((sg/i)*12-3)
        i+=1
    grstat.scatter(Br, R, c = "red", marker=".") #вывод графика
    
i=0

if(num == 1):
    gr1.set_title("Метод серединных квадратов")
    while i<(n*2):
        rlen = len(str(r))-2 #вычисляется разрядность
        ri *= 10**rlen #определение разряда десятичной части
        x = r*ri #перевод десятичного значения в целое число
        x2 = x*x #запись десятичных частей числа в xi
        x = x2 // (ri) #взятие середины полученного числа
        x = int(x%(10**rlen))
        ri = x #присвоение нового значения r
        if(i>=n): #условия занесения значения в координаты x и y соответственно
            r1.append(ri/(10**rlen)) 
            ix.append(random.random())
        else:
            r2.append(ri/(10**rlen))
            iy.append(random.random())
        i+=1
    print(ravn(r1, n))
    print(MD(r1, n))
    print(stat(r1, n))
       
if(num == 2):
    gr1.set_title("Метод серединных произведений")
    while i<(n*2):
        rlen = len(str(r))-2 #вычисляется разрядность
        ri *= 10**rlen #определение разряда десятичной части
        x1 = r*ri #перевод десятичного значения в целое число
        x2 = ri2*ri #перевод десятичного значения в целое число
        xi = x1*x2 #запись десятичных частей числа в xi
        x = xi // (ri) #взятие середины полученного числа
        x = int(x%(10**rlen))
        ri = x #присвоение нового значения r
        if(i>=n): #условия занесения значения в координаты x и y соответственно
            r1.append(ri/(10**rlen)) 
            ix.append(random.random()) 
        else:
            r2.append(ri/(10**rlen))
            iy.append(random.random())
        ri2 = ri/(10**rlen) #запоминание предыдущего числа 
        i+=1
    print(ravn(r1, n))
    print(MD(r1, n))
    print(stat(r1, n))
    
if(num == 3):
    gr1.set_title("Метод перемешивания")
    while i<(n*2):
        j = 0
        k = 0
        h = 0
        razr = len(str(r))-2 #вычисление длины строки
        ri = 10**razr #определение разряда десятичной части
        xi = r*ri #перевод десятичного значения в целое число
        per = str(xi) #перевод значения в строку, затем в массив
        per = list(per)
        x1i = per[(razr//4):razr] #взятие среза без начальных (конечных) значений соответственно
        x2i = per[-(razr//4)-2:-2]
        while k<razr//4: #взятие среза оставшихся значений значений
            x1i.append(per[k])
            k+=1
        while j<razr-2:
            x2i.append(per[j])
            j+=1
        while x1i[h]=="0": #условия, при которых убираются левые значения равные нулю, во избежание вырождения
            ran = random.randint(0,9)
            ran = str(ran)
            if(x1i[h]=="0"):
                x1i.append(ran)
            h+=1
        h=0
        while x2i[h]=="0":
            ran = random.randint(0,9)
            ran = str(ran)
            if(x2i[h]=="0"):
                x2i.append(ran)
            h+=1
        h=0
        x1i = float(''.join(x1i)) #перевод строковых значений обратно в числа
        x2i = float(''.join(x2i))
        xsum = x1i + x2i #суммирование чисел
        if(len(str(xsum))-2>razr): #условие, когда длина получившегося значения больше необходимых
            xsum = list(str(xsum))
            xsum = xsum[1:-2] #отбрасывание левого бита
            while xsum[h]=="0": #условие, при котором убираются левые значения равные нулю, во избежание вырождения
                ran = random.randint(0,9)
                ran = str(ran)
                if(xsum[h]=="0"):
                    xsum.append(ran)
                h+=1
            xsum = float(''.join(xsum))
        if(i>=n): #условия занесения значения в координаты x и y соответственно
            r1.append(xsum/(10**razr))
            ix.append(random.random())
        else:
            r2.append(xsum/(10**razr))
            iy.append(random.random())  
        r = xsum #присвоение нового значения r
        R1 = ix
        i+=1
    print(ravn(R1, n))
    print(MD(R1, n))
    print(stat(R1, n))
        
if(num==4):
    gr1.set_title("Линейный конгруэнтный метод") 
    seed = time.time() #взятие текущего времени
    l = len(str(m)) #длина значения M
    n=n*2
    rl = [0 for i in range(n)] #создание массива rl
    rl[0]=math.ceil(seed) #округление начального значения до большего для разных значений при каждом запуске
    for i in range(1,n):
        rl[i]=math.ceil(math.fmod((a*rl[i-1]+b),m)) #рекуррентная формула
        if(i>=n/2): #условия занесения значения в координаты x и y соответственно
            r1.append(rl[i]/10**l) 
            ix.append(random.random()) 
        if(i<=n/2):
            r2.append(rl[i]/10**l)
            iy.append(random.random())
    print(ravn(r1, n/2))
    print(MD(r1, n/2))
    print(stat(r1, n/2))
    
gr1.scatter(r1, r2, c = "deeppink", marker=".") #вывод графика метода
gr2.scatter(ix, iy, c = "deeppink", marker=".") #вывод графика рандома
plt.show() #вывод графика теста равномерного распределения
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
