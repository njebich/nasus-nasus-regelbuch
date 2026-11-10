---
title: Psi (PSI)
aliases: [Psi, PSI, Psi-Probe, PSI-Probe, Psi-Wert, Psi-Stufe, Psi-Fähigkeit, Psi-Fähigkeiten, Stufen-Erschwerung, MpZ, MbS, Manamangel, PSI-Manabrand, Ausdauerkosten Psi, Psi-Patzer]
status: entwurf
---

# Psi (PSI)

Der Held wirkt eine Psi-Fähigkeit, indem er eine Psi-Stufe von 1 bis 7 wählt, auf den Psi-Wert würfelt und Mana und Ausdauer zahlt. Misslingt die Probe, kostet ihn das Mana. Patzt er, verliert er die Kontrolle über die Fähigkeit und ist kampfunfähig.

Halbierungen in diesem Kapitel werden sofort aufgerundet ([[Wuerfeln-und-Proben]]).

## Wer Psi wirken kann

Der Held kann eine Psi-Fähigkeit nur wählen, wenn seine Aura und seine Magie beide größer als 0 sind ([[Attribute]]). Der Fertigkeitswert spielt dafür keine Rolle. Dieselbe Voraussetzung gilt für KI und Spruchmagie.

## Der Psi-Wert

Der Held wählt vor dem Wurf die Psi-Stufe, auf der er die Fähigkeit wirken will. Dann gilt:

```text
Psi-Wert = Fertigkeit + Eigenschaftsbonus + Aura + Magie
           − MBE − Stufen-Erschwerung (Fähigkeit, gewählte Stufe)
```

- **Fertigkeit** ist der Talentwert ([[Glossar#TaW|TaW]]), den der Held in die einzelne Psi-Fähigkeit investiert hat.
- **Eigenschaftsbonus** ist der Eigenschaftsbonus der Eigenschaft, die der Fähigkeit fest zugeordnet ist ([[Eigenschaften]]).
- **Aura** und **Magie** sind die beiden Attribute des Helden.
- **MBE** ist die Mentale Behinderung ([[Glossar#MBE|MBE]], [[Behinderung-und-Erschwernis]]). Psi ist eine geistige Probe. Es zählt nur die Mentale Behinderung, die Körperliche Behinderung nie.
- **Stufen-Erschwerung** ist für jede Fähigkeit und jede Psi-Stufe ein eigener Wert.

Der Psi-Wert enthält keine Division. Er kann negativ werden, wenn die Stufen-Erschwerung hoch und die Fertigkeit niedrig ist. Für verringerte Probenwerte gilt die allgemeine Regel ([[Wuerfeln-und-Proben]]).

## Wurf und Erfolgsstufen

Der Held würfelt W30 − W12. Ist das Ergebnis höchstens so hoch wie der Psi-Wert, gelingt die Probe. Die Erfolgsstufe bestimmt, wie viele Bonuspunkte der Held bekommt ([[Wuerfeln-und-Proben]]):

- Wurf 1: guter Erfolg, 1 Bonuspunkt.
- Wurf 21: meisterlicher Erfolg, 2 Bonuspunkte.
- Wurf 29: fröhlicher Erfolg, 3 Bonuspunkte.
- Jedes andere Ergebnis bis zum Psi-Wert: normaler Erfolg, kein Bonuspunkt.
- Ergebnis über dem Psi-Wert, ohne Pasch: Fehlschlag. Die Manakosten bei Misslingen sind fällig.
- Wurf 0 (Pasch): Patzer. Die Manakosten bei Misslingen sind fällig, dazu gilt die Patzer-Regel unten.

Das Talent für den guten Erfolg der Psi ([[Talente-die-Werte-veraendern]]) verändert nur die Schwelle des guten Erfolgs. Statt des Wurfs 1 gilt bei Stufe 1 des Talents die Magie und bei Stufe 2 die Magie plus der Eigenschaftsbonus der Fähigkeit. Die Schwelle ist auf die Hälfte des Psi-Werts begrenzt. Die Schwellen für meisterlich und fröhlich verändert kein Talent.

## Manakosten beim Wirken

Jede Fähigkeit hat Manakosten je Zeiteinheit (MpZ). Sie gelten für die gewählte Psi-Stufe.

Die Zeiteinheit ist ein Block von der Länge der Wirkungsdauer, die bei der Fähigkeit steht. Steht dort zum Beispiel „Macht Sekunden“, ist ein Block Macht Sekunden lang ([[Stufe-Kreis-Macht-und-Rerolls|Macht]]). Jeder angefangene Block kostet voll.

Der Held kann die Fähigkeit jederzeit abbrechen. Dann endet die Zahlung. Jede Psi-Fähigkeit ist bipolar ([[Magie-Wirkungsdauer-und-Konzentration]]).

Hat eine Fähigkeit die Wirkungsdauer „permanent“ (Destruktion, Geschosse ablenken, Telekinetisches Geschoss), sind die Manakosten je Zeiteinheit eine einmalige Zahlung.

Reicht das Mana während der Wirkungsdauer nicht, entscheidet der Held: Er trägt die Folgen des Manamangels (siehe unten) oder beendet die Fähigkeit.

## Bonuspunkte

Nach einem Erfolg verteilt der Held seine Bonuspunkte sofort. Jeder Punkt hebt die gewählte Psi-Stufe um 1 oder halbiert die Manakosten je Zeiteinheit. Die Halbierung kostet 1 Punkt und ist höchstens einmal wählbar. Die Verteilung der Punkte ist frei.

Die Psi-Stufe steigt höchstens auf 7. Punkte, die weder in eine Stufenanhebung noch in die Halbierung passen, verfallen.

Die Stufen-Erschwerung und die Manakosten je Zeiteinheit richten sich nach der gewählten Stufe vor der Anhebung. Die halbierten Manakosten werden aufgerundet.

## Manakosten bei Misslingen

Jede Fähigkeit hat für jede Psi-Stufe Manakosten bei Scheitern der Probe (MbS). Sie sind bei jedem Fehlschlag fällig und bei jedem Patzer.

Bei einem normalen Fehlschlag kostet es den vollen Wert der gewählten Stufe.

### Patzer

Bei einem Patzer würfelt der Held eine Pechsprobe, genau wie bei der Spruchmagie ([[Spruchmagie#Zauberpatzer und Pechsprobe|Zauberpatzer und Pechsprobe]]). Das ist eine eigene Probe mit W30 − W12. Sie ergibt Pech (Manakosten mal 2), Glück (mal 0,5) oder Kein Pech (mal 1). Der Faktor gilt für den vollen Wert der Manakosten bei Scheitern.

Außerdem gerät die Fähigkeit außer Kontrolle. Was genau geschieht, bestimmt der Meister nach seinem Ermessen. Der Held ist sofort kampfunfähig (in der Selbstbeherrschungstabelle „KK − 2“): für W15 + W6 Kampfrunden, danach automatisch Sturz ([[Zustaende-Katalog]]). Dafür würfelt er keine eigene Selbstbeherrschungsprobe, und das Ergebnis der Pechsprobe ändert daran nichts. Nasenbluten ist Erzählung und hat keine weitere Wirkung.

## Manamangel

Reicht das Mana des Helden nicht, um die fälligen Manakosten bei Scheitern zu zahlen (bei einem Patzer einschließlich des Faktors der Pechsprobe), gilt:

1. Der fehlende Betrag wird halbiert und aufgerundet. So viel Schaden nimmt die Trefferzone Kopf ([[Treffer-und-Schaden]]). Erreicht der Kopf dabei 0 Lebensenergie, geht der übrige Schaden auf die Gesundheit.
2. Der Held würfelt unbedingt eine Selbstbeherrschungsprobe, erschwert um den Schadensbetrag.
3. Misslingt sie, würfelt er zusätzlich eine Probe auf den Mentalen Fokus ([[Magie-Wirkungsdauer-und-Konzentration]]).

Reicht das Mana genau, entfällt der Manamangel. Es wird nur der übliche Betrag abgezogen.

Bei einem Patzer ohne verfügbares Mana gelten beide Folgen zugleich: die Kampfunfähigkeit und der Schaden durch den Manamangel. Eine Selbstbeherrschungsprobe aus dem Manamangel ist unabhängig von der Kampfunfähigkeit. Beide Zustände bestehen nebeneinander.

## Aufrechterhalten

Solange eine Psi-Fähigkeit läuft, verringert sie die freie Magie des Helden um die gewählte Psi-Stufe. Die freie Magie ist die Magie abzüglich der Summe aller gewählten Psi-Stufen. Freie Magie, freie Aura (KI) und verfügbare Weisheit (Spruchmagie) sind voneinander unabhängig ([[Magie-Wirkungsdauer-und-Konzentration]]).

## Ausdauerkosten

Das Wirken einer Psi-Fähigkeit kostet zusätzlich zum Mana Ausdauer ([[Ausdauer]]). Beide Kosten werden unabhängig voneinander gezahlt.

```text
Ausdauerkosten = gewählte Psi-Stufe
```

Maßgeblich ist die Psi-Stufe, die der Held vor dem Wurf gewählt hat. Eine Stufe, die ein Bonuspunkt erst nach dem Wurf anhebt, zählt nicht. Die Kosten sind immer positiv.

Sie fallen am Ende der Vorbereitungsdauer an, im Moment des Wurfs ([[Magie-Wirkungsdauer-und-Konzentration]]). Sie hängen nicht vom Ergebnis ab: Bei Erfolg (auch gut, meisterlich und fröhlich), Fehlschlag und Patzer zahlt der Held dieselbe Ausdauer.

Das Aufrechterhalten einer Psi-Fähigkeit kostet keine Ausdauer.

## Beispiele

**Psi-Wert.** Der Held hat Fertigkeit 12, Eigenschaftsbonus 3, Aura 4, Magie 3 und MBE 0. Er wählt Psi-Stufe 3. Die Stufen-Erschwerung der Stufe 3 ist 9 (Beispielwert Telekinetisches Geschoss). Der Psi-Wert ist 12 + 3 + 4 + 3 − 0 − 9 = 13.

**Guter Erfolg.** Der Wurf ist 1, ein guter Erfolg mit 1 Bonuspunkt. Der Held setzt ihn auf die Stufenanhebung. Die Fähigkeit wirkt auf Stufe 4, die Manakosten je Zeiteinheit bleiben die der Stufe 3. Die Ausdauerkosten sind 3, die gewählte Stufe, nicht 4.

**Fröhlicher Erfolg.** Der Held hat Stufe 6 gewählt und einen fröhlichen Erfolg (3 Bonuspunkte). Ein Punkt hebt die Stufe auf 7, die Obergrenze. Ein Punkt halbiert die Manakosten je Zeiteinheit. Der dritte Punkt verfällt. Die Ausdauerkosten sind 6, unabhängig von Anhebung und Obergrenze.

**Fehlschlag mit Manamangel.** Derselbe Held wählt Stufe 3. Das Ergebnis liegt über dem Psi-Wert. Die Manakosten bei Scheitern der Stufe 3 sind 30, sein Mana ist 22. Es fehlen 30 − 22 = 8, halbiert 4. Die Trefferzone Kopf nimmt 4 Schaden. Der Held würfelt eine Selbstbeherrschungsprobe, erschwert um 4. Misslingt sie, würfelt er zusätzlich auf den Mentalen Fokus.

**Fehlschlag auf Stufe 4.** Bei einem Fehlschlag auf der gewählten Stufe 4 zahlt der Held 4 Ausdauer. Die Manakosten bei Scheitern kommen dazu. Beides ist unabhängig voneinander fällig.

**Patzer.** Der Wurf ist 0. Die Pechsprobe ergibt 0, also Pech: Die Manakosten bei Scheitern der Stufe 3 (30) werden mit 2 multipliziert, fällig sind 60. Fehlt Mana, folgt der Manamangel mit dem neuen Fehlbetrag. Der Held ist außerdem kampfunfähig (KK − 2, W15 + W6 Kampfrunden, danach Sturz), und das Nasenbluten ist Erzählung.

**Patzer mit Glück.** Bei einem anderen Patzer ergibt die Pechsprobe 21, also Glück: 30 × 0,5 = 15 sind fällig. Die Kampfunfähigkeit gilt trotzdem.
