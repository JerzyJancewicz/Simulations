import math


choice = input("Wprowadź jednostkę w której bedziesz wprowadzał wartość x: "
                "\n Wpisz 'r', żeby wporwadzic wartosc w radianach"
                "\n Wpisz 's', żeby wporwadzic wartosc w stopniach\n")

while choice != 'r' or choice != 's':
    if choice == 'r' or choice == 's':
        break
    else:
        print("\nNiepoprawna jednostka")
        choice = input("Wprowadź jednostkę jeszcze raz: "
                       "\n Wpisz 'r', żeby wporwadzic wartosc w radianach"
                       "\n Wpisz 's', żeby wporwadzic wartosc w stopniach\n")

value = input("Wprowadź wartość x w "+"'"+choice+"'"+": ")


def taylor(x, times):
    taylor_sin = x - ((x ** 3) / math.factorial(3))
    tmp_taylor = taylor_sin
    z = 5
    for a in range(times):
        if a % 2 == 0:
            taylor_sin = tmp_taylor + ((x ** z) / math.factorial(z))
        else:
            taylor_sin = tmp_taylor - ((x ** z) / math.factorial(z))
        tmp_taylor = taylor_sin
        z = z + 2

    return taylor_sin


def check_x(numb):
    numb_normalized = numb % (2 * math.pi)

    if 0 < numb_normalized <= math.pi/2:
        return numb_normalized
    elif math.pi/2 < numb_normalized <= math.pi:
        return math.pi - numb_normalized
    elif math.pi < numb_normalized <= 3/2*math.pi:
        return math.pi - numb_normalized
    elif 3/2*math.pi < numb_normalized <= 2*math.pi:
        return numb_normalized - 2*math.pi
    else:
        return 0


taylor_numb = 0
b_sin = 0
if choice == 's':
    radian = math.radians(float(value))
    b_sin = math.sin(radian)
    taylor_numb = taylor(check_x(radian), 10)
elif choice == 'r':
    b_sin = math.sin(float(value))
    taylor_numb = taylor(check_x(float(value)), 10)

measurement_error = b_sin - taylor_numb

print("taylor: "+str(taylor_numb) + "\n" + "sin: " + str(b_sin) + "\n" + "measurement error: " + str(measurement_error))
