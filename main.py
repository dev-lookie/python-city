import time
import os
import colorsys
import random

versie = "1.8"

MAP = os.path.dirname(os.path.abspath(__file__))
SPELER_BESTAND = os.path.join(MAP, "speler.txt")
GEBOUWEN_BESTAND = os.path.join(MAP, "gebouwen.txt")

INKOMSTEN_PER_INWONER = 10

GROEN = "\033[32m"
ROOD = "\033[31m"
ORANJE = "\033[38;2;255;165;0m"
BLAUW = "\033[34m"
PAARS = "\033[35m"
GEEL = "\033[33m"
WIT = "\033[37m"
ZWART = "\033[30m"
RESET = "\033[0m"


# ==================== BESTANDEN LEZEN ====================

# ---------- lees_speler ----------
def lees_speler():
    speler = {}
    with open(SPELER_BESTAND, "r", encoding="utf-8") as bestand:
        for regel in bestand:
            regel = regel.strip()
            if regel == "" or regel.startswith("#"):
                continue
            naam, waarde = regel.split("=")
            speler[naam.strip()] = int(waarde.strip())
    return speler


# ---------- lees_gebouwen ----------
def lees_gebouwen():
    gebouwen = {}
    with open(GEBOUWEN_BESTAND, "r", encoding="utf-8") as bestand:
        for regel in bestand:
            regel = regel.strip()
            if regel == "" or regel.startswith("#"):
                continue
            naam, prijs, tevredenheid, inkomen, min_inwoners, max_inwoners = regel.split(",")
            gebouwen[naam.strip()] = {
                "prijs": int(prijs),
                "tevredenheid": int(tevredenheid),
                "inkomen": int(inkomen),
                "min_inwoners": int(min_inwoners),
                "max_inwoners": int(max_inwoners),
            }
    return gebouwen


speler = lees_speler()
gebouwen = lees_gebouwen()


# ==================== HULPFUNCTIES ====================

# ---------- kleur_print ----------
def kleur_print(tekst, kleur):
    print(kleur + tekst + RESET)


# ---------- scherm_wissen ----------
def scherm_wissen():
    os.system("cls" if os.name == "nt" else "clear")


# ---------- laad_animatie ----------
def laad_animatie(tekst):
    for i in range(4):
        print("\r" + tekst + "." * i + "\033[0m", end="", flush=True)
        time.sleep(1)

    print("\r\033[30m" + tekst + "." * 5 + "\033[0m")


# ---------- regenboog ----------
def regenboog(tekst, snelheid=0.04):
    hue = 0

    try:
        while True:
            uitvoer = ""

            for i, letter in enumerate(tekst):
                kleur_hue = (hue + i * 0.025) % 1.0
                r, g, b = colorsys.hsv_to_rgb(kleur_hue, 1, 1)

                R = int(r * 255)
                G = int(g * 255)
                B = int(b * 255)

                uitvoer += (
                    f"\033[38;2;{R};{G};{B}m{letter}"
                )

            print("\r" + uitvoer + "\033[0m", end="", flush=True)

            hue = (hue + 0.005) % 1.0
            time.sleep(snelheid)

    except KeyboardInterrupt:
        print("\033[0m")
        print()


# ==================== SCHERMEN ====================

# ---------- toon_titel ----------
def toon_titel():
    scherm_wissen()
    kleur_print("==============================", GROEN)
    kleur_print("          python city", GROEN)
    kleur_print(f"          Version {versie}", GEEL)
    kleur_print("==============================", GROEN)


# ---------- toon_start_gegevens ----------
def toon_start_gegevens():
    kleur_print("========== gegevens ==========", PAARS)
    print(f"Geld: €{speler['Geld']}")
    print(f"Inwoners: {speler['Inwoners']}")
    print(f"Tevredenheid: {speler['tevredenheid']}%")
    kleur_print(f"Schulden: €{speler['schulden']}", ROOD)
    kleur_print(f"maand: {speler['maand']}", GEEL)
    kleur_print(f"Inkomsten: €{speler['inkomsten']}", GROEN)
    print(f"huizen: {speler['huizen']}")
    print(f"winkels: {speler['winkels']}")
    print(f"fabrieken: {speler['fabrieken']}")
    print(f"parken: {speler['parken']}")
    print(f"pretparken: {speler['pretparken']}")
    kleur_print("------------------------------", BLAUW)


# ---------- toon_menu ----------
def toon_menu():
    print("wat wil je doen?")
    print("")
    print("1. stad bekijken")
    print("2. gegevens bekijken")
    print("3. volgende maand")
    print("4. gebouw bouwen")
    print("5. geld lenen")
    print("6. loterij spelen")
    print("7. stoppen")
    kleur_print("------------------------------", BLAUW)


# ---------- stad_bekijken ----------
def stad_bekijken():
    scherm_wissen()
    kleur_print("============ stad ============", PAARS)
    print(f"huizen: {speler['huizen']}")
    print(f"winkels: {speler['winkels']}")
    print(f"fabrieken: {speler['fabrieken']}")
    print(f"parken: {speler['parken']}")
    print(f"pretparken: {speler['pretparken']}")
    kleur_print("------------------------------", BLAUW)


# ---------- gegevens_bekijken ----------
def gegevens_bekijken():
    scherm_wissen()
    kleur_print("========== gegevens ==========", PAARS)
    print(f"Geld: €{speler['Geld']}")
    print(f"inwoners: {speler['Inwoners']}")
    print(f"huizen: {speler['huizen']}")
    kleur_print(f"Schulden: €{speler['schulden']}", ROOD)
    kleur_print(f"Inkomsten: €{speler['inkomsten']}", GROEN)
    print(f"Tevredenheid: {speler['tevredenheid']}%")
    kleur_print(f"maand: {speler['maand']}", GEEL)
    print(f"winkels: {speler['winkels']}")
    print(f"fabrieken: {speler['fabrieken']}")
    print(f"parken: {speler['parken']}")
    print(f"pretparken: {speler['pretparken']}")
    kleur_print("------------------------------", BLAUW)


# ==================== VOLGENDE MAAND ====================

# ---------- willekeurige_gebeurtenis ----------
def willekeurige_gebeurtenis():
    randomevent = random.randint(1, 10)
    if randomevent == 1:
        kleur_print("er is een brand uitgebroken in je stad!", ROOD)
        schade = random.randint(100, 1000)
        print(f"je moet €{schade} betalen om de schade te herstellen")
        speler["Geld"] = speler["Geld"] - schade

    if randomevent == 2:
        kleur_print("er is een festival in je stad!", GROEN)
        speler["tevredenheid"] = speler["tevredenheid"] + 5
        print("je tevredenheid is gestegen met 5%")

    if randomevent == 3:
        kleur_print("er is een economische crisis in je stad!", ROOD)
        speler["inkomsten"] = speler["inkomsten"] - (speler["inkomsten"] * 0.1)
        print("je inkomsten zijn gedaald met 10%")

    if randomevent == 4:
        kleur_print("er is een ongeluk gebeurd in je stad!", ROOD)
        schade = random.randint(50, 500)
        print(f"je moet €{schade} betalen om de schade te herstellen")
        speler["Geld"] = speler["Geld"] - schade

    if randomevent == 5:
        kleur_print("het was een rustige maand.", GROEN)

    if randomevent == 6:
        kleur_print("er is een nieuwe wet aangenomen in je stad!", GROEN)
        speler["tevredenheid"] = speler["tevredenheid"] + 10
        print("je tevredenheid is gestegen met 10%")

    if randomevent == 7:
        kleur_print("het was een rustige maand.", GROEN)

    if randomevent == 8:
        kleur_print("er is een nieuwe technologie ontwikkeld in je stad!", GROEN)
        speler["inkomsten"] = speler["inkomsten"] + (speler["inkomsten"] * 0.1)
        print("je inkomsten zijn gestegen met 10%")

    if randomevent == 9:
        kleur_print("er is een overval gepleegd in je stad!", ROOD)
        schade = random.randint(1, 500)
        print(f"je moet €{schade} betalen om de schade te herstellen")
        speler["Geld"] = speler["Geld"] - schade

    if randomevent == 10:
        kleur_print("er is een nieuwe attractie geopend in je pretpark!", GROEN)
        speler["tevredenheid"] = speler["tevredenheid"] + 5
        print("je tevredenheid is gestegen met 5%")


# ---------- toon_belasting ----------
def toon_belasting():
    winkels = speler["winkels"]
    fabrieken = speler["fabrieken"]
    pretparken = speler["pretparken"]

    if winkels > 0:
        print(f"je hebt {winkels} winkels, je krijgt €{winkels * gebouwen['winkel']['inkomen']} belasting van de winkels!")

        if fabrieken > 0:
            print(f"je hebt {fabrieken} fabrieken, je krijgt €{fabrieken * gebouwen['fabriek']['inkomen']} belasting van de fabrieken!")

    if pretparken > 0:
        print(f"je hebt {pretparken} pretparken, je krijgt €{pretparken * gebouwen['pretpark']['inkomen']} belasting van de pretparken!")

    if winkels == 0 and pretparken == 0 and fabrieken == 0:
        print("je hebt geen gebouwen die inkomsten opleveren")


# ---------- bereken_inkomsten ----------
def bereken_inkomsten():
    return (
        (speler["winkels"] * gebouwen["winkel"]["inkomen"])
        + (speler["fabrieken"] * gebouwen["fabriek"]["inkomen"])
        + (speler["pretparken"] * gebouwen["pretpark"]["inkomen"])
        + (speler["Inwoners"] * INKOMSTEN_PER_INWONER)
    )


# ---------- schulden_afbetalen ----------
def schulden_afbetalen():
    if speler["schulden"] > 0:
        speler["schuldbedrag"] = speler["schulden"] / 10
        print(f"je hebt schulden en je moet €{speler['schuldbedrag']} afbetalen")
        speler["schulden"] = speler["schulden"] - speler["schuldbedrag"]
        print(f"schulden: €{speler['schulden']}")
        speler["Geld"] = speler["Geld"] - speler["schuldbedrag"]


# ---------- volgende_maand ----------
def volgende_maand():
    scherm_wissen()

    kleur_print("======= volgende maand =======", PAARS)

    toon_belasting()

    kleur_print("------------------------------", BLAUW)

    willekeurige_gebeurtenis()

    kleur_print("------------------------------", BLAUW)
    print(f"Geld: €{speler['Geld']}")
    speler["inkomsten"] = bereken_inkomsten()
    kleur_print(f"Inkomsten: €{speler['inkomsten']}", GROEN)
    speler["Geld"] += speler["inkomsten"]
    print(f"Inwoners: {speler['Inwoners']}")
    print(f"huizen: {speler['huizen']}")
    print(f"fabrieken: {speler['fabrieken']}")
    print(f"parken: {speler['parken']}")
    print(f"pretparken: {speler['pretparken']}")
    print(f"Tevredenheid: {speler['tevredenheid']}%")
    speler["maand"] = speler["maand"] + 1
    speler["inkomsten"] = 0
    if speler["maand"] > 24:
        kleur_print("------------------------------", BLAUW)
        regenboog("je hebt 24 maanden gespeeld, het spel is afgelopen, bedankt voor het spelen!")
        exit()

    print(f"Maand: {speler['maand']}")
    print("")
    schulden_afbetalen()


# ==================== GEBOUWEN BOUWEN ====================

# ---------- bouw_huis ----------
def bouw_huis():
    huis = gebouwen["huis"]
    if speler["Geld"] >= huis["prijs"]:
        print("je bouwt een huis")
        inwoners_toevoegen = random.randint(huis["min_inwoners"], huis["max_inwoners"])
        print(f"je krijgt {inwoners_toevoegen} inwoners!")
        print("")
        speler["Geld"] = speler["Geld"] - huis["prijs"]
        speler["huizen"] = speler["huizen"] + 1
        speler["Inwoners"] = speler["Inwoners"] + inwoners_toevoegen
        speler["tevredenheid"] = speler["tevredenheid"] + huis["tevredenheid"]
    else:
        print("je hebt niet genoeg geld om een huis te bouwen")


# ---------- bouw_winkel ----------
def bouw_winkel():
    winkel = gebouwen["winkel"]
    if speler["Geld"] >= winkel["prijs"]:
        print("")
        print("je bouwt een winkel")
        print(f"je krijgt €{winkel['inkomen']} belasting per maand van de winkel!")
        speler["Geld"] = speler["Geld"] - winkel["prijs"]
        speler["winkels"] = speler["winkels"] + 1
        speler["tevredenheid"] = speler["tevredenheid"] + winkel["tevredenheid"]
    else:
        print("je hebt niet genoeg geld om een winkel te bouwen")


# ---------- bouw_park ----------
def bouw_park():
    park = gebouwen["park"]
    if speler["Geld"] >= park["prijs"]:
        print("")
        print("je bouwt een park")
        speler["Geld"] = speler["Geld"] - park["prijs"]
        speler["parken"] = speler["parken"] + 1
        speler["tevredenheid"] = speler["tevredenheid"] + park["tevredenheid"]
    else:
        print("je hebt niet genoeg geld om een park te bouwen")


# ---------- bouw_fabriek ----------
def bouw_fabriek():
    fabriek = gebouwen["fabriek"]
    if speler["Geld"] >= fabriek["prijs"]:
        print("")
        print("je bouwt een fabriek")
        speler["Geld"] = speler["Geld"] - fabriek["prijs"]
        speler["fabrieken"] = speler["fabrieken"] + 1
        speler["tevredenheid"] = speler["tevredenheid"] + fabriek["tevredenheid"]
    else:
        print("je hebt niet genoeg geld om een fabriek te bouwen")


# ---------- bouw_pretpark ----------
def bouw_pretpark():
    pretpark = gebouwen["pretpark"]
    if speler["Geld"] >= pretpark["prijs"]:
        print("")
        print("je bouwt een pretpark")
        speler["Geld"] = speler["Geld"] - pretpark["prijs"]
        speler["pretparken"] = speler["pretparken"] + 1
        speler["tevredenheid"] = speler["tevredenheid"] + pretpark["tevredenheid"]
    else:
        print("je hebt niet genoeg geld om een pretpark te bouwen")


# welke functie hoort bij welk gebouw (naam komt uit gebouwen.txt)
BOUW_FUNCTIES = {
    "huis": bouw_huis,
    "winkel": bouw_winkel,
    "park": bouw_park,
    "fabriek": bouw_fabriek,
    "pretpark": bouw_pretpark,
}


# ---------- gebouw_bouwen ----------
def gebouw_bouwen():
    scherm_wissen()
    laad_animatie("loading menu")
    if speler["Geld"] <= 0:
        kleur_print(f"balans: €{speler['Geld']}", ROOD)
    else:
        kleur_print(f"balans: €{speler['Geld']}", GROEN)
    kleur_print("========== gebouwen ==========", PAARS)

    namen = list(gebouwen.keys())
    for nummer, naam in enumerate(namen, start=1):
        print(f" {nummer}. {naam:<9}€{gebouwen[naam]['prijs']}")
    print(f" {len(namen) + 1}. terug naar hoofdmenu")
    kleur_print("------------------------------", BLAUW)

    gebouw_keuze = input("wat wil je bouwen?")
    if gebouw_keuze == str(len(namen) + 1):
        print("je hebt gekozen om terug te gaan naar het hoofdmenu")
        scherm_wissen()
    elif gebouw_keuze.isdigit() and 1 <= int(gebouw_keuze) <= len(namen):
        naam = namen[int(gebouw_keuze) - 1]
        if naam in BOUW_FUNCTIES:
            BOUW_FUNCTIES[naam]()
        else:
            print(f"een {naam} kan nog niet gebouwd worden")


# ==================== GELD LENEN ====================

# ---------- geld_lenen ----------
def geld_lenen():
    scherm_wissen()
    kleur_print("========= geld lenen =========", PAARS)
    print("je hebt gekozen om geld te lenen")
    print("schulden worden afgeschreven aan het einde van de maand")
    print("")
    speler["Geld"] = speler["Geld"] + 1000
    print(f"Geld: €{speler['Geld']}")
    speler["schulden"] = speler["schulden"] + 1000
    print(f"Schulden: €{speler['schulden']}")


# ==================== LOTERIJ ====================

# ---------- loterij_spelen ----------
def loterij_spelen():
    scherm_wissen()
    laad_animatie("loading minigame")

    kleur_print("========= loterij spelen =========", PAARS)
    print("je hebt gekozen om de loterij te spelen")
    print("je kan €100 inzetten om mee te doen aan de loterij")
    print("als je wint krijg je €10.000")
    print("als je verliest verlies je €100")
    print("")
    loterij_keuze = input("wil je meedoen aan de loterij? (ja/nee)")
    if loterij_keuze == "ja":
        if speler["Geld"] >= 100:
            print("")
            print("je doet mee aan de loterij")
            speler["Geld"] = speler["Geld"] - 100
            loterij_winst = random.randint(1, 10)
            if loterij_winst in [1, 5, 9]:
                print("je hebt gewonnen!")
                speler["Geld"] = speler["Geld"] + 10000
                print(f"Geld: €{speler['Geld']}")
            else:
                print("je hebt verloren!")
                print(f"Geld: €{speler['Geld']}")
        else:
            print("je hebt niet genoeg geld om mee te doen aan de loterij")
    elif loterij_keuze == "nee":
        print("je hebt gekozen om niet mee te doen aan de loterij")
    else:
        kleur_print("dit is geen geldige invoer", ROOD)
        kleur_print("probeer ja of nee in te voeren", ROOD)


# ==================== SPEL ====================

# ---------- stoppen ----------
def stoppen():
    print("je hebt gekozen om het spel te stoppen")
    exit()


# ---------- verwerk_keuze ----------
def verwerk_keuze(keuze):
    if keuze == "1":
        stad_bekijken()

    elif keuze == "2":
        gegevens_bekijken()

    elif keuze == "3":
        volgende_maand()

    elif keuze == "4":
        gebouw_bouwen()

    elif keuze == "5":
        geld_lenen()

    elif keuze == "6":
        loterij_spelen()

    elif keuze == "7":
        stoppen()

    elif keuze == "1983":
        speler["maand"] += 25

    elif keuze == "1982":
        speler["Geld"] += 1000000000

    else:
        kleur_print("dit is geen geldige invoer", ROOD)
        kleur_print("probeer 1, 2, 3, 4, 5, 6 of 7 in te voeren", ROOD)


# ---------- controleer_geld ----------
def controleer_geld():
    if speler["Geld"] <= 0:
        kleur_print("------------------------------", BLAUW)
        kleur_print("je hebt geen geld meer, je kan niet verder spelen", ORANJE)
        kleur_print("leen geld van de bank om verder te spelen", ORANJE)
        kleur_print("of ga door naar de volgende maand om inkomsten te krijgen", ORANJE)
        print("")


# ---------- hoofdmenu ----------
def hoofdmenu():
    while speler["maand"] <= 24:
        keuze = ""
        while keuze != "6":
            laad_animatie("loading")
            toon_menu()
            keuze = input("maak een keuze:")

            verwerk_keuze(keuze)

            controleer_geld()


# ---------- start_spel ----------
def start_spel():
    toon_titel()
    laad_animatie("loading Game")
    toon_start_gegevens()
    hoofdmenu()


# ==================== PROGRAMMA STARTEN ====================

if __name__ == "__main__":
    start_spel()
