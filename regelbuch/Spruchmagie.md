---
title: Spruchmagie (SM)
aliases: [Spruchmagie, SM, Zauberprobe, Zauber-Probe, Zauberwert, Zauberstufe, Zauberpatzer, Pechsprobe, Manabrand, Bonusmenü, Hauszauber, Hauszauber-Slots, Hauszauber-Slot, Ausdauerkosten Magie, Ausdauerkosten Spruchmagie, Schnell Zaubern]
status: entwurf
---

# Spruchmagie (SM)

Der Magus wirkt einen Zauber, indem er ihn vorbereitet, am Ende der Vorbereitung auf den Zauberwert würfelt und Mana und Ausdauer zahlt. Je besser der Wurf, desto mehr Bonuspunkte darf er auf den Zauber verteilen. Patzt er, entscheidet eine Pechsprobe, was ihn das Mana kostet.

Halbierungen und andere Teilungen in diesem Kapitel werden sofort aufgerundet ([[Wuerfeln-und-Proben]]).

## Zauber lernen: Grad und Hauszauber

Jeder Zauber hat einen Grad von 1 bis 7. Der Magus kann einen Zauber lernen, wenn sein Grad nicht über seiner Weisheit liegt. Die Weisheit ist Kreis + 1 ([[Attribute]], [[Stufe-Kreis-Macht-und-Rerolls]]).

- Grad bis Weisheit: Der Zauber ist ohne weiteres lernbar.
- Grad gleich Weisheit + 1: Der Zauber ist nur lernbar, wenn ein Hauszauber-Slot frei ist.
- Grad über Weisheit + 1: Der Zauber ist nicht lernbar.

Ein Zauber vom Grad Weisheit + 1 heißt Hauszauber, solange er einen Slot belegt. Die Slots gelten schulenübergreifend. Es gibt keine feste Zuordnung von Slot zu Zauber.

### Wie viele Slots der Held hat

Die Zahl der Slots hängt nur an den Talentpunkten ([[Glossar#TaP|TaP]]), die in Talenten der Talentgruppe Magier stecken ([[Talente]]). Gezählt werden die TaP-Kosten aller Talente dieser Gruppe, die der Held aktuell hält. Die Zahl heißt hier Magier-TaP.

```text
Slots = größtes n ≥ 0 mit 6 · n · (n + 1) ≤ Magier-TaP
```

Unter 12 Magier-TaP gibt es keinen Slot. Mit mehr Magier-TaP wächst die Zahl der Slots ohne Obergrenze weiter. Die ersten Schwellen:

| Slots | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|--:|--:|--:|--:|--:|--:|--:|
| ab Magier-TaP | 12 | 36 | 72 | 120 | 180 | 252 | 336 |

Belegt ist ein Slot durch jeden Zauber mit FW über 0, dessen Grad gleich Weisheit + 1 ist. Die Slots und die belegten Slots werden bei jeder Änderung der Magier-TaP, der Weisheit oder eines Zauber-FW neu gezählt.

### Hauszauber steigern und verlieren

- Ein Hauszauber, der einen Slot belegt, bleibt steigerbar, solange die Zahl der belegten Slots nicht über der Zahl der Slots liegt.
- Steigt die Weisheit, verschiebt sich Weisheit + 1. Ein früherer Hauszauber ist dann ein regulärer Zauber und belegt keinen Slot mehr.
- Die Slots regeln nur den Zugang zu Grad Weisheit + 1. Alle weiteren Voraussetzungen des Steigerns gelten unabhängig davon.
- Gibt es keinen Zauber vom Grad Weisheit + 1, belegt kein Zauber einen Slot.

### Zu viele Hauszauber

Belegen mehr Zauber einen Slot, als der Held Slots hat, ist der Charakter nicht regelkonform. Sinken die Magier-TaP durch eine Umentscheidung bei den Talenten unter eine Schwelle, gilt das sofort.

Der Held wird regelkonform, indem der Spieler bei so vielen Hauszaubern wie nötig den FW auf 0 zurücksteigert. Der Spieler wählt, welche. Bis dahin ist kein weiterer Hauszauber lernbar.

Außerhalb einer laufenden Session darf der Spieler jederzeit zurücksteigern und bekommt alle Entwicklungspunkte voll erstattet. Jede Rückgabe wird aufgeschrieben und am Tisch bekannt gegeben. Während einer laufenden Session sind die Talentwahlen gesperrt, die Magier-TaP können dann nicht sinken ([[Zeit-und-Spielablauf]]).

## Der Zauberwert

Ein Zauber ist nur versuchbar, wenn die Fertigkeit im Zauber mindestens 1 ist und der Zauberwert nach allen Abzügen mindestens 1 bleibt. Sonst ist der Zauber nicht wirkbar. Ein Zauberwert von genau 1 genügt.

```text
Zauberwert = Magie + Eigenschaftsbonus + Fertigkeit
             − MBE − Stufen-Erschwerung − weitere Erschwerung
```

- **Magie** ist das Attribut des Helden ([[Attribute]]).
- **Eigenschaftsbonus** ist der Eigenschaftsbonus der Eigenschaft, die im Zauberbuch beim Zauber steht ([[Eigenschaften]]). Bei den fünf Schulen Elementarbeschwörung und Kampfmagie gilt eine feste Eigenschaft je Schule: Feuer Mut, Wasser Athletik, Luft Schnelligkeit, Erde Stärke, Magie Ausstrahlung.
- **Fertigkeit** ist der Fertigkeitswert ([[Glossar#FW|FW]]) im gelernten Zauber.
- **MBE** ist die Mentale Behinderung ([[Glossar#MBE|MBE]], [[Behinderung-und-Erschwerung]]). Die Zauberprobe ist eine geistige Probe. Es zählt nur die Mentale Behinderung, die Körperliche Behinderung nie.
- **Stufen-Erschwerung** steht für jeden Zauber und jede Zauberstufe im Zauberbuch.
- **Weitere Erschwerung** ist ein Wert, den der Meister im Einzelfall vor dem Wurf ansagt.

## Die Zauberstufe

Der Magus wählt vor dem Wurf die Zauberstufe 1, 2 oder 3. Jeder Zauber braucht mindestens 1 Sekunde Vorbereitungszeit, gleich auf welcher Stufe.

- **Stufe 1:** Die Vorbereitungszeit ist voll. Geste und Formel sind beide erforderlich. Kein Talent ist nötig.
- **Stufe 2:** Die Vorbereitungszeit ist halbiert. Eines von beiden entfällt, nicht beide. Der Held braucht dafür das Talent Stufe 2 Zaubern.
- **Stufe 3:** Die Vorbereitungszeit ist gedrittelt. Weder Geste noch Formel sind erforderlich. Der Held braucht dafür das Talent Stufe 3 Zaubern.

Ohne das jeweilige Talent ist Stufe 2 oder 3 nicht wählbar, gleich wie hoch die Fertigkeit ist.

Das Talent Schnell Zaubern verkürzt die Vorbereitungszeit weiter. Die Vorbereitungszeit wird durch einen Teiler geteilt. Ohne das Talent ist der Teiler 1, 2 und 3 für die Zauberstufen 1, 2 und 3. Mit dem Talent gilt:

| Schnell Zaubern | Stufe 1 | Stufe 2 | Stufe 3 |
|---|--:|--:|--:|
| ohne | 1 | 2 | 3 |
| Stufe 1 | 2 | 3 | 4 |
| Stufe 2 | 3 | 4 | 5 |
| Stufe 3 | 4 | 5 | 6 |

Die Stufen des Talents addieren sich nicht. Es zählt nur die höchste, die der Held besitzt. Geste und Formel bleiben bei Zauberstufe 1 immer beide nötig, bei Zauberstufe 2 fällt immer nur eines weg.

## Wurf und Erfolgsstufen

Die Zauberprobe wird am Ende der Vorbereitungszeit einmal gewürfelt, mit W30 − W12. Der Zauberwert wird zu diesem Zeitpunkt aus den dann gültigen Werten berechnet. Ist das Ergebnis höchstens so hoch wie der Zauberwert, gelingt die Probe. Die Erfolgsstufe bestimmt, wie viele Bonuspunkte der Magus bekommt ([[Wuerfeln-und-Proben]]):

- Wurf 1: guter Erfolg, 1 Bonuspunkt.
- Wurf 21: meisterlicher Erfolg, 2 Bonuspunkte.
- Wurf 29: fröhlicher Erfolg, 3 Bonuspunkte. Das gilt nur mit dem Vorteil Kind der Fröhlichkeit ([[Gaben-und-Schwaechen]]). Ohne ihn zählt die 29 wie jedes andere Ergebnis.
- Jedes andere Ergebnis bis zum Zauberwert: normaler Erfolg, kein Bonuspunkt.
- Ergebnis über dem Zauberwert, ohne Pasch: Fehlschlag.
- Wurf 0 (Pasch): Patzer. Siehe unten.

Das Talent für den guten Erfolg der Spruchmagie ([[Talente-die-Werte-veraendern]]) verändert nur die Schwelle des guten Erfolgs. Statt des Wurfs 1 gilt bei Stufe 1 des Talents die Weisheit und bei Stufe 2 die Weisheit plus der Eigenschaftsbonus des Zaubers. Die Schwelle ist auf die Hälfte des Zauberwerts begrenzt. Die Schwellen für meisterlich und fröhlich verändert kein Talent.

## Bonuspunkte

Nach einem Erfolg verteilt der Magus seine Bonuspunkte sofort. Er darf sie frei auf mehrere Optionen verteilen. Die Optionen dürfen zusammen nicht mehr kosten als die Punkte, die er hat. Nicht ausgegebene Punkte verfallen.

Jede Option gehört zu einer Achse: Wirkung, Reichweite, Wirkungsdauer, Beherrschung, Kosten oder Effektdauer ([[Magie-Wirkungsdauer-und-Konzentration]]). Je Achse ist nur eine Stufe wählbar, und jede Option höchstens einmal.

**1 Punkt:**
- halbe Manakosten,
- halbe Effektdauer,
- 2-fache Wirkung,
- 2-fache Reichweite,
- 2-fache Wirkungsdauer,
- Beherrschung mit 2-facher Macht ([[Stufe-Kreis-Macht-und-Rerolls|Macht]]),
- Zauber kopieren.

**2 Punkte:**
- 3-fache Wirkung,
- 3-fache Reichweite,
- 3-fache Wirkungsdauer,
- Beherrschung mit 3-facher Macht.

**3 Punkte:**
- 4-fache Wirkung,
- 4-fache Reichweite,
- 4-fache Wirkungsdauer,
- Beherrschung mit 4-facher Macht.

Halbe Manakosten, halbe Effektdauer und Zauber kopieren gibt es nur für 1 Punkt, auch bei einem größeren Budget. Die halben Werte werden aufgerundet.

### Zauber kopieren

Der Zauber wirkt ein zweites Mal in derselben Kampfrunde. Beide Wirkungen treten automatisch mit normalem Effekt ein, es gibt keinen zweiten Wurf. Als Ziele sind bis zu zwei Ziele in Sichtweite möglich, mit Körperfokus ([[Magie-Wirkungsdauer-und-Konzentration]]) auch ein ungesehenes Ziel. Die vollen Manakosten sind für jede Wirkung einzeln fällig. Bei jeder Erfolgsstufe sind es zwei Wirkungen.

Wählt der Magus Zauber kopieren, verteilt er die übrigen Punkte frei auf die beiden Wirkungen. Für jede Wirkung gilt jede Achse höchstens einmal.

## Gelingen und Misslingen

**Die Probe gelingt.** Die Effektdauer beginnt. Sie führt in einer Rampe zum vollen Effekt. Der Effekt ist währenddessen halbiert, sofern der Zauber nichts anderes angibt. Sie beginnt normalerweise in der Kampfrunde nach dem Ende der Vorbereitungszeit. Ist die Effektdauer des Zaubers „sofort“, beginnt der Effekt sofort. Danach beginnt die Wirkungsdauer. „Sofort“ ist ein einmaliges Ereignis. „Permanent“ bedeutet, dass der Effekt sofort eintritt und nie von selbst endet ([[Magie-Wirkungsdauer-und-Konzentration]]).

**Die Probe misslingt oder der Zauber wird abgebrochen.**
- Scheitert die Probe in der Vorbereitungszeit selbst, auch durch Abbruch in dieser Phase, sind die halben Manakosten fällig.
- Wird der Zauber während der bereits laufenden Effektdauer nach einer gelungenen Probe abgebrochen, sind die vollen Manakosten fällig.
- Ein Zauberpatzer ersetzt diese Kosten durch das Ergebnis der Pechsprobe.

## Zauberpatzer und Pechsprobe

Bei einem Patzer (Wurf 0) würfelt der Magus eine eigene Probe mit W30 − W12, die Pechsprobe. Sie wird nicht nach den Erfolgsstufen gelesen, sondern nach dieser Tabelle:

| Wurf der Pechsprobe | Ausgang | Manakosten |
|---|---|---|
| 0 | Pech | mal 2 |
| 21 oder 29 | Glück | mal 0,5 |
| jeder andere Wurf über 21 + Glück | Pech | mal 2 |
| alles Übrige | Kein Pech | mal 1 |

Bei 21 oder 29 gilt Glück unbedingt, gleich wie hoch das Attribut Glück ist ([[Attribute]]). Das Band „über 21 + Glück“ reicht bei Glück 0 von 22 bis 28. Es wird mit jedem Punkt Glück schmaler und ist bei Glück 7 leer.

Der Faktor wirkt auf die vollen Manakosten des Zaubers.

## Manabrand

Reicht das Mana des Magus nicht, um fällige Manakosten zu zahlen, gilt:

1. Der fehlende Betrag wird halbiert und aufgerundet. Diesen Betrag zieht der Magus der Trefferzone Kopf als Lebensenergie ab ([[Treffer-und-Schaden]]).
2. Er würfelt unbedingt eine Selbstbeherrschungsprobe, erschwert um den Verlust an Lebensenergie. Das gilt unabhängig davon, ob seine Trefferschwelle überschritten wurde.
3. Misslingt sie, würfelt er zusätzlich eine Probe auf den Mentalen Fokus ([[Magie-Wirkungsdauer-und-Konzentration]]). Die Folgen eines Fehlschlags dieser Probe gelten, wo sie einschlägig sind.

Das gilt für jede fällige Zahlung: beim regulären Wirken, beim Misslingen, beim Abbruch in der Effektdauer und bei den Kosten nach einer Pechsprobe.

Solange Blutmagie wirkt (Talent Blutmagie, Stufen 1 bis 3), entfällt die Selbstbeherrschungsprobe vollständig.

Was aus dem Zauber wird, hängt von der Zauberart ab:
- Einmalige und anhaltende Zauber treten trotzdem in die Effektdauer ein, gleich wie die Proben ausgehen. Der Zauber gilt als knapp gelandet, bevor die Fokussierung verloren ging.
- Bipolare Zauber brechen sofort ab und treten nicht in die Effektdauer ein, wenn sowohl die Selbstbeherrschungsprobe als auch die Probe auf den Mentalen Fokus misslingen.

Reicht das Mana für die fälligen Kosten, auch nach einer Pechsprobe, gibt es keinen Manabrand.

## Ausdauerkosten

Zaubern kostet zusätzlich zum Mana Ausdauer ([[Ausdauer]]). Beide Kosten werden unabhängig voneinander gezahlt.

```text
Ausdauerkosten beim Wirken = Zaubergrad
```

Die gewählte Zauberstufe ändert die Ausdauerkosten nicht.

Sie fallen am Ende der Vorbereitungsdauer an, im Moment der Zauberprobe ([[Magie-Wirkungsdauer-und-Konzentration]]). Sie hängen nicht vom Ergebnis ab: Bei Erfolg, Misserfolg und Patzer zahlt der Magus dieselbe Ausdauer.

Das Aufrechterhalten eines Zaubers kostet keine Ausdauer, auch nicht, wenn mehrere Zauber gleichzeitig laufen.

## Beispiele

**Zauberwert.** Der Magus hat Magie 3, Eigenschaftsbonus 4, Fertigkeit 12 und MBE 0. Die Stufen-Erschwerung (Beispielwert) ist 6, die weitere Erschwerung 2. Der Zauberwert ist 3 + 4 + 12 − 0 − 6 − 2 = 11.

**Meisterlicher Erfolg.** Der Wurf ist 21, ein meisterlicher Erfolg mit 2 Bonuspunkten. Der Magus kann „3-fache Reichweite“ wählen (2 Punkte) oder „2-fache Wirkung“ (1 Punkt) plus „2-fache Wirkungsdauer“ (1 Punkt). Beides zusammen mit „3-facher Reichweite“ geht nicht, denn die Summe wäre 4 Punkte bei 2 vorhandenen.

**Patzer mit Manabrand.** Der Wurf ist 0, ein Patzer. Die Pechsprobe ergibt 25, der Magus hat Glück 3. Es gilt 25 über 21 + 3 = 24, also Pech: Die Manakosten werden mit 2 multipliziert. Bei Manakosten von 6 (Beispielwert) sind 12 fällig. Sein verfügbares Mana ist 8. Es fehlen 12 − 8 = 4, halbiert 2. Die Trefferzone Kopf verliert 2 Lebensenergie. Der Magus würfelt eine Selbstbeherrschungsprobe, erschwert um 2. Misslingt sie, würfelt er zusätzlich auf den Mentalen Fokus.

**Patzer ohne Manabrand.** Hat der Magus für die Kosten nach der Pechsprobe genug Mana, gibt es keinen Manabrand.

**Hauszauber.** Der Held hat 90 Magier-TaP. Es gilt 6 · 3 · 4 = 72 ≤ 90 < 120, also hat er 3 Slots. Bei Weisheit 4 sind bis zu drei Zauber vom Grad 5 lernbar. Bei 11 Magier-TaP hat er 0 Slots, ein Zauber vom Grad Weisheit + 1 ist nicht lernbar.

Ein anderer Held hat Weisheit 4 und 1 Slot. Er hat einen Grad-5-Zauber mit FW 3, damit ist 1 Slot belegt. Ein zweiter Grad-5-Zauber ist nicht lernbar, der erste bleibt steigerbar. Steigt die Weisheit auf 5, ist der Grad-5-Zauber regulär, und kein Slot ist belegt.

**Ausdauer.** Bei Zaubergrad 3 sind die Ausdauerkosten beim Wirken 3. Ein Zauber, der über 4 Kampfrunden aufrechterhalten wird, kostet dafür keine Ausdauer. Drei gleichzeitig aufrechterhaltene Zauber ebenfalls nicht.
