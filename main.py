# !/bin/python3
# Author: phga
# Date: 2021-10-28
# Description: Example code that enables implementation of possible solutions
#              for a question from the final exam written by Computer Engineers
from random import randint

################ NICHT RELEVANT UM AUFGABE ZU BEARBEITEN

# Wen es interessiert: Das hier nennt sich list comprehension
zeiterfassungstabelle = [[tag, randint(6, 10) * i, randint(1, 30) * i - 1]
                         for i in [1, 2]
                         for tag in range(1, 32) if randint(0, 3)]
# Zeitentabelle noch nach Tagen sortieren
zeiterfassungstabelle = sorted(zeiterfassungstabelle, key=lambda row: row[0])


################ Hilfsfunktionen

def tageImMonat(monat, jahr):
    return 31  # lel


def schreibeKopf(persnr, jahr, monat):
    monat = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli",
             "August", "September", "Oktober", "November", "Dezember"][monat - 1]
    heading = f'Mitarbeiter: {persnr: <5}{" " * 8}{monat} {jahr}'
    tbl_heading = f'Tag  Kommen  Gehen   Anwesenheit  Bemerkung{" " * 6}'
    tbl_spacer = "=" * len(tbl_heading)
    print("\n" + heading)
    print(tbl_heading)
    print(tbl_spacer)


def schreibeZeile(tag, std1, min1, std2, min2, anwTag, bemerkung):
    anwStd = anwTag // 60
    anwMin = anwTag % 60
    if std1 == -1 and min1 == -1:
        sm1 = " " * 5
        anwT = "00:00"
    else:
        sm1 = f'{std1:02}:{min1:02}'
        anwT = f'{anwStd:02}:{anwMin:02}'

    if std2 == -1 and min2 == -1:
        sm2 = " " * 5
        anwT = "00:00"
    else:
        sm2 = f'{std2:02}:{min2:02}'
        anwT = f'{anwStd:02}:{anwMin:02}'

    tbl_row = f'{tag: <5}{sm1}   {sm2}   {anwT}{" " * 8}{bemerkung}'
    print(tbl_row)


def schreibeFuss(anwMonat):
    anwStd = anwMonat // 60
    anwMin = anwMonat % 60
    tbl_spacer = "=" * 48
    footer = f'Summe Anwesenheit:  {anwStd:02}:{anwMin:02}'
    print(tbl_spacer)
    print(footer + "\n")


################ LÖSUNGSANSATZ HIER BEGINNEN

# Wichtige Infos aus der Angabe:
#
# Pro Tag max. zwei Zeiten
# => 2 Zeiten: Kommen, Gehen, (Gehen - Kommen), ---
# => 1 Zeit:   Kommen, -----, 00:00           , "Buchung fehlt"
# => 0 Zeit:   ------, -----, 00:00           , "nicht anwesend"
#
# Ende der Liste: Summe der Anwesenheitszeichen
# Ausgabe: Tabelle für einen Monat für einen MA

def erzeugeListe(persnr, zeiten, jahr, monat):
    # Implementierung hier hin (:
    schreibeKopf(persnr, jahr, monat)
    awm = 0;
    pairs_time = [[0, 0, 0, 0, 0, 0, '']]
    no_pairs_time = [[0, 0, 0, 0, 0, 0, '']]
    to_remove_time = [[0, 0, 0]]
    for i in zeiterfassungstabelle:
        for x in zeiterfassungstabelle:
            if i[0] == x[0] and i[1] < x[1]:
                to_remove_time.append(i)
                to_remove_time.append(x)
                pairs_time.append([i[0], i[1], i[2], x[1], x[2], 0, ''])
    pairs_time.remove([0, 0, 0, 0, 0, 0, ''])
    to_remove_time.remove([0, 0, 0])
    for i in to_remove_time:
        zeiterfassungstabelle.remove(i)
    for i in zeiterfassungstabelle:
        no_pairs_time.append([i[0], i[1], i[2], 0, 0, 0, 'Buchung fehlt'])
    no_pairs_time.remove([0, 0, 0, 0, 0, 0, ''])
    res = sorted(pairs_time + no_pairs_time)
    if len(res) < 31:
        for x in range(1, 31):
            if x == res[x][0]:
                a = 0
            else:
                res.insert(x, [x, 0, 0, 0, 0, 0, 'nicht anwesend'])
    res.remove([1, 0, 0, 0, 0, 0, 'nicht anwesend'])

    for i in res:
        schreibeZeile(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
    schreibeFuss(awm)


pass

################ TABELLE ERZEUGEN
erzeugeListe(12345, zeiterfassungstabelle, 2021, 10)
