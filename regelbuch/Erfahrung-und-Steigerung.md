---
title: Erfahrung und Steigerung (EP, SP, TaP)
aliases: [Erfahrungspunkte, EP, Steigerungspunkte, SP, SP-Budget, Talentpunkte, TaP, Talentpunkte-Budget, Steigern, Steigerung, Erfahrung]
status: entwurf
---

# Erfahrung und Steigerung (EP, SP, TaP)

Der Held sammelt Erfahrungspunkte (EP). Aus ihnen ergeben sich seine Steigerungspunkte (SP) und seine Talentpunkte (TaP). Mit diesen beiden Währungen kauft er seine Werte, Vor- und Nachteile und Talente.

## Drei getrennte Währungen

- **EP** zeigen den Gesamtfortschritt. Sie werden nur gesammelt und nie ausgegeben. EP kaufen nichts.
- **SP** sind die wichtigste Kaufwährung. Mit ihnen kauft der Held Eigenschaften ([[Attribute|Attribute]]), Sprache und Kultur sowie Vor- und Nachteile. SP werden ausgegeben und können durch Rückgabe oder Verkauf wieder frei werden.
- **TaP** sind eine eigene Währung nur für Talente.

## Erfahrungspunkte

### Die gesamten EP

Die gesamten EP eines Helden sind die Summe aller EP, die er je erhalten hat. Jede Vergabe erhöht sie unwiderruflich. Sie werden nie verringert.

Alle Vergaben zählen gleich, gleichgültig woher sie stammen. Mehrere Vergaben werden einfach addiert. Ein Held ohne jede Vergabe hat 0 EP und steht auf Stufe 0 und Kreis 0.

### Woher EP kommen

Es gibt genau zwei Quellen:

- Der Meister vergibt reguläre EP **pro Session**, nicht nur zum Ende eines Abenteuers.
- Der Meister gibt eigene Meister-EP an einen Helden ab.

Sessions sind Teile eines Abenteuers, Abenteuer sind Teile einer Kampagne ([[Zeit-und-Spielablauf|Zeit und Spielablauf]]).

Wie viele EP der Meister bei einer Vergabe gibt, liegt in seinem Ermessen. Für die Höhe einer regulären Session-Vergabe gibt es keine Formel und keine Richtgröße, ebenso wenig für die Frage, wie schnell ein Meister Meister-EP erwirbt. Die einzige Ausnahme ist die Nachziehregel unten.

### Meister-EP

Meister-EP gehören dem Menschen am Spieltisch, der Meister ist, nicht einem Helden. Aus diesem Guthaben gibt der Meister nach eigenem Ermessen EP an Helden ab.

Das Guthaben wächst mit jeder Session aus zwei Quellen, die sich addieren:

- ein fester Zuwachs von 200 EP, unabhängig von der Zahl der Spieler;
- zusätzlich 0 bis 25 EP je anwesendem Spieler. Wie viele, bestimmt jeder Spieler nach eigenem freiem Ermessen. Sie sind an den Meister gerichtet.

### Gehobener Start

Beim gehobenen Start erhält der Held genau eine meisterlich vergebene Vergabe von 1600 EP. Einen eigenen Bonus auf SP oder TaP gibt es dafür nicht. Der Start wirkt nur über die gesamten EP.

### Nachziehregel

Liegt die Stufe eines Helden unter der höchsten Stufe der übrigen Mitspieler, wird seine reguläre Session-Vergabe skaliert:

```text
Stufendifferenz = höchste Stufe der Mitspieler − eigene Stufe
Multiplikator   = (10 + Stufendifferenz) / 10
```

Bei einer Stufendifferenz von 0 ist der Multiplikator 1, es wird also nicht skaliert. Die Nachziehregel gilt nur für die reguläre Session-Vergabe, nicht für das Meister-EP-Guthaben.

### Was aus den EP folgt

Die gesamten EP bestimmen allein die [[Stufe-Kreis-Macht-und-Rerolls|Stufe und den Kreis]] des Helden. Die Stufe ergibt sich nur aus den gesamten EP, nicht aus Start-SP oder anderen gewährten SP.

Aus der Stufe folgen die gewährten TaP, aus den gesamten EP unmittelbar die gewährten SP. Beide Rechnungen stehen unten. Weitere Einflüsse auf die gewährten TaP und die gewährten SP gibt es nicht. Eine Obergrenze gibt es für beide nicht.

## Steigerungspunkte

### Das Budget

```text
gewährte SP    = 6400 + gesamte EP
ausgegebene SP = Summe der Kosten aller SP-Käufe, die der Held aktuell hält
verfügbare SP  = gewährte SP − ausgegebene SP
```

Die Kosten eines Kaufs sind meist positiv und verbrauchen SP. Hat ein Nachteil jedoch den Katalogwert −N, sind seine Kosten −N. Das senkt die ausgegebenen SP um N und erhöht die verfügbaren SP um N, so als hätte der Held N SP gutgeschrieben bekommen. Die verfügbaren SP können dadurch über die gewährten SP hinaus steigen. Das ist beabsichtigt.

### Sprache und Kultur

Muttersprache (50 SP) und Kultur (40 SP) kauft der Held mit SP aus dem regulären Vorrat, wie jeden anderen SP-Kauf. Es gibt keine kostenlose Erstsprache oder Heimatkultur, und die gewährten SP steigen dafür nicht. Mehr dazu steht im Kapitel [[Herkunft-Ort-Sprache-Schrift-Kultur|Herkunft]].

Bei der Charaktererstellung müssen mindestens 90 SP der Käufe aus Sprach- und Kulturfertigkeiten stammen. Das ist eine Mindestausgabe, kein zusätzliches Budget.

## Talentpunkte

Der Held kauft [[Talente|Talente]] mit Talentpunkten:

```text
gewährte TaP    = 20 + Stufe × 5
ausgegebene TaP = Summe der TaP-Kosten aller Talente, die der Held aktuell hält
verfügbare TaP  = gewährte TaP − ausgegebene TaP
```

Jedes Talent hat feste Kosten im Katalog. Jedes Talent, das der Held aktuell hält, zählt als Ausgabe und kostet seine TaP. Einen Bestätigungs- oder Gültigkeitsstatus dafür gibt es nicht.

## Zu wenig SP oder TaP

Ein freiwilliger Kauf, der die verfügbaren SP oder die verfügbaren TaP unter 0 drücken würde, wird als Ganzes abgelehnt. Es wird nichts davon ausgeführt.

Die einzige Ausnahme ist der Strafeintrag bei Wiederbelebung (siehe unten). Er ist kein freiwilliger Kauf und wird immer angewendet, auch wenn er die verfügbaren SP unter 0 drückt. Ein Held mit verfügbaren SP unter 0 ist ungültig und darf nicht gespielt werden, bis er durch Rückgabe anderer Käufe wieder mindestens 0 verfügbare SP hat.

## Für wen es gilt

SP und TaP gelten für jedes Individuum einer spielbaren Spezies, auch für Nichtspielercharaktere. Das SP-Budget gilt für alle SP-finanzierten Bereiche (Attribute, Sprache und Kultur, Vor- und Nachteile und weitere), nicht nur für die Attribute.

Kreaturen und Untote sind ausgenommen. Sie erhalten frei vergebene Werte im Statblock, ohne SP und TaP.

## Rückgabe und Neuverteilung

Außerhalb einer laufenden Session kann der Held jeden SP-Kauf und jeden TaP-Kauf frei rückgängig machen. Er bekommt die Punkte voll erstattet. Während einer Session ist die Rückgabe gesperrt, genau wie bei den [[Attribute|Attributen]].

Jede Rückgabe wird protokolliert und am Tisch angesprochen. Sie darf nicht stillschweigend geschehen.

### Sprache und Kultur

Für Sprache und Kultur gilt dieselbe Regel, auch für Muttersprache und Kultur. Gibt ein Held dadurch seine einzige gesprochene Sprache zurück, wird er stumm und kann nicht mehr kommunizieren. Der Charakterbogen zeigt diesen Zustand ausdrücklich an.

### Vor- und Nachteile

[[Vor-und-Nachteile|Vor- und Nachteile]] sind grundsätzlich frei kauf- und verkaufbar. Die Erstattung beträgt genau 1:1, und die Protokollierung gilt auch hier. Für einzelne Nachteile müssen zusätzlich Voraussetzungen erfüllt sein:

- Ein durch Verletzung verlorenes Auge oder Körperteil lässt sich über Heilung auf Grad 5, KI-Regeneration oder „Ruf des Tepod“ entfernen. Bei der Erschaffung gewählte Nachteile wie Einäugig sind dauerhaft und nicht entfernbar.
- Furcht und Sucht brauchen zusätzlich die Freigabe des Meisters.
- Permanente Blueprint-Merkmale lassen sich grundsätzlich nicht entfernen.

## Wiederbelebung

SP gehen durch gewöhnliches Spielgeschehen nicht verloren. Die einzige Ausnahme ist die Wiederbelebung.

### Der Strafwert

Sobald ein Held für tot erklärt wird, wird der Strafwert aus seinen zu diesem Zeitpunkt gesamten EP berechnet. Danach bleibt er unverändert. Spätere EP-Zuwächse ändern ihn nicht mehr. Er wird aus den gesamten EP berechnet, nie aus den gewährten SP.

```text
Strafwert = 10 % der gesamten EP
```

Das Ergebnis wird nach den Regeln aus [[Wuerfeln-und-Proben|Würfeln und Proben]] gerundet.

### Der Eintrag

Wird der Held wiederbelebt und gilt ein Strafwert, entsteht genau ein neuer Eintrag nach dem Muster:

```text
Am [Tag] durch [Heiler] in [Ort] wiederbelebt
```

Der Eintrag begleitet den Helden dauerhaft wie ein Vorteil. Seine Kosten sind der Strafwert, und er zählt wie jeder andere gehaltene SP-Kauf zu den ausgegebenen SP. Einen eigenen Abzug gibt es nicht.

Wird ein Held mehrfach wiederbelebt, sammelt er mehrere solche Einträge. Sie werden nie überschrieben. Jeder weitere Tod verwendet die dann aktuellen gesamten EP, die zwischen zwei Toden meist weiter gewachsen sind. Aufeinanderfolgende Strafwerte sind unabhängig voneinander und in der Regel nicht gleich.

### Wann kein Strafwert entsteht

Wann ein Strafwert entsteht und wann nicht (Schonfrist von 24 Stunden, Duellsegen, Kreaturen), steht im Kapitel [[Tod-und-Wiederbelebung|Tod und Wiederbelebung]].

### Der tote Held und die Session

Für den toten Helden gilt der Zustand „außerhalb einer aktiven Session“, auch wenn am Tisch gerade eine Session läuft. Der Spieler darf deshalb frei Käufe zurückgeben und neu verteilen, um die verfügbaren SP wieder auf mindestens 0 zu bringen.

### Wieder ins Spiel

Ein Held darf erst wieder gespielt werden, wenn eine von zwei Bedingungen erfüllt ist:

- Er lebt und hat mindestens 0 verfügbare SP.
- Er ist untot. Untote sind vom SP-Budget ausgenommen und brauchen keine gültige SP-Bilanz.

## Beispiele

Ein Held startet mit dem gehobenen Start und hat nur diese eine Vergabe:

```text
gesamte EP   = 1600
Stufe        = 15
gewährte TaP = 20 + 15 × 5 = 95
gewährte SP  = 6400 + 1600 = 8000
```

Ein Held ohne jede Vergabe hat 6400 gewährte SP (6400 + 0).

Ein Held mit 1600 gesamten EP stirbt und wird wiederbelebt:

```text
Strafwert = 10 % von 1600 = 160
→ neuer Eintrag „Am [Tag] durch [Heiler] in [Ort] wiederbelebt“, Kosten 160
→ ausgegebene SP steigen um 160, verfügbare SP sinken um 160
```
