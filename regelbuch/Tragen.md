---
title: Tragen
aliases: [Tragen, Traglast, Belastung, Belastungsstufe, Belastungszustand, Keine Belastung, Leicht Belastet, Belastet, Schwer Belastet, Maximal Last, Überlastet, Gefahr Last, Ausdauerkosten Tragen]
status: entwurf
---

# Tragen

Der Held trägt Lasten, und je mehr er trägt, desto mehr Ausdauer kostet es ihn. Sieben Belastungsstufen reichen von „Keine Belastung“ bis „Gefahr Last“. Jede hat ein Gewicht in Kilogramm, bis zu dem sie gilt, und eigene Ausdauerkosten ([[Ausdauer]]). Das Gewicht hängt von der Stärke des Helden und von seiner Sonderfertigkeit Tragen ab ([[Sonderfertigkeiten]]).

## Die sieben Belastungsstufen

Der Meister legt fest, in welcher Belastungsstufe sich der Held befindet. Sie ergibt sich nicht von selbst aus dem Gewicht, das er bei sich hat. Die Gewichte der Tabelle sind der Anhaltspunkt für diese Entscheidung.

Das Gewicht einer Stufe ist die Summe aus zwei Teilen: Stärke mal ein Faktor und der Wert der Sonderfertigkeit Tragen mal ein zweiter Faktor. Die Stärke ist die volle [[Eigenschaften|Eigenschaft]], nicht der Eigenschaftsbonus.

| Belastungsstufe | Gewicht in kg | Ausdauerkosten |
|---|---|---|
| Keine Belastung | Stärke × 1 + Tragen × 0,5 | kein Verlust |
| Leicht Belastet | Stärke × 1,5 + Tragen × 1 | −3 pro Stunde |
| Belastet | Stärke × 2,5 + Tragen × 2 | −10 pro Stunde |
| Schwer Belastet | Stärke × 4 + Tragen × 3,5 | −1 pro Minute |
| Maximal Last | Stärke × 7,5 + Tragen × 5,5 | −1 pro Sekunde |
| Überlastet | Stärke × 11 + Tragen × 8 | −3 pro Sekunde |
| Gefahr Last (Extremsituation) | Stärke × 15 + Tragen × 11 | −6 pro Sekunde |

Stunde, Minute und Sekunde sind Zeiteinheiten der Spielwelt. Sie gelten unabhängig von der Dauer einer Kampfrunde ([[Zeit-und-Spielablauf|Zeit und Spielablauf]]).

### Rundung

Gerechnet wird in ganzen Kilogramm. Jedes Produkt, also Stärke mal Faktor und Tragen mal Faktor, wird einzeln auf ganze Kilogramm aufgerundet. Danach werden die beiden Teile addiert ([[Wuerfeln-und-Proben|Würfeln und Proben]]).

## Fehlende Gliedmaßen

Fehlende Gliedmaßen senken das Gewicht jeder Stufe. Jede fehlende Gliedmaße zählt gleich, ob Arm oder Bein. Die Mindestzahl von zwei funktionsfähigen Gliedmaßen gilt hier nicht. Welche Merkmale der Held hat, steht in [[Aussehen-Schlaf-Sinne-und-Koerper|Aussehen, Schlaf, Sinne und Körper]].

| Fehlende Gliedmaßen | Faktor auf das Gewicht |
|---|---|
| 0 | mal 1,00 |
| 1 | mal 0,75 |
| 2 | mal 0,50 |
| 3 | mal 0,25 |
| 4 | ganz unmöglich |

Der Faktor wirkt auf die Summe der beiden aufgerundeten Teile. Das Produkt wird auf ganze Kilogramm aufgerundet. Bei vier fehlenden Gliedmaßen trägt der Held in keiner Stufe etwas. Die Ausdauerkosten bleiben unverändert.

## Boni auf das Gewicht

**KI-Fähigkeit Kraftakt.** Jeder Punkt, den der Held in Kraftakt investiert hat ([[KI]]), erhöht das Gewicht um 8 kg. Der Bonus gilt für alle sieben Stufen zugleich und wird nach der Rundung addiert.

**Zauber „Körperliche Eigenschaft erhöhen“ und „Körperliche Eigenschaft senken“.** Wird bei diesen Zaubern die Stärke gewählt ([[Spruchmagie]]), erhöht oder senkt der Zauber die Stärke um das Doppelte des Attributs Magie. Beim Senken sinkt die Stärke nie unter 1. Alle sieben Gewichte werden mit der so veränderten Stärke neu berechnet.

## Reihenfolge

1. Die Stärke ermitteln, bei einem Zauber auf die Stärke mit ihrer veränderten Zahl.
2. Jeden der zwei Teile der Stufenformel mit dieser Stärke und dem Wert der Sonderfertigkeit Tragen berechnen und einzeln aufrunden, dann addieren.
3. Bei fehlenden Gliedmaßen den Faktor auf die Summe anwenden und das Produkt aufrunden.
4. Den Bonus von Kraftakt addieren.

## Beispiele

### Ein Held mit Stärke 12 und Tragen 8

Der Held ist unbehindert und hat weder Kraftakt noch einen Zauber auf sich. Die Gewichte seiner Stufen sind:

```text
Keine Belastung:  12 × 1   + 8 × 0,5 =  12 +  4 =  16 kg
Leicht Belastet:  12 × 1,5 + 8 × 1   =  18 +  8 =  26 kg
Belastet:         12 × 2,5 + 8 × 2   =  30 + 16 =  46 kg
Schwer Belastet:  12 × 4   + 8 × 3,5 =  48 + 28 =  76 kg
Maximal Last:     12 × 7,5 + 8 × 5,5 =  90 + 44 = 134 kg
Überlastet:       12 × 11  + 8 × 8   = 132 + 64 = 196 kg
Gefahr Last:      12 × 15  + 8 × 11  = 180 + 88 = 268 kg
```

### Aufrunden

Ein Held hat Stärke 11 und Tragen 8. In der Stufe „Leicht Belastet“ ist 11 × 1,5 = 16,5, aufgerundet 17. Dazu kommt 8 × 1 = 8. Das Gewicht ist 17 + 8 = 25 kg.

Ein Held hat Stärke 13 und Tragen 3. In der Stufe „Maximal Last“ ist 13 × 7,5 = 97,5, aufgerundet 98, und 3 × 5,5 = 16,5, aufgerundet 17. Das Gewicht ist 98 + 17 = 115 kg.

### Eine Gliedmaße fehlt

Der Held hat Stärke 12 und Tragen 8 und ihm fehlt eine Gliedmaße. In der Stufe „Belastet“ sind die Teile 30 und 16, die Summe ist 46. Der Faktor 0,75 ergibt 34,5, aufgerundet 35 kg.

### Kraftakt

Derselbe Held (Stärke 12, Tragen 8) hat 3 Punkte in Kraftakt. Das sind 3 × 8 = 24 kg mehr in jeder Stufe: „Keine Belastung“ 16 + 24 = 40 kg, „Gefahr Last“ 268 + 24 = 292 kg.

### Zauber auf die Stärke

Ein Zauber erhöht die Stärke des Helden (Stärke 12, Tragen 8). Das Attribut Magie ist 6, die Stärke steigt um 12 auf 24. In der Stufe „Belastet“ ergibt das 24 × 2,5 = 60 plus 8 × 2 = 16, also 76 kg statt 46 kg.

Ein anderer Zauber senkt die Stärke desselben Helden. Das Attribut Magie ist 3, die Stärke sinkt um 6 auf 6. In der Stufe „Belastet“ ergibt das 6 × 2,5 = 15 plus 16, also 31 kg statt 46 kg.
