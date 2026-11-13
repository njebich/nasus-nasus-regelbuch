---
title: KI
aliases: [KI, KI-Fähigkeiten, KI-Fähigkeit, KI-Probe, Mentale Erschöpfung, ME, Mentale Kapazität, MK, Meister der Grundfertigkeiten, Ausdauerkosten KI, Pro+B-Staffel, Erschwerung-Verteilung]
status: entwurf
---

# KI

KI ist innere Kraft, die sich für den Adepten wie eine jederzeit abrufbare besondere Stärke anfühlt. Der Held kann sie bewusst einsetzen, ohne Mana zu verbrauchen. Er wählt dazu eine KI-Fähigkeit, bestimmt eine Erschwerung, würfelt die KI-Probe und zahlt mit Mentaler Erschöpfung und mit Ausdauer.

KI ist ausschließlich lebenden Wesen zugänglich. Nicht einmal Thaumaturgen in der Spielwelt sind sicher, ob KI überhaupt Magie ist. Deshalb schließt die Angst „Magie“ die KI ausdrücklich aus.

## Voraussetzung

Der Held kann KI nur einsetzen, wenn sowohl seine Aura als auch seine Magie größer als 0 sind (siehe [[Attribute]]). Dieselbe Bedingung gilt für jede Form der Magie.

Attributs-Boni durch Artefakte wirken in Formeln, aber nicht in Regelgrenzen. Ein dauerhaftes Artefakt, das die Intelligenz erhöht, zählt zum Beispiel nicht für ein festes Mindest-Intelligenz-Erfordernis.

Außerdem braucht der Held während der Vorbereitungszeit mindestens 1 freie Aura (siehe [[Magie-Wirkungsdauer-und-Konzentration]]).

## Die KI-Fähigkeiten

Es gibt 30 KI-Fähigkeiten. Jede hat einen festen Eigenschaftsbonus, der in ihre Probe eingeht, und eigene Basiswerte für Vorbereitungsdauer (VD) und Wirkungsdauer (WD). Alles andere gilt für alle Fähigkeiten gleich und steht in diesem Kapitel.

Der Held kauft jede Fähigkeit einzeln. Der Fertigkeitswert ([[Glossar#FW|FW]]) ist die Zahl der Punkte, die er in diese Fähigkeit investiert hat. Er bezahlt sie mit Entwicklungspunkten. Die Kurve ist der Gesamtpreis für den ganzen Fertigkeitswert:

```text
Kosten(FW) = 0                          bei FW = 0
Kosten(FW) = 10 + (FW − 1) × FW ÷ 2   sonst
```

Die Division ergibt immer eine ganze Zahl, denn (FW − 1) × FW ist immer gerade. Beispiel: Wert 1 kostet 10, Wert 2 zusammen 11, Wert 3 zusammen 13.

## Die KI-Probe

Gewürfelt wird W30 − W12 (siehe [[Wuerfeln-und-Proben]]). Der Probenwert ist:

```text
Probenwert = FW + Eigenschaftsbonus + 2 × Magie − MBE
```

Der Eigenschaftsbonus ist der, der zur Fähigkeit gehört (siehe [[Eigenschaften]]). KI ist eine geistige Probe. Die mentale Behinderung (MBE) wird deshalb vom Probenwert abgezogen, nicht als Erschwerung nach dem Wurf (siehe [[Behinderung-und-Erschwerung]]).

Die Probe gelingt nach dieser Bedingung:

```text
Wurfziel = Probenwert − Erschwerung − (ME vorher ÷ 2)
Wurf ≤ Wurfziel
```

Ein Wurf, der genau so hoch ist wie das Wurfziel, gelingt. Beispiel: Wurfziel 14, Wurf 14: Die Probe gelingt.

ME vorher ist die Mentale Erschöpfung des Helden vor diesem Wirken (siehe unten).

### Ergebnis und Bonuspunkte

- **Normaler Erfolg:** Die Fähigkeit wirkt normal. Die Mentale Erschöpfung steigt um (Erschwerung − Aura) ÷ 2.
- **Guter Erfolg:** 1 Bonuspunkt. Die Mentale Erschöpfung steigt wie beim normalen Erfolg.
- **Meisterlicher Erfolg:** 2 Bonuspunkte. Die Mentale Erschöpfung steigt wie beim normalen Erfolg.
- **Fröhlicher Erfolg:** 3 Bonuspunkte. Die Mentale Erschöpfung steigt wie beim normalen Erfolg.
- **Gescheitert:** Keine Wirkung. Die Mentale Erschöpfung steigt um (Erschwerung − Aura + Differenz zwischen Wurf und Probenwert) ÷ 2.
- **Patzer:** Keine Wirkung. Die Mentale Erschöpfung steigt um die volle Erschwerung.

Der Held verteilt die Bonuspunkte frei auf drei Verwendungen. Die Summe darf die Bonuspunkte des Ergebnisses nicht übersteigen, und jede Verwendung nutzt nur eine Stufe:

| Punkte | Wirkung | Wirkungsdauer | zusätzliche ME-Reduktion um |
|---|---|---|---|
| 1 | × 2 | × 2 | (Erschwerung − Aura) ÷ 4 |
| 2 | × 3 | × 3 | (Erschwerung − Aura) ÷ 6 |
| 3 | × 4 | × 4 | (Erschwerung − Aura) ÷ 8 |

## Die Erschwerung

Der Spieler wählt bei jedem Wirken frei eine Erschwerung. Sie macht die Probe schwerer und finanziert dafür die Wirkung der Fähigkeit. Er verteilt sie frei auf drei Verwendungen:

- die Wirkungsstärke,
- die Verkürzung der Vorbereitungszeit,
- die Verlängerung der Wirkungsdauer.

### Wirkungsstärke

Im Wirkungstext vieler Fähigkeiten steht ein Teil wie „+A pro+B“. Mit der zugeteilten Erschwerung ergibt er bei Erfolg:

```text
A × (zugeteilte Erschwerung ÷ B, abgerundet)
```

Nur volle Schritte zählen. Die Division rundet hier ab.

### Vorbereitungszeit und Wirkungsdauer

- **Vorbereitung:** N zugeteilte Erschwerungspunkte (N mindestens 2) teilen die Vorbereitungsdauer durch N.
- **Effektdauer:** Bei KI ist sie immer sofort. Eine Anlaufphase gibt es nie. Das Zeitmodell erklärt das Kapitel [[Magie-Wirkungsdauer-und-Konzentration]].
- **Wirkungsdauer:** N zugeteilte Erschwerungspunkte (N mindestens 2) multiplizieren die Wirkungsdauer mit N.

## Mentale Erschöpfung und Mentale Kapazität

Jedes Wirken belastet den Geist des Adepten. Zwei Werte halten das fest.

**Mentale Kapazität (MK)** ist die Obergrenze:

```text
MK = Willenskraft + Aura + Vitalität + Stufe des Helden + Mentale Kapazität (Sonderfertigkeit)
```

**Mentale Erschöpfung (ME)** ist der Wert, der sich ansammelt. Sie steigt bei jedem Wirken um:

```text
ME = (Erschwerung − Aura) ÷ 2
```

Die Division rundet auf die nächste ganze Zahl auf. Das Ergebnis ist mindestens 0. Liegt die Erschwerung bei oder unter der Aura, kostet das Wirken also keine ME, und der Wert wird nie negativ. Das Talent „Immer halbe ME“ halbiert jede ME-Berechnung. Auch diese Halbierung rundet auf. Die ME fällt einmal beim Wirken an. Sie fällt nicht in jeder Kampfrunde der Wirkungsdauer erneut an.

**Regeneration:** Die ME sinkt jede Minute um Aura ÷ 2 (auf die nächste ganze Zahl aufgerundet), bis auf 0.

**Überlauf:** Übersteigt die gesamte ME die MK, erleidet der Adept ME − MK als Schaden auf die Trefferzone Kopf. Der Adept erleidet den vollen Fehlbetrag. Anders als bei Manabrand wird er nicht halbiert. Der Schaden löst dieselbe Folgekette aus wie Manabrand: eine bedingungslose Selbstbeherrschungs-Probe, erschwert um den Schadensbetrag. Misslingt sie, folgt zusätzlich eine Probe auf den Mentalen Fokus (siehe [[Magie-Wirkungsdauer-und-Konzentration]]). Das Kapitel [[Treffer-und-Schaden]] erklärt die Trefferzonen.

## Ausdauerkosten

Das Wirken einer KI-Fähigkeit kostet zusätzlich [[Ausdauer]]. Die Kosten kommen zu den ME-Kosten hinzu und ersetzen sie nicht. Beide werden unabhängig voneinander verbraucht.

```text
Ausdauerkosten = gewählte Erschwerung ÷ 3
```

Die Division rundet auf die nächste ganze Zahl auf. Maßgeblich ist die Erschwerung, die der Spieler vor dem Wirken gewählt hat.

Das Aufrechterhalten kostet keine Ausdauer. Die Kosten fallen mit dem Ende der Vorbereitungsdauer an, wenn die entscheidende KI-Probe gewürfelt wird. Es spielt keine Rolle, wie die Probe ausgeht: Bei Erfolg jeder Stufe, bei Scheitern und bei Patzer fallen dieselben Ausdauerkosten an. Die Bonuspunkte verändern die gewählte Erschwerung nicht. Alle Ausdauerkosten stehen auch in der [[Ausdauerkosten-Uebersicht]].

## Unterbrechung während der Vorbereitung

Wird der Held in der Vorbereitungszeit über der [[Glossar#TS|Trefferschwelle]] getroffen und misslingt seine Selbstbeherrschungs-Probe, muss er eine Probe auf den Mentalen Fokus ablegen. Sie ist um die Verrissgröße der Selbstbeherrschungs-Probe erschwert (siehe [[Magie-Wirkungsdauer-und-Konzentration]]). Gelingt sie, behält er das Wirken. Misslingt sie, schlägt das Wirken fehl. Es kostet trotzdem ME, nämlich (Erschwerung − Aura) ÷ 2, mindestens 0.

## Stapelung und Geltungsbereich

- KI-Boni sind keine magischen Boni.
- Sie stapeln additiv mit Boni von Artefakten und von Spruchmagie auf denselben Wert.
- Mehrere KI-Quellen auf denselben Wert stapeln nicht untereinander. Es gilt nur der höchste anwendbare KI-Modifikator.
- Dieselbe KI-Fähigkeit kann nie zweimal gleichzeitig auf denselben Adepten wirken. Die schwächere Instanz verfällt.
- Bewusstlosigkeit beendet sofort alle aktiven KI-Fähigkeiten.

## Besondere Fähigkeiten

### Meister der Grundfertigkeiten

Diese Fähigkeit hat kein festes Ziel. Der Held bekommt eine wachsende Auswahl an Grundfertigkeiten (siehe [[Grundfertigkeiten]]). Bei FW 1 wählt er eine, bei FW 5 eine weitere, danach mit je 5 weiteren FW eine weitere:

```text
wählbare Grundfertigkeiten = 1 + (FW ÷ 5, abgerundet)
```

Die Division rundet hier ab. Bei FW 1, 4, 5, 9, 10 und 15 sind es 1, 1, 2, 2, 3 und 4 Grundfertigkeiten.

### Abhärtung

Die Lebensenergie (LE), die Abhärtung gewährt, wirkt als Leberschutz. Sie steht an derselben Stelle der Reihenfolge der Schadensberechnung wie jeder andere Leberschutz (siehe [[Treffer-und-Schaden]]).

## Rundung in diesem Kapitel

Abgerundet werden die Staffel „+A pro+B“ und die Zahl der wählbaren Grundfertigkeiten bei Meister der Grundfertigkeiten. Alle anderen Divisionen runden auf die nächste ganze Zahl auf, nämlich die Rechnungen der Mentalen Erschöpfung, die zusätzliche ME-Reduktion durch Bonuspunkte, die Regeneration, die Halbierung durch das Talent und die Ausdauerkosten. Die allgemeine Rundungsregel steht im Kapitel [[Wuerfeln-und-Proben]].

## Beispiele

**Die Staffel und die Mentale Erschöpfung.** Eine Fähigkeit wirkt „Willenskraft +2 pro+1 und Selbstbeherrschung +2 pro+1 und Trefferschwelle +1 pro+2“. Der Probenwert ist 30, die gewählte Erschwerung 14, und der Held teilt sie ganz der Wirkungsstärke zu. Das Wurfziel ist 30 − 14 = 16 (ohne vorherige ME). Bei Erfolg steigen Willenskraft und Selbstbeherrschung um je 2 × 14 = 28 und die Trefferschwelle um 1 × (14 ÷ 2) = 7. Die ME-Kosten sind (14 − Aura) ÷ 2. Bei Aura 7 sind das 4, mit dem Talent „Immer halbe ME“ 2.

**Gleichgewicht und Feingefühl.** Der Adept hat Magie 3, Aura 4, Geschicklichkeit 17 und FW 24. Er will ein Wurfziel von etwa 15, ein Wirken in 1 Kampfrunde und eine Wirkungsdauer von 60 Sekunden.

```text
Eigenschaftsbonus (Geschicklichkeit 17) = 17 ÷ 2, aufgerundet 9, minus 5 = 4
Probenwert = 24 + 4 + 2 × 3 − MBE (hier 0) = 34
Erschwerung für Wurfziel 15: 34 − E = 15, also E = 19
ME bei normalem Erfolg = (19 − 4) ÷ 2 = 7,5, aufgerundet 8
                         (mit dem Talent „Immer halbe ME“: 4)
Freie Aura = 4 (keine weiteren aktiven Effekte)

Vorbereitung: Basis 6 Sekunden, Ziel 1 Sekunde: 6 ÷ N = 1, also N = 6
Wirkungsdauer: Basis 10 Sekunden, Ziel 60 Sekunden: 10 × N = 60, also N = 6
Verbrauchte Erschwerung: 6 + 6 = 12 von 19, es bleiben 7 für die Wirkungsstärke

Geschicklichkeit +2 pro+1                   → +14   (2 × 7)
Fernkampf-Basiswerte +1 pro+2               → +3    (7 ÷ 2, abgerundet)
Initiative +1 pro+3                         → +2    (7 ÷ 3, abgerundet)
Freiklettern +0,006 m/s pro+1               → +0,042 m/s
```

**Ausdauerkosten.** Bei gewählter Erschwerung 12 und normalem Erfolg kostet das Wirken 12 ÷ 3 = 4 Ausdauer. Bei Erschwerung 19 und meisterlichem Erfolg sind es 19 ÷ 3 = 6,33, aufgerundet 7. Die 2 Bonuspunkte aus dem Erfolg ändern daran nichts. Bei Erschwerung 14 und einem Patzer sind es 14 ÷ 3, aufgerundet 5 Ausdauer. Dazu kommt die volle Erschwerung als ME-Anstieg. Beide Ressourcen sind unabhängig voneinander fällig.
