---
title: Nahkampf (NK)
aliases: [Nahkampf, NK, Hauptfertigkeit, Nahkampf-Hauptfertigkeit, Spezialisierung, Pool-Punkte, AT-Probe, PA-Probe, AW-Probe, Angriffsprobe, Paradeprobe, Ausweichprobe, Ausweichen, Waffenklasse, WK, Nahkampf-Patzer, Ausdauerkosten Nahkampf]
status: entwurf
---

# Nahkampf (NK)

Im Nahkampf greift der Held mit einer Waffe an, wehrt mit ihr einen Angriff ab oder weicht ihm aus. Jede dieser drei Handlungen hat einen eigenen Wert und eine eigene Probe, und jede kostet [[Ausdauer]]. Dieses Kapitel beschreibt, woraus die Werte bestehen, wie der Held sie kauft, wie die Proben laufen und was sie an Ausdauer kosten. Wie ein Nahkampf Runde für Runde abläuft, steht in [[Nahkampf-im-Kampf]] und in [[Nahkampf-Gruppen-und-das-Meisterscreen-Gitter]].

Teilungen und Malnahmen in den Formeln dieses Kapitels werden sofort aufgerundet, bevor der nächste Schritt folgt ([[Wuerfeln-und-Proben]]). Die Waffenklasse rundet auf halbe Punkte (siehe unten).

## Die Werte des Helden

### Hauptfertigkeit

Der Held kauft für jede Waffenkategorie eine eigene Hauptfertigkeit mit Steigerungspunkten ([[Erfahrung-und-Steigerung]]). Die Kaufkurve lautet „Wert × 25“. Es gibt fünf Hauptfertigkeiten:

- Hiebwaffen
- Klingenwaffen
- Stangenwaffen
- Stichwaffen
- Unbewaffnet

Aus der Hauptfertigkeit und zwei [[Eigenschaften]] ergibt sich der Normalwert der Attacke (nAT) und der Parade (nPA):

```text
nAT bzw. nPA = (Eigenschaft 1 + Eigenschaft 2 + Hauptfertigkeit) / 3, höchstens 20
```

Bei der Attacke ist Eigenschaft 1 immer Mut. Eigenschaft 2 ist Athletik bei Hieb-, Klingen- und Stangenwaffen und Schnelligkeit bei Stich- und Unbewaffnet. Bei der Parade sind es für alle fünf Kategorien Athletik und Schnelligkeit.

### Spezialisierung

Unter jeder Hauptfertigkeit kann der Held Spezialisierungen kaufen, zum Beispiel Schwerter unter Klingenwaffen. Jede Spezialisierung hat einen eigenen Talentwert (TaW), den der Held mit Steigerungspunkten kauft. Jeder einzelne Talentwert-Punkt kostet:

- 15 Steigerungspunkte, wenn die Spezialisierung unter derselben Hauptfertigkeit die höchstwertige ist,
- 8 Steigerungspunkte, wenn genau eine andere Spezialisierung höherwertig ist,
- 4 Steigerungspunkte, wenn mindestens zwei andere höherwertig sind.

Maßgeblich ist der Stand unmittelbar vor dem Punkt, nicht die Reihenfolge der bisherigen Käufe. Eine andere Spezialisierung zählt nur dann als höherwertig, wenn ihr Wert echt größer ist. Bei Gleichstand gilt der höhere Preis.

Beispiel: Drei Spezialisierungen a, b und c stehen alle bei 0. Der erste Punkt auf a kostet 15, denn niemand ist höher. Der erste Punkt auf b kostet 8, denn a (1) ist höher. Der erste Punkt auf c kostet 4, denn a und b sind höher. Danach stehen alle drei bei 1, und der nächste Punkt kostet auf jeder von ihnen wieder 15.

Beispiel: Die Spezialisierungen a, b und c stehen bei 24, 14 und 13. Der Held steigert c zweimal. Der erste Punkt (13 auf 14) kostet 4, denn a (24) und b (14) sind höher als 13. Der zweite Punkt (14 auf 15) kostet 8, denn nur a (24) ist höher als 14, b (14) ist gleich. Zusammen sind das 12 Steigerungspunkte.

### Pool-Punkte

Jede Waffe, die der Held besitzt, hat eigene Pool-Punkte. Das ist ein Vorrat an Zusatzpunkten, den er auf Attacke und Parade dieser Waffe verteilt. Zwei verschiedene Langschwerter derselben Spezialisierung teilen sich keinen Vorrat.

```text
Pool-Punkte der Waffe = Überschuss Attacke + Überschuss Parade
                        + Talentwert der zugehörigen Spezialisierung
                        − bereits ausgegebene Pool-Punkte
```

Der Überschuss ist der Betrag, um den der Wert der Waffe über 20 hinausgeht. Gerechnet wird mit dem Wert ohne die Obergrenze 20: Formel der Hauptfertigkeit, plus der Bonus der Waffe auf Attacke bzw. Parade, plus der dauerhafte Bonus aus dem Kampfstil-Talent. Der Wert, mit dem der Held tatsächlich würfelt, bleibt bei 20. Was darüber liegt, fließt in die Pool-Punkte.

Das Kampfstil-Talent (Offensiver Kampfstil, Verteidiger) wirkt dauerhaft und flach. Es zählt nur die höchste Stufe, die der Held besitzt, nicht mehrere zusammen ([[Kampf-Talente]]).

Ein Talent, das die Schwelle für den guten oder meisterlichen Erfolg anhebt, gibt es im Nahkampf nicht. Diese Schwellen steigen ausschließlich mit Pool-Punkten.

### Normal, gut und meisterlich

Der Held verteilt die Pool-Punkte auf drei Werte der Attacke und drei Werte der Parade:

- nAT und nPA: der Normalwert, der Wert der Probe selbst. Höchstens 20.
- gAT und gPA: die Schwelle des guten Erfolgs. Ohne Pool-Punkte liegt sie bei 1.
- mAT und mPA: die Schwelle des meisterlichen Erfolgs. Ohne Pool-Punkte liegt sie bei 21.

Der Wert aus der Formel kann durch Pool-Punkte weiter angehoben werden, höchstens bis 20. Für g und m gelten Obergrenzen, die vom Normalwert abhängen:

```text
Obergrenze g = n / 2
Obergrenze m = 21 + (Obergrenze g − 1) / 2
```

Beispiel: nAT 20 erlaubt gAT bis 10 und mAT bis 21 + (10 − 1) / 2 = 21 + 5 = 26. Der Held hat dann nAT, gAT und mAT von 20, 10 und 26.

Diese Obergrenzen wirken beim Verteilen der Punkte, gegen den Normalwert ohne Behinderung und Erschwerung. Die drei Werte je Waffe sind die Klassen von Attacke und Parade, mit denen das Meisterscreen-Gitter arbeitet ([[Nahkampf-Gruppen-und-das-Meisterscreen-Gitter]]).

### Verteilung auf Attacke und Parade

Die verteilten Pool-Punkte der Attacke-Seite dürfen sich von denen der Parade-Seite um höchstens 1 unterscheiden. Das gilt in beide Richtungen. Steht eine Seite schon an ihrem eigenen Maximum (nAT, gAT und mAT bzw. nPA, gPA und mPA voll ausgebaut) und kann deshalb nicht mehr aufholen, darf die Differenz größer sein.

### Waffen unter zwei Hauptfertigkeiten

36 Waffen des Waffenkatalogs sind unter zwei verschiedenen Paaren aus Hauptfertigkeit und Spezialisierung aufgeführt. Das Barbarenschwert steht zum Beispiel unter Klingenwaffen / Schwerter und unter Klingenwaffen / Zweihänder. Der Held kann eine solche Waffe unter jeder der beiden trainierten Fertigkeiten führen, jeweils mit dem eigenen Attacke- und Parade-Wert.

### Zweite Hand

Führt der Held die Waffe in der Sekundärhand und hat kein passendes Talent, werden seine investierten Pool-Punkte halbiert. Die Obergrenzen für g und m werden dann aus dem halbierten Normalwert neu bestimmt. Herleitung und Beispiel stehen bei den Talenten der Sekundärhand ([[Kampf-Talente]]).

## Ausweichen

Das Ausweichen hat keine Hauptfertigkeit, keine Spezialisierung und keine Pool-Punkte. Es gibt zwei Grundwerte. Der Held wählt bei jeder Probe, welchen er benutzt:

```text
defensives Ausweichen (defAW) = (Athletik + Schnelligkeit + Glück + Ausweichen) / 5 + 6
offensives Ausweichen (offAW) = (Athletik + Schnelligkeit + Glück + Ausweichen) / 5 + 2
```

Glück ist ein [[Attribute|Attribut]], Ausweichen eine [[Sonderfertigkeiten|Sonderfertigkeit]]. Der gewählte Grundwert ist der Normalwert n der Probe.

Dazu kommen die Schwellen des guten und des meisterlichen Erfolgs. Sie sind für beide Arten gleich:

```text
gAW = (Eigenschaftsbonus Athletik + Gutes Ausweichen) / 5 + 1, höchstens n / 2
mAW = (Eigenschaftsbonus Schnelligkeit + Meisterliches Ausweichen) / 5 + 21,
      höchstens 21 + ((Obergrenze von gAW) − 1) / 2
```

Gutes Ausweichen und Meisterliches Ausweichen sind Sonderfertigkeiten. Der Held kauft sie mit Steigerungspunkten, jede höchstens bis 12. Ein Talent, das diese Grenze anhebt, gibt es nicht. Den Eigenschaftsbonus erklärt das Kapitel [[Eigenschaften]].

## Behinderung und Erschwerung

Zwei Dinge senken die Werte, und sie wirken verschieden:

- Die Körperliche Behinderung ([[Glossar#KBE|KBE]]) zieht von allen drei Werten direkt ab.
- Eine Erschwerung zieht nur vom Normalwert ab. Der Wert für den guten und der für den meisterlichen Erfolg werden nicht neu berechnet, sondern nur nach oben begrenzt, und zwar gegen den gesenkten Normalwert.

Beide sind erklärt in [[Behinderung-und-Erschwernis]]. Bei der Attacke zählt von den beiden Behinderungen nur die KBE. Die Mentale Behinderung ([[Glossar#MBE|MBE]]) wird bei Attacke-Proben nicht abgezogen. Bei Parade und Ausweichen zählt ebenfalls nur die KBE.

Bestätigte Erschwerungen im Nahkampf gibt es zwei: die freiwillige Erschwerung der Attacke und die Erschwerung durch Blindheit. Ist der Held blind, beträgt sie 18; dazu kommt der Malus aus den Komplementärsinnen ([[Aussehen-Schlaf-Sinne-und-Koerper]]). Eine Liste regulärer Erschwerungen wie im Fernkampf gibt es im Nahkampf nicht.

### Freiwillige Erschwerung der Attacke

Der Held kann seine Attacke freiwillig erschweren. Die Parade kann er nicht freiwillig erschweren. Je +3 gewählter Erschwerung bekommt er wahlweise 2 Trefferzonen-Rerolls ([[Treffer-und-Schaden]]) oder 2 Steigerungspunkte. Sie wirkt wie jede andere Erschwerung.

### Überzählige Pool-Punkte schützen den Normalwert

Pool-Punkte, die der Held nicht auf nAT, gAT oder mAT verteilt hat, heißen überzählig. Sie fangen zuerst die KBE ab, mit dem Rest jede Erschwerung. Sie schützen aber nur den Normalwert, nicht die Schwellen für gut und meisterlich.

Der Zusatz „ausgebaut“ steht für den Wert, den der Held gekauft und verteilt hat, vor Behinderung und Erschwerung. Ohne Zusatz steht der Wert, mit dem die Probe tatsächlich läuft.

```text
Rest = größerer Wert aus 0 und (überzählige Pool-Punkte − KBE)

nAT  = nAT ausgebaut
       − größerer Wert aus 0 und (KBE − überzählige Pool-Punkte)
       − größerer Wert aus 0 und (Erschwerung − Rest)

gAT  = kleinerer Wert aus
         (größerer Wert aus 1 und (gAT ausgebaut − KBE))
         und (nAT / 2)

mAT  = kleinerer Wert aus
         (größerer Wert aus 21 und (mAT ausgebaut − KBE))
         und (21 + (gAT − 1) / 2)
```

Für die Parade gelten dieselben Formeln mit nPA, gPA und mPA.

Beim Ausweichen gibt es keine Pool-Punkte, also auch keinen Schutz. Hier steht „ausgebaut“ für den Wert aus den Formeln im Abschnitt Ausweichen:

```text
n    = gewählter Grundwert − KBE − Erschwerung

gAW  = kleinerer Wert aus
         (größerer Wert aus 1 und (gAW ausgebaut − KBE))
         und (n / 2)

mAW  = kleinerer Wert aus
         (größerer Wert aus 21 und (mAW ausgebaut − KBE))
         und (21 + (gAW − 1) / 2)
```

Beispiel: nAT, gAT und mAT stehen bei 20, 10 und 26. Der Held hat 6 überzählige Pool-Punkte und KBE 3. Der Rest beträgt 3. Der Normalwert bleibt 20, gAT sinkt auf 7 und mAT auf 23.

Weitere Beispiele mit Ausgangswerten 20 / 10 / 26 und ohne Erschwerung:

| KBE | überzählige Pool-Punkte | nAT | gAT | mAT |
|---:|---:|---:|---:|---:|
| 10 | 0 | 10 | 1 | 21 |
| 10 | 5 | 15 | 1 | 21 |
| 5 | 0 | 15 | 5 | 21 |
| 5 | 5 | 20 | 5 | 21 |

Beispiel zur freiwilligen Erschwerung: nAT ausgebaut 20, 2 überzählige Pool-Punkte, gewählte Erschwerung 3 (dafür 2 Trefferzonen-Rerolls oder 2 Steigerungspunkte). Der Normalwert beträgt 20 − (3 − 2) = 19.

### Zu wenig Stärke für die Waffe

Jede Waffe hat eine Mindeststärke. Bei Waffen, die einhändig und zweihändig geführt werden können, hängt sie vom Griff ab. Hat der Held weniger Stärke, bleibt die Waffe nutzbar, auch mit Pool-Punkten. Für jeden fehlenden Stärkepunkt gilt:

- Der Normalwert der Attacke und der Parade sinkt um 3. Eine Untergrenze gibt es nicht.
- Der Schaden der Waffe sinkt um 1, aber nicht unter 0.

Der Malus auf den Normalwert wirkt wie eine Erschwerung. Überzählige Pool-Punkte schützen nicht davor. Die Werte für gut und meisterlich werden nicht gesenkt, sondern gegen den gesenkten Normalwert begrenzt.

Beispiel: nAT, gAT und mAT stehen bei 20, 10 und 26. Der Held hat Stärke 8, die Waffe Mindeststärke 11, es fehlen also 3 Punkte. Der Normalwert sinkt um 9 auf 11. gAT wird auf höchstens 11 / 2 = 5,5, aufgerundet 6 begrenzt. mAT wird auf höchstens 21 + (6 − 1) / 2 = 23,5, aufgerundet 24 begrenzt. Die Proben laufen mit 11 / 6 / 24, und der Schaden der Waffe sinkt um 3.

## Die Proben

Attacke, Parade und Ausweichen werden mit W30 − W12 gewürfelt. Das Ergebnis liegt zwischen 0 und 29. Für diese drei Proben gilt eine eigene Rechnung statt der allgemeinen Formel für Differenzproben ([[Wuerfeln-und-Proben]]).

### Erfolg und Misserfolg

Ergibt der Wurf höchstens den Normalwert nach Behinderung und Erschwerung, gelingt die Probe. Ist das Ergebnis größer, misslingt sie.

### Die Erfolgsstufen

Die Stufen der Probenergebnis-Leiter richten sich bei diesen Proben nach den eigenen Schwellen:

- Das Ergebnis ist gleich der Schwelle für gut: guter Erfolg.
- Das Ergebnis ist gleich der Schwelle für meisterlich: meisterlicher Erfolg.
- Das Ergebnis ist 29: fröhlicher Erfolg. Das geht nur mit dem Vorteil Kind der Fröhlichkeit, den jeder Spielercharakter hat ([[Gaben-und-Schwaechen]]).
- Das Ergebnis ist 0: Patzer.

### Patzer

Ein Patzer wird nicht nach Ermessen des Meisters entschieden, sondern mit der Patzertabelle des Nahkampfs. Gewürfelt wird 2W6 minus die Schwelle für gut (bei einem Attackepatzer gAT, bei einem Paradepatzer gPA, bei einem Ausweichpatzer gAW, jeweils nach Behinderung und Erschwerung). Ein negatives Ergebnis zählt als 0.

| Wurf | Wirkung |
|---|---|
| 0 (gilt auch für 1 und 2) | wie gescheitert |
| 3 bis 4 | Stolpern, 1 sec. PA-Kl.-1 |
| 5 bis 6 | Waffenarm festgehalten: PA-Kl.-1, jede sec. Stä-Vergleichsprobe gegen den Nahkampf-Gegner |
| 7 | Status Sturz (KK-2, erfolgreiche Ath-Probe: Straucheln) |
| 8 bis 9 | Status entwaffnet (entspricht dem Eintrag Band 12 der Selbstbeherrschungstabelle, PA-Kl.-1) |
| 10 und mehr | Selbst Treffer, höchster W in TP |

### Sehr niedriger Wert

Fällt der fertige Normalwert auf 1 oder darunter, schiebt sich die Leiter nach hinten. Gezählt wird nach dem Schutz durch überzählige Pool-Punkte, nach der Erschwerung und nach dem Malus für zu wenig Stärke. Das gilt für Attacke, Parade, Ausweichen und Fernkampf gleich:

- Bei einem Normalwert von 1 liegt der gute Erfolg bei Wurf 21 und der meisterliche Erfolg bei Wurf 29. Einen fröhlichen Erfolg gibt es nicht.
- Bei einem Normalwert unter 1 liegt schon der Erfolg selbst bei Wurf 21 und der gute Erfolg bei Wurf 29. Meisterlicher und fröhlicher Erfolg entfallen.

Beispiel: nAT ausgebaut 20, KBE 19 und 6 überzählige Pool-Punkte ergeben 20 − (19 − 6) = 7. Die Leiter schiebt sich nicht. Ohne die Pool-Punkte ergäbe 20 − 19 = 1 eine verschobene Leiter.

### Verteidigung und Treffer

Jede Seite würfelt ihre eigene Probe. Der Verteidiger wählt je Probe zwischen Parade, defensivem Ausweichen und offensivem Ausweichen. Wie die Ergebnisse beider Seiten zusammen einen Treffer ergeben, regelt das Meisterscreen-Gitter ([[Nahkampf-Gruppen-und-das-Meisterscreen-Gitter]]).

## Waffenklasse (WK)

Jede Nahkampfwaffe und jedes Schild hat eine Waffenklasse. Sie macht das relative Gewicht zweier Gegenstände vergleichbar. Gebraucht wird sie bei der Klingenbruch-Probe (als Unterschied zweier Waffenklassen, [[Nahkampf-im-Kampf]]), beim Kampf mit zwei Waffen ([[Kampf-Talente]]) und für die Ausdauerkosten unten.

### Die Waffenklasse eines Gegenstands

Die Waffenklasse ist die Basis-WK der Katalogzeile plus der Modifikator des Materials ([[Nahkampfwaffen]]). Bei Schilden ist es dieselbe Rechnung mit dem Material-Modifikator der Schilde. Sie kann negativ sein. Die Basiszeile Unbewaffnet hat die Basis-WK −2, ein kleines Messer −1. Es gibt kein Minimum und kein Maximum.

Jede Rechnung mit der Waffenklasse rundet nach jedem Schritt auf das nächste halbe, bei negativen Werten vom Betrag weg.

### Die effektive Waffenklasse

In drei Lagen zählt statt der Katalog-WK eine effektive WK. Die Lagen schließen sich gegenseitig aus. Ein Schild ist nie Teil der Zwei-Waffen-Rechnung, und eine Zwei-Waffen-Kombination nie Teil der Regel für Waffe und Schild.

**Zweihändig geführte Waffe.** Eine Waffe, die normalerweise einhändig geführt wird, wird zweihändig geführt:

```text
effektive WK = WK × 1,5
```

Das geht nur, wenn die Waffe laut Katalog sowohl einen einhändigen als auch einen zweihändigen Griff hat. Ein Boden für diese Rechnung existiert nicht: Bei der Basis-WK −1 ist die effektive WK −1,5.

**Kampf mit zwei Waffen.** Führt der Held zwei Nahkampfwaffen gleichzeitig, ohne Schild, gelten ein Wert für den Angriff und einer für die Parade:

```text
höhere WK = größere der beiden WK
AT-WK     = größerer Wert aus (höhere WK) und (höhere WK × 1,5)
PA-WK     = größerer Wert aus (höhere WK) und (WK der ersten + WK der zweiten)
```

Dadurch wird eine negative WK durch Malnehmen oder Addieren nie schlechter als die bessere Einzelwaffe. Negative Waffenklassen sind ausdrücklich erlaubt, eine Mindest-WK von 0 gibt es nicht.

Die Rechnung gilt nur, wenn alle fünf Bedingungen erfüllt sind:

- Der Held hat die passende Talentstufe.
- Die aktuelle WK beider Waffen liegt höchstens beim Kappungswert des Talents.
- Beide Gegenstände dürfen einhändig im Nahkampf geführt werden.
- Keine der beiden Waffen hat die Spezialisierung Schild.
- Es ist keine Stangenwaffe beteiligt.

Geprüft wird die aktuelle WK, also Basis-WK und Material zusammen.

**Waffe und Schild.** Führt der Held eine einhändige Nahkampfwaffe zusammen mit einem Schild, gelten zwei getrennte Werte, in welcher Hand auch immer was gehalten wird:

```text
AT-WK = aktuelle WK der Nahkampfwaffe
PA-WK = aktuelle WK des Schildes
```

Es wird weder die höhere WK für beide Handlungen benutzt noch die Summe gebildet. Diese Rechnung gilt immer, wenn tatsächlich Waffe und Schild geführt werden, auch ohne das Talent für den Kampf mit zwei Waffen. Jede Schild-Parade benutzt die WK des Schildes anstelle der WK der Waffe, auch außerhalb dieser Ausrüstung, etwa bei einer Schild-Parade im Zusammenhang mit der Klingenbruch-Probe.

Es zählt die WK im Augenblick der Aktion (Parade, Klingenbruch-Probe, Ausdauerkosten), mit der Ausrüstung, dem Griff und den Talenten, die der Held dann hat.

### Beispiele zur Waffenklasse

Eine Waffe mit Katalog-WK 6, zweihändig geführt: effektive WK = 6 × 1,5 = 9.

Weitere zweihändige Beispiele zur Rundung: WK 7 ergibt 10,5; WK 5,5 ergibt 8,25 und wird zu 8,5; WK 6,5 ergibt 9,75 und wird zu 10.

Zwei kleine Messer aus Eisen, WK −1 und −1, im Kampf mit zwei Waffen: höhere WK −1. AT-WK = größerer Wert aus −1 und −1,5 = −1. PA-WK = größerer Wert aus −1 und −2 = −1.

Kleines Messer (WK −1) und großes Messer (WK 0): höhere WK 0, AT-WK 0, PA-WK 0.

Zwei Waffen mit WK 2 und 3: höhere WK 3. AT-WK = größerer Wert aus 3 und 4,5 = 4,5. PA-WK = größerer Wert aus 3 und 5 = 5.

Zwei Waffen mit WK 5,5 und 4: höhere WK 5,5. AT-WK = größerer Wert aus 5,5 und 8,25 (gerundet 8,5) = 8,5. PA-WK = größerer Wert aus 5,5 und 9,5 = 9,5.

Ein Dolch aus Eisen (WK 2) und ein Rundschild aus Holz (Basis-WK 8, Material-Modifikator −1,5, also Schild-WK 6,5). Der Kampf mit zwei Waffen ist hier nicht anwendbar, weil ein Schild beteiligt ist: AT-WK = 2 (Dolch), PA-WK = 6,5 (Schild). Es gibt keine Kombination.

## Ausdauerkosten im Nahkampf

Jede Nahkampfhandlung kostet Ausdauer ([[Ausdauer]]). Die Kosten hängen von der Waffenklasse ab. Der Betrag wird von der aktuellen Ausdauer abgezogen.

```text
Attacke und offensives Ausweichen:  5 + WK, aufgerundet, mindestens 3
Parade und defensives Ausweichen:   (5 + WK) / 2, aufgerundet, mindestens 2
```

Die Untergrenzen gelten, egal wie negativ die WK wird. Eine Obergrenze gibt es nicht.

### Welche WK zählt

Gerechnet wird immer mit der Katalog-WK (Basis plus Material) der Waffe oder des Schildes, die der Held bei dieser Handlung tatsächlich führt. Die drei effektiven Waffenklassen von oben fließen hier nie ein:

- Zweihändig geführt zählt die normale Katalog-WK, nicht WK × 1,5.
- Im Kampf mit zwei Waffen zählt für jede Handlung die WK der Waffe, die gerade zuschlägt oder pariert, nicht die kombinierten Werte.
- Eine Schild-Parade folgt der Paradeformel mit der WK des Schildes. Sie wird nicht anders behandelt als eine Parade mit einer Waffe.
- Offensives und defensives Ausweichen führen keine Waffe. Hier gilt immer die Waffenklasse von Unbewaffnet (−2), gleich welche Waffe der Held in der Hand hält.

### Extra-Aktionen und Aktionsketten

Eine Extra-Aktion ([[Glossar#EA|EA]]), die das Meisterscreen-Gitter gewährt ([[Nahkampf-Gruppen-und-das-Meisterscreen-Gitter]]), kostet nach derselben Formel wie ihre Art: eine Attacke wie eine Attacke, eine Parade oder ein Ausweichen wie eine Parade bzw. ein Ausweichen, mit der WK der dabei geführten Waffe. Der Held muss eine gewährte Extra-Aktion nicht ausführen. Verzichtet er, kostet sie nichts.

Kosten mehrerer ausgeführter Handlungen werden immer addiert, auch wenn eine Handlung die Folge einer anderen ist. Löst das offensive Ausweichen eine bewaffnete Extra-Aktion aus, die tatsächlich ausgeführt wird, fallen die Kosten für beide an. Misslingt das defensive Ausweichen und der Held pariert stattdessen, fallen die Kosten für beides an. Nur eine abgelehnte Extra-Aktion bleibt kostenlos.

### Ausnahme Umwerfen

Die Kampfaktion Umwerfen ([[Nahkampf-im-Kampf]]) kostet fest 5 Ausdauer statt der Attacken-Formel. Die Fähigkeit Mit Schild umwerfen kostet nach der Paradeformel mit der WK des Schildes.

### Beispiele zu den Ausdauerkosten

Langschwert, WK 6, einhändig:

- Attacke = 5 + 6 = 11.
- Parade = (5 + 6) / 2 = 5,5, gerundet 6.

Unbewaffnet, WK −2:

- Attacke = 5 − 2 = 3.
- Parade = (5 − 2) / 2 = 1,5, gerundet 2.

Kleines Messer, WK −1:

- Attacke = 5 − 1 = 4.
- Parade = (5 − 1) / 2 = 2.

Schild-Parade mit Schild-WK 8 (Waffe und Schild): Parade = (5 + 8) / 2 = 6,5, gerundet 7. Es sind nicht die vollen 8 Punkte.

Ein Schwert mit WK 6 wird zweihändig geführt (effektive WK 9): Attacke = 5 + 6 = 11. Gerechnet wird mit 6, nicht mit 9.

Ein Langschwert mit WK 5,5:

- Attacke = 5 + 5,5 = 10,5, gerundet 11.
- Parade = (5 + 5,5) / 2 = 5,25, gerundet 6.

Eine Waffe mit WK −8 gibt es im Katalog nicht, die Rechnung zeigt aber die Untergrenzen:

- Attacke = 5 − 8 = −3. Es gilt die Untergrenze 3.
- Parade = (5 − 8) / 2 = −1,5, gerundet −2. Es gilt die Untergrenze 2.

Der Held führt ein Langschwert und weicht aus. Das Ausweichen führt keine Waffe, es gilt die WK von Unbewaffnet (−2):

- offensives Ausweichen = 5 − 2 = 3.
- defensives Ausweichen = (5 − 2) / 2 = 1,5, gerundet 2.
