def abstracta ( lado : int , cubos : int = 4) -> tuple :
    area = cubos * 6 * lado**2
    volumen = cubos * lado **3
    return lado , area , volumen

print(abstracta(37,9))
print ( abstracta (41 , 2) )
print ( abstracta (26 , 4) )
print ( abstracta (17 , 5) )