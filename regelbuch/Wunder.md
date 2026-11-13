---
title: Wunder
aliases: [Wunder, Wunder-Probe, Wunderprobe, Gebet, Gebets-Talent, Stoßgebet, Ritual, Karmapool, KPP-Maximum, KPP-Basis, MinKarma, Gute Wunderprobe, Wunder-Patzer]
status: entwurf
---

# Wunder

Der Geweihte wirkt ein Wunder, indem er auf seinen Ausstrahlungsbonus plus Gebets-Talent minus den Malus des Wunders würfelt. Bezahlt wird aus dem Karmapool, dem Vorrat an Karma-Pool-Punkten ([[Glossar#KPP|KPP]]). Gelingt die Probe, kostet das Wunder den vollen KPP-Wert. Misslingt sie, kostet es die Hälfte. Patzt der Geweihte, entscheidet eine Pechsprobe über die Kosten.

Teilungen in diesem Kapitel werden sofort aufgerundet ([[Wuerfeln-und-Proben]]). Wie der Held Geweihter wird und seine Grade kauft, steht im Kapitel [[Religion]].

## Wann ein Wunder versuchbar ist

Der Held kann ein Wunder nur versuchen, wenn alle diese Bedingungen erfüllt sind.

**Religion und Sekte.** Im Charakterbogen sind eine Religion und eine Sekte gewählt. Ohne beides ist kein Wunder versuchbar, auch kein Allgemeines.

Von den Wundern sind 13 allgemein. Sie gelten für jede gewählte Religion und Sekte. Jedes religionsspezifische Wunder gehört zu einem Gott und einer Sekte (zurzeit alle 47: der jeweilige Gott und die Sekte Orthodox). Es ist nur versuchbar, wenn die Religion und die Sekte im Charakterbogen beide dazu passen. Bei einer anderen Sekte bleiben nur die allgemeinen Wunder.

**Gebets-Talent gelernt.** Jedes Wunder hat ein Gebet: Stoß, Wunder oder Ritual. Das Gebet bestimmt das Talent, das die Probe liefert:

- Stoß: das Talent Stoßgebet.
- Wunder: das Talent Wunder.
- Ritual: das Talent Ritual.

Diese drei Talente zählen zu den Wissens-, Handwerks- und Kulturfertigkeiten ([[Glossar#WHK|WHK]]), aber nicht zu ihrem normalen Katalog. Der Held kauft sie nur als Geweihten-Talente ([[Religion]]). Ist der Fertigkeitswert ([[Glossar#FW|FW]]) des Gebets-Talents kleiner als 1, gibt es für dieses Wunder keine Probe, gleich wie hoch das Karma ist. Hat der Held keines der drei Talente, gibt es für kein Wunder eine Probe.

**Karma-Schwelle.** Jedes Wunder hat ein Mindest-Karma (MinKarma). Liegt das Karma des Helden darunter, ist das Wunder gesperrt ([[Attribute]]). Das gilt unabhängig vom Talent: Der Held kann das Gebets-Talent gelernt haben und trotzdem unter dem Mindest-Karma eines bestimmten Wunders liegen.

**Karmapool deckt die Kosten.** Der aktuelle Karmapool muss mindestens den vollen KPP-Wert des Wunders decken. Diese Prüfung läuft vor jeder Veränderung der Kosten durch einen Patzer. Ist sie nicht erfüllt, ist das Wunder gar nicht erst versuchbar.

## Die Wunder-Probe

```text
Probe = Ausstrahlungsbonus + FW des Gebets-Talents − Malus
```

- **Ausstrahlungsbonus** ist der Eigenschaftsbonus der Ausstrahlung ([[Eigenschaften]]). Er ist für alle Wunder dieselbe Eigenschaft. Wunder haben keine eigene Eigenschaft.
- **FW des Gebets-Talents** ist der Fertigkeitswert des Talents, das das Gebet des Wunders bestimmt.
- **Malus** ist ein fester Erschwerungswert des einzelnen Wunders. Es gibt weder Stufen noch Grade.

Die Formel enthält keine Division. Die Probe kann negativ werden, wenn der Malus den Ausstrahlungsbonus plus FW übersteigt. Dafür gilt die allgemeine Regel für verringerte Probenwerte ([[Wuerfeln-und-Proben]]).

### Wurf und Erfolg

Die Wunder-Probe ist eine einfache Probe. Der Held würfelt W30 − W12. Ist das Ergebnis höchstens so hoch wie die Probe, gelingt sie, sonst misslingt sie.

Bei einem Patzer (Wurf 0) gilt immer die eigene Patzer-Regel unten, so wie bei Spruchmagie, Psi und KI ([[Spruchmagie]], [[Psi]], [[KI]]).

### Gute Wunderprobe

Das Talent Gute Wunderprobe ([[Talente-die-Werte-veraendern]]) verändert nur die Schwelle des guten Erfolgs. Statt des Wurfs 1 gilt bei Stufe 1 des Talents das Karma und bei Stufe 2 das Karma plus die Aura. Die Schwelle ist auf die Hälfte der Probe begrenzt.

Die Probe selbst bleibt unverändert. Beide Werte werden nebeneinander geschrieben, in der Form Probe/gSchwelle, sobald die Schwelle größer als 1 ist. Sie werden weder addiert noch ersetzt.

## Der Karmapool

Das Maximum des Karmapools ist:

```text
KPP-Maximum = KPP-Basis (Geweihtengrad) + Karma × 10
```

KPP-Basis je Geweihtengrad ([[Religion]]):

- Grad 0 (kein Titel): 0
- Grad 1, Niederer: 100
- Grad 2, Minderer: 125
- Grad 3, Konfirmierter: 150
- Grad 4, Etablierter: 175
- Grad 5, Angesehener: 200
- Grad 6, Gesalbter: 225
- Grad 7, Heiliger: 250

Der Geweihtengrad ist die höchste Stufe der aktiven Religion, die der Held besitzt. Das Maximum fällt nie unter 0. Bei Grad 0 und Karma 0 ist es 0. Bei Grad 0 (kein Geweihten-Talent) ist die KPP-Basis 0, das Maximum ist Karma × 10. Ein Held, der nicht Geweihter ist und Karma aus einem Artefakt hat, hat also trotzdem ein Maximum über 0.

### Regeneration

Der aktuelle Karmapool regeneriert jeden Tag um:

```text
Geweihtengrad / 2 + Karma / 2
```

Jede Division wird einzeln aufgerundet, dann wird addiert. Der Karmapool steigt nie über das KPP-Maximum.

## Kosten beim Wirken

Das Wirken eines Wunders zieht den KPP-Wert des Wunders vom aktuellen Karmapool ab:

- **Probe gelingt:** der volle KPP-Wert.
- **Probe misslingt (ohne Patzer):** der halbe KPP-Wert, aufgerundet.
- **Patzer:** siehe unten.

Bei zwei Wundern steht statt einer Zahl eine Formel als KPP-Wert, zum Beispiel Karma × 10. Dort wird zuerst die Formel ausgewertet und dann wie bei jedem festen KPP-Wert verfahren.

## Patzer und Pechsprobe

Bei einem Patzer ersetzt eine Pechsprobe die halben Kosten des Misslingens. Sie ist eine eigene Probe mit W30 − W12, genau wie bei der Spruchmagie ([[Spruchmagie#Zauberpatzer und Pechsprobe|Zauberpatzer und Pechsprobe]]). Sie ergibt Pech (Kosten mal 2), Glück (mal 0,5) oder Kein Pech (mal 1). Der Faktor gilt für den vollen KPP-Wert des Wunders. Ein Glück-Ergebnis wird aufgerundet.

Ein Fehlschlag ohne Patzer bleibt bei den halben Kosten.

### Zu wenig Karmapool

Für Wunder gibt es keinen Schaden bei zu wenig Karmapool. Stattdessen gilt die Prüfung oben gegen den vollen KPP-Wert. Besteht der Held sie, patzt aber, und die Pechsprobe verdoppelt die fälligen Kosten über den aktuellen Karmapool hinaus, sinkt der Karmapool auf 0. Es entsteht kein zusätzlicher Schaden, und das Scheitern wird nicht nachträglich verändert. Der Karmapool wird nie negativ.

## Beispiele

**Probe.** Das Gebet ist Stoß, der FW des Stoßgebets ist 8, der Ausstrahlungsbonus 3 und der Malus 4. Die Probe ist 3 + 8 − 4 = 7.

**Karmapool.** Der Held hat Geweihtengrad 4 (Etablierter) und Karma 6. Das KPP-Maximum ist 175 + 6 × 10 = 235.

**Gesperrt.** Ein Held mit Karma 2 betrachtet ein Wunder mit MinKarma 3. Das Wunder ist gesperrt, gleich wie hoch sein FW ist.

**Regeneration.** Der Held hat Geweihtengrad 3 und Karma 5. Der Karmapool steigt pro Tag um 3 / 2 + 5 / 2, aufgerundet je Division, also 2 + 3 = 5, höchstens bis zum KPP-Maximum.

**Kosten bei Wunder mit KPP-Wert 15.**
- Das Wunder gelingt: Der Karmapool sinkt um 15.
- Das Wunder misslingt ohne Patzer: Der Karmapool sinkt um 8 (15 / 2 = 7,5, aufgerundet).
- Das Wunder patzt, die Pechsprobe ergibt 5. Das ist kein Pech (nicht über 21 + Glück): mal 1. Der Karmapool sinkt um 15, nicht um die Hälfte.
- Das Wunder patzt, die Pechsprobe ergibt 0. Pech, mal 2: Der Karmapool sinkt um 30.
- Das Wunder patzt, die Pechsprobe ergibt 21. Glück, mal 0,5: Der Karmapool sinkt um 8 (15 × 0,5 = 7,5, aufgerundet).

**Karmapool deckt die Kosten nicht.** Der Held hat einen aktuellen Karmapool von 10 und betrachtet ein Wunder mit KPP-Wert 15. Die Kosten sind nicht gedeckt, das Wunder ist nicht versuchbar, gleich wie hoch FW und MinKarma sind.

**Patzer über den Karmapool hinaus.** Der Held hat einen aktuellen Karmapool von 15. Das reicht für die Kosten eines Wunders mit KPP-Wert 15. Der Wurf patzt, die Pechsprobe ergibt Pech, fällig sind 30. Der Karmapool sinkt auf 0, ohne zusätzlichen Schaden.

**Religion und Sekte.** Im Charakterbogen stehen die Religion Lloth und die Sekte Orthodox: Es sind 13 allgemeine und 11 Wunder der Lloth wählbar, zusammen 24. Steht dort die Religion Lloth mit einer anderen Sekte, sind es nur die 13 allgemeinen Wunder. Ist keine Religion oder keine Sekte gewählt, ist kein Wunder versuchbar.
