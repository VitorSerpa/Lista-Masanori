string = """“The Python Software Foundation and the global Python community  welcome  and  encourage  participation  by  everyone.  Our  community  is  based  on mutual respect, tolerance, and encouragement, and we are working to help each other live up to  these  principles.  We  want  our  community  to  be  more  diverse:  whoever  you  are,  and whatever  your  background,  we  welcome  you."""

lista = string.split()
listaSeparada = []

for i in lista:
    if i[0] == "p" or i[-1] == "n":
        listaSeparada.append(i)

print(listaSeparada)