---
title: Ausdauer
aliases: [Ausdauer, Ausdauer-Maximum, Erschöpfung, Nullpunkt-Behinderung, Ausdauer-Regeneration, Ausdauerregeneration]
status: entwurf
---

# Ausdauer

Für körperliche Anstrengung über das Normalmaß hinaus gibt der Held Ausdauer aus. Sinkt sie auf 0, bekommt er Behinderungen auf seine Proben. Sobald die Anstrengung vollständig endet, erholt er sich wieder.

Ausdauer kosten Nahkampfhandlungen ([[Nahkampf]]), das Halten eines gespannten Bogens ([[Fernkampf]]), Zaubern ([[Spruchmagie]]), das Abfangen des Rückstoßes einer [[Feuerwaffen|Feuerwaffe]], Gehen, Laufen, Sprinten, Marschieren und Springen ([[Bewegung]]) sowie das Tragen von Lasten ([[Tragen]]). Was eine Handlung kostet, steht im Kapitel der Handlung, zusammengefasst in der [[Ausdauerkosten-Uebersicht|Ausdauerkosten-Übersicht]]. Dieses Kapitel sagt, wie viel Ausdauer der Held hat, was ihr Fehlen bewirkt und wie sie zurückkehrt.

## Das Maximum

Das Maximum hängt von den [[Eigenschaften]] Athletik, Konstitution und Stärke, vom [[Attribute|Attribut]] Vitalität, von der [[Stufe-Kreis-Macht-und-Rerolls|Stufe]] und von der [[Sonderfertigkeiten|Sonderfertigkeit]] Ausdauer ab:

```text
Maximum = (3 × Athletik + 3 × Konstitution + Stärke) / 2
          + 3 × Vitalität + Stufe + 2 × Sonderfertigkeit Ausdauer
```

### Der aktuelle Wert

Bei der Charaktererschaffung und zu Beginn jedes neuen Abenteuers (siehe [[Zeit-und-Spielablauf|Zeit und Spielablauf]]) steht die aktuelle Ausdauer auf dem Maximum. Danach sinkt sie durch Verbrauch und steigt durch Regeneration.

Sie kann unter 0 fallen.

## Erschöpfung

Erreicht die aktuelle Ausdauer den Wert 0, bekommt der Held eine Körperliche Behinderung ([[Glossar#KBE|KBE]]) von +3 und zugleich eine Mentale Behinderung ([[Glossar#MBE|MBE]]) von +3. Beide Behinderungen sind in [[Behinderung-und-Erschwerung|Behinderung und Erschwerung]] erklärt.

Für jeden weiteren vollen Schritt von −5 Ausdauer steigen KBE und MBE um weitere +3. Gezählt werden volle Schritte, nicht einzelne Punkte.

- 0: KBE +3 und MBE +3
- −5: KBE +6 und MBE +6
- −10: KBE +9 und MBE +9
- und so weiter

Diese Behinderung kommt zu jeder anderen Behinderung hinzu.

## Regeneration

### Wann sie beginnt

Die Regeneration beginnt erst, wenn die Belastung vollständig geendet hat. Während einer laufenden Anstrengung erholt sich der Held nicht teilweise. Das gilt für jede Quelle des Verbrauchs gleich: Nahkampf, Fernkampf, Magie, Tragen und Bewegung.

Ein Zeitsprung, der eine laufende Belastung nicht beendet, bringt keine Regeneration, egal wie lang er ist. Die Regeln für lange Zeitsprünge (siehe unten) setzen eine tatsächliche Ruhe- oder Schlafsituation voraus, nicht bloß eine Zeitspanne.

### Bis 80 %

Ohne Handlung und ohne körperliche Belastung regeneriert der Held so:

- Bis 60 % des Maximums regeneriert er pro Sekunde.
- Von 60 % bis 80 % regeneriert er pro Minute.

Beide Raten haben dieselbe Punktzahl. Sie hängt von der Haltung ab und beruht auf dem Eigenschaftsbonus der Athletik (siehe [[Eigenschaften]]):

```text
stehend        = Vitalität + Eigenschaftsbonus Athletik, mindestens 3
kniend/sitzend = stehend × 2
liegend        = stehend × 4
```

Ein sehr schwacher Held regeneriert stehend also mindestens 3 Ausdauer pro Sekunde, sitzend oder kniend mindestens 6 und liegend mindestens 12.

Sekunde und Minute sind Zeiteinheiten der Spielwelt. Sie gelten unabhängig von der Dauer einer Kampfrunde (siehe [[Zeit-und-Spielablauf|Zeit und Spielablauf]]).

### Oberhalb von 80 %

Den Rest über 80 % regeneriert nur Schlaf: 3 % des Maximums pro Stunde, bis 100 % erreicht sind.

Ein Held ohne jede Handlung und Belastung, aber ohne Schlaf, bleibt bei 80 % des Maximums stehen, auch nach beliebig langen Zeitsprüngen.

### Im Kampf

Im Kampf regeneriert der Held in jeder Kampfrunde, die als Ruhe zählt, die Rate seiner Haltung (siehe oben). Eine Kampfrunde dauert zurzeit eine Sekunde. Eine Ruhe-Kampfrunde bringt also zurzeit den vollen Wert der Haltung. Allgemein bringt sie die Sekundenrate für die Dauer einer Kampfrunde.

Eine Kampfrunde zählt nur dann als Ruhe, wenn der Held in ihr

- keinen Schaden erlitten hat und
- keine Bewegungsaktion durchgeführt hat, deren Grundkosten an Aktionskosten ([[Glossar#AK|AK]]) größer als 0 sind (siehe [[Kampfrunde-Aktionen-Initiative-und-Sicht|Kampfrunde, Aktionen, Initiative und Sicht]]).

Es zählen die Grundkosten. Senkt eine gelungene Kampf-Laufen-Probe die tatsächlich gezahlten AK der Bewegung auf 0, zählt die Kampfrunde trotzdem nicht als Ruhe. Das gilt für alle drei Haltungen gleich.

### Zeitsprünge außerhalb des Kampfs

Lässt der Meister außerhalb des Kampfes Zeit vergehen, bestimmt er die Regeneration aus der Zeitspanne und aus der Situation, die er dem Helden zuweist: Haltung, Schlaf, Belastung.

Ein Zeitsprung wird in Abschnitten entlang der 60-%-Grenze und der 80-%-Grenze verrechnet. Jede Rate gilt nur bis zur eigenen Grenze, nie über eine größere Zeitspanne hinweg. So geht der Meister vor:

1. Er bestimmt, wie viele Punkte bis zur 60-%-Grenze fehlen, und danach, wie viele von dort bis zur 80-%-Grenze.
2. Er bestimmt für jeden Abschnitt, wie viel Zeit er mit seiner Rate braucht, und zieht diese Zeit von der verfügbaren Zeit ab. Er arbeitet die Abschnitte in dieser Reihenfolge ab, bis die Zeit aufgebraucht ist oder 80 % erreicht sind.
3. Erst danach greift die Regeneration oberhalb von 80 %, und nur, wenn für die verbleibende Zeit eine Schlafphase vorliegt.

#### Zeitsprünge über 8 Stunden

- **Mit Schlaf:** Dauert ein Zeitsprung länger als 8 Stunden und hat der Held in dieser Zeit geschlafen, springt die aktuelle Ausdauer direkt auf das Maximum. Die Abschnitte werden nicht einzeln gerechnet. Über 8 Stunden erreicht jede Ausgangslage 100 %.
- **Ohne Schlaf:** Dauert ein Zeitsprung länger als 8 Stunden und hat der Held nicht geschlafen, muss der Meister das ausdrücklich markieren oder bestätigen, bevor er die Regeneration rechnet. Danach rechnet er normal. Die Ausdauer bleibt bei 80 % gedeckelt, weil kein Schlaf vorliegt.

## Nicht-lebende Wesen

Nicht-lebende Wesen, zum Beispiel Untote, Golems und Elementare, haben unendliche Ausdauer. Ihr Maximum ist unendlich, und ihre aktuelle Ausdauer bleibt immer auf diesem Maximum. Ihre Handlungen kosten weiterhin Ausdauer wie bei jedem anderen Wesen. Der Verbrauch erreicht das Maximum aber nie, und deshalb tritt die Erschöpfung nie ein.

Nur das Leben entscheidet darüber, nicht ob das Wesen Held, NSC oder Kreatur ist. Freilebende Kreaturen haben wie jeder lebende Held eine endliche Ausdauer, solange sie nicht zu den nicht-lebenden Wesen zählen.

Wird ein lebender Held nicht-lebend, zum Beispiel durch die Verwandlung zum Untoten, ist sein Maximum in diesem Moment unendlich. Der frühere Wert der aktuellen Ausdauer ist ab dann ohne Bedeutung.

## Beispiele

### Maximum und Raten

Ein Held hat Athletik 10, Konstitution 12, Stärke 14, Vitalität 6, Stufe 5 und Sonderfertigkeit Ausdauer 3. Sein Eigenschaftsbonus Athletik ist 10 / 2 − 5 = 0.

```text
Maximum  = (3×10 + 3×12 + 14) / 2 + 3×6 + 5 + 2×3
         = 80 / 2 + 18 + 5 + 6
         = 40 + 29
         = 69

stehend  = 6 + 0 = 6
sitzend  = 6 × 2 = 12
liegend  = 6 × 4 = 24
```

### Erschöpfung

- Der Held hat aktuelle Ausdauer 0: KBE +3, MBE +3.
- Er fällt auf −7 und hat damit einen Schritt von −5 überschritten: KBE +6, MBE +6.

### Drei Kampfrunden

Derselbe Held steht. Seine stehende Rate ist 6, seine aktuelle Ausdauer 0 von Maximum 69.

- Kampfrunde 1: Er erleidet keinen Schaden und handelt nicht. Die Kampfrunde zählt als Ruhe, die Ausdauer steigt von 0 auf 6.
- Kampfrunde 2: Er geht (Grundkosten 1 AK). Die Kampf-Laufen-Probe gelingt und senkt die gezahlten AK auf 0. Die Kampfrunde zählt nicht als Ruhe, weil die Grundkosten größer als 0 AK waren. Die Ausdauer bleibt bei 6.
- Kampfrunde 3: Ein Treffer verletzt den Helden. Die Kampfrunde zählt nicht als Ruhe, die Ausdauer bleibt bei 6.

### 30 Minuten liegend

Der Held liegt 30 Minuten lang. Seine aktuelle Ausdauer ist 0 von Maximum 69. Die 60-%-Grenze liegt bei 42 (60 % von 69 sind 41,4, gerundet 42), die 80-%-Grenze bei 56 (55,2, gerundet 56), die liegende Rate bei 24.

- Von 0 auf 42 in der Sekundenrate: 24 pro Sekunde, praktisch sofort.
- Von 42 auf 56 in der Minutenrate: 14 Punkte bei 24 pro Minute, das dauert etwa 0,6 Minuten.
- Danach regeneriert er ohne Schlaf nicht weiter. Die restlichen etwa 29 Minuten bringen nichts über 56.

### 9 Stunden mit Schlaf

Der Held hat aktuelle Ausdauer 0 von Maximum 69 und schläft in den 9 Stunden. Seine Ausdauer springt direkt auf 69 (100 %). Die Abschnitte werden nicht gerechnet.

### 10 Stunden ohne Schlaf

Der Held wacht oder reist 10 Stunden ohne Rast. Der Meister bestätigt das ausdrücklich, bevor er die Regeneration rechnet. Danach rechnet er normal. Das Ergebnis bleibt bei 80 % gedeckelt, weil der Held nicht geschlafen hat.

### Ein Untoter im Nahkampf

Ein Untoter führt eine Nahkampfattacke aus, die regulär Ausdauer in Höhe der Waffenklasse ([[Glossar#WK|WK]]) kostet. Sein Maximum ist unendlich, seine aktuelle Ausdauer bleibt trotz Abzug unendlich. Sie wird nie 0 oder negativ, also tritt keine Erschöpfung ein.

### Ein schwacher Held

Der Held hat Vitalität 2 und Athletik 4. Sein Eigenschaftsbonus Athletik ist 4 / 2 − 5 = −3.

- Vitalität plus Eigenschaftsbonus ergeben 2 + (−3) = −1. Das liegt unter der Untergrenze von 3. Stehend regeneriert er daher 3 pro Sekunde beziehungsweise Kampfrunde.
- Sitzend sind es 3 × 2 = 6, liegend 3 × 4 = 12.
