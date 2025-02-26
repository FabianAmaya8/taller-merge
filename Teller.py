from math import gcd
from datetime import datetime

def calcular_mcd_y_edad(num1, num2, anio_nacimiento):
  
    mcd = gcd(num1, num2)
    
 
    anio_actual = datetime.now().year
    edad = anio_actual - anio_nacimiento
    
    return mcd, edad


num1 = 36
num2 = 48
anio_nacimiento = 2000

resultado = calcular_mcd_y_edad(num1, num2, anio_nacimiento)
print(f"El MCD es: {resultado[0]}")
print(f"La edad es: {resultado[1]}")
