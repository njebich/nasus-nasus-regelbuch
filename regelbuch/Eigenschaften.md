---
title: Eigenschaften (Eig)
aliases: [Eigenschaften, Eigenschaft, Eig, Eigenschaftsbonus, Eigenschaftsboni, Eigenschaftsprobe, Eigenschafts-Probe, Maximaltalent, Artgrenze, Intelligenz, Mut, Sinnesschärfe, Willenskraft, Ausstrahlung, Athletik, Geschicklichkeit, Konstitution, Schnelligkeit, Stärke]
status: entwurf
---

# Eigenschaften (Eig)

Der Held hat zehn Eigenschaften. Er kauft sie mit Steigerungspunkten, und aus jeder Eigenschaft ergibt sich ein Eigenschaftsbonus, mit dem viele Formeln rechnen. Auf jede Eigenschaft kann der Held auch würfeln.

Fünf Eigenschaften sind geistig:

- Intelligenz
- Mut
- Sinnesschärfe
- Willenskraft
- Ausstrahlung

Fünf sind körperlich:

- Athletik
- Geschicklichkeit
- Konstitution
- Schnelligkeit
- Stärke

Eigenschaften sind nicht dasselbe wie [[Attribute]]. Die Attribute sind sechs eigene Werte (Aura, Glück, Karma, Magie, Vitalität, Weisheit) mit eigener Kostenkurve und eigenem Höchstwert.

Für alle zehn Eigenschaften gelten dieselben Regeln für Kosten, Grenzen und Erhöhungen. Jede Eigenschaft unterscheidet sich nur durch ihren Namen und ihre Grenzen je Volk.

## Kauf und Kosten

Der Held kauft eine Eigenschaft mit Steigerungspunkten ([[Glossar#SP|SP]]). Der gekaufte Wert liegt zwischen 0 und 64 und ist immer eine ganze Zahl. Es wird nie gerundet.

Die Kosten sind für alle zehn Eigenschaften gleich. Jeder Schritt kostet:

```text
Schritt 1 bis 11:   je 30 SP
ab Schritt 12:      Kosten des Schritts davor + 3
                    (gleichbedeutend: 3 × Schrittnummer − 3)
Gesamtkosten(Wert) = Summe aller Schritte von 1 bis Wert
```

Beispiele:

```text
Wert 11:  330 SP   (11 × 30)
Wert 31:  1560 SP
Wert 64:  6213 SP
```

Der Kauf einer Eigenschaft hängt an keiner Sperre und keiner Freischaltung. Bei den Attributen ist das anders (siehe [[Attribute]]).

## Grenzen nach Volk und Rolle

Für jedes Volk und jede Eigenschaft gibt es drei Werte:

- das Erschaffungsminimum,
- das Erschaffungsmaximum,
- das Maximum ab Kreis 3. Es beträgt bei jedem Volk und jeder Eigenschaft 31.

Die vollständige Tabelle mit allen elf Völkern und zehn Eigenschaften steht im Kapitel [[Spezies]].

Welche Grenze wie bindet, hängt von der Rolle der Figur ab.

### Spielercharakter

Das Erschaffungsminimum des Volkes ist verbindlich.

Das Erschaffungsmaximum des Volkes ist verbindlich, solange der Held unter Kreis 3 ist. Ab Kreis 3 gilt als verbindliches Maximum:

```text
31 + anwendbare Maximaltalente
```

Diese Umstellung gilt sofort, wenn der Held Kreis 3 erreicht. Den Kreis erklärt das Kapitel [[Stufe-Kreis-Macht-und-Rerolls]].

### Nichtspielercharakter, nicht untot

Bei einem Nichtspielercharakter (NSC), der nicht untot ist, ist das Erschaffungsminimum des Volkes verbindlich. Das Maximum ist dasselbe wie beim Spielercharakter: unter Kreis 3 das Erschaffungsmaximum, ab Kreis 3 dann 31 + Maximaltalente.

### Kreaturen

Kreaturen sind von diesen Grenzen ausgenommen. Ihre Werte vergibt der Meister frei.

Jede Figur gehört entweder einem spielbaren Volk an oder nicht. Gehört sie einem spielbaren Volk an, ist sie Spielercharakter oder Nichtspielercharakter und folgt den Grenzen oben. Gehört sie keinem an, ist sie eine Kreatur mit frei vergebenen Werten. Einen Zwischenfall, in dem ein Nichtspielercharakter eines nicht gelisteten Volkes handvergebene Werte ohne Grenzen hat, gibt es nicht.

### Untote

Untote sind ebenfalls ausgenommen, ihre Werte werden frei vergeben. Das gilt, gleichgültig ob ein Untoter als Nichtspielercharakter oder als Kreatur geführt wird.

## Das Talent für das Maximum

Zu jeder Eigenschaft gibt es ein Talent, das ihr Maximum um 5 erhöht. Es kostet 6 Talentpunkte ([[Glossar#TaP|TaP]]) und ist erst ab Kreis 3 kaufbar. Unter Kreis 3 kann es der Held nicht kaufen, und seine Erhöhung gilt deshalb nie unter Kreis 3. Die Talente stehen im Kapitel [[Talente-die-Maxima-anheben]].

Trägt der Held für eine Eigenschaft den Nachteil Schlechte Eigenschaft, ist das Talent für sie gesperrt. Nach dem Verkauf des Nachteils ist es wieder kaufbar.

## Schlechte Eigenschaft

Der Nachteil Schlechte Eigenschaft ersetzt das Maximum der Eigenschaft durch einen festen Deckel: 7 unter Kreis 3, 9 ab Kreis 3. Das Erschaffungsminimum des Volkes bleibt wirksam, wird aber nach oben auf den Deckel begrenzt. Der Erschaffungswert liegt dann zwischen dem kleineren von Minimum und Deckel und dem Deckel. Bei einem NSC mit hohem Minimum ist der Deckel deshalb der verbindliche Zielwert. Alle Einzelheiten stehen im Kapitel [[Gaben-und-Schwaechen]].

Der Deckel beschränkt nur den Kauf, das reguläre Maximum und das Talent. Magische oder göttliche Erhöhungen, die nur in Formeln wirken, bleiben davon unberührt.

## Magische und göttliche Erhöhungen

Wirken mehrere magische oder göttliche Erhöhungen gleichzeitig auf dieselbe Eigenschaft, zählt nur die höchste einzelne. Sie teilen sich eine Stapelungsgruppe.

Eine solche Erhöhung wirkt in Formeln, aber nicht in den Regelgrenzen:

- Formeln verwenden den gekauften Wert plus die höchste anwendbare Erhöhung.
- Voraussetzungen, Maxima, Zugangsschwellen und andere Regelgrenzen verwenden den gekauften Wert ohne Erhöhung.

Die Erhöhung ändert weder den gekauften Wert noch dessen Kosten. Auch Abzüge durch den Meister wirken als Effekte auf den gekauften Wert. Sie überschreiben ihn nicht.

Dieselben Regeln gelten für die Attribute.

## Rückgabe

Außerhalb einer laufenden Session kann der Held gekaufte Eigenschaftspunkte jederzeit zurückgeben. Er bekommt die aufsummierten SP voll erstattet. Während einer Session ist die Rückgabe gesperrt. Dieselbe Regel gilt für Attribute, Talentpunkte und Steigerungspunkte (siehe [[Erfahrung-und-Steigerung]]).

Jede Rückgabe wird protokolliert und am Tisch angesagt.

## Der Eigenschaftsbonus

Der Eigenschaftsbonus ist eine abgeleitete Zahl. Viele Formeln rechnen mit ihm statt mit dem rohen Wert der Eigenschaft. Das betrifft [[KI]], [[Psi]], [[Spruchmagie]], die Standardprobe der [[Wissens-Handwerks-und-Kulturfertigkeiten|Wissens-, Handwerks- und Kulturfertigkeiten]], Mana, [[Stufe-Kreis-Macht-und-Rerolls|Macht]], Gutes und Meisterliches Ausweichen ([[Nahkampf]]), Freiklettern und Geschirrklettern ([[Klettern-und-Schwimmen]]). Es gibt weitere Verwendungen. Außerhalb solcher Formeln hat der Bonus keine eigene Bedeutung.

Es gibt zehn Eigenschaftsboni, einen je Eigenschaft. Alle folgen derselben Formel. Kein Bonus hat eigene Kosten, ein eigenes Minimum oder Maximum oder eine eigene Herkunft. Gekauft werden nur die Eigenschaften selbst. Auch die Grenzen und das Talent für das Maximum gelten nur für sie.

### Die Formel

```text
Eigenschaftsbonus = (Eigenschaft ÷ 2, auf die nächste ganze Zahl aufgerundet) − 5
```

Die Eigenschaft ist ihr wirksamer Wert, also nach allen Effekten. Bei Kreaturen ist es der frei vergebene Wert. Das Aufrunden geschieht einmal, vor dem Abzug von 5. Wie das Regelwerk überall rundet, steht im Kapitel [[Wuerfeln-und-Proben]].

Ein Effekt kann den Bonus nur verändern, indem er die Eigenschaft selbst verändert. Der Bonus wird danach aus dem neuen wirksamen Wert berechnet.

Die Formel gilt für jeden gleich: Spielercharaktere, NSC, Kreaturen und Untote. Keiner von ihnen hat einen Bonus, der von seiner Eigenschaft abweicht.

### Negative Boni

Der Bonus hat keine Untergrenze und keine Obergrenze. Eine niedrige Eigenschaft ergibt einen negativen Bonus. Er wird unverändert übernommen und nicht auf 0 gesetzt.

### Beispiele

Der Held hat Athletik 14. Die Hälfte ist 7, der Bonus ist 7 − 5 = 2.

Der Held hat Mut 9. Die Hälfte ist 4,5, aufgerundet 5. Der Bonus ist 5 − 5 = 0.

Der Held hat Stärke 5. Die Hälfte ist 2,5, aufgerundet 3. Der Bonus ist 3 − 5 = −2.

Weitere Werte am Rand des Bereichs: Eigenschaft 0 ergibt −5, Eigenschaft 64 ergibt 32 − 5 = 27.

## Die Eigenschaftsprobe

Bei einer Eigenschaftsprobe würfelt der Held auf den Rohwert einer seiner zehn Eigenschaften. Der Probenwert ist:

```text
Probenwert = Eigenschaft − Behinderung
```

Es zählt der Rohwert der Eigenschaft, nicht der Eigenschaftsbonus.

Welche Behinderung (BE) abgezogen wird, ergibt sich von selbst aus der gewählten Eigenschaft. Bei einer geistigen Eigenschaft zählt die mentale Behinderung (MBE), bei einer körperlichen die körperliche Behinderung (KBE). Das Kapitel [[Behinderung-und-Erschwernis]] erklärt beides.

Gewürfelt wird W30 − W12. Der Würfelwurf und die Auswertung folgen der allgemeinen Probe (siehe [[Wuerfeln-und-Proben]]):

```text
Ergebnis = Differenz − Erschwerung
```

Ein positives Ergebnis heißt geschafft, ein negatives gescheitert. Es ist eine Einzelprobe, keine Gegenprobe.

Die Erfolgsstufen sind Patzer, Fehlschlag, Erfolg, guter Erfolg, meisterlicher Erfolg und fröhlicher Erfolg. Die Schwellen sind fest bei 1, 21 und 29. Kein Talent verschiebt sie. Bei der Eigenschaftsprobe gilt das genauso wie bei der Attributsprobe.

Manche Zustände verbieten Proben, zum Beispiel Bewusstlos. Eigenschaftsproben sind davon ausgenommen. Der Held kann sie auch dann würfeln.

### Beispiel: Beherrschung widerstehen

Das Ziel eines Beherrschungs-Zaubers würfelt in einem festen Abstand eine Eigenschaftsprobe, zum Beispiel auf Willenskraft. Der Abstand hängt vom Zauber ab, zum Beispiel alle 10 Sekunden. Zur Eigenschaft kommt die eigene Macht des Ziels, abgezogen wird die Macht des Magiers:

```text
Probenwert = Eigenschaft + Macht des Ziels − Macht des Magiers
```

Ein Erfolg beendet den Zauber sofort. Hat der Zauber mehrere Ziele zugleich, zählt für jedes Ziel die Summe der Macht-Werte aller Ziele. Die Probe jedes einzelnen Ziels wird also mit der Zahl der Ziele leichter. Was Macht ist, steht im Kapitel [[Stufe-Kreis-Macht-und-Rerolls|Stufe, Kreis, Macht und Rerolls]].

Ein Magier mit Macht 20 beherrscht gleichzeitig zwei Ziele mit Macht 6 und Macht 4. Für jedes Ziel zählt die Summe 10, der Probenwert ist also die Eigenschaft + 10 − 20 = Eigenschaft − 10. Würde er nur das erste Ziel beherrschen, wäre er die Eigenschaft + 6 − 20 = Eigenschaft − 14.

Auch wenn das Ziel die Probe immer wieder würfelt und sie gegen den Magier erschwert ist, bleibt es eine Einzelprobe des Ziels. Es ist keine Vergleichsprobe.
