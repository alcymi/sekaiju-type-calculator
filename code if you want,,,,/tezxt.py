

import tkinter as tk

import string
import numpy as np
from operator import itemgetter

import pyglet, os


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

SUPERCOMBINATION = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
c = 0
for x in SUPERCOMBINATION:
    SUPERCOMBINATION[c] = (names[c], SUPERCOMBINATION[c])
    c += 1
SUPERalle = []


OVERALL = [Neutral,Pyro,Aqua,Flora,Shock,Frost,Earth,Toxic,Insect,Sky,Metal,Light,Dark,Astral,Magic,Mythic,Combat,Lost,Sound,Sweet,Void,Drowned,Zero,Inferno,Eternal,Divine,stupid,Slam,Jam,Fishing]

def the_pairer(allTypings,labels):
    count = 0
    for x in allTypings:
        count2 = 0
        for y in allTypings[count]:
            allTypings[count][count2] = (labels[count2],allTypings[count][count2])
            count2 += 1
        count += 1

def type_multiplier(mixture,pure):
    count = 0
    for x in mixture:
        mixture[count] = (mixture[count][0], np.round(mixture[count][1] * pure[count][1], 2))
        count += 1
    return mixture

def addNeutral(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Neutral")
    combination = type_multiplier(combination, Neutral)
    update()
def addPyro(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Pyro")
    combination = type_multiplier(combination, Pyro)
    update()
def addAqua(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Aqua")
    combination = type_multiplier(combination, Aqua)
    update()
def addFlora(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Flora")
    combination = type_multiplier(combination, Flora)
    update()
def addShock(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Shock")
    combination = type_multiplier(combination, Shock)
    update()
def addFrost(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Frost")
    combination = type_multiplier(combination, Frost)
    update()
def addEarth(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Earth")
    combination = type_multiplier(combination, Earth)
    update()
def addToxic(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Toxic")
    combination = type_multiplier(combination, Toxic)
    update()
def addInsect(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Insect")
    combination = type_multiplier(combination, Insect)
    update()
def addSky(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Sky")
    combination = type_multiplier(combination, Sky)
    update()
def addMetal(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Metal")
    combination = type_multiplier(combination, Metal)
    update()
def addLight(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Light")
    combination = type_multiplier(combination, Light)
    update()
def addDark(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Dark")
    combination = type_multiplier(combination, Dark)
    update()
def addAstral(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Astral")
    combination = type_multiplier(combination, Astral)
    update()
def addMagic(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Magic")
    combination = type_multiplier(combination, Magic)
    update()
def addMythic(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Mythic")
    combination = type_multiplier(combination, Mythic)
    update()
def addCombat(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Combat")
    combination = type_multiplier(combination, Combat)
    update()
def addLost(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Lost")
    combination = type_multiplier(combination, Lost)
    update()
def addSound(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Sound")
    combination = type_multiplier(combination, Sound)
    update()
def addSweet(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Sweet")
    combination = type_multiplier(combination, Sweet)
    update()
def addVoid(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Void")
    combination = type_multiplier(combination, Void)
    update()
def addDrowned(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Drowned")
    combination = type_multiplier(combination, Drowned)
    update()
def addZero(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Zero")
    combination = type_multiplier(combination, Zero)
    update()
def addInferno(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Inferno")
    combination = type_multiplier(combination, Inferno)
    update()
def addEternal(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Eternal")
    combination = type_multiplier(combination, Eternal)
    update()
def addDivine(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Divine")
    combination = type_multiplier(combination, Divine)
    update()
def addstupid(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("stupid")
    combination = type_multiplier(combination, stupid)
    update()
def addSlam(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Slam")
    combination = type_multiplier(combination, Slam)
    update()
def addJam(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Jam")
    combination = type_multiplier(combination, Jam)
    update()
def addFishing(alle=SUPERalle,combination=SUPERCOMBINATION):
    alle.append("Fishing")
    combination = type_multiplier(combination, Fishing)
    update()

def reset(alle=SUPERalle, combination=SUPERCOMBINATION):
    for c in range(len(names)):
        combination[c] = (names[c], 1)
    alle.clear()
    update()

the_pairer(OVERALL,names)

TYPE_BG = {
    "Neutral": "#cccccc",
    "Pyro":    "#cd0204",
    "Aqua":    "#80a5ff",
    "Flora":   "#07a919",
    "Shock":   "#f0f03f",
    "Frost":   "#affffa",
    "Earth":   "#9c6321",
    "Toxic":   "#c142b7",
    "Insect":  "#fbb041",
    "Sky":     "#6eeaf5",
    "Metal":   "#868686",
    "Light":   "#fffeeb",
    "Dark":    "#2f2f2f",
    "Astral":  "#4f2f90",
    "Magic":   "#fa3cef",
    "Mythic":  "#8579fb",
    "Combat":  "#811516",
    "Lost":    "#0cbd91",
    "Sound":   "#ffda9a",
    "Sweet":   "#ffc0fe",
    "Void":    "#534b7d",
    "Drowned": "#130a48",
    "Zero":    "#111111",
    "Inferno": "#3b0000",
    "Eternal": "#3e0c16",
    "Divine":  "#261547",
    "stupid":  "#b8fe79",
    "Slam":    "#ec7d50",
    "Jam":     "#d07e87",
    "Fishing": "#564236"
}

TYPE_FG = {
    "Neutral": "#1b2a35",
    "Pyro":    "#1b2a35",
    "Aqua":    "#1b2a35",
    "Flora":   "#1b2a35",
    "Shock":   "#1b2a35",
    "Frost":   "#1b2a35",
    "Earth":   "#1b2a35",
    "Toxic":   "#1b2a35",
    "Insect":  "#1b2a35",
    "Sky":     "#1b2a35",
    "Metal":   "#1b2a35",
    "Light":   "#1b2a35",
    "Dark":    "#1b2a35",
    "Astral":  "#1b2a35",
    "Magic":   "#1b2a35",
    "Mythic":  "#1b2a35",
    "Combat":  "#1b2a35",
    "Lost":    "#1b2a35",
    "Sound":   "#1b2a35",
    "Sweet":   "#1b2a35",
    "Void":    "#534b7d",
    "Drowned": "#0000ff",
    "Zero":    "#03e89b",
    "Inferno": "#ec1a00",
    "Eternal": "#fc2f58",
    "Divine":  "#ffff00",
    "stupid":  "#fd5c96",
    "Slam":    "#79e857",
    "Jam":     "#a0ff2e",
    "Fishing": "#1b2a35"
}

def setup_text_tags():
    for name in names:
        chart.tag_config(f"type_{name}",
                         background=TYPE_BG.get(name, "#cccccc"),
                         foreground=TYPE_FG.get(name, "#1b2a35"))
    chart.tag_config("mult_-3",      foreground="#ff2828")
    chart.tag_config("mult_-2",      foreground="#ff9c5b")
    chart.tag_config("mult_-1",      foreground="#fff35b")
    chart.tag_config("mult_0",       foreground="#ffffff")
    chart.tag_config("mult_1",       foreground="#a4ff5b")
    chart.tag_config("mult_2",       foreground="#5bff94")
    chart.tag_config("mult_3",       foreground="#34ffc9")
    chart.tag_config("mult_-3_dark", foreground="#ff2828", background="#212121")
    chart.tag_config("mult_-2_dark", foreground="#ff9c5b", background="#212121")
    chart.tag_config("mult_-1_dark", foreground="#fff35b", background="#212121")
    chart.tag_config("mult_0_dark",  foreground="#ffffff", background="#212121")
    chart.tag_config("mult_1_dark",  foreground="#a4ff5b", background="#212121")
    chart.tag_config("mult_2_dark",  foreground="#5bff94", background="#212121")
    chart.tag_config("mult_3_dark",  foreground="#34ffc9", background="#212121")
    chart.tag_config("header",       foreground="#aaaaaa")
    chart.tag_config("slash",        foreground="#888888")

def mult_tag(value, flip):
    if flip % 2 == 0:
        if value <= 0.2:    return "mult_-3_dark"
        elif value <= 0.5:  return "mult_-2_dark"
        elif value <= 0.99: return "mult_-1_dark"
        elif value == 1:    return "mult_0_dark"
        elif value <= 1.25: return "mult_1_dark"
        elif value <= 1.7:  return "mult_2_dark"
        else:               return "mult_3_dark"
    else:
        if value <= 0.2:    return "mult_-3"
        elif value <= 0.5:  return "mult_-2"
        elif value <= 0.99: return "mult_-1"
        elif value == 1:    return "mult_0"
        elif value <= 1.25: return "mult_1"
        elif value <= 1.7:  return "mult_2"
        else:               return "mult_3"

def typeNamer():
    if not SUPERalle:
        chart.insert("end", "|--:--|\n", "header")
        return
    for idx, name in enumerate(SUPERalle):
        if idx > 0:
            chart.insert("end", " / ", "slash")
        chart.insert("end", name, f"type_{name}")
    chart.insert("end", "\n")

def chartPrinter(printee):
    chart.insert("end", "will take [x] times damage from:\n", "header")
    v = 1
    for a, b in printee:
        chart.insert("end", f" {a} ", f"type_{a}")
        chart.insert("end", f"  {b}x\n", mult_tag(b,v))
        v += 1

def update():
    if SUPERCOMBINATION[29][1] > 1.5:
        SUPERCOMBINATION[29] = (names[29], 1.5)
    if SUPERCOMBINATION[26][1] > 1.5:
        SUPERCOMBINATION[26] = (names[26], 1.5)

    returnee = sorted(SUPERCOMBINATION, key=itemgetter(1), reverse=True) \
               if sortBool.get() else SUPERCOMBINATION
    wa = 0
    wawa = 1
    if positionBool.get():
        wa = 1
        wawa = 0
    chartFrame.grid(row=wa, column=wawa, sticky="n", padx=10)

    chart.config(state="normal")
    chart.delete("1.0", "end")
    typeNamer()
    chartPrinter(returnee)
    chart.config(state="disabled")


pyglet.font.add_file("./CYGGY/font/AccanthisADFStd-Bold.otf")

window = tk.Tk()

window.iconbitmap("./CYGGY/Cygnet.ico")

window.title("Sekaiju Type Defense Calculator v1.1")

# window.configure(bg="#36333e")

# w = tk.Label(window, text ='Sekaiju Typing Defense Calculator', font = "50").grid(row=0,column=0)
# w.pack()

buttonFrame = tk.Frame(window)
buttonFrame.grid(row=0,column=0,sticky="n")

NeutralButton = tk.Button(buttonFrame,text="Neutral",command=addNeutral,font=("AccanthisADFStd-Bold"),bg="#cccccc",fg="#1b2a35",width=8).grid(row=0,column=0)
PyroButton = tk.Button(buttonFrame,text="Pyro",command=addPyro,font=("AccanthisADFStd-Bold"),bg="#cd0204",fg="#1b2a35",width=8).grid(row=1,column=0)
AquaButton = tk.Button(buttonFrame,text="Aqua",command=addAqua,font=("AccanthisADFStd-Bold"),bg="#80a5ff",fg="#1b2a35",width=8).grid(row=2,column=0)
FloraButton = tk.Button(buttonFrame,text="Flora",command=addFlora,font=("AccanthisADFStd-Bold"),bg="#07a919",fg="#1b2a35",width=8).grid(row=3,column=0)
ShockButton = tk.Button(buttonFrame,text="Shock",command=addShock,font=("AccanthisADFStd-Bold"),bg="#f0f03f",fg="#1b2a35",width=8).grid(row=4,column=0)
FrostButton = tk.Button(buttonFrame,text="Frost",command=addFrost,font=("AccanthisADFStd-Bold"),bg="#affffa",fg="#1b2a35",width=8).grid(row=5,column=0)
EarthButton = tk.Button(buttonFrame,text="Earth",command=addEarth,font=("AccanthisADFStd-Bold"),bg="#9c6321",fg="#1b2a35",width=8).grid(row=6,column=0)
ToxicButton = tk.Button(buttonFrame,text="Toxic",command=addToxic,font=("AccanthisADFStd-Bold"),bg="#c142b7",fg="#1b2a35",width=8).grid(row=7,column=0)
InsectButton = tk.Button(buttonFrame,text="Insect",command=addInsect,font=("AccanthisADFStd-Bold"),bg="#fbb041",fg="#1b2a35",width=8).grid(row=8,column=0)
SkyButton = tk.Button(buttonFrame,text="Sky",command=addSky,font=("AccanthisADFStd-Bold"),bg="#6eeaf5",fg="#1b2a35",width=8).grid(row=9,column=0)
MetalButton = tk.Button(buttonFrame,text="Metal",command=addMetal,font=("AccanthisADFStd-Bold"),bg="#868686",fg="#1b2a35",width=8).grid(row=0,column=1)
LightButton = tk.Button(buttonFrame,text="Light",command=addLight,font=("AccanthisADFStd-Bold"),bg="#fffeeb",fg="#1b2a35",width=8).grid(row=1,column=1)
DarkButton = tk.Button(buttonFrame,text="Dark",command=addDark,font=("AccanthisADFStd-Bold"),bg="#2f2f2f",fg="#1b2a35",width=8).grid(row=2,column=1)
AstralButton = tk.Button(buttonFrame,text="Astral",command=addAstral,font=("AccanthisADFStd-Bold"),bg="#4f2f90",fg="#1b2a35",width=8).grid(row=3,column=1)
MagicButton = tk.Button(buttonFrame,text="Magic",command=addMagic,font=("AccanthisADFStd-Bold"),bg="#fa3cef",fg="#1b2a35",width=8).grid(row=4,column=1)
MythicButton = tk.Button(buttonFrame,text="Mythic",command=addMythic,font=("AccanthisADFStd-Bold"),bg="#8579fb",fg="#1b2a35",width=8).grid(row=5,column=1)
CombatButton = tk.Button(buttonFrame,text="Combat",command=addCombat,font=("AccanthisADFStd-Bold"),bg="#811516",fg="#1b2a35",width=8).grid(row=6,column=1)
LostButton = tk.Button(buttonFrame,text="Lost",command=addLost,font=("AccanthisADFStd-Bold"),bg="#0cbd91",fg="#1b2a35",width=8).grid(row=7,column=1)
SoundButton = tk.Button(buttonFrame,text="Sound",command=addSound,font=("AccanthisADFStd-Bold"),bg="#ffda9a",fg="#1b2a35",width=8).grid(row=8,column=1)
SweetButton = tk.Button(buttonFrame,text="Sweet",command=addSweet,font=("AccanthisADFStd-Bold"),bg="#ffc0fe",fg="#1b2a35",width=8).grid(row=9,column=1)
VoidButton = tk.Button(buttonFrame,text="      ",command=addVoid,font=("AccanthisADFStd-Bold"),bg="#534b7d",fg="#1b2a35",width=8).grid(row=0,column=2)
DrownedButton = tk.Button(buttonFrame,text="Drowned",command=addDrowned,font=("AccanthisADFStd-Bold"),bg="#130a48",fg="#0000ff",width=8).grid(row=1,column=2)
ZeroButton = tk.Button(buttonFrame,text="Zero",command=addZero,font=("AccanthisADFStd-Bold"),bg="#111111",fg="#03e89b",width=8).grid(row=2,column=2)
InfernoButton = tk.Button(buttonFrame,text="Inferno",command=addInferno,font=("AccanthisADFStd-Bold"),bg="#3b0000",fg="#ec1a00",width=8).grid(row=3,column=2)
EternalButton = tk.Button(buttonFrame,text="Eternal",command=addEternal,font=("AccanthisADFStd-Bold"),bg="#3e0c16",fg="#fc2f58",width=8).grid(row=4,column=2)
DivineButton = tk.Button(buttonFrame,text="Divine",command=addDivine,font=("AccanthisADFStd-Bold"),bg="#261547",fg="#ffff00",width=8).grid(row=5,column=2)
stupidButton = tk.Button(buttonFrame,text="stupid",command=addstupid,font=("AccanthisADFStd-Bold"),bg="#b8fe79",fg="#fd5c96",width=8).grid(row=6,column=2)
SlamButton = tk.Button(buttonFrame,text="Slam",command=addSlam,font=("AccanthisADFStd-Bold"),bg="#ec7d50",fg="#79e857",width=8).grid(row=7,column=2)
JamButton = tk.Button(buttonFrame,text="Jam",command=addJam,font=("AccanthisADFStd-Bold"),bg="#d07e87",fg="#a0ff2e",width=8).grid(row=8,column=2)
FishingButton = tk.Button(buttonFrame,text="Fishing",command=addFishing,font=("AccanthisADFStd-Bold"),bg="#564236",fg="#1b2a35",width=8).grid(row=9,column=2)

# killButton = tk.Button(buttonFrame,text="k sdfjka nxc sk dsfhg",command=window.destroy,font=("AccanthisADFStd-Bold"),width=8).grid(row=10,column=1)

resetButton = tk.Button(buttonFrame,text="Clear",command=reset,font=("AccanthisADFStd-Bold"),width=8).grid(row=10,column=2)

positionBool = tk.BooleanVar()
positionButton = tk.Checkbutton(buttonFrame,text="Vert.",variable=positionBool,command=update,font=("AccanthisADFStd-Bold"),width=5).grid(row=10,column=1)


sortBool = tk.BooleanVar(value=True)
sortButton = tk.Checkbutton(buttonFrame,text="Sort",variable=sortBool,command=update,font=("AccanthisADFStd-Bold"),width=5).grid(row=10,column=0)

chartFrame = tk.Frame(window)
chartFrame.grid(row=0, column=1, sticky="n", padx=10)
chart = tk.Text(chartFrame, width=26,height=33, font=("AccanthisADFStd-Bold",12), bg="#252525",
                fg="#1b2a35", state="disabled", wrap="word")
chart.pack()
setup_text_tags()
update()

# https://www.pythonguis.com/tutorials/packaging-tkinter-applications-windows-pyinstaller/

window.mainloop()