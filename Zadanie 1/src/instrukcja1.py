print("Zadanie1")

operation = ""
op = ""
x = 0
y = 1
z = 0

#modulo
division = int(x)/int(y)
rest = int(x)%int(y)
result = "Wynik dzielenia:", division, "Reszta z dzielenia:", rest

def calc():

    #działania
    operators = {"+": x+y, "-": x-y, "*": x*y, "/": x/y, "mod": result}
    global op
    global operation

    if z == "1":
        print(operators["+"])
        op = (operators["+"])
        operation = "dodawanie "
    elif z == "2":
        print(operators["-"])
        op = (operators["-"])
        operation = "odejmowanie "
    elif z == "3":
        print(operators["*"])
        op = (operators["*"])
        operation = "mnozenie "
    elif z == "4":
        print(operators["/"])
        op = (operators["/"])
        operation = "dzielenie "
    elif z == "5":
        print(operators["mod"])
        op = (operators["mod"])
        operation = "modulo "
    else:
        print("Wybrałeś nieprawidłowy numer operacji!")


def history():
    #historia
    file = open('historia.txt', 'a')
    try:
        import readline
    except ImportError:
        import pyreadline as readline
        print(readline.get_current_history_length())
    file.write(str(readline.get_current_history_length()))

def saveToLogFile():
    #zapisywanie logów do pliku
    f = open('logs.txt', 'a')
    f.write("Data operacji: ")
    import time;
    localtime = time.asctime( time.localtime(time.time()) )
    f.write(str(localtime))
    f.write(", Pierwsza liczba: ")
    f.write(str(x))
    f.write(", Druga liczba: ")
    f.write(str(y))
    f.write(", Operacja: ")
    f.write(operation)
    f.write(", Wynik: ")
    f.write(str(op))
    f.write("\n")
    f.close()

while True:
    menu = int(input("Wybierz funkcję:\n1)Kalkulator\n2)Historia\n0)Koniec programu\n"))

    if menu == 1:
        x = int(input("Podaj pierwszą liczbę:"))
        y = int(input("Podaj drugą liczbę:"))
        z = input("Wybierz jaką operację chcesz wykonać na liczbach: 1-dodawanie, 2-odejmowanie, 3-mnożenie, 4-dzielenie, 5-modulo: ")
        calc()
        saveToLogFile()
    elif menu == 2:
        history()
    elif menu == 0:
        break