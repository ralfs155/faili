# while ir cikls ar nosacijumu, kamēr nosacījums ir spēkā , cikls strādā.
skaitlis =int(input("Cikls ir 4+4="))

while skaitlis!=8: # nosacījums ir ievadītais skaitlis nav 8
    print("nepareizi")# cikla ķermenis-cikla atkārtojamās
    skaitlis =int(input("Cikls ir 4+4="))
print("pareizi!")