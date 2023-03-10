import sys as s
import matplotlib.pyplot as plot
import numpy as num
from HelperFunctions import getValue

# also important jest zakaz float ale
# Python's built-in float type has double precision (it's a C double in CPython, a Java double in Jython)


# krotka z human-readable nazwami funkcji
functions = ('0.1x\u00b3 - 2x\u00b2 + x + 13', '3sin(x)', '3\u02e3 - 2', 'sin(0.1x\u00b3 - 2x\u00b2 + x + 13',
             '2^(0.1x\u00b3 - 2x\u00b2 + x + 13) - 13', '1.3^(13cos(x) - 1')


# Metoda bisekcji
def bisection(i, start, end, stoperan, iteracjopsilon):
    # i - wybrana funkcja
    # start i end - krańce przedziału
    # stoperan - przyjmuje dwie wartości i w zależności od niej warunkiem stopu jest osiagnięta dokładność (epsilon... ) albo liczba iteracji
    # iteracjopsilon - przechowuje wartość epsilonu lub liczby iteracji

    startValue = float(getValue(i, start))  # wpisuje do zmiennej by wielokrotnie tego nie wyliczac
    endValue = float(getValue(i, end))  # wpisuje do zmiennej by wielokrotnie tego nie wyliczac
    if (startValue * endValue > 0):
        print("Choosen section is incorrect.")
        s.exit()
    iterations = 0
    while True:
        iterations = iterations + 1
        m = float((start + end) / 2)  # wyznaczam środek przedziału
        tempValue = float(getValue(i, m))  # wpisuje do zmiennej by wielokrotnie tego nie wyliczac
        if (tempValue == 0):  # przypadek gdy 'm' to miejsce zerowe
            return m, iterations
        if (stoperan == 1):  # jeżeli stoperan jest na 1 to sprawdza dokładność
            if (abs(tempValue) < iteracjopsilon):  # abs, bo moduł funkcji w wymaganiach
                return m, iterations
        if (
                tempValue * startValue > 0):  # w lewej części przedziału nie ma miejsca zerowego, zmniejszamy go do rozmiaru prawej części
            start = m
        else:
            end = m  # przedział zmniejszamy do lewej części

        if (stoperan == 2):  # jeżeli stoperan jest na 2 to sprawdza liczbę iteracji
            if (iteracjopsilon == iterations):
                return m, iterations


# Koniec bisekcji


# Metoda Reguly Falsi - jest ona bardzo podobna jak pisałem

def falsi(i, start, end, stoperan, iteracjopsilon):
    startValue = float(getValue(i, start))  # wpisuje do zmiennej by wielokrotnie(całe dwa razy) tego nie wyliczac
    endValue = float(getValue(i, end))  # wpisuje do zmiennej by wielokrotnie(całe dwa razy) tego nie wyliczac
    if (startValue * endValue > 0):
        print("Chosen section is incorrect.")
        s.exit()
    iterations = 0  # pierwsza iteracja to jeszcze niezmniejszony przedział
    while True:
        iterations = iterations + 1
        x1 = float(
            (startValue * end - endValue * start) / (startValue - endValue))  # wyznaczam punkt przecięcia cięciwy z OX
        tempValue = float(getValue(i, x1))  # wpisuje do zmiennej by wielokrotnie tego nie wyliczac
        if (tempValue == 0):  # przypadek gdy 'x1' to miejsce zerowe
            return x1, iterations
        if (stoperan == 1):  # jeżeli stoperan jest na 1 to sprawdza dokładność
            if (abs(tempValue) < iteracjopsilon):
                return x1, iterations
        if (
                tempValue * startValue > 0):  # w lewej części przedziału nie ma miejsca zerowego, to zmniejszamy go do rozmiaru prawej części
            start = x1
        else:
            end = x1  # przedział zmniejszamy do lewej części

        if (stoperan == 2):  # jeżeli stoperan jest na 2 to sprawdza liczbę iteracji
            if (iteracjopsilon == iterations):
                return x1, iterations


# Koniec Reguly Falsi

def menufunctions():
    print("Choose which function's zero you want to find:")
    print("1.Polynomial: " + functions[0])
    print("2.Trigonometric Function: " + functions[1])
    print("3.Exponential Function: " + functions[2])
    print("4.Composition of polynomial and trigonometric functions: " + functions[3])
    print("5.Composition of polynomial and exponential functions: " + functions[4])
    print("6.Composition of trigonometric and exponential functions: " + functions[5])


# Rysowanie wykresu funkcji
def plots(i, start, end, x0):
    density = float(0.1)
    offset = (end - start) * 0.2  # pewne przesunięcie, żeby narysować trochę więcej wykresu funkcji
    oX_values = num.arange(start - offset, end + offset, density)  # gotowa lista argumentów
    oY_values = [getValue(i, x) for x in oX_values]  # generowanie listy na podstawie innej listy
    plot.plot(oX_values, oY_values)  # rysowanie wykresu
    plot.scatter(x0, getValue(i, x0), color='red')
    plot.axhline(0, color='black')
    plot.axvline(0, color='black')
    plot.xlabel("X")
    plot.ylabel("Y")
    plot.title(functions[i - 1])
    plot.show()


if __name__ == '__main__':
    i = -1  # deklaracja zmiennych do wyboru w programie
    start = 0
    end = 1
    stoperan = -1
    iteracjopsilon = 0.01

    print("Metody Numeryczne i Optymalizacja - Program #1")
    print("Comparison of bisection and regula falsi methods")
    menufunctions()
    print("If you want to end this program choose 0.")
    while (i < 0 or i > 6):
        i = int(input())
    if (i == 0):
        s.exit()

    print("Choose start of the section:")
    start = float(input())
    print("Choose end of the section:")
    end = float(input())
    if (start > end):
        tmp = start
        start = end
        end = tmp

    while (stoperan < 1 or stoperan > 2):
        print("Choose when methods should stop:")
        print("1.Specified accuracy achieved")
        print("2.Number of iterations reached")
        stoperan = int(input())
        if (stoperan < 1 or stoperan > 2):
            print("Wrong data. Try again")

    if (stoperan == 1):
        print("Enter accuraccy:")
        iteracjopsilon = float(input())
    else:
        print("Enter number of iterations")
        iteracjopsilon = int(input())

    x0, iterations = bisection(i, start, end, stoperan, iteracjopsilon)
    print("Zero found using bisection method: " + str(x0))
    print("Iterations: " + str(iterations))
    plots(i, start, end, x0)
    x0, iterations = falsi(i, start, end, stoperan, iteracjopsilon)
    print("Zero found using regula falsi method: " + str(x0))
    print("Iterations: " + str(iterations))
    # plots(i, start, end, x0)
