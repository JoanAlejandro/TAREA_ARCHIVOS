import csv
while True:
    x=0
    with open('salesJan2025.csv') as f:
        lectura=csv.reader(f, delimiter=",")
        y=input("Digite un pais de suramerica: ")
        y=y.title()
        for row in lectura:
            if row[0]==y:
                print("Sus Ventas son: ", row[1])
                x=1
        if x==0:
            print("PAIS INCORRECTO, Vuelva a escribir...")

