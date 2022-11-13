import random
import math
import time

m=99999999
a=12345676
b=12345
r1 = []
n = 37
p=36
my = 0   
i = 0
startmoney = 1000 # сколько денег будет на старте
c = 0.1 # коэффициент ставки
win = 0 # количество побед
loose = 0 # количество проигрышей
games = 0 # количество игр
balance = [] # статистика 1
games = [] # статистика 2


money = startmoney # начинаем играть с полной суммой


#линейный конгруэнтный метод
def lkm(seed,n):
    l = len(str(m))
    r = [0 for i in range(n)]
    r[0]=math.ceil(seed)
    for i in range(1,n):
        r[i]=math.ceil(math.fmod((a*r[i-1]+b),m))
        r1.append(r[i]/10**l) 
    return r1


# играем, пока у нас есть деньги
while money > 0:
    ran = random.randint(0,36)
    t0=time.time()
    # print(t0)
    rk = lkm(t0,n) 
    # print(rk)
    num = rk[ran] #присвоение рандомного числа из последовательности рандомных чисел
    # print(num)
    num = int(num*100)  #преобразование этого числа в обычное число для игры
    if num>p:
        num=int(num/2.75)
    
    bet = startmoney * c # ставка —  постоянная часть от первоначальной суммы
    
    v = int(input("Введите число(сделайте ставку) от 0 до 36: "))
    
    rk = lkm(t0,n) 
    # print(rk)
    num = rk[ran] #присвоение рандомного числа из последовательности рандомных чисел
    # print(num)
    num = int(num*100)  #преобразование этого числа в обычное число для игры
    if num>p:
        num=int(num/2.75)
    
    if bet > money: # если ставка получилась больше, чем у нас осталось денег — ставим всё, что осталось, чтобы не уйти в минус
        bet = money # после ставки количество денег уменьшилось
    money -= bet
    balance.append(money) # записываем очередную игру в статистику — деньги и номер игры 
    games.append(len(games)+1) # крутим рулетку, на которой 37 чисел, включая 0. Мы ставим на конкретное число
    print("Вы сделали ставку на число: " + str(v))
    print("Шарик попал на число: " + str(num))
    if v == num: # условие выигрыша
        money += bet * 2 # получаем назад нашу ставку в двойном размере
        win += 1 # увеличиваем количество побед
        print("Вы выиграли")
    else:
        loose += 1 # иначе — увеличиваем количество проигрышей
        print("Вы проиграли")

games = win + loose
print("Выиграно ставок: " + str(win) + " (" + str(win/games * 100) + "%). " + " Проиграно ставок: " + str(loose)  + " (" + str(loose/games * 100) + "%). ") # выводим результат игры по первой стратегии






















