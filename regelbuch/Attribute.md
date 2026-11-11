---
title: Attribute (Att)
aliases: [Attribute, Attribut, Att, Attributsprobe, Attribut-Probe, Aura, Glück, Karma, Magie, Vitalität, Weisheit, Glücksprobe, Aura-Probe, Basismaximum]
status: entwurf
---

# Attribute (Att)

Der Held hat sechs Attribute: Aura, Glück, Karma, Magie, Vitalität und Weisheit. Fünf davon kauft er mit Entwicklungspunkten. Die Weisheit steigt von selbst mit dem Kreis. Aus den Attributen entstehen viele weitere Werte des Helden, zum Beispiel Mana, [[Stufe-Kreis-Macht-und-Rerolls|Macht]], [[Ausdauer]], Gesundheit, Ausweichen, Trefferschwelle und Karma-Pool-Punkte. Wer zaubern, Psi wirken oder KI einsetzen will, braucht außerdem Aura und Magie (siehe unten).

Attribute und [[Eigenschaften]] sind verschiedene Werte. Die Eigenschaften sind zehn eigene Werte mit eigener Kostenkurve und eigenen Höchstwerten. Die Attribute haben eine andere Kostenkurve und ihre eigene, nach Kreis gestaffelte Obergrenze.

## Die Weisheit

Die Weisheit wird nicht gekauft. Sie beträgt immer:

```text
Weisheit = Kreis + 1
```

Ein Held mit Kreis 0 hat Weisheit 1. Die Weisheit kostet keine Entwicklungspunkte, hat kein eigenes Höchstmaß und unterliegt nicht dem Höchstwert der gekauften Attribute. Den Kreis erklärt das Kapitel [[Stufe-Kreis-Macht-und-Rerolls]].

## Kauf und Kosten

Der Held kauft Aura, Glück, Karma, Magie und Vitalität mit Entwicklungspunkten ([[Glossar#EP|EP]]). Der Wert ist immer eine ganze Zahl. Alle Kosten sind ganzzahlig, es wird nie gerundet.

Die Kosten sind für alle fünf Attribute gleich und werden aufsummiert:

```text
Gesamtkosten(Wert) = 10 × Wert² + 70 × Wert
Preis für den nächsten Schritt (Wert → Wert + 1) = 80 + 20 × Wert
```

| Wert | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Preis des Schritts | – | 80 | 100 | 120 | 140 | 160 | 180 | 200 | 220 |
| Gesamtkosten (EP) | 0 | 80 | 180 | 300 | 440 | 600 | 780 | 980 | 1200 |

Beispiele: Ein Held, der sein Attribut auf 1 kauft, zahlt 80 EP. Auf 4 kostet es insgesamt 440 EP, auf 7 insgesamt 980 EP. Der Schritt von 6 auf 7 kostet 80 + 20 × 6 = 200 EP.

Die gekauften Attribute zählen zu den ausgegebenen EP des Helden ([[Erfahrung-und-Steigerung]]). Boni aus Artefakten verändern die Kosten nicht.

### Der Höchstwert

Wie hoch der Held ein gekauftes Attribut kaufen darf, hängt vom Kreis ab:

```text
Höchstwert = 4 + Kreis, höchstens aber 7
```

| Kreis | Höchstwert |
|---:|---:|
| 0 | 4 |
| 1 | 5 |
| 2 | 6 |
| ab 3 | 7 |

Maßgeblich ist der Kreis des Helden, nicht seine Stufe. Der Höchstwert gilt für jede Spezies gleich, für Spielercharaktere wie für Nichtspielercharaktere (NSC). Anders als bei den Eigenschaften hängt er von keinem Volk ab.

Ein Held mit Kreis 0 kann sein Attribut also höchstens auf 4 kaufen. Das kostet insgesamt 440 EP.

Der Kreis kann nur steigen. Ein regulär gekaufter Wert liegt deshalb nie über dem später geltenden Höchstwert.

### Das Talent für das Höchstmaß

Für jedes gekaufte Attribut gibt es ein eigenes Talent, das nur das Maximum dieses einen Attributs um 1 anhebt. Es kostet 18 Talentpunkte ([[Glossar#TaP|TaP]]) und ist erst ab Kreis 3 kaufbar. Unter Kreis 3 kann der Held es nicht kaufen. Mit dem Talent liegt der Höchstwert bei 8, und Wert 8 kostet 1200 EP, wie die Tabelle zeigt. Für die Weisheit gibt es das Talent nicht. Die Talente stehen im Kapitel [[Talente-die-Maxima-anheben]].

## Wer die Attribute kauft

Die Kauf- und Obergrenzregeln gelten für Spielercharaktere und für NSC einer spielbaren Spezies. Gehört eine Figur keiner spielbaren Spezies an, ist sie eine Kreatur. Ihre Attributwerte vergibt der Meister frei. Es gibt keinen Zwischenfall, in dem ein NSC einer nicht spielbaren Spezies handvergebene Attribute hat. Untote sind ebenfalls ausgenommen: Ihre Werte werden frei vergeben, gleichgültig, ob sie als NSC oder als Kreatur geführt werden.

## Zugang zu Karma und Magie

### Karma

Karma ist bei der Erschaffung verborgen und bleibt auf 0, bis der Held Geweihter oder Paladin ist. Dafür braucht er die erste Stufe der Geweihten-Kette seiner Religion (siehe [[Religion]]). Diese Stufe hebt die Sperre. Sie setzt nicht voraus, dass der Held schon Karma über 0 hat.

Verliert der Held die letzte Stufe der Kette, ist Karma wieder gesperrt. Das geschieht, wenn er im Charakterbogen die Religion wechselt oder wenn der Meister ihm die Stufe entzieht. Beides ist nur außerhalb einer Session möglich. Der gekaufte Wert von Karma wird dann auf 0 gesetzt, und der Held bekommt die dafür ausgegebenen EP zurück.

Ein göttliches Karma-Artefakt bleibt davon unberührt. Ein Held, der kein Geweihter ist, erhält das wirksame Karma des Artefakts voll, einschließlich seines Beitrags zu den Karma-Pool-Punkten und zur Macht.

### Aura und Magie

KI, Psi und Spruchmagie setzen voraus, dass sowohl die gekaufte Magie als auch die gekaufte Aura über 0 liegen. Es zählen die gekauften Werte. Ein Artefakt, das Aura oder Magie erhöht, erfüllt diese Voraussetzung nicht. Die Kapitel dazu: [[KI]], [[Psi]] und [[Spruchmagie]].

## Glück bei der Erschaffung

Die Erschaffung eines Spielercharakters schlägt für Glück den Wert 1 vor und füllt ihn vor. Das ist kein Mindestwert und keine Gratisgabe: Die 80 EP für den Wert 1 zählen wie jeder Kauf, und der Spieler darf Glück auf 0 senken. Für die anderen vier gekauften Attribute gibt es keinen Vorschlag.

## Magische und göttliche Erhöhungen

Wirken mehrere magische oder göttliche Erhöhungen gleichzeitig auf dasselbe Attribut, zählt nur die höchste positive. Alle diese Erhöhungen teilen sich eine Stapelungsgruppe. Attributs-Artefakte gelten als göttlich (siehe [[Artefakte]]).

Eine solche Erhöhung wirkt in Formeln, aber nicht in den Regelgrenzen:

- Formeln verwenden den gekauften Wert plus die höchste anwendbare Erhöhung.
- Höchstwerte, Sperren und Voraussetzungen verwenden den gekauften Wert ohne Erhöhung.

Die Erhöhung ändert weder den gekauften Wert noch dessen Kosten. Der wirksame Wert kann deshalb über dem Höchstwert liegen, aber nur in Formeln.

Auch die Weisheit wird so behandelt. In Formeln wie Mana und Macht beträgt sie Kreis + 1 plus die höchste anwendbare Erhöhung. Für Regelgrenzen wie den Lerngrad der Spruchmagie gilt nur Kreis + 1. Ein Held mit Kreis 3 und einem Artefakt, das die Weisheit um 2 erhöht, rechnet in der Macht mit Weisheit 6. Für den Lerngrad zählt nur Weisheit 4.

## Rückgabe

Außerhalb einer laufenden Session kann der Held gekaufte Attribute jederzeit zurückgeben. Er bekommt die aufsummierten EP genau erstattet. Während einer Session ist die Rückgabe gesperrt.

Der Meister entzieht keine EP und senkt keinen gekauften Wert direkt. Eine Senkung in einer Szene ist ein Abzug auf den gekauften Wert, kein neuer Kaufwert. Gewährt der Meister dem Helden einen Nachteil, wirkt dieser mit seinem vollen EP-Effekt: Die verfügbaren EP des Helden steigen um die volle Gutschrift. Die gesamten Abenteuerpunkte ändern sich dadurch nie.

Jede Rückgabe wird protokolliert und am Tisch angesagt.

## Die Attributsprobe

Bei einer Attributsprobe würfelt der Held auf den Wert eines seiner sechs Attribute. Es gibt sie für Aura, Glück, Karma, Magie, Vitalität und Weisheit. Jede dieser sechs Proben ist gleichrangig.

Der Probenwert ist der Rohwert des Attributs:

```text
Probenwert = Attribut
```

Weder eine Eigenschaft noch ein Eigenschaftsbonus, eine Fertigkeit oder eine Spezialisierung gehen ein. Auch eine Behinderung wird nicht abgezogen: Attributsproben sind gegen Behinderung immun. Eine weitere Sonderregel zur Erschwernis gibt es nicht. Eine äußere Erschwernis oder Erleichterung wird wie bei jeder Einfachen Probe verrechnet (siehe [[Behinderung-und-Erschwernis]]).

Gewürfelt wird W30 − W12. Der Würfelwurf und die Auswertung folgen der allgemeinen Probe (siehe [[Wuerfeln-und-Proben]]):

```text
Ergebnis = Differenz − Erschwerung
```

Ein positives Ergebnis heißt geschafft, ein negatives gescheitert. Es ist eine Einzelprobe, keine Gegenprobe.

Die Erfolgsstufen sind Patzer, Fehlschlag, Erfolg, guter Erfolg, meisterlicher Erfolg und fröhlicher Erfolg. Die Schwellen sind fest bei 1, 21 und 29. Kein Talent verschiebt sie.

Manche Zustände verbieten Proben, zum Beispiel Bewusstlos. Attributsproben sind davon ausgenommen. Der Held kann sie auch dann würfeln.

### Die Glücksprobe

Die Glücksprobe ist die am besten belegte Attributsprobe. Der Held kann sie als Verteidigung gegen Fernkampf- und Magie-Angriffe einsetzen, gleichrangig neben Ausweichen und Parade. Für sie gilt:

- Sie kostet nichts, auch keine AK ([[Glossar#AK|Aktionskosten]]). Ausweichen ([[Glossar#AW|AW]]) und Parade ([[Glossar#PA|PA]]) kosten den Verteidiger dagegen AK.
- Der Held kann sie beliebig oft pro Kampfrunde würfeln.
- Gegen denselben einzelnen Angriff aber nur einmal.
- Auch als Verteidigung bleibt sie eine Einzelprobe des Verteidigers, keine Vergleichsprobe zwischen zwei Seiten.

Ein Schütze zielt auf den Helden. Der Spieler würfelt eine Glücksprobe gegen diesen Schuss. Gegen denselben Schuss kann er sie nicht noch einmal würfeln. Schießt der Gegner erneut, ist das ein neuer Angriff, und der Spieler darf wieder würfeln.

### Die Aura-Probe

Die Spruchmagie verwendet Proben auf die Aura. Beim Zauber Subjektives Manaloch (Antimagie, Grad 6) verliert das Ziel sein gesamtes Mana, außer es besteht die Aura-Probe. Dann verliert es nur die Hälfte seines aktuellen Manas, aufgerundet. Beispiel: Bei 41 Mana sind es 21 Verlust, es bleiben 20. Diese Probe läuft als gewöhnliche Attributsprobe auf den Rohwert der Aura, ohne die Sonderregeln der Glücksprobe.

Karma, Magie, Vitalität und Weisheit stehen ebenso als eigene Attributsprobe zur Verfügung. Ein Meister kann eine Erschwernis ansagen, etwa für eine erschwerte Glücksprobe. Das ist eine Entscheidung des Meisters im Einzelfall, keine feste Regel.
