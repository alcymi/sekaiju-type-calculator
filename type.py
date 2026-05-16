
import string
import numpy as np
from operator import itemgetter

pppppp = 2
ppppp = 1.5
pppp = 1.3
ppp = 1.25
pp = 1.15
p = 1.1
n = 1
f = 0.75
ff = 0.67
fff = 0.25
i = 0.1

names = ["Neutral","Pyro","Aqua","Flora","Shock","Frost","Earth","Toxic","Insect","Sky","Metal","Light","Dark",
         "Astral","Magic","Mythic","Combat","Lost","Sound","Sweet","Void","Drowned","Zero","Inferno","Eternal",
         "Divine","stupid","Slam","Jam","Fishing"]
#Neutral,Pyro,Aqua,Flora,Shock,Frost,Earth,Toxic,Insect,Sky,Metal,Light,Dark,Astral,Magic,Mythic,Combat,Lost,Sound,Sweet,Void,Drowned,Zero,Inferno,Eternal,Divine,stupid,Slam,Jam,Fishing

Neutral = [n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,ppppp,n,n,n,n,pppp,n,n,n,ppppp]
Pyro    = [n,ff,ppppp,ff,n,ff,ppppp,n,n,ppppp,ff,n,n,n,n,ppppp,n,n,n,n,ff,ppppp,ff,ff,ppppp,pppp,ff,n,n,ppppp]
Aqua    = [n,ff,ff,ppppp,ppppp,ff,n,ppppp,n,n,ff,n,n,n,n,n,n,ff,ppppp,ff,ff,n,ff,ppppp,n,pppp,ppppp,n,n,ppppp]
Flora   = [n,ppppp,ff,ff,ff,ppppp,ff,ppppp,ppppp,ppppp,n,ff,n,n,n,n,n,n,n,ff,ff,ff,n,ppppp,n,pppp,n,ff,ppppp,ppppp]
Shock   = [n,n,n,n,i,n,ppppp,n,n,ff,ff,n,n,n,n,ppppp,n,n,n,n,n,n,n,n,ppppp,pppp,n,n,n,ppppp]
Frost   = [n,ppppp,n,n,n,ff,n,n,n,n,ppppp,n,n,ff,n,n,ppppp,ppppp,n,n,n,n,ff,ppppp,ff,pppp,n,n,n,ppppp]
Earth   = [n,ff,ppppp,ppppp,ff,ppppp,n,n,n,n,n,n,n,ppppp,n,n,ppppp,ff,ff,n,ff,ppppp,ppppp,ff,n,pppp,n,ff,ppppp,ppppp]
Toxic   = [n,n,ppppp,ff,n,n,ppppp,ff,ff,n,n,n,n,n,ppppp,n,n,n,n,ff,n,n,n,n,ppppp,pppp,ppppp,ppppp,ff,ppppp]
Insect  = [n,ppppp,n,ff,n,n,n,n,n,ppppp,n,n,n,n,n,n,ppppp,ppppp,ff,i,n,n,n,ppppp,n,pppp,ppppp,n,n,ppppp]
Sky     = [n,n,n,ff,ppppp,ppppp,i,n,ff,n,n,n,ppppp,n,n,n,n,ff,n,n,n,ff,ppppp,n,n,pppp,n,n,n,ppppp]
Metal   = [n,ppppp,ppppp,ff,n,ff,ppppp,i,ff,ff,ff,ff,n,ff,ff,ff,ppppp,n,ppppp,n,n,ppppp,ff,ppppp,n,pppp,ppppp,ppppp,ff,ppppp]
Light   = [n,n,n,ppppp,n,n,n,n,n,n,n,ff,ppppp,n,ff,n,ff,ff,n,n,ppppp,ppppp,n,n,ppppp,pppp,ff,n,n,ppppp]
Dark    = [n,n,n,n,n,ppppp,n,n,n,n,n,ppppp,ff,ff,n,n,i,n,n,ppppp,ppppp,ff,n,n,n,pppp,n,n,n,ppppp]
Astral  = [n,n,n,n,ff,n,n,ff,ppppp,n,n,ppppp,ppppp,ppppp,i,n,ff,n,i,n,ppppp,n,n,n,ff,pppp,n,ppppp,ppppp,ppppp]
Magic   = [n,ff,ff,n,n,n,n,ppppp,ppppp,n,ppppp,n,n,ppppp,n,i,ff,n,ppppp,n,n,ff,ppppp,ff,n,pppp,n,ff,ppppp,ppppp]
Mythic  = [n,ff,ff,ff,ff,ppppp,n,n,n,n,n,n,n,n,ppppp,ppppp,n,ppppp,n,n,n,ff,ppppp,ff,n,pppp,ppppp,ff,ppppp,ppppp]
Combat  = [n,n,n,n,n,n,ff,ff,n,n,n,n,ff,ppppp,ppppp,n,n,n,n,ppppp,n,n,n,n,n,pppp,n,n,n,ppppp]
Lost    = [n,n,n,n,n,n,n,n,n,ppppp,n,ppppp,ff,ff,ff,n,n,n,n,ppppp,ppppp,n,i,ff,ppppp,pppp,ppppp,ppppp,ff,ppppp]
Sound   = [n,n,n,n,ppppp,n,n,n,n,n,n,ppppp,ppppp,ppppp,ff,n,i,n,ppppp,n,n,n,n,n,n,pppp,ff,n,n,ppppp]
Sweet   = [n,ppppp,n,n,n,ff,n,ppppp,ppppp,n,n,n,n,ff,n,n,n,n,n,n,n,n,ff,ppppp,n,pppp,n,ppppp,ff,ppppp]
Void    = [ppppp,ppppp,ppppp,ppppp,n,n,ppppp,n,n,n,n,ff,ff,ppppp,n,n,n,ff,n,n,ppppp,n,i,ppppp,ff,ppppp,n,n,n,ppppp]
Drowned = [n,fff,ff,ppppp,ppppp,ff,ff,ppppp,n,ppppp,ff,n,n,n,n,n,n,i,ff,n,ff,ff,ff,ppp,n,ff,i,f,ppp,ppppp]
Zero    = [n,pp,n,n,n,ff,n,n,n,n,ppppp,n,n,ff,ff,n,ppppp,ppppp,n,n,n,n,ff,pppppp,ff,ff,n,ppp,f,ppppp]
Inferno = [n,ff,i,ff,n,ff,ppppp,n,n,ppppp,ff,n,n,n,n,ppppp,n,ppppp,n,n,ff,fff,ppppp,ff,fff,ff,i,n,n,ppppp]
Eternal = [ppppp,n,n,n,ff,n,n,n,n,n,n,ff,n,ppppp,ppppp,ff,ppppp,ff,n,n,ff,n,p,n,ff,ppppp,n,n,n,ppppp]
Divine  = [n,pp,pp,pp,pp,pp,pp,pp,n,n,n,p,p,n,ppppp,pp,ppppp,ppppp,n,n,ff,ff,ppppp,ff,fff,ff,n,n,n,ppppp]
stupid  = [n,ppppp,ff,n,n,n,n,i,ff,n,ff,ppppp,n,n,n,ff,n,ff,ppppp,ppppp,n,n,n,ppppp,pppppp,pppppp,ff,n,n,ppppp]
Slam    = [n,n,n,ppppp,n,n,ppppp,ff,n,n,ff,n,n,ff,ppppp,ppppp,n,ff,n,ff,n,ppppp,n,n,n,ppppp,n,ff,ppppp,ppppp]
Jam     = [n,n,n,ff,n,n,ff,ppppp,n,n,ppppp,n,n,ff,ff,ff,n,ppppp,n,ff,n,ff,n,n,n,ppppp,n,ppppp,ff,ppppp]
Fishing = [n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,n,ff,ff,n,n,n,ff]


OVERALL = [Neutral,Pyro,Aqua,Flora,Shock,Frost,Earth,Toxic,Insect,Sky,Metal,Light,Dark,Astral,Magic,Mythic,Combat,Lost,Sound,Sweet,Void,Drowned,Zero,Inferno,Eternal,Divine,stupid,Slam,Jam,Fishing]

def the_pairer(allTypings,labels):
    count = 0
    for x in allTypings:
        count2 = 0
        for y in allTypings[count]:
            allTypings[count][count2] = (labels[count2],allTypings[count][count2])
            count2 += 1
        count += 1

def printy(typings):
    for a,b in typings:
        print(f"{a}: {b}x")

def type_multiplier(mixture,pure):
    count = 0
    for x in mixture:
        mixture[count] = (mixture[count][0], np.round(mixture[count][1] * pure[count][1], 2))
        count += 1
    return mixture

the_pairer(OVERALL,names)
combination = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
c = 0
for x in combination:
    combination[c] = (names[c], combination[c])
    c += 1

print("Example! Use PYRO or any type for monotyping! Use PYRO/AQUA for duotyping! (Capitalization does not matter!) (Spelling does,,,)")
print("Technically, PYRO/AQUA/FLORA/VOID/DIVINE works! ([TYPE], [TYPE1/TYPE2], [TYPE1/TYPE2/TYPE3] are all viable!)")
inp = input("Enter the type/types:")
inp = inp.lower()

counter = 0
fullTyping = ""
alle = inp.split("/")
while len(alle) != 0:
    if alle[0] == "neutral":
        combination = type_multiplier(combination,Neutral)
    if alle[0] == "pyro":
        combination = type_multiplier(combination,Pyro)
    if alle[0] == "aqua":
        combination = type_multiplier(combination,Aqua)
    if alle[0] == "flora":
        combination = type_multiplier(combination,Flora)
    if alle[0] == "shock":
        combination = type_multiplier(combination,Shock)
    if alle[0] == "frost":
        combination = type_multiplier(combination,Frost)
    if alle[0] == "earth":
        combination = type_multiplier(combination,Earth)
    if alle[0] == "toxic":
        combination = type_multiplier(combination,Toxic)
    if alle[0] == "insect":
        combination = type_multiplier(combination,Insect)
    if alle[0] == "sky":
        combination = type_multiplier(combination,Sky)
    if alle[0] == "metal":
        combination = type_multiplier(combination,Metal)
    if alle[0] == "light":
        combination = type_multiplier(combination,Light)
    if alle[0] == "dark":
        combination = type_multiplier(combination,Dark)
    if alle[0] == "astral":
        combination = type_multiplier(combination,Astral)
    if alle[0] == "magic":
        combination = type_multiplier(combination,Magic)
    if alle[0] == "mythic":
        combination = type_multiplier(combination,Mythic)
    if alle[0] == "combat":
        combination = type_multiplier(combination,Combat)
    if alle[0] == "lost":
        combination = type_multiplier(combination,Lost)
    if alle[0] == "sound":
        combination = type_multiplier(combination,Sound)
    if alle[0] == "sweet":
        combination = type_multiplier(combination,Sweet)
    if alle[0] == "void":
        combination = type_multiplier(combination,Void)
    if alle[0] == "drowned":
        combination = type_multiplier(combination,Drowned)
    if alle[0] == "zero":
        combination = type_multiplier(combination,Zero)
    if alle[0] == "inferno":
        combination = type_multiplier(combination,Inferno)
    if alle[0] == "eternal":
        combination = type_multiplier(combination,Eternal)
    if alle[0] == "divine":
        combination = type_multiplier(combination,Divine)
    if alle[0] == "stupid":
        combination = type_multiplier(combination,stupid)
    if alle[0] == "slam":
        combination = type_multiplier(combination,Slam)
    if alle[0] == "jam":
        combination = type_multiplier(combination,Jam)
    if alle[0] == "fishing":
        combination = type_multiplier(combination,Fishing)
    temp = alle.pop(0)
    if temp != "stupid":
        temp = temp.capitalize()
    if counter == 0:
        fullTyping += temp
    else:
        fullTyping += "/" + temp
    counter += 1
if combination[29][1] > 1.5:
    combination[29] = (names[29],1.5)
if combination[26][1] > 1.5:
    combination[26] = (names[26],1.5)

combinationSorted = sorted(combination,key=itemgetter(1),reverse=True)

print(f"{fullTyping} will take [x] damage from:")
printy(combinationSorted)

