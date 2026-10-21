if Geld <= 0:
    kleur_print(f"balans: €{Geld}", ROOD)
else:
    kleur_print(f"balans: €{Geld}", GROEN)
    
                 randomevent = random.randint(1, 10)
                if randomevent == 1:
                    kleur_print("er is een brand uitgebroken in je stad!", ROOD)
                    schade = random.randint(100, 1000)
                    print(f"je moet €{schade} betalen om de schade te herstellen")
                    Geld = Geld - schade
                
                if randomevent == 2:
                    kleur_print("er is een festival in je stad!", GROEN)
                    tevredenheid = tevredenheid + 5
                    print("je tevredenheid is gestegen met 5%")
                
                if randomevent == 3:
                    kleur_print("er is een economische crisis in je stad!", ROOD)
                    inkomsten = inkomsten - (inkomsten * 0.1)
                    print("je inkomsten zijn gedaald met 10%")
                
                if randomevent == 4:
                    kleur_print("er is een ongeluk gebeurd in je stad!", ROOD)
                    schade = random.randint(50, 500)
                    print(f"je moet €{schade} betalen om de schade te herstellen")
                    Geld = Geld - schade
                    
                if randomevent == 5:
                    kleur_print("er is een natuurlijke ramp in je stad!", ROOD)
                    schade = random.randint(1000, 5000)
                    print(f"je moet €{schade} betalen om de schade te herstellen")
                    Geld = Geld - schade
                    
                if randomevent == 6:
                    kleur_print("er is een nieuwe wet aangenomen in je stad!", GROEN)
                    tevredenheid = tevredenheid + 10
                    print("je tevredenheid is gestegen met 10%")
                    
                if randomevent == 7:
                    kleur_print("er is een nieuwe wet aangenomen in je stad!", ROOD)
                    tevredenheid = tevredenheid - 10
                    print("je tevredenheid is gedaald met 10%")
                    
                if randomevent == 8:
                    kleur_print("er is een nieuwe technologie ontwikkeld in je stad!", GROEN)
                    inkomsten = inkomsten + (inkomsten * 0.1)
                    print("je inkomsten zijn gestegen met 10%")
                    
                if randomevent == 9:
                    kleur_print("er is een overval gepleegd in je stad!", ROOD)
                    schade = random.randint(100, 1000)
                    print(f"je moet €{schade} betalen om de schade te herstellen")
                    Geld = Geld - schade
                    
                if randomevent == 10:
                    kleur_print("er is een nieuwe attractie geopend in je pretpark!", GROEN)
                    tevredenheid = tevredenheid + 5
                    print("je tevredenheid is gestegen met 5%")