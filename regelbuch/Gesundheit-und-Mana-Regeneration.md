---
title: Gesundheit und Mana: Regeneration
aliases: [Mana-Regeneration, Gesundheit-Regeneration, LE-Regeneration, Regeneration, Schlafwurf, Schlafphase, Registufe, Rast]
status: entwurf
---

# Gesundheit und Mana: Regeneration

Der Held erholt sich von selbst. Sein Mana kommt jede Stunde ein Stück zurück. Nach einer langen Schlafphase würfelt er außerdem, wie viel Mana, Gesundheit und Lebensenergie der Trefferzonen ([[Glossar#LE|LE]]) er zurückbekommt. Wie gut die Rast ist, bestimmt die Regenerationsstufe ([[Glossar#Registufe|Registufe]]), die der Meister festlegt.

## Mana pro Stunde

Das Mana des Helden regeneriert pro Stunde:

```text
Mana pro Stunde = Aura × 2
```

Das Talent „Mana-Regeneration“ erhöht die Stundenrate:

- Stufe 1 multipliziert die Stundenrate mit 1,5.
- Stufe 2 multipliziert sie mit 2.

Es gilt nur die stärker wirkende Stufe. Die Stufen stapeln sich nicht. Das Ergebnis der Multiplikation wird sofort nach den Rundungsregeln aus [[Wuerfeln-und-Proben|Würfeln und Proben]] gerundet, noch bevor der Schlafwurf (siehe unten) dazukommt. Das Talent wirkt nur auf die Stundenrate, nicht auf den Schlafwurf. Mehr zu diesem Talent steht im Kapitel [[Talente-die-Werte-veraendern|Talente, die Werte verändern]].

Die Stundenrate wird nicht gleichmäßig verteilt. Der Held erhält sie als einen Betrag in der letzten Sekunde vor Beginn der nächsten vollen Stunde. Er erhält sie nur, wenn sein Mana zu diesem Zeitpunkt unter dem Maximum liegt. Lässt der Meister Zeit vergehen ([[Zeit-und-Spielablauf|Zeit und Spielablauf]]), gibt es für jede dabei vollendete Stunde eine solche Gutschrift. Die gesamte Regeneration ist durch das Mana-Maximum gedeckelt. Das Mana fällt nie unter 0.

## Schlaf als Erholung

### Die Schlafphase

Der Schlafwurf setzt eine abgeschlossene Schlafphase von mindestens 6 Stunden voraus. Als Schlafphase zählen:

- der Zustand Schlaf;
- ein Zustand Bewusstlos von mindestens 6 Stunden;
- ein Zustand Koma von mindestens 6 Stunden. Beim Koma kommt der Schlafwurf zusätzlich zum Regenerationstakt des Komas.

Die Zustände stehen im [[Zustaende-Katalog|Zustandskatalog]].

Eine kürzere Schlafphase gibt keinen anteiligen Schlafwurf. Der Wurf entfällt ganz. Die Stundenrate des Manas läuft während einer kürzeren Schlafphase trotzdem normal weiter.

Aneinandergereihte Schlafphasen von je mindestens 6 Stunden geben je einen eigenen Schlafwurf. Es gibt aber höchstens 2 Schlafwürfe in jedem rollenden Zeitraum von 24 Stunden. Ein Schlafwurf zählt nur, wenn in den 24 Stunden davor höchstens ein weiterer lag.

Beispiele: 12 Stunden Schlaf am Stück sind 2 Phasen und geben 2 Würfe. Der Abenteuerbeginn ist um 08:00. Schlaf von 22:00 bis 10:00 gibt Würfe um 04:00 und um 10:00. Schlaf von 10:00 bis 22:00 gibt um 16:00 keinen Wurf mehr.

Gewürfelt wird, sobald die Schlafphase abgeschlossen ist. Hunger, Durst und Schlafmangel ändern diese Regeneration nicht. Sie wirken nur über die Behinderung ([[Behinderung-und-Erschwerung|Behinderung und Erschwerung]]).

### Die Registufe

Der Meister legt die Registufe für den Ruheabschnitt fest, nach der Qualität des Rastplatzes und weiteren Umständen der Lage. Die Registufe bestimmt den Würfel des Schlafwurfs:

| Registufe | Würfelstufe |
|---:|---|
| 0 oder weniger | 0 |
| 1 | W4 |
| 2 | W6 |
| 3 | W8 |
| 4 | W10 |
| 5 | W12 |
| 6 | W20 |
| 7 oder mehr | W30 |

Mana und Gesundheit verwenden dieselbe Tabelle.

Legt der Meister eine gemeinsame Registufe für eine ganze Rastgruppe fest, würfelt trotzdem jeder Held einzeln, mit eigenem Wurf und eigener Vitalität.

### Rüstung im Schlaf

Die im Schlaf getragene Rüstung mindert die Registufe des Helden je nach ihrer Lage ([[Ruestung|Rüstung]]):

| Lage | Malus auf die Registufe |
|---:|---|
| 0 | keiner |
| 1 | keiner |
| 2 | −1 |
| 3 | −2 |
| 4 | −3 |
| 5 | −2, außer das Material ist Stoff oder Spinnwebe (dort keiner) |

Trägt der Held mehrere Lagen, zählt nur der höchste Malus. Mali mehrerer Lagen addieren sich nicht.

Der Malus wirkt auf den Schlafwurf für Gesundheit und auf den Schlafwurf für Mana gleichermaßen.

## Der Schlafwurf für Mana

Eine abgeschlossene Schlafphase gibt dem Helden einen einmaligen Wurf auf die Würfelstufe seiner Registufe. Das Ergebnis kommt zur Stundenrate dazu. Die gesamte Regeneration (Stundenrate plus Schlafwurf) bleibt durch das Mana-Maximum gedeckelt.

## Der Schlafwurf für Gesundheit und LE

### Wie viele Punkte der Held erhält

Der Held würfelt auf die Würfelstufe seiner Registufe. Zum Ergebnis kommt seine Vitalität dazu ([[Attribute|Attribute]]):

```text
Punkte = Wurf auf die Würfelstufe + Vitalität
```

Wurf und Verteilung gelten pro Held. Jeder Held würfelt und verteilt seine Punkte mit seiner eigenen Vitalität.

### Wohin die Punkte gehen

Der Held verteilt die Punkte einzeln in dieser Reihenfolge:

1. Der erste Punkt geht auf die Gesundheit.
2. Danach geht je ein Punkt auf jede Trefferzone, deren LE auf 0 steht, in dieser festen Reihenfolge: Kopf, Brust, Unterleib, Arm rechts, Arm links, Bein rechts, Bein links. Bei Kreaturen gilt die Zonenreihenfolge der Kreatur ([[Kreaturen-im-Kampf|Kreaturen im Kampf]]). Mehrere Zonen mit LE 0 werden strikt nacheinander in dieser Reihenfolge bedient, nie gleichzeitig oder anteilig.
3. Steht keine Trefferzone mehr bei LE 0, gehen weitere Punkte wieder auf die Gesundheit.
4. Kann die Gesundheit keine weiteren Punkte mehr aufnehmen, gehen die restlichen Punkte einzeln auf die Trefferzone mit der niedrigsten LE. Nach jedem Punkt wird neu bestimmt, welche Zone das ist.

Die Verteilung endet, wenn alle Punkte verteilt sind oder Gesundheit und alle Zonen ihr Maximum erreicht haben. Kein Wert steigt über sein Maximum. Die Maximalwerte von Gesundheit und LE stehen im Kapitel [[Kreaturen-im-Kampf|Kreaturen im Kampf]].

### Zauber und KI-Fähigkeiten, die den Schlaf stärken

Diese Wirkungen stapeln sich untereinander und mit dem Rüstungs-Malus.

**Ruhiger Schlaf** (Spruchmagie, Schule Heilung, Grad 1): Die Würfelstufe steigt um 1, wenn das Ziel mindestens 6 Stunden schläft. Die Aufwach-Sinnesschärfe-Probe wird um 6 erschwert.

**Schlaf der Heilung** (Spruchmagie, Schule Heilung, Grad 2): Die Würfelstufe steigt um 2, und die Punkte steigen zusätzlich um Magie × 2. Es zählt die Magie des Wirkenden, nicht die des schlafenden Ziels, wenn Wirkender und Ziel verschiedene Personen sind. Die Aufwach-Probe wird um 12 erschwert.

Eine Würfelstufe höher bedeutet eine Zeile höher in der Tabelle oben, also eine um 1 höhere Registufe. Der Rüstungs-Malus und der Würfelstufen-Bonus liegen auf derselben Skala. Sie können sich gegenseitig aufheben.

**Heilender Schlaf** (KI-Fähigkeit, [[KI|KI]]): Der Effekt wirkt unabhängig vom Wurf und von der Verteilung oben. Am Ende der 6-stündigen Schlafphase heilt er zusätzlich 1 LE pro Punkt der Erschwerung, die der Magier beim Wirken frei gewählt hat. Jede Trefferzone und die Gesundheit erhalten diesen Betrag gleichzeitig und unabhängig voneinander. Es gibt keine Priorisierung. Jeder Wert bleibt am eigenen Maximum gedeckelt. Der Effekt kommt zusätzlich zum normalen Schlafwurf. Die Aufwach-Sinnesschärfe-Probe wird um denselben Erschwerungs-Wert erschwert.

Mehr zu den Zaubern steht im Kapitel [[Spruchmagie|Spruchmagie]].

## Beispiele

**Mana pro Stunde.** Ein Held mit Aura 5 regeneriert ohne Talent 5 × 2 = 10 Mana pro Stunde. Mit der zweiten Stufe des Talents sind es 10 × 2 = 20 Mana pro Stunde.

**Mana im Schlaf.** Ein Held mit Aura 3 schläft 8 Stunden, die Registufe ist 4. Er regeneriert 3 × 2 × 8 = 48 Mana aus der Stundenrate (ohne Talent). Dazu würfelt er einmal einen W10 (Registufe 4). Beides zusammen ist durch das Mana-Maximum gedeckelt.

**Punkte für Gesundheit und LE.** Ein Held hat Vitalität 6 und Registufe 5 ohne Rüstungsmalus. Die Würfelstufe ist W12. Der Wurf ergibt 8, also hat er 8 + 6 = 14 Punkte.

**Verteilung.** Der Kopf und das rechte Bein des Helden stehen auf LE 0. Die Gesundheit ist bei 80 % ihres Maximums, alle übrigen Zonen sind voll. Der Held hat 14 Punkte:

```text
Punkt 1       → Gesundheit
Punkt 2       → Kopf (LE 0 → 1; Kopf kommt in der Reihenfolge zuerst)
Punkt 3       → Bein rechts (LE 0 → 1; einzige Zone mit LE 0)
Punkte 4 bis 14 → wieder auf Gesundheit, bis sie ihr Maximum erreicht;
                  danach einzeln auf die jeweils niedrigste Zonen-LE
```

**Rüstung im Schlaf.** Ein Held schläft in einer Lage-5-Rüstung aus Drachenschuppe. Das Material ist weder Stoff noch Spinnwebe, also gilt der Malus von −2 auf die Registufe. Er wirkt auf den Schlafwurf für Gesundheit und für Mana. Eine Lage-5-Rüstung aus Stoff erhält diesen Malus nicht.

**Ruhiger Schlaf.** Der Zauber ist gewirkt. Der Schläfer hat Vitalität 6 und Registufe 5 ohne Rüstungsmalus. Die Würfelstufe steigt um 1, die Tabellenzeile springt von Registufe 5 (W12) auf Registufe 6 (W20). Der Wurf ergibt 8, die Punkte sind 8 + 6 = 14. Es wird mit W20 statt W12 gewürfelt.

**Schlaf der Heilung.** Der Schläfer hat Vitalität 6 und Registufe 5 ohne Rüstungsmalus. Die Wirkende hat Magie 4. Die Würfelstufe steigt um 2, die Tabellenzeile springt von Registufe 5 (W12) auf Registufe 7 (W30, das Tabellenmaximum ab Registufe 7). Der Wurf ergibt 8. Die Punkte sind 8 + 6 (Vitalität des Schläfers) + 8 (Magie × 2 der Wirkenden, nicht des Schläfers) = 22.

**Rüstung und Zauber heben sich auf.** Ein Held trägt eine Lage-3-Rüstung (−2) und hat Schlaf der Heilung auf sich gewirkt (+2). Die Registufe ändert sich netto nicht und bleibt 5 (W12). Der Bonus von Magie × 2 auf die Punkte gilt trotzdem zusätzlich.

**Heilender Schlaf.** Der Magier hat beim Wirken eine Erschwerung von 15 gewählt. Unabhängig vom Wurf und der Verteilung erhalten am Ende der 6-stündigen Schlafphase jede Trefferzone und die Gesundheit zusätzlich 15 LE, jeweils am eigenen Maximum gedeckelt. Bei den meisten Helden ist damit am nächsten Morgen praktisch alles geheilt. Die Aufwach-Sinnesschärfe-Probe ist um 15 erschwert.
