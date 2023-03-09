import math as m
import sys as s


# also important jest zakaz float ale
# Python's built-in float type has double precision (it's a C double in CPython, a Java double in Jython)

# Metoda Hornera: 'x' to najwyższa potęga,
# 'wielomian' to tablica ze współczynnikami w kolejności od najwyższej potęgi do zerowej (uważać na współczynnik 0)

def horner(wielomian, x):
    wartosc = wielomian[0]

    for i in range(1,
                   len(wielomian)):  # x^3 -2x^2 + 3x + 4 = x(x^2 - 2x + 3) + 4 = x(x(x - 2) + 3) - 4 -> działania po kolei:[[ w[0] * x + w[1] ] * x + w[2] ] * x + w[3]
        wartosc = wartosc * x + wielomian[
            i]  # 1*3 -2 = 1, then 1*3 + 3 = 6, then 6*3 + 4 = 22                                      [[ 1    * 3 + (-2) ] * 3 + 3    ] * 3 + 4

    return wartosc


# Test Metody Hornera
# wielomian = [1, -2, 3, 4]
# x = 3
# print("Wielomian wynosi: ", horner(wielomian,x))


# Funkcja potęgująca: miałem robić ale zobaczyłem to: 2^4
# print(2**4)

# Wybór funkcji: 'i' oznacza wybraną funkcję, 'x' wartość argumentu
# można inne zrobić if u care
def getValue(i, x):
    wn = [1.5, -2.5, 3.3, 4.1]  # na sztywno wpisane, by użyć w hornerze
    if i == 1:  # 1.5x^3 - 2.5x^2 + 3.3x + 4.1
        return horner(wn, x)
    elif i == 2:  # 2sin(x) + 3
        return 2 * m.sin(x) + 3
    elif i == 3:  # 1.4^x + 0.5
        return (1.4) ** x + 0.5
    elif i == 4:  # złożenie nr 1: x * cos(1.5^x+1)
        return x * m.cos((1.5) ** x + 1)
    elif i == 5:  # złożenie nr 2: 8^(x-1) * sin(cos(tan(x)))
        return 8 ** (x - 1) * m.sin(m.cos(m.tan(x)))
    elif i == 6:
        return x - 1
    else:  # zrobiłem tak że gdy użytkownik zjebie to bierze wielomian spod 1
        return horner(wn, x);


# Jak będzie sprawdzany znak?
# start = -100
# end = 100
# if (getValue(1, start) * getValue(1, end) < 0):
#    print("Na krańcach przedziału jest inny znak, czyli dalej w tym przedziale szukamy")


# Metoda bisekcji
def bisection(i, start, end, stoperan, iteracjopsilon):
    # i - wybrana funkcja
    # start i end - krańce przedziału
    # stoperan - przyjmuje dwie wartości i w zależności od niej warunkiem stopu jest osiagnięta dokładność (epsilon... ) lub liczba iteracji
    # iteracjopsilon - przechowuje wartość epsilonu lub liczby iteracji

    startValue = float(getValue(i, start))  # wpisuje do zmiennej by wielokrotnie(całe dwa razy) tego nie wyliczac
    endValue = float(getValue(i, end))  # wpisuje do zmiennej by wielokrotnie(całe dwa razy) tego nie wyliczac
    if (startValue * endValue > 0):
        print("Choosen section is incorrect.")
        s.exit()

    while True:
        m = float((start + end) / 2)  # wyznaczam środek przedziału
        tempValue = float(getValue(i, m))  # wpisuje do zmiennej by wielokrotnie tego nie wyliczac
        if (tempValue == 0):  # przypadek gdy 'm' to miejsce zerowe
            return m
        if (stoperan == 1):  # jeżeli stoperan jest na 1 to sprawdza dokładność
            if (abs(tempValue) < iteracjopsilon):
                return m
        if (
                tempValue * startValue > 0):  # w lewej części przedziału nie ma miejsca zerowego, to zmniejszamy go do rozmiaru prawej części
            start = m
        else:
            end = m  # przedział zmniejszamy do lewej części

        if (stoperan == 2):  # jeżeli stoperan jest na 2 to sprawdza ilość iteracji
            iterations = 1  # pierwsza iteracja to jeszcze niezmniejszony przedział chyba
            iterations = iterations + 1
            if (iteracjopsilon == iterations):
                return m


# Koniec bisekcji


# Metoda Reguly Falsi - jest ona bardzo podobna jak pisałem

def falsi(i, start, end, stoperan, iteracjopsilon):
    startValue = float(getValue(i, start))  # wpisuje do zmiennej by wielokrotnie(całe dwa razy) tego nie wyliczac
    endValue = float(getValue(i, end))  # wpisuje do zmiennej by wielokrotnie(całe dwa razy) tego nie wyliczac
    if (startValue * endValue > 0):
        print("Choosen section is incorrect.")
        s.exit()

    while True:
        c = float((startValue * end - endValue * start) / (startValue - endValue))  # wyznaczam punkt przecięcia z OX
        tempValue = float(getValue(i, c))  # wpisuje do zmiennej by wielokrotnie tego nie wyliczac
        if (tempValue == 0):  # przypadek gdy 'c' to miejsce zerowe
            return c
        if (stoperan == 1):  # jeżeli stoperan jest na 1 to sprawdza dokładność
            if (abs(tempValue) < iteracjopsilon):
                return c
        if (
                tempValue * startValue > 0):  # w lewej części przedziału nie ma miejsca zerowego, to zmniejszamy go do rozmiaru prawej części
            start = c
        else:
            end = c  # przedział zmniejszamy do lewej części

        if (stoperan == 2):  # jeżeli stoperan jest na 2 to sprawdza ilość iteracji
            iterations = 1  # pierwsza iteracja to jeszcze niezmniejszony przedział chyba
            iterations = iterations + 1
            if (iteracjopsilon == iterations):
                return m

# Koniec Reguly Falsi

# Interfejs
# Wybierz funkcję - 5 do wyboru [i]
# Wybierz przedział [start i end]
# Wybierz stoperan [stoperan]
# Wybierz epsilon/liczbę iteracji [iteracjopsilon]
# then
# bisection(i,start,end,stoperan,iteracjopsilon)
# falsi(i,start,end,stoperan,iteracjopsilon)
def menufunctions():
    print("Choose which function's zero you want to find:")
    print("1.Polynomial")
    print("2.Trigonometric Function")
    print("3.Exponential Function")
    print("4.Composition of polynomial and trigonometric functions")
    print("5.Composition of polynomial and exponential functions")
    print("6.Composition of trigonometric and exponential functions")

if __name__ == '__main__':
    i = -1   # deklaracja zmiennych do wyboru w programie
    start = 0
    end = 1
    stoperan = -1
    iteracjopsilon = 0.01

    print("Metody Numeryczne i Optymalizacja - Program #1")
    print("Comparison of bisection and regula falsi methods")
    menufunctions()
    print("If you want to end this program choose 0.")
    while(i < 0 or i > 6):
        i = int(input())
    if(i == 0):
        s.exit()

    print("Choose start of the section:")
    start = float(input())
    print("Choose end of the section:")
    end = float(input())
    if( start > end ):
        tmp = start
        start = end
        end = tmp

    while(stoperan < 1 or stoperan > 2 ):
        print("Choose when functions should stop:")
        print("1.Specified accuracy achieved")
        print("2.Number of iterations reached")
        stoperan = int(input())
        if(stoperan < 1 or stoperan > 2):
            print("Wrong data. Try again")

    if(stoperan == 1):
        print("Enter accuraccy:")
        iteracjopsilon = float(input())
    else:
        print("Enter number of iterations")
        iteracjopsilon = int(input())

    print("Zero found using bisection method: " + str(bisection(i,start,end,stoperan,iteracjopsilon)))
    print("Zero found using regula falsi method: " + str(falsi(i,start,end,stoperan,iteracjopsilon)))




