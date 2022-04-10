d, m, a = int(input("Dia: ")), int(input("Mês: ")), int(input("Ano: "))
if m == 2:
    r = a % 4
    if r == 0:
        if d > 0 and d < 30:
            print("Valid")
        else:
            print("Invalid")
    else:
        if d > 0 and d < 29:
            print("Valid")
        else:
            print("Invalid")
else:
    if m == 4 or m == 6 or m == 9 or m == 11:
        if d > 0 and d < 31:
            print("Valid")
        else:
            print("Invalid")
    else:
        if d > 0 and d < 32:
            print("Valid")
        else:
            print("Invalid")