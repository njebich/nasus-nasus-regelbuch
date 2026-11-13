---
title: Abenteuer-, Entwicklungs- und Talentpunkte (AP, EP, TaP)
aliases: [Abenteuerpunkte, AP, Entwicklungspunkte, EP, EP-Budget, Talentpunkte, TaP, Talentpunkte-Budget, Steigern, Steigerung, Erfahrung, Erfahrung und Steigerung]
status: entwurf
---

# Abenteuer-, Entwicklungs- und Talentpunkte (AP, EP, TaP)

Der Held sammelt Abenteuerpunkte (AP). Aus ihnen ergeben sich seine Entwicklungspunkte (EP) und seine Talentpunkte (TaP). Mit diesen beiden Währungen kauft er seine Werte, Vor- und Nachteile und Talente.

## Drei getrennte Währungen

- **AP** zeigen den Gesamtfortschritt. Sie werden nur gesammelt und nie ausgegeben. AP kaufen nichts.
- **EP** sind die wichtigste Kaufwährung. Mit ihnen kauft der Held Eigenschaften ([[Attribute|Attribute]]), Sprache und Kultur sowie Vor- und Nachteile. EP werden ausgegeben und können durch Rückgabe oder Verkauf wieder frei werden.
- **TaP** sind eine eigene Währung nur für Talente.

## Abenteuerpunkte

### Die gesamten AP

Die gesamten AP eines Helden sind die Summe aller AP, die er je erhalten hat. Jede Vergabe erhöht sie unwiderruflich. Sie werden nie verringert.

Alle Vergaben zählen gleich, gleichgültig woher sie stammen. Mehrere Vergaben werden einfach addiert. Ein Held ohne jede Vergabe hat 0 AP und steht auf Stufe 0 und Kreis 0.

### Woher AP kommen

Es gibt genau zwei Quellen:

- Der Meister vergibt reguläre AP **pro Session**, nicht nur zum Ende eines Abenteuers.
- Der Meister gibt eigene Meister-AP an einen Helden ab.

Sessions sind Teile eines Abenteuers, Abenteuer sind Teile einer Kampagne ([[Zeit-und-Spielablauf|Zeit und Spielablauf]]).

Wie viele AP der Meister bei einer Vergabe gibt, liegt in seinem Ermessen. Für die Höhe einer regulären Session-Vergabe gibt es keine Formel und keine Richtgröße, ebenso wenig für die Frage, wie schnell ein Meister Meister-AP erwirbt. Die einzige Ausnahme ist die Nachziehregel unten.

### Meister-AP

Meister-AP gehören dem Menschen am Spieltisch, der Meister ist, nicht einem Helden. Aus diesem Guthaben gibt der Meister nach eigenem Ermessen AP an Helden ab.

Das Guthaben wächst mit jeder Session aus zwei Quellen, die sich addieren:

- ein fester Zuwachs von 200 AP, unabhängig von der Zahl der Spieler;
- zusätzlich 0 bis 25 AP je anwesendem Spieler. Wie viele, bestimmt jeder Spieler nach eigenem freiem Ermessen. Sie sind an den Meister gerichtet.

### Gehobener Start

Beim gehobenen Start erhält der Held genau eine meisterlich vergebene Vergabe von 1600 AP. Einen eigenen Bonus auf EP oder TaP gibt es dafür nicht. Der Start wirkt nur über die gesamten AP.

### Nachziehregel

Liegt die Stufe eines Helden unter der höchsten Stufe der übrigen Mitspieler, wird seine reguläre Session-Vergabe skaliert:

```text
Stufendifferenz = höchste Stufe der Mitspieler − eigene Stufe
Multiplikator   = (10 + Stufendifferenz) / 10
```

Bei einer Stufendifferenz von 0 ist der Multiplikator 1, es wird also nicht skaliert. Die Nachziehregel gilt nur für die reguläre Session-Vergabe, nicht für das Meister-AP-Guthaben.

### Was aus den AP folgt

Die gesamten AP bestimmen allein die [[Stufe-Kreis-Macht-und-Rerolls|Stufe und den Kreis]] des Helden. Die Stufe ergibt sich nur aus den gesamten AP, nicht aus Start-EP oder anderen gewährten EP.

Aus der Stufe folgen die gewährten TaP, aus den gesamten AP unmittelbar die gewährten EP. Beide Rechnungen stehen unten. Weitere Einflüsse auf die gewährten TaP und die gewährten EP gibt es nicht. Eine Obergrenze gibt es für beide nicht.

## Entwicklungspunkte

### Das Budget

```text
gewährte EP    = 6400 + gesamte AP
ausgegebene EP = Summe der Kosten aller EP-Käufe, die der Held aktuell hält
verfügbare EP  = gewährte EP − ausgegebene EP
```

Die Kosten eines Kaufs sind meist positiv und verbrauchen EP. Hat ein Nachteil jedoch den Katalogwert −N, sind seine Kosten −N. Das senkt die ausgegebenen EP um N und erhöht die verfügbaren EP um N, so als hätte der Held N EP gutgeschrieben bekommen. Die verfügbaren EP können dadurch über die gewährten EP hinaus steigen. Das ist beabsichtigt.

### Sprache und Kultur

Muttersprache (50 EP) und Kultur (40 EP) kauft der Held mit EP aus dem regulären Vorrat, wie jeden anderen EP-Kauf. Es gibt keine kostenlose Erstsprache oder Heimatkultur, und die gewährten EP steigen dafür nicht. Mehr dazu steht im Kapitel [[Herkunft-Ort-Sprache-Schrift-Kultur|Herkunft]].

Bei der Charaktererstellung müssen mindestens 90 EP der Käufe aus Sprach- und Kulturfertigkeiten stammen. Das ist eine Mindestausgabe, kein zusätzliches Budget.

## Talentpunkte

Der Held kauft [[Talente|Talente]] mit Talentpunkten:

```text
gewährte TaP    = 20 + Stufe × 5
ausgegebene TaP = Summe der TaP-Kosten aller Talente, die der Held aktuell hält
verfügbare TaP  = gewährte TaP − ausgegebene TaP
```

Jedes Talent hat feste Kosten im Katalog. Jedes Talent, das der Held aktuell hält, zählt als Ausgabe und kostet seine TaP. Einen Bestätigungs- oder Gültigkeitsstatus dafür gibt es nicht.

## Zu wenig EP oder TaP

Ein freiwilliger Kauf, der die verfügbaren EP oder die verfügbaren TaP unter 0 drücken würde, wird als Ganzes abgelehnt. Es wird nichts davon ausgeführt.

Die einzige Ausnahme ist der Strafeintrag bei Wiederbelebung (siehe unten). Er ist kein freiwilliger Kauf und wird immer angewendet, auch wenn er die verfügbaren EP unter 0 drückt. Ein Held mit verfügbaren EP unter 0 ist ungültig und darf nicht gespielt werden, bis er durch Rückgabe anderer Käufe wieder mindestens 0 verfügbare EP hat.

## Für wen es gilt

EP und TaP gelten für jedes Individuum einer spielbaren Spezies, auch für Nichtspielercharaktere. Das EP-Budget gilt für alle EP-finanzierten Bereiche (Attribute, Sprache und Kultur, Vor- und Nachteile und weitere), nicht nur für die Attribute.

Kreaturen und Untote sind ausgenommen. Sie erhalten frei vergebene Werte im Statblock, ohne EP und TaP.

## Rückgabe und Neuverteilung

Außerhalb einer laufenden Session kann der Held jeden EP-Kauf und jeden TaP-Kauf frei rückgängig machen. Er bekommt die Punkte voll erstattet. Während einer Session ist die Rückgabe gesperrt, genau wie bei den [[Attribute|Attributen]].

Jede Rückgabe wird protokolliert und am Tisch angesprochen. Sie darf nicht stillschweigend geschehen.

### Sprache und Kultur

Für Sprache und Kultur gilt dieselbe Regel, auch für Muttersprache und Kultur. Gibt ein Held dadurch seine einzige gesprochene Sprache zurück, wird er stumm und kann nicht mehr kommunizieren. Der Charakterbogen zeigt diesen Zustand ausdrücklich an.

### Vor- und Nachteile

[[Vor-und-Nachteile|Vor- und Nachteile]] sind grundsätzlich frei kauf- und verkaufbar. Die Erstattung beträgt genau 1:1, und die Protokollierung gilt auch hier. Für einzelne Nachteile müssen zusätzlich Voraussetzungen erfüllt sein:

- Ein durch Verletzung verlorenes Auge oder Körperteil lässt sich über Heilung auf Grad 5, KI-Regeneration oder „Ruf des Tepod“ entfernen. Bei der Erschaffung gewählte Nachteile wie Einäugig sind dauerhaft und nicht entfernbar.
- Furcht und Sucht brauchen zusätzlich die Freigabe des Meisters.
- Permanente Blueprint-Merkmale lassen sich grundsätzlich nicht entfernen.

## Wiederbelebung

EP gehen durch gewöhnliches Spielgeschehen nicht verloren. Die einzige Ausnahme ist die Wiederbelebung.

### Der Strafwert

Sobald ein Held für tot erklärt wird, wird der Strafwert aus seinen zu diesem Zeitpunkt gesamten AP berechnet. Danach bleibt er unverändert. Spätere AP-Zuwächse ändern ihn nicht mehr. Er wird aus den gesamten AP berechnet, nie aus den gewährten EP.

```text
Strafwert = 10 % der gesamten AP
```

Das Ergebnis wird nach den Regeln aus [[Wuerfeln-und-Proben|Würfeln und Proben]] gerundet.

### Der Eintrag

Wird der Held wiederbelebt und gilt ein Strafwert, entsteht genau ein neuer Eintrag nach dem Muster:

```text
Am [Tag] durch [Heiler] in [Ort] wiederbelebt
```

Der Eintrag begleitet den Helden dauerhaft wie ein Vorteil. Seine Kosten sind der Strafwert, und er zählt wie jeder andere gehaltene EP-Kauf zu den ausgegebenen EP. Einen eigenen Abzug gibt es nicht.

Wird ein Held mehrfach wiederbelebt, sammelt er mehrere solche Einträge. Sie werden nie überschrieben. Jeder weitere Tod verwendet die dann aktuellen gesamten AP, die zwischen zwei Toden meist weiter gewachsen sind. Aufeinanderfolgende Strafwerte sind unabhängig voneinander und in der Regel nicht gleich.

### Wann kein Strafwert entsteht

Wann ein Strafwert entsteht und wann nicht (Schonfrist von 24 Stunden, Duellsegen, Kreaturen), steht im Kapitel [[Tod-und-Wiederbelebung|Tod und Wiederbelebung]].

### Der tote Held und die Session

Für den toten Helden gilt der Zustand „außerhalb einer aktiven Session“, auch wenn am Tisch gerade eine Session läuft. Der Spieler darf deshalb frei Käufe zurückgeben und neu verteilen, um die verfügbaren EP wieder auf mindestens 0 zu bringen.

### Wieder ins Spiel

Ein Held darf erst wieder gespielt werden, wenn eine von zwei Bedingungen erfüllt ist:

- Er lebt und hat mindestens 0 verfügbare EP.
- Er ist untot. Untote sind vom EP-Budget ausgenommen und brauchen keine gültige EP-Bilanz.

## Beispiele

Ein Held startet mit dem gehobenen Start und hat nur diese eine Vergabe:

```text
gesamte AP   = 1600
Stufe        = 15
gewährte TaP = 20 + 15 × 5 = 95
gewährte EP  = 6400 + 1600 = 8000
```

Ein Held ohne jede Vergabe hat 6400 gewährte EP (6400 + 0).

Ein Held mit 1600 gesamten AP stirbt und wird wiederbelebt:

```text
Strafwert = 10 % von 1600 = 160
→ neuer Eintrag „Am [Tag] durch [Heiler] in [Ort] wiederbelebt“, Kosten 160
→ ausgegebene EP steigen um 160, verfügbare EP sinken um 160
```
