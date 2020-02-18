def menu():
    keuze = input(
        "Welkom bij Mastermind! Kies een gamemode. \n[a] Raad de geheime code \n[b] Wees de gamemaster \n[c] Spelregels\n")
    if keuze.lower() == "a":
        secret()
    elif keuze.lower() == "b":
        algoritme1()
    elif keuze.lower() == "c":
        print("\n***Bij de gamemode -Raad de geheime code- wordt er een 4 cijferige code "
              "gegenereerd en is het aan u de taak om deze binnen 10 pogingen te raden."
              "\nLukt dat niet dan heeft de computer gewonnen.***"
              "\n\n***Bij de gamemode -Wees de gamemaster- mag uzelf een 4 cijferige code opmaken "
              "en raadt de computer d.m.v. algoritmes."
              "\nLukt dat de computer niet in 10 pogingen dan bent u de winnaar!")
menu()