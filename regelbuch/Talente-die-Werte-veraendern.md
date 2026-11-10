---
title: Talente, die Werte verändern
aliases: [Talent-Modifikator, Talent-Faktor, Zäher Bursche, Mana-Regeneration, Guter-Erfolg-Schwelle, Gute-Familie, Spruchgüte, Gute KI, Gute PSI, Gute Wunder, Fernkampfgeschick, Zuschlag, Schwelle des guten Erfolgs]
status: entwurf
---

# Talente, die Werte verändern

Manche Talente ändern, wie sich ein Wert des Helden ergibt. Sie addieren einen Zuschlag, multiplizieren einen Wert mit einem Faktor, ersetzen die Schwelle des guten Erfolgs oder verschieben die Schwellen des guten und des meisterlichen Erfolgs im Fernkampf. Sie heben nicht das Maximum eines Werts an ([[Talente-die-Maxima-anheben|Talente, die Maxima anheben]]), sondern den Wert selbst.

Bei allen vier gilt die Regel der [[Talente|Stufenketten]]: Es zählt nur die höchste Stufe, die der Held besitzt. Die niedrigere Stufe bleibt Voraussetzung, trägt aber nichts mehr bei.

## Zuschlag: Zäher Bursche

Ein Talent mit Zuschlag addiert einen festen Bonus auf einen Wert des Helden, der sich sonst schon aus anderen Regeln ergibt. Zäher Bursche ist ein solches Talent. Es hat drei Stufen und wirkt auf bis zu drei Werte zugleich: die Selbstbeherrschung ([[Glossar#SB|SB]]), die Gesundheit und die Trefferschwelle ([[Glossar#TS|TS]]).

Der Bonus ist der Gesamtwert der Stufe, kein Zuwachs gegenüber der Stufe davor:

- **Stufe 1:** Selbstbeherrschung +1, Gesundheit +2.
- **Stufe 2:** Selbstbeherrschung +3, Gesundheit +4, Trefferschwelle +1.
- **Stufe 3:** Selbstbeherrschung +6, Gesundheit +7, Trefferschwelle +2.

Jeder der Werte wird für sich ausgewertet. Es zählt der höchste Bonus, den eine besessene Stufe für diesen Wert gibt.

Beispiel: Der Held besitzt Zäher Bursche Stufe 2 (nicht Stufe 3). Er bekommt Selbstbeherrschung +3, Gesundheit +4 und Trefferschwelle +1. Auf die Selbstbeherrschung zählt nicht +1 +3 = +4, denn nur der eigene Wert von Stufe 2 zählt.

Mehr zu Selbstbeherrschung, Gesundheit und Trefferschwelle steht in den Kapiteln [[Treffer-und-Schaden]] und [[Gesundheit-und-Mana-Regeneration]].

## Faktor: Mana-Regeneration

Ein Talent mit Faktor multipliziert einen Wert des Helden mit einer festen Zahl. Die Mana-Regeneration ist ein solches Talent. Es hat zwei Stufen und wirkt auf die natürliche Mana-Regeneration ([[Gesundheit-und-Mana-Regeneration|Gesundheit und Mana: Regeneration]]):

- **Stufe 1:** Faktor 1,5.
- **Stufe 2:** Faktor 2,0.

Der Faktor ist ein absoluter Faktor, kein zusätzlicher Aufschlag. Es gilt der höchste Faktor der besessenen Stufen, mindestens aber 1. Die zweite Stufe ersetzt die erste, sie multipliziert nicht zusätzlich mit ihr. Das Ergebnis der Multiplikation wird wie jede Multiplikation sofort gerundet ([[Wuerfeln-und-Proben|Würfeln und Proben]]).

Beispiel: Der Held besitzt beide Stufen. Stufe 1 ist Voraussetzung für Stufe 2. Der wirksame Faktor ist 2,0 und nicht 1,5 × 2,0 = 3,0.

## Schwelle des guten Erfolgs: Spruchmagie, KI, Psi und Wunder

Jede Probe wird auf der Leiter der Erfolgsstufen ausgewertet: Patzer, Fehlschlag, Erfolg, guter Erfolg, meisterlicher Erfolg, fröhlicher Erfolg ([[Wuerfeln-und-Proben|Würfeln und Proben]]). Bei Spruchmagie, KI, Psi und Wundern lässt sich die Schwelle für den guten Erfolg durch ein Talent verändern. Jede dieser vier Probenarten hat ein Paar aus Stufe 1 und Stufe 2:

| Probenart | Talent | Stufe 1 ersetzt die Schwelle durch | Stufe 2 ersetzt sie durch |
|---|---|---|---|
| [[Spruchmagie]] | Spruchgüte | Weisheit | Weisheit + Eigenschaftsbonus |
| [[KI]] | Gute KI | Magie | Magie + Aura |
| [[Psi]] | Gute PSI | Magie | Magie + Eigenschaftsbonus |
| [[Wunder]] | Gute Wunder | Karma | Karma + Aura |

Der Eigenschaftsbonus ist der Bonus der Eigenschaft, die zur Fähigkeit oder zum Zauber gehört ([[Eigenschaften]]). Weisheit, Magie, Karma und Aura sind [[Attribute]].

### Wie das Talent wirkt

Ohne eines dieser Talente hat jede Probenart eine feste Schwelle für den guten Erfolg. Sie steht im Kapitel der Probenart. Stufe 1 ersetzt diese Schwelle durch einen einzelnen Attributswert. Stufe 2 ersetzt sie durch die Summe aus demselben Attributswert und einem zweiten Term, je nach Probenart Aura oder Eigenschaftsbonus.

Das Ergebnis ist nach oben begrenzt. Die Schwelle des guten Erfolgs überschreitet nie die Hälfte des normalen Erfolgswerts der Probe, also des Werts, bis zu dem die Probe gelingt. Die Halbierung wird nach der allgemeinen Rundungsregel gerundet ([[Wuerfeln-und-Proben|Würfeln und Proben]]).

Jedes Paar ist eine Stufenkette mit zwei Stufen. Stufe 2 setzt Stufe 1 voraus. Stufe 2 ersetzt den Wert von Stufe 1, beide werden nicht addiert.

Jedes Talent hat feste Talentpunkte-Kosten, die sich je Probenart unterscheiden. Die vier Probenarten beeinflussen einander nicht. Ein Held kann zum Beispiel Spruchgüte Stufe 2 und Gute KI Stufe 1 unabhängig voneinander besitzen.

Das Talent verändert nur die Schwelle des guten Erfolgs.

### Beispiele

- Der Held besitzt Gute KI Stufe 2. Die Schwelle des guten Erfolgs der KI ist Magie + Aura, höchstens die Hälfte des normalen Erfolgswerts.
- Der Held besitzt Gute Wunder Stufe 1 (nicht Stufe 2). Die Schwelle des guten Erfolgs der Wunder ist Karma, höchstens die Hälfte des normalen Erfolgswerts.
- Der Held besitzt Spruchgüte Stufe 1, seine Weisheit ist 6, und sein Zauberwert ist 20. Die Hälfte des Zauberwerts ist 10. Die Schwelle ist 6, denn 6 liegt unter 10.
- Hätte derselbe Held Weisheit 14, gälte nicht 14, sondern 10. Das ist die Hälfte des Zauberwerts.

## Fernkampfgeschick

Fernkampfgeschick hat drei Stufen. Es verschiebt die Schwellen des guten und des meisterlichen Erfolgs der Fernkampfprobe ([[Fernkampf]]).

Ohne das Talent liegen die Schwellen bei 1 für den guten und bei 21 für den meisterlichen Erfolg. Das Talent kann diese Schwellen nur anheben, nie unter diese Werte senken.

### Die drei Stufen

- **Stufe 1:** Die Schwelle des guten Erfolgs wird mit dem Teiler 4 berechnet.
- **Stufe 2:** Der Teiler für den guten Erfolg ist 3. Er ersetzt den Teiler 4 von Stufe 1.
- **Stufe 3:** Sie enthält Stufe 2 vollständig, der Teiler 3 für den guten Erfolg bleibt also in Kraft. Zusätzlich gilt der Teiler 20 für den meisterlichen Erfolg. Stufe 3 setzt wie jede Stufe die Stufe darunter voraus, hier also Stufe 2.

### Die Schwellen

Ausgangswert ist der Normalwert der Fernkampfprobe für das gewählte Reichweitenband (Basiswert plus Reichweitenmodifikator, ohne Erschwerungen). Die Schwellen ergeben sich genau einmal aus diesem Normalwert:

```text
gut         = 1 + Normalwert ÷ Teiler (3 oder 4)
meisterlich = 21 + Normalwert ÷ 20
```

Die Division wird gerundet, bevor 1 oder 21 addiert wird ([[Wuerfeln-und-Proben|Würfeln und Proben]]). Der Wert für „gut“ gilt nur, wenn er größer als 1 ist, sonst bleibt es bei 1. Der Wert für „meisterlich“ gilt nur, wenn er größer als 21 ist, sonst bleibt es bei 21. Ein Normalwert von 0 oder weniger lässt beide Schwellen bei 1 und 21.

Jedes Reichweitenband hat seinen eigenen Normalwert und damit seine eigenen Schwellen. Der Teiler ist für alle gleich.

### Der Deckel bei Erschwerung

Die Schwellen werden nicht neu berechnet, wenn der Schütze eine Erschwerung ansagt. Sie bleiben, wie sie aus dem Normalwert folgen, und werden nur nach oben begrenzt. Der endgültige Erfolgswert (E) ist der Normalwert nach Abzug der Erschwerungen und der Körperlichen Behinderung ([[Behinderung-und-Erschwernis|Behinderung und Erschwernis]]). Dann gilt:

```text
gut final         = kleinerer Wert aus gut und (E ÷ 2)
meisterlich final = kleinerer Wert aus meisterlich und (21 + (gut final − 1) ÷ 2)
```

Beide Divisionen werden gerundet. Der Deckel verhindert, dass die Zone des guten und des meisterlichen Erfolgs den stark gesenkten Erfolgswert überlappt oder überschreitet. Ohne Erschwerung ist E gleich dem Normalwert, und der Deckel greift nie, denn mit einem Teiler von mindestens 3 wächst die Schwelle immer langsamer als die Hälfte des Normalwerts.

### Beispiele

Normalwert 12, nur Stufe 1 (Teiler 4): gut = 1 + 12 ÷ 4 = 1 + 3 = 4.

Normalwert 12, Stufe 2 (Teiler 3, ersetzt Stufe 1): gut = 1 + 12 ÷ 3 = 1 + 4 = 5.

Normalwert 12, zusätzlich Stufe 3 (Teiler 20): meisterlich = 21 + 12 ÷ 20 = 21 + 1 = 22, denn 0,6 wird auf 1 gerundet.

Beispiel mit Deckel: Die Fernkampf-Basis ist 20, der Reichweitenmodifikator der Waffe bei 30 Metern ist +6, und der Held besitzt alle drei Stufen. Der Normalwert ist 26.

- gut = 1 + 26 ÷ 3 = 1 + 9 = 10 (8,67 wird auf 9 gerundet)
- meisterlich = 21 + 26 ÷ 20 = 21 + 2 = 23 (1,3 wird auf 2 gerundet)

Bei Erschwerung 9 ist E = 17:

- gut final = kleinerer Wert aus 10 und 17 ÷ 2 = 9 (8,5 wird auf 9 gerundet), also 9
- meisterlich final = kleinerer Wert aus 23 und 21 + (9 − 1) ÷ 2 = 25, also 23

Bei Erschwerung 19 ist E = 7:

- gut final = kleinerer Wert aus 10 und 7 ÷ 2 = 4 (3,5 wird auf 4 gerundet), also 4
- meisterlich final = kleinerer Wert aus 23 und 21 + (4 − 1) ÷ 2 = 23 (1,5 wird auf 2 gerundet), also 23
