p = "Aceasta este o propozitie"
p2= "        frumoasa       "

print('Functia startswith:')
print(p.startswith('Aceasta'))
print(p.startswith('este'))
print('\n')

print('Functia endswith:')
print(p.endswith('pro'))
print(p.endswith('tie'))
print('\n')

print('Functia replace:')
print(p.replace('propozitie','masina'))
print('\n')

print('Functia lower:')
print(p.lower())
print('\n')

print('Functia upper:')
print(p.upper())
print('\n')

print('Functia strip:') #scoate spatiul de la inceput si final
p2 = p2.strip()
print(p2)
print('\n')

print('Functia rstrip:')
p2 = p2.strip()
print(p2)
print('\n')

print('Functia isalpha:') #returneaza True daca toate caracterele sunt litere din alfabet (a-z)
print(p.isalpha())
print('\n')

print('Functia isupper') #returneaza True daca toate caracterele sunt scrise cu majuscule
print(p.isupper())
print('\n')