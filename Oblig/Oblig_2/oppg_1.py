# oppgave 1a
# Her legger bruken inn et tall eller tekst.
number = input("Hva er meningen med livet? ")
# Her sjekkes det om brukeren har lagt inn et tall.
try:
    number = int(number)
# Om det ikke er tall, gi beskjed om å skrive et tall.
except ValueError:
    number = None
    print("Du må skrive et tall.")
# Dersom ValueError dukker opp, koden stoppes.
    exit("Kjør koden på nytt!")
# Sjekker om numret er 42.
if number == 42:
    print("Det stemmer, meningen med livet er 42!")
# Oppgave 1b
# Sjekker om numret er høyre enn 30 men mindre en 50, hvis ikke print ut feil.
elif 30 < number < 50:
    print("Nærme, men feil.")
else:
    print("FEIL!")
