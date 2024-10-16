Startgeld = 1
Prozentsatz_0_1 = round(0.001,3)
Prozentsatz_i = round(0)
Zähler = 1
with open("my_file.txt", "w") as file:
    file.write(f"Prozentsatz\tNach d*Tagen hat man 99.999% des Geldes\n")
    while Zähler > 0 and Prozentsatz_i <= 1/30.4375:
        Prozentsatz_i += Prozentsatz_0_1/30.4375
        Zähler -= Prozentsatz_0_1/30.4375
        Geld = 1
        Tage = 0
        Zähler = round(Zähler,3)
        while Geld > 0.00001:
            Tage += 1
            Geld = Geld*(1-Prozentsatz_i)
        if (Prozentsatz_i*100)*30.4375 >= 100:
            break
        file.write(f"{round((Prozentsatz_i*100)*30.4375,3)}%\t{Tage}\n")
Startgeld = 1
Prozentsatz_0_1 = round(0.001,3)
Prozentsatz_i = round(0)
Zähler = 1
with open("my_file2.txt", "w") as file:
    file.write(f"Prozentsatz\tNach m*Monaten hat man 99.999% des Geldes\n")
    while Zähler > 0 and Prozentsatz_i <= 1:
        Prozentsatz_i += Prozentsatz_0_1
        Zähler -= Prozentsatz_0_1
        Geld = 1
        Monate = 0
        Zähler = round(Zähler,3)
        while Geld > 0.01:
            Monate += 1
            Geld = Geld*(1-Prozentsatz_i)
        if (Prozentsatz_i*100) >= 100:
            break
        file.write(f"{round((Prozentsatz_i*100),3)}%\t{Monate}\n")
Startgeld = 1
Prozentsatz_0_1 = round(0.001,3)
Prozentsatz_i = round(0)
Zähler = 1
with open("my_file3.txt", "w") as file:
    file.write(f"Prozentsatz\tNach n Jahren hat man 99.999% des Geldes verloren\n")
    while Zähler > 0 and Prozentsatz_i <= 1:
        Prozentsatz_i += Prozentsatz_0_1*12
        Zähler -= Prozentsatz_0_1*12
        Geld = 1
        Monate = 0
        Zähler = round(Zähler,3)
        while Geld > 0.00001:
            Monate += 1
            Geld = Geld*(1-Prozentsatz_i)
        if (Prozentsatz_i*100) >= 100:
            break
        file.write(f"{round((Prozentsatz_i*100)*12,3)}%\t{Monate}\n")