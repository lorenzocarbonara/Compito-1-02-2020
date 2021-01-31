prenotazioni=[]
conferma_y=[]
conferma_n=[]
while True:
    prenotazioni=input("Inserire nome e cognome: (Per interrompere digitare 0) ")
    if prenotazioni=="0":
        break
    else:
        prenotazioni.append(prenotazioni)
        conferma=input("Il partecipante deve ricevere la conferma? ")
        if conferma=="Sì":
            conferma_y.append(prenotazioni)
        elif conferma=="No":
            conferma_n.append(prenotazioni)
print("I partecipanti a ricevere le conferme sono: ", conferma_y)