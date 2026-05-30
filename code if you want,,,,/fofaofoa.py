import tkinter as tk
from tkinter import font, PhotoImage
import pyautogui
import time
import threading
import keyboard
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
    for count in range(len(mixture)):
        mixture[count] = (mixture[count][0], np.round(mixture[count][1] * pure[count][1], 2))

type_map = {"Neutral":Neutral,"Pyro":Pyro,"Aqua":Aqua,"Flora":Flora,"Shock":Shock,"Frost":Frost,"Earth":Earth,
            "Toxic":Toxic,"Insect":Insect,"Sky":Sky,"Metal":Metal,"Light":Light,"Dark":Dark,"Astral":Astral,
            "Magic":Magic,"Mythic":Mythic,"Combat":Combat,"Lost":Lost,"Sound":Sound,"Sweet":Sweet,"Void":Void,
            "Drowned":Drowned,"Zero":Zero,"Inferno":Inferno,"Eternal":Eternal,"Divine":Divine,"stupid":stupid,
            "Slam":Slam,"Jam":Jam,"Fishing":Fishing
            }

def add_type(name):
    SUPERalle.append(name)
    type_multiplier(SUPERCOMBINATION, type_map[name])
    update()

def reset():
    for c in range(len(names)):
        SUPERCOMBINATION[c] = (names[c], 1)
    SUPERalle.clear()
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
    cygnet.grid(row=12, column=0, columnspan=3, sticky="ew")
    if positionBool.get():
        wa = 1
        wawa = 0
        cygnet.grid_remove()
        # window.geometry("235x850")

    chartFrame.grid(row=wa, column=wawa, sticky="n", padx=10)

    chart.tag_config("type_Dark",foreground="#1b2a35")
    chart.tag_config("type_Fishing",foreground="#1b2a35")
    chart.tag_config("type_Astral",foreground="#1b2a35")
    chart.tag_config("type_Combat",foreground="#1b2a35")
    DarkButton.configure(fg="#1b2a35")
    FishingButton.configure(fg="#1b2a35")
    AstralButton.configure(fg="#1b2a35")
    CombatButton.configure(fg="#1b2a35")
    if ezreadBool.get():
        chart.tag_config("type_Dark", foreground="#fffeeb")
        chart.tag_config("type_Fishing", foreground="#fffeeb")
        chart.tag_config("type_Astral", foreground="#fffeeb")
        chart.tag_config("type_Combat", foreground="#fffeeb")
        DarkButton.configure(fg="#fffeeb")
        FishingButton.configure(fg="#fffeeb")
        AstralButton.configure(fg="#fffeeb")
        CombatButton.configure(fg="#fffeeb")

    chart.config(state="normal")
    chart.delete("1.0", "end")
    typeNamer()
    chartPrinter(returnee)
    chart.config(state="disabled")

def update_hotkey():
    """Opens a new window to set the hotkey."""

    def set_new_hotkey():
        global hotkey
        new_key = hotkey_entry.get().strip().lower()
        if new_key:
            keyboard.remove_hotkey(hotkey)
            hotkey = new_key
            keyboard.add_hotkey(hotkey, toggle_clicking)
            hotkey_window.destroy()

    hotkey_window = tk.Toplevel(window)
    hotkey_window.iconbitmap("./CYGGY/Cygnet.ico")
    hotkey_window.title("Set AutoClicker Hotkey")
    hotkey_window.geometry("250x100")

    tk.Label(hotkey_window, text="Enter new hotkey:",font=fonty).pack(pady=5)
    hotkey_entry = tk.Entry(hotkey_window,font=fonty, width=10)
    hotkey_entry.pack(pady=5)

    set_button = tk.Button(hotkey_window, text="Set Hotkey",font=fonty, command=set_new_hotkey)
    set_button.pack(pady=5)

clicking = False
click_interval = 0.01  # Default to 5 seconds
hotkey = "f6"  # Default hotkey
mouse_button = "left"  # Default mouse button
click_type = "single"  # Default click type (single or double)

def click_loop():
    """Loop to perform auto-clicking."""
    global clicking
    while clicking:
        if click_type == "single":
            pyautogui.click(button=mouse_button)
        else:
            pyautogui.doubleClick(button=mouse_button)
        time.sleep(click_interval)

def start_clicking():
    """Starts the auto-clicking process."""
    global clicking
    if not clicking:
        clicking = True
        threading.Thread(target=click_loop, daemon=True).start()

def stop_clicking():
    """Stops the auto-clicking process."""
    global clicking
    clicking = False

def toggle_clicking():
    """Toggles clicking state when hotkey is pressed."""
    if clicking:
        stop_clicking()
    else:
        start_clicking()


window = tk.Tk()

window.resizable(False,False)

# window.geometry("450x530")

content = ""
with open('font.txt') as f:
    contents = f.read()
contents.strip()
f.close()

fonty = tk.font.Font(family=contents,size=12)

fonts = list(font.families())

BANNEDFONTS = ["Cambria Math","Gabriola"]
fonts = [f for f in fonts if f not in BANNEDFONTS]

for f in fonts:
    f.replace(" ","")

option = tk.StringVar(value=contents)

def font_change():
    global fonty
    selected = option.get()
    fonty = tk.font.Font(family=selected,size=12)
    chart.configure(font=fonty)

    NeutralButton['font'] = fonty
    PyroButton['font'] = fonty
    AquaButton['font'] = fonty
    FloraButton['font'] = fonty
    ShockButton['font'] = fonty
    FrostButton['font'] = fonty
    EarthButton['font'] = fonty
    ToxicButton['font'] = fonty
    InsectButton['font'] = fonty
    SkyButton['font'] = fonty
    MetalButton['font'] = fonty
    LightButton['font'] = fonty
    DarkButton['font'] = fonty
    AstralButton['font'] = fonty
    MagicButton['font'] = fonty
    MythicButton['font'] = fonty
    CombatButton['font'] = fonty
    LostButton['font'] = fonty
    SoundButton['font'] = fonty
    SweetButton['font'] = fonty
    VoidButton['font'] = fonty
    DrownedButton['font'] = fonty
    ZeroButton['font'] = fonty
    InfernoButton['font'] = fonty
    EternalButton['font'] = fonty
    DivineButton['font'] = fonty
    stupidButton['font'] = fonty
    SlamButton['font'] = fonty
    JamButton['font'] = fonty
    FishingButton['font'] = fonty

    resetButton['font'] = fonty
    positionButton['font'] = fonty
    sortButton['font'] = fonty
    ezreadButton['font'] = fonty
    autoClickerButton['font'] = fonty
    shinyButton['font'] = fonty

    update()

def shiny_font_change():
    global fonty
    selected = option.get()
    fonty = tk.font.Font(family=selected,size=12)

    dropOddsText['font'] = fonty
    oneText['font'] = fonty
    dropOddsEntry['font'] = fonty
    luckText['font'] = fonty
    luckEntry['font'] = fonty
    shinyMirrorButton['font'] = fonty
    glisteningAmuletButton['font'] = fonty
    goldRushButton['font'] = fonty
    shinyOutput['font'] = fonty

def on_key_press(event):
    if event.char.isdigit() or event.keysym == "BackSpace" or event.keysym == "period":
        event.widget.after(0,shiny_calcy)
        return
    return "break"

def shiny_calcy():
    global luckValue
    global dropRate
    global modifiedOdds
    dropRate = float(dropOddsEntry.get())
    luckValue = float(luckEntry.get())
    shinyBoost = 1
    goldRushMulti = 1
    itemString = f"With a luck of {luckValue} and a drop rate of 1/{round(dropRate)}, "

    shinyMirror = shinyMirrorBool.get()
    glisteningAmulet = glisteningAmuletBool.get()
    goldRush = goldRushBool.get()

    if shinyMirror and glisteningAmulet and goldRush:
        shinyBoost = 5
        goldRushMulti = 1.2
        itemString += f"the shiny odds while using a ShinyMirror, GlisteningAmulet and GoldRush are "
    elif glisteningAmulet and goldRush:
        shinyBoost = 3
        goldRushMulti = 1.2
        itemString += f"the shiny odds while using a GlisteningAmulet and GoldRush are "
    elif shinyMirror and goldRush:
        shinyBoost = 2
        goldRushMulti = 1.2
        itemString += f"the shiny odds while using a ShinyMirror and GoldRush are "
    elif shinyMirror and glisteningAmulet:
        shinyBoost = 5
        itemString += f"the shiny odds while using a ShinyMirror and GlisteningAmulet are "
    elif shinyMirror:
        shinyBoost = 2
        itemString += f"the shiny odds while using a ShinyMirror are "
    elif glisteningAmulet:
        shinyBoost = 3
        itemString += f"the shiny odds while using a GlisteningAmulet are "
    elif goldRush:
        shinyBoost = 1.2
        itemString += f"the shiny odds while using a GoldRush are "
    else:
        itemString += f"the base shiny odds are "

    modifiedOdds = np.ceil(dropRate * (((1000 / shinyBoost) / goldRushMulti) / ((luckValue + 1) / 2)) / (luckValue + 1))

    itemString += f"1/{round(modifiedOdds)}."

    shinyOutput.config(state="normal")
    shinyOutput.delete("1.0", "end")
    shinyOutput.insert("end", itemString)
    shinyOutput.config(state="disabled")

def open_shiny():
    shinyWindow = tk.Toplevel()
    shinyWindow.title("Cyggy's Sekaiju Calculator v1.3")
    shinyWindow.iconbitmap("./CYGGY/Cygnet.ico")
    shinyWindow.resizable(False,False)

    shinyFrame = tk.Frame(shinyWindow)
    shinyFrame.grid(row=0,column=0)

    entryFrames = tk.Frame(shinyFrame)
    entryFrames.grid(row=0,column=0)

    dropOddsFrame = tk.Frame(entryFrames)
    dropOddsFrame.grid(row=0,column=0)
    global dropOddsText
    dropOddsText = tk.Label(dropOddsFrame,text="Enter Drop Odds:",font=fonty)
    dropOddsText.grid(row=0,column=0,columnspan=2)

    global oneText
    oneText = tk.Label(dropOddsFrame,text="1/",font=fonty,width=2)
    oneText.grid(row=1,column=0,sticky="e")

    global dropOddsEntry
    dropOddsEntry = tk.Entry(dropOddsFrame,font=fonty,width=8)
    dropOddsEntry.grid(row=1,column=1,sticky="w")
    dropOddsEntry.bind("<KeyPress>", on_key_press)

    luckFrame = tk.Frame(entryFrames)
    luckFrame.grid(row=1,column=0)
    global luckText
    luckText = tk.Label(luckFrame,text="Enter Luck:",font=fonty)
    luckText.grid(row=0,column=0)

    global luckEntry
    luckEntry = tk.Entry(luckFrame,font=fonty,width=8)
    luckEntry.grid(row=1,column=0)
    luckEntry.bind("<KeyPress>", on_key_press)

    shinyButtonFrame = tk.Frame(shinyFrame)
    shinyButtonFrame.grid(row=0,column=1)

    global shinyMirrorButton
    global shinyMirrorBool
    shinyMirrorBool = tk.BooleanVar()
    shinyMirrorButton = tk.Checkbutton(shinyButtonFrame,text="ShinyMirror",variable=shinyMirrorBool,command=shiny_calcy,font=fonty,width=16)
    shinyMirrorButton.grid(row=0,column=0,sticky="w")

    global glisteningAmuletButton
    global glisteningAmuletBool
    glisteningAmuletBool = tk.BooleanVar()
    glisteningAmuletButton = tk.Checkbutton(shinyButtonFrame,text="GlisteningAmulet",variable=glisteningAmuletBool,command=shiny_calcy,font=fonty,width=16)
    glisteningAmuletButton.grid(row=1,column=0,sticky="w")

    global goldRushButton
    global goldRushBool
    goldRushBool = tk.BooleanVar()
    goldRushButton = tk.Checkbutton(shinyButtonFrame,text="GoldRush",variable=goldRushBool,command=shiny_calcy,font=fonty,width=16)
    goldRushButton.grid(row=2,column=0,sticky="w")

    global shinyOutput
    # shinyOutput = tk.Label(shinyWindow,text="I AM THE OUTPUT :3",font=fonty)
    # shinyOutput.grid(row=1,column=0,columnspan=2)

    shinyOutput = tk.Text(shinyWindow, width=40, height=4, font=fonty, state="disabled", wrap="word")
    shinyOutput.grid(row=2,column=0,pady=5)

    shinyOutput.config(state="normal")
    shinyOutput.insert("end","I AM THE OUTPUT :3","header")
    shinyOutput.config(state="disabled")

    optionmenu = tk.OptionMenu(shinyWindow, option, *fonts, command=lambda x: shiny_font_change())
    optionmenu.grid(row=3, column=0)

keyboard.add_hotkey(hotkey, toggle_clicking)

window.iconbitmap("./CYGGY/Cygnet.ico")

title = window.title("Cyggy's Sekaiju Calculator v1.3")

ALLECHARTFRAME = tk.Frame(window)
ALLECHARTFRAME.grid(row=0,column=0)

# window.configure(bg="#36333e")

# w = tk.Label(window, text ='Sekaiju Typing Defense Calculator', font = "50").grid(row=0,column=0)
# w.pack()

buttonFrame = tk.Frame(ALLECHARTFRAME)
buttonFrame.grid(row=0,column=0,sticky="n")

NeutralButton = tk.Button(buttonFrame,text="Neutral",command=lambda e="Neutral":add_type(e),font=fonty,bg="#cccccc",fg="#1b2a35",width=8)
NeutralButton.grid(row=0,column=0)
PyroButton = tk.Button(buttonFrame,text="Pyro",command=lambda e="Pyro":add_type(e),font=fonty,bg="#cd0204",fg="#1b2a35",width=8)
PyroButton.grid(row=1,column=0)
AquaButton = tk.Button(buttonFrame,text="Aqua",command=lambda e="Aqua":add_type(e),font=fonty,bg="#80a5ff",fg="#1b2a35",width=8)
AquaButton.grid(row=2,column=0)
FloraButton = tk.Button(buttonFrame,text="Flora",command=lambda e="Flora":add_type(e),font=fonty,bg="#07a919",fg="#1b2a35",width=8)
FloraButton.grid(row=3,column=0)
ShockButton = tk.Button(buttonFrame,text="Shock",command=lambda e="Shock":add_type(e),font=fonty,bg="#f0f03f",fg="#1b2a35",width=8)
ShockButton.grid(row=4,column=0)
FrostButton = tk.Button(buttonFrame,text="Frost",command=lambda e="Frost":add_type(e),font=fonty,bg="#affffa",fg="#1b2a35",width=8)
FrostButton.grid(row=5,column=0)
EarthButton = tk.Button(buttonFrame,text="Earth",command=lambda e="Earth":add_type(e),font=fonty,bg="#9c6321",fg="#1b2a35",width=8)
EarthButton.grid(row=6,column=0)
ToxicButton = tk.Button(buttonFrame,text="Toxic",command=lambda e="Toxic":add_type(e),font=fonty,bg="#c142b7",fg="#1b2a35",width=8)
ToxicButton.grid(row=7,column=0)
InsectButton = tk.Button(buttonFrame,text="Insect",command=lambda e="Insect":add_type(e),font=fonty,bg="#fbb041",fg="#1b2a35",width=8)
InsectButton.grid(row=8,column=0)
SkyButton = tk.Button(buttonFrame,text="Sky",command=lambda e="Sky":add_type(e),font=fonty,bg="#6eeaf5",fg="#1b2a35",width=8)
SkyButton.grid(row=9,column=0)
MetalButton = tk.Button(buttonFrame,text="Metal",command=lambda e="Metal":add_type(e),font=fonty,bg="#868686",fg="#1b2a35",width=8)
MetalButton.grid(row=0,column=1)
LightButton = tk.Button(buttonFrame,text="Light",command=lambda e="Light":add_type(e),font=fonty,bg="#fffeeb",fg="#1b2a35",width=8)
LightButton.grid(row=1,column=1)
DarkButton = tk.Button(buttonFrame,text="Dark",command=lambda e="Dark":add_type(e),font=fonty,bg="#2f2f2f",fg="#1b2a35",width=8)
DarkButton.grid(row=2,column=1)
AstralButton = tk.Button(buttonFrame,text="Astral",command=lambda e="Astral":add_type(e),font=fonty,bg="#4f2f90",fg="#1b2a35",width=8)
AstralButton.grid(row=3,column=1)
MagicButton = tk.Button(buttonFrame,text="Magic",command=lambda e="Magic":add_type(e),font=fonty,bg="#fa3cef",fg="#1b2a35",width=8)
MagicButton.grid(row=4,column=1)
MythicButton = tk.Button(buttonFrame,text="Mythic",command=lambda e="Mythic":add_type(e),font=fonty,bg="#8579fb",fg="#1b2a35",width=8)
MythicButton.grid(row=5,column=1)
CombatButton = tk.Button(buttonFrame,text="Combat",command=lambda e="Combat":add_type(e),font=fonty,bg="#811516",fg="#1b2a35",width=8)
CombatButton.grid(row=6,column=1)
LostButton = tk.Button(buttonFrame,text="Lost",command=lambda e="Lost":add_type(e),font=fonty,bg="#0cbd91",fg="#1b2a35",width=8)
LostButton.grid(row=7,column=1)
SoundButton = tk.Button(buttonFrame,text="Sound",command=lambda e="Sound":add_type(e),font=fonty,bg="#ffda9a",fg="#1b2a35",width=8)
SoundButton.grid(row=8,column=1)
SweetButton = tk.Button(buttonFrame,text="Sweet",command=lambda e="Sweet":add_type(e),font=fonty,bg="#ffc0fe",fg="#1b2a35",width=8)
SweetButton.grid(row=9,column=1)
VoidButton = tk.Button(buttonFrame,text="      ",command=lambda e="Void":add_type(e),font=fonty,bg="#534b7d",fg="#1b2a35",width=8)
VoidButton.grid(row=0,column=2)
DrownedButton = tk.Button(buttonFrame,text="Drowned",command=lambda e="Drowned":add_type(e),font=fonty,bg="#130a48",fg="#0000ff",width=8)
DrownedButton.grid(row=1,column=2)
ZeroButton = tk.Button(buttonFrame,text="Zero",command=lambda e="Zero":add_type(e),font=fonty,bg="#111111",fg="#03e89b",width=8)
ZeroButton.grid(row=2,column=2)
InfernoButton = tk.Button(buttonFrame,text="Inferno",command=lambda e="Inferno":add_type(e),font=fonty,bg="#3b0000",fg="#ec1a00",width=8)
InfernoButton.grid(row=3,column=2)
EternalButton = tk.Button(buttonFrame,text="Eternal",command=lambda e="Eternal":add_type(e),font=fonty,bg="#3e0c16",fg="#fc2f58",width=8)
EternalButton.grid(row=4,column=2)
DivineButton = tk.Button(buttonFrame,text="Divine",command=lambda e="Divine":add_type(e),font=fonty,bg="#261547",fg="#ffff00",width=8)
DivineButton.grid(row=5,column=2)
stupidButton = tk.Button(buttonFrame,text="stupid",command=lambda e="stupid":add_type(e),font=fonty,bg="#b8fe79",fg="#fd5c96",width=8)
stupidButton.grid(row=6,column=2)
SlamButton = tk.Button(buttonFrame,text="Slam",command=lambda e="Slam":add_type(e),font=fonty,bg="#ec7d50",fg="#79e857",width=8)
SlamButton.grid(row=7,column=2)
JamButton = tk.Button(buttonFrame,text="Jam",command=lambda e="Jam":add_type(e),font=fonty,bg="#d07e87",fg="#a0ff2e",width=8)
JamButton.grid(row=8,column=2)
FishingButton = tk.Button(buttonFrame,text="Fishing",command=lambda e="Fishing":add_type(e),font=fonty,bg="#564236",fg="#1b2a35",width=8)
FishingButton.grid(row=9,column=2)

# killButton = tk.Button(buttonFrame,text="k sdfjka nxc sk dsfhg",command=window.destroy,font=(fonty),width=8).grid(row=10,column=1)

resetButton = tk.Button(buttonFrame,text="Clear",command=reset,font=fonty,width=8)
resetButton.grid(row=10,column=2)

positionBool = tk.BooleanVar()
positionButton = tk.Checkbutton(buttonFrame,text="Vert.",variable=positionBool,command=update,font=fonty,width=5)
positionButton.grid(row=10,column=1)

sortBool = tk.BooleanVar(value=True)
sortButton = tk.Checkbutton(buttonFrame,text="Sort",variable=sortBool,command=update,font=fonty,width=5)
sortButton.grid(row=10,column=0)

ezreadBool = tk.BooleanVar()
ezreadButton = tk.Checkbutton(buttonFrame,text="EZRead",variable=ezreadBool,command=update,font=fonty,width=5)
ezreadButton.grid(row=11,column=2)

autoClickerButton = tk.Button(buttonFrame,text="AutoKlik",command=update_hotkey,bg="#F0A689",font=fonty,width=8)
autoClickerButton.grid(row=11,column=0)

shinyButton = tk.Button(buttonFrame,text="Shiny",command=open_shiny,bg="#5555ff",font=fonty,width=8)
shinyButton.grid(row=11,column=1)

chartFrame = tk.Frame(ALLECHARTFRAME)
chartFrame.grid(row=1, column=1, sticky="n", padx=10)
chart = tk.Text(chartFrame, width=26,height=33, font=fonty, bg="#252525",
                fg="#1b2a35", state="disabled", wrap="word")

cyggy = tk.PhotoImage(file=".\\CYGGY\\Cygnet.png")

cygnet = tk.Label(buttonFrame,image=cyggy)
cygnet.grid(row=12,column=0,columnspan=3,sticky="ew")

chart.pack()
setup_text_tags()
update()

optionmenu = tk.OptionMenu(window,option, *fonts,command=lambda x: font_change())
optionmenu.grid(row=2,column=0)

for item in range(len(fonts)):
    optionmenu['menu'].entryconfig(item, font=font.Font(family=fonts[item], size=12))

# option.trace('w', lambda *a: lb.config(font=optionmenu['menu'].entrycget(option.get(),'font')))

# https://www.pythonguis.com/tutorials/packaging-tkinter-applications-windows-pyinstaller/

window.mainloop()

