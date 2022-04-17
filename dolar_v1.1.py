# Addons
from colorama import Fore, Back, Style

# Conversor
Dolar = float(input("Quantos US$ você quer converter para real?"))

# Dolar 16 de abril de 2022 (BRT)  
Real = Dolar*4.70

# Resultado
print (Fore.GREEN + "R$" + "{:.2f}".format(Real))
