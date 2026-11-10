---
title: Stufe, Kreis, Macht und Rerolls
aliases: [Stufe, Kreis, Stufe und Kreis, Macht, Rerolls, Reroll, Neuwurf, Stufe/Kreis]
status: entwurf
---

# Stufe, Kreis, Macht und Rerolls

Aus den gesammelten [[Erfahrung-und-Steigerung|Erfahrungspunkten]] ergeben sich zwei Kennzahlen des Helden: seine Stufe und sein Kreis. Der Kreis bestimmt, wie viele Rerolls der Held pro Session hat. Die Macht des Helden hängt ebenfalls vom Kreis ab.

## Stufe und Kreis

Stufe und Kreis hängen nur an den gesamten Erfahrungspunkten (EP) des Helden. Steigerungspunkte, Talentpunkte oder andere Quellen spielen keine Rolle. Beide Werte werden immer gemeinsam bestimmt. Sie ändern sich, sobald die gesamten EP eine neue Schwelle erreichen.

Der Held hat die höchste Stufe, deren EP-ab-Wert die gesamten EP nicht übersteigt. Genau auf der Schwelle gilt die neue Stufe: Bei 10200 EP hat der Held Stufe 49 und Kreis 7, nicht Stufe 48.

Der Kreis folgt aus der Stufe:

```text
Kreis = Wurzel der Stufe, abgerundet
```

Die Wurzel wird hier nicht kaufmännisch gerundet, sondern immer abgerundet. Stufe 8 hat Kreis 2, Stufe 9 hat Kreis 3.

Mit 0 EP hat der Held Stufe 0 und Kreis 0. Niedriger geht es nicht. Nach oben gibt es keine Grenze.

### Wie viele EP eine Stufe kostet

Die ersten Stufen folgen einem eigenen, unregelmäßigen Tempo. Die Schwellen steigen in Schritten von 20, 40, 60 und 80 EP:

```text
Stufe 1 ab 20 EP
Stufe 2 ab 60 EP
Stufe 3 ab 120 EP
Stufe 4 ab 200 EP
```

Stufe 0 bis 3 gehören zu Kreis 0 und Kreis 1, Stufe 4 beginnt Kreis 2.

Danach kostet jede Stufe 50 EP mal die Zahl des Kreises, in dem sie liegt. Das ist die Rate des Kreises. Kreis 3 hat die Rate 150, Kreis 4 die Rate 200 und so weiter. Eine Stufe innerhalb eines Kreises c (zwischen c² und (c+1)²) liegt um diese Rate über der vorigen:

```text
EP ab (Stufe) = EP ab (Stufe − 1) + 50 × c
```

Die erste Stufe eines neuen Kreises c (ab Kreis 3) kostet noch die Rate des vorigen Kreises. Erst die Stufen danach kosten die Rate des neuen Kreises:

```text
EP ab (c²) = EP ab (c² − 1) + 50 × (c − 1)
```

Dieses Muster gilt für jeden Kreis ohne Obergrenze. Die Kreis-Grenzen liegen bei Stufe 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196 und so weiter, jeweils beim Quadrat des Kreises.

Wo ein Kreis beginnt:

| Kreis | erste Stufe | EP ab |
|---:|---:|---:|
| 0 | 0 | 0 |
| 1 | 1 | 20 |
| 2 | 4 | 200 |
| 3 | 9 | 700 |
| 4 | 16 | 1750 |
| 5 | 25 | 3550 |
| 6 | 36 | 6300 |
| 7 | 49 | 10200 |
| 8 | 64 | 15450 |
| 9 | 81 | 22250 |
| 10 | 100 | 30800 |
| 11 | 121 | 41300 |
| 12 | 144 | 53950 |
| 13 | 169 | 68950 |

Die Stufentabelle führt jede Stufe bis Stufe 195 (Kreis 13) auf. Jede höhere Stufe lässt sich mit derselben Regel berechnen.

### Gilt für jeden

Stufe und Kreis werden für jede Spielfigur gleich bestimmt, auch für Kreaturen und Untote. Die Berechnung kennt keine Boni, Mali oder Ausnahmen.

### Beispiele

```text
0 EP     → Stufe 0,   Kreis 0
1600 EP  → Stufe 15,  Kreis 3
10200 EP → Stufe 49,  Kreis 7
85850 EP → Stufe 195, Kreis 13   (letzte Zeile der Tabelle)
86500 EP → Stufe 196, Kreis 14
```

Das letzte Beispiel folgt aus der Regel: Stufe 196 beginnt Kreis 14 und kostet noch die Rate von Kreis 13, also 85850 + 50 × 13 = 86500 EP.

## Macht

Die Macht des Helden ist die Summe aus diesen Werten:

```text
Macht = Aura + Magie + Weisheit + Karma + Kreis + Eigenschaftsbonus Willenskraft
```

Aura, Magie, Weisheit und Karma sind [[Attribute|Attribute]]. Den Eigenschaftsbonus der Willenskraft erklärt das Kapitel [[Eigenschaften|Eigenschaften]].

## Rerolls

Ein Reroll ist ein Neuwurf. Der Spieler kann damit einen Wurf, der ihm nicht passt, verwerfen und noch einmal werfen. Rerolls sind eine begrenzte Ressource des Helden, die jede Session neu zur Verfügung steht.

### Wie viele Rerolls der Held hat

Das Maximum an Rerolls ist gleich dem Kreis des Helden. Es gibt keinen anderen Weg, es zu erhöhen: Kein Talent, kein Zauber, kein Wunder, kein Artefakt und kein Trank steigert die Zahl der Rerolls. Ein Held mit Kreis 0 hat keine Rerolls.

Die Rerolls sind ein Vorrat zwischen 0 und dem Maximum. Jeder Neuwurf verbraucht einen Reroll. Ist der Vorrat leer, ist kein Reroll möglich, außer über die Gruppen-Ausnahme unten.

Zu Beginn jeder Session füllt sich der Vorrat wieder bis zum Maximum. Dafür löst der Meister aus, dass eine neue Session beginnt. Sonst ändert sich der Vorrat nur durch Ausgabe. Steigt der Held im Kreis auf, steigt auch das Maximum. Der aktuelle Vorrat füllt sich dadurch aber nicht auf, das geschieht erst zur nächsten Session.

### Was ein Reroll bewirkt

Ein Reroll verwirft einen Wurf vollständig. Gehören zu dem Wurf mehrere Würfel, etwa ein W30 und ein W12, werden sie zusammen neu geworfen. Der neue Wert ersetzt den alten bedingungslos. Es zählt nicht der bessere der beiden Werte, auch ein schlechteres Ergebnis zählt.

Ein Reroll darf auch einen Erfolg verwerfen. Ob der Spieler das tut, entscheidet er selbst.

### Auf welche Würfe

Ein Reroll gilt für jeden Wurf. Es gibt keine Wurfart, die ausgenommen ist:

- jede Probe: Eigenschaft, Grundfertigkeit, Wissens-, Handwerks- und Kulturfertigkeit, Attribut, Attacke, Parade, Ausweichen, Fernkampf, Zauber, Psi, KI, Wunder, Selbstbeherrschung, Initiative, Bruchtest und Proben auf Tabellen;
- jeden sonstigen Wurf, zum Beispiel einen Schadenswurf oder einen Trefferzonenwurf.

Auch ein Patzer darf mit einem Reroll verworfen werden.

### Wessen Würfe

Ein Spieler darf mit seinen eigenen Rerolls wiederholen:

- seine eigenen Würfe;
- offen geworfene Würfe des Meisters;
- verdeckt geworfene Würfe des Meisters.

Bei einem verdeckten Wurf wissen die Spieler, dass gewürfelt wurde und worum es geht, zum Beispiel bei einem Angriff eines Nichtspielercharakters auf einen Helden. Nur die Würfelaugen bleiben aus Gründen der Übersicht verborgen.

Nicht wiederholen darf ein Spieler:

- **geheime** Würfe des Meisters. Bei ihnen sollen die Spieler nicht einmal wissen, dass oder worauf gewürfelt wurde, zum Beispiel bei einer versteckten Wahrnehmungsprobe gegen einen Hinterhalt;
- Würfe anderer Spieler.

Eine Ausnahme gilt für den Wurf eines anderen Spielers, der selbst keine Rerolls mehr hat. Soll dieser Wurf dennoch wiederholt werden, opfern alle Spieler je einen Reroll für diesen einen Neuwurf.

### Mehrfach und nach Kenntnis des Ergebnisses

Derselbe Wurf darf mehrfach wiederholt werden, solange der Vorrat nicht leer ist: Reroll auf Reroll, bis das Ergebnis passt oder der Vorrat leer ist. Jeder Neuwurf kostet einen Reroll.

Der Spieler entscheidet nach Kenntnis der Lage. Die Situation ist abgelaufen, ihre Folgen stehen fest, und erst dann setzt er den Reroll ein. Er darf also gezielt ein bereits bekanntes schlechtes Ergebnis kippen.

### Folgewürfe

Zwischen dem Wurf und dem Reroll können weitere Würfe gefallen sein, die auf dem ursprünglichen Ergebnis aufbauten. Ein Reroll kann solche Würfe ungültig machen. Dann werden sie neu geworfen. Der Meister entscheidet, welche Folgen bestehen bleiben und welche Würfe neu zu werfen sind. Auch diese neuen Würfe darf der Spieler wieder mit Rerolls wiederholen, solange er Vorrat hat.

Wie weit zurück ein Wurf noch wiederholt werden darf, entscheidet außerhalb des Kampfes der Meister. Im Kampf gelten eigene Regeln, siehe [[Treffer-und-Schaden|Treffer und Schaden]].

### Beispiele

Eine Grundfertigkeitsprobe misslingt. Der Wurf W30 − W12 ergibt 24, der Probenwert ist 15, der Held scheitert um 9. Der Spieler hat 3 Rerolls und setzt einen ein. Der neue Wurf ergibt 6, und die Probe gelingt um 9. Der Vorrat sinkt von 3 auf 2. Wäre der neue Wurf 27 gewesen, würde die 27 zählen. Zurück zur 24 gibt es nicht. Solange der Vorrat nicht leer ist, darf der Spieler denselben Wurf noch einmal wiederholen.

Der Meister würfelt offen die Wahrnehmungsprobe eines Nichtspielercharakters, die die Gruppe entdeckt. Ein Spieler gibt einen eigenen Reroll aus, um diesen Wurf zu wiederholen. Das ist zulässig. Hätte der Meister geheim gewürfelt, ohne dass die Gruppe von der Probe weiß, wäre der Wurf nicht wiederholbar. Ein bloß verdeckt geworfener Wurf bliebe wiederholbar.

Ein Spieler hat 0 Rerolls, und sein wichtiger Wurf ist misslungen. Die vier Spieler am Tisch opfern je einen Reroll. Dieser eine Wurf wird einmal wiederholt.
