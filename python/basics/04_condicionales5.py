"""
pide salario y desempeño (1-5)
si el desempeño es :
>4 = 15%
>3 = 10%
>2 = 5%
>1 = 2%
"""
salario=float(input("Ingresa el salario"))
desempenio=int(input("Ingresa el desempeño (1-5)"))
if(desempenio<6):
    if(desempenio>4):
        print(f"Nuevo salario = {salario*0.15+salario}")
    else:
        if(desempenio>3):
            print(f"Nuevo salario = {salario*0.10+salario}")
        else:
            if(desempenio>2):
                print(f"Nuevo salario = {salario*0.05+salario}")
            else:
                if(desempenio>1):
                    print(f"Nuevo salario = {salario*0.02+salario}")
                else:
                    print(f"Salario = {salario}")
else:
    print(f"Desempeño mal ingresado")