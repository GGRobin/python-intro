# -------------------------------------------------------
# Autor: Adam Kubicki
# Zadanie 1 - Laboratorium 1 (Python Intro)
# -------------------------------------------------------
# Cel programu:
# 1. Połączenie dwóch list przy użyciu funkcji wbudowanej zip()
# 2. Użycie funkcji sqrt() z modułu math
# 3. Obsługa wyjątków (ValueError, ZeroDivisionError)
# -------------------------------------------------------

# importujemy moduł math z biblioteki standardowej
import math  # dokumentacja: https://docs.python.org/3/library/math.html

# tworzymy dwie listy z wartościami liczbowymi
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# łączymy listy w pary przy pomocy funkcji zip()
polaczone = list(zip(lista1, lista2))  # dokumentacja: https://docs.python.org/3/library/functions.html#zip
print("Połączone listy:", polaczone)

# używamy funkcji sqrt() z modułu math do obliczenia pierwiastka kwadratowego
pierwiastek = math.sqrt(16)
print("Pierwiastek z 16 to:", pierwiastek)

# obsługa wyjątków - zabezpieczenie przed błędnym inputem
try:
    liczba = int(input("Podaj liczbę całkowitą: "))
    wynik = 10 / liczba
    print("Wynik dzielenia:", wynik)

# jeśli użytkownik poda coś, co nie jest liczbą
except ValueError:
    print("Błąd: wprowadź liczbę całkowitą!")

# jeśli użytkownik wpisze 0 (dzielenie przez zero)
except ZeroDivisionError:
    print("Błąd: nie można dzielić przez zero!")
