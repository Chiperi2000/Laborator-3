#Cerinta: Citiți de la tastatură numele și prenumele într-un singur text și afișați separat, pe câte un rând numele și prenumele.

#Rezolvare:

Numele_si_prenumele = input("Scrieti numele si prenumele: ")
print("Numele:",Numele_si_prenumele.split(" ",1)[0] )
print("Prenumele:",Numele_si_prenumele.split(" ",1)[1] )