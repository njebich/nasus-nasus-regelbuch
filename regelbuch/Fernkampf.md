---
title: Fernkampf (FK)
aliases: [Fernkampf, FK, FK-Probe, Fernkampfprobe, FK-Erschwerungen, FK-Erschwerung, Fernkampf-Erschwernisse, Reichweitenband, Reichweitenmodifikator, Waffen-RW-Mod, Fernkampf-Patzer, FK-Patzertabelle, Ausdauerkosten Fernkampf, Ausdauerkosten Bögen, Ausdauerkosten Armbrüste, Ausdauerkosten Wurfwaffen, Ausdauerkosten Feuerwaffen, Spannen, Zielen, Nachladen]
status: entwurf
---

# Fernkampf (FK)

Im Fernkampf schießt oder wirft der Held auf ein Ziel. Wie gut ihm das gelingt, hängt von seinen Fähigkeiten, von der Waffe, von der Entfernung und von der Lage ab, in der er schießt. Dieses Kapitel beschreibt den Wert der Fernkampfprobe, die Reichweite der Waffen, die Erschwerungen, die Patzer und die Ausdauerkosten von Feuerwaffen, Bögen, Armbrüsten und Wurfwaffen. Wie ein Schuss im Kampf abläuft, steht in [[Fernkampf-im-Kampf]].

Teilungen und Malnahmen in den Formeln dieses Kapitels werden sofort aufgerundet, bevor der nächste Schritt folgt ([[Wuerfeln-und-Proben]]).

## Der Basiswert

Der Basiswert des Helden für den Fernkampf ist:

```text
Basiswert = (Sinnesschärfe + Geschicklichkeit + Wert der Waffenkategorie
             [+ Spezialisierung]) / 4
```

Der Basiswert hat keine Obergrenze von 20. Sinnesschärfe und Geschicklichkeit sind [[Eigenschaften]]. Die Waffenkategorie (zum Beispiel Bögen oder Armbrüste) ist ein Fernkampfwert, den der Held mit Steigerungspunkten kauft ([[Erfahrung-und-Steigerung]]). Eine Spezialisierung darunter kann hinzukommen.

Jeder Talentwert-Punkt einer Spezialisierung kostet nach demselben Rangprinzip wie im Nahkampf ([[Nahkampf]]) 10, 5 oder 3 Steigerungspunkte: 10 für die höchstwertige Spezialisierung unter derselben Hauptfertigkeit, 5 für die zweithöchste, 3 für jede weitere.

## Reichweite und Reichweitenmodifikator

Jede Fernkampfwaffe hat im Waffenkatalog sechs Reichweitenmodifikatoren, einen je Entfernungsband: 10, 30, 60, 100, 150 und 210 Meter. Es gilt das erste Band, das die Zielentfernung abdeckt: bis 10 m das Band 10, von 11 bis 30 m das Band 30, von 31 bis 60 m das Band 60, von 61 bis 100 m das Band 100, von 101 bis 150 m das Band 150 und von 151 bis 210 m das Band 210. Der Modifikator dieses Bandes wird zum Basiswert addiert:

```text
Normalwert = Basiswert + Reichweitenmodifikator
```

Ist der Eintrag eines Bandes das Zeichen „x“, ist ein Schuss auf diese Entfernung nicht möglich. Es wird kein Wurf angeboten.

Die Katalogwerte sind teils stark negativ, bei manchen Armbrüsten auf 100 Meter zum Beispiel −39. Ein negativer Normalwert bleibt ein regulärer, schwerer Probenwert. Eine besondere Regel, die ihn automatisch scheitern lässt, gibt es nicht. Die Werte der Feuerwaffen stehen bei den [[Feuerwaffen]]. Der Reichweitenwert der Munition fließt nicht in die Probe ein.

Trifft ein Schuss jenseits der Maximalreichweite (RW) der Waffe, sinkt der Schaden (SP) um (Entfernung − RW) / RW. Das Ergebnis wird aufgerundet. Näheres steht in [[Fernkampf-im-Kampf]].

### Beispiel für Bögen

Ein Kurzbogen (Goblin) hat bei 10 Meter den Modifikator +8, bei 60 Meter −13, bei 100 Meter −25 und bei 150 Meter „x“. Der Schütze hat den Basiswert 10.

- Bei 10 Meter ist der Normalwert 10 + 8 = 18.
- Bei 60 Meter ist er 10 − 13 = −3.
- Bei 100 Meter ist er 10 − 25 = −15.
- Bei 150 Meter ist kein Schuss möglich.

## Gute und meisterliche Erfolge

Die Schwelle des guten und des meisterlichen Erfolgs hängt vom Talent Fernkampfgeschick ab ([[Talente-die-Werte-veraendern]]). Beide werden genau einmal aus dem Normalwert berechnet, vor jeder Erschwerung und Behinderung:

```text
gut         = 1 + Normalwert / Teiler
meisterlich = 21 + Normalwert / 20
```

Der Teiler für den guten Erfolg ist 3 bei Fernkampfgeschick Stufe 2 und 4 bei Stufe 1. Ohne diese Stufen ist er nicht aktiv. Der Teiler 20 für den meisterlichen Erfolg gilt bei Fernkampfgeschick Stufe 3, sonst ist er nicht aktiv.

Der Wert für gut wird nur benutzt, wenn er größer als 1 ist. Der Wert für meisterlich wird nur benutzt, wenn er größer als 21 ist.

Beispiel: Fernkampfgeschick Stufe 2 und ein Normalwert von 18. Dann ist gut = 1 + 18 / 3 = 7.

## Erschwerungen im Fernkampf

Die FK-Erschwerungen und FK-Erleichterungen sind der gemeinsame Begriff für alle Abzüge und Zuschläge der Lage auf eine Fernkampfprobe, außer dem Reichweitenmodifikator der Waffe und der Behinderung. Sie fallen in diese acht Kategorien:

- Schütze: Lage. Sie besteht aus der Körperhaltung und aus der Angabe Freihand oder Aufgelegt. Beides sind zwei unabhängige Angaben, und beide sind erforderlich.
- Schütze: Bewegung
- Schütze: Zieldauer
- Ziel: Größe, einschließlich der Unterspalte für die Spezies
- Ziel: Bewegung
- Relative Bewegung im Fahrzeug, auch auf einem Reittier
- Sicht, einschließlich der Sichtmods und der Sichthilfen, die sie kontern
- Wetter

Wer joggt oder läuft, sprintet oder fällt, kann nicht zielen. Für ihn bleibt nur der direkte Schuss. Außer Atem darf der Schütze zielen, ebenso von einer Kutsche aus. Vom Pferd aus darf er nur zielen, wenn das Pferd im Schritt geht, nicht im Trab oder Galopp. Das Reitsystem folgt nach Version 1; bis dahin entscheidet der Meister.

Für jede Kategorie gilt der Wert der Tabelle genau, ohne Schätzung und ohne Zwischenwerte. Erschwerung und Erleichterung sind zwei getrennte Werte ohne Vorzeichen. Die Erschwerungen aller zutreffenden Kategorien werden addiert und abgezogen, die Erleichterungen aller zutreffenden Kategorien werden addiert und hinzugezählt.

### Sichthilfen ersetzen die Sicht-Erschwerung

Eine Sichthilfe hebt die Sicht-Erschwerung nicht auf, sondern ersetzt sie. Die kleinere Erschwerung der Sichthilfe tritt an die Stelle der Erschwerung des Sichtmods. Welche Sichthilfe welche Sichtmods mit welchem Ersatzwert kontert, steht in [[Aussehen-Schlaf-Sinne-und-Koerper]].

### Trefferzonen-Rerolls

Bei einer Erschwerung von +3 erhält der Schütze 2 Trefferzonen-Rerolls ([[Treffer-und-Schaden]]). Bei schlechter Sicht erhält er nur 1 Trefferzonen-Reroll pro +3. Als schlechte Sicht gelten Nebel, Nacht, Dämmerung, absolute Dunkelheit, geblendet und alle Wetter-Mods.

### Absolute Dunkelheit und Blindheit

Absolute Dunkelheit ist ein Zustand der Umgebung. Sie bedeutet nicht, dass der Held blind ist. Der persönliche Zustand blind ist ein eigenes Paket:

- Die Erschwerung beträgt 18 plus K-Mod. K-Mod ist der Malus aus den Komplementärsinnen ([[Aussehen-Schlaf-Sinne-und-Koerper]]).
- Sie gilt auf Nahkampf, Fernkampf und Zauber, außer bei Ziel Selbst oder Berührung.
- Im Fernkampf und in der Magie gilt dafür der Deutschuss.

Ein persönlich blinder Held ist immun gegen die gesamte Sicht-Kategorie der FK-Erschwerungen. Sein Fernkampf, Nahkampf und Zauber wird allein vom Paket Blind bestimmt, nicht zusätzlich.

Der Deutschuss ist die eigene Erschwerung für das Zielen auf einen Gegner, den der Held seit mindestens 1 Kampfrunde ([[Zeit-und-Spielablauf|Zeit]]) nicht gesehen hat. Sie beträgt 15. Ein sehender Held in absoluter Dunkelheit (Erschwerung 18) gegen einen solchen Gegner (Deutschuss 15) zählt nicht 33. Beide haben dieselbe Ursache: Das Ziel wird nicht wahrgenommen. Es gilt nur die schlechtere, hier also 18. Sicht und Sicht lassen sich nicht kombinieren. Damit landet ein sehender Held in absoluter Dunkelheit bei demselben Wert wie ein blinder (18, plus K-Mod, sobald der Zustand Blind gilt). Nur die Ursache ist eine andere: die Umgebung beim einen, der persönliche Zustand beim anderen.

## Die Fernkampfprobe

Die Fernkampfprobe wird mit W30 − W12 gewürfelt. Das Ergebnis liegt zwischen 0 und 29. Wie die Probe sonst läuft, entspricht dem Nahkampf: eine eigene Rechnung statt der allgemeinen Formel für Differenzproben ([[Wuerfeln-und-Proben]]).

### Der Wert der Probe

Von den beiden Behinderungen zählt nur die Körperliche Behinderung ([[Glossar#KBE|KBE]]). Die Mentale Behinderung zählt bei Angriffsproben im Nahkampf wie im Fernkampf nicht ([[Behinderung-und-Erschwernis]]).

Die KBE zieht direkt vom Wert ab, auch von den Schwellen für gut und meisterlich. Erschwerungen und Erleichterungen ändern nur den Normalwert. Die Schwellen für gut und meisterlich werden dadurch nicht neu berechnet, sondern nur nach oben begrenzt, und zwar gegen den gesenkten Normalwert.

```text
Normalwert nach Abzügen:
  n = Normalwert − Erschwerungen + Erleichterungen − KBE

gut nach KBE:         (größerer Wert aus 1 und (gut − KBE))
meisterlich nach KBE: (größerer Wert aus 21 und (meisterlich − KBE))

Schwelle gut        = kleinerer Wert aus (gut nach KBE) und (n / 2)
Schwelle meisterlich = kleinerer Wert aus (meisterlich nach KBE)
                       und (21 + (Schwelle gut − 1) / 2)
```

Der Basiswert hat keine Obergrenze. Ein Normalwert über 20 fängt deshalb KBE und Erschwerungen von selbst ab. Wirksam für die Probe ist aber höchstens 20. Was darüber liegt, geht verloren.

Beispiel: Ein Schütze hat den Basiswert 20. Bei 30 Meter hat die Waffe +6, der Normalwert ist 26. Er besitzt alle drei Stufen Fernkampfgeschick. Es gilt gut = 10 und meisterlich = 23. Die KBE ist 0.

- Erschwerung 9: n = 17. Die Schwelle für gut ist der kleinere Wert aus 10 und 9, also 9. Die Schwelle für meisterlich ist der kleinere Wert aus 23 und 25, also 23.
- Erschwerung 19: n = 7. Die Schwelle für gut ist der kleinere Wert aus 10 und 4, also 4. Die Schwelle für meisterlich ist der kleinere Wert aus 23 und 23, also 23.

### Erfolg und Misserfolg

Ergibt der Wurf höchstens n, gelingt die Probe. Ist das Ergebnis größer, misslingt sie. Gleich der Schwelle für gut ist ein guter, gleich der Schwelle für meisterlich ein meisterlicher Erfolg. Ein Ergebnis von 29 ist ein fröhlicher Erfolg, aber nur mit dem Vorteil Kind der Fröhlichkeit ([[Gaben-und-Schwaechen]]).

### Sehr niedriger Wert

Fällt der fertige Wert n nach Abzug von KBE und Erschwerungen auf 1 oder darunter, schiebt sich die Leiter nach hinten, genau wie bei der Attacke im Nahkampf ([[Nahkampf]]):

- Bei einem Wert von 1 liegt der gute Erfolg bei Wurf 21 und der meisterliche Erfolg bei Wurf 29. Einen fröhlichen Erfolg gibt es nicht.
- Bei einem Wert unter 1 liegt schon der Erfolg selbst bei Wurf 21 und der gute Erfolg bei Wurf 29. Meisterlicher und fröhlicher Erfolg entfallen.

### Das Ziel wehrt sich

Das Ziel kann Ausweichen, Parade oder eine Glücksprobe würfeln, um dem Schaden zu entgehen. Ausweichen und Parade kosten die Verteidiger-Aktion. Die Glücksprobe ist frei und beliebig oft möglich, aber höchstens einmal je einzelnem Angriff. Wie sich das Ergebnis zum Treffer verbindet, steht in [[Fernkampf-im-Kampf]].

### Patzer

Bei einem Patzer gilt die eigene Patzertabelle des Fernkampfs. Ein Patzer trifft das Ziel nie, gleich auf welche Entfernung der Schütze gezielt hat.

Gewürfelt wird ein W12, dazu kommt der Patzermodifikator der Waffe. Ergebnisse jenseits der Tabellenenden zählen wie die Endzeilen.

| Wurf | Wirkung |
|---|---|
| bis 2 | weit verfehlt |
| 3 bis 4 | keine Zündung: neu laden, doppelte Dauer |
| 5 bis 6 und 10 | Fehlzündung, Malus auf den Reichweitenmodifikator |
| 7 | Kugel bleibt stecken, Malus auf den Reichweitenmodifikator |
| 8 und 11 | Lauf beschädigt, Malus auf den Reichweitenmodifikator |
| 9 | Mechanismus zerstört, die Waffe ist unbrauchbar |
| 12 und mehr | Explosion der Pulverkammer: W15 TP, halb auf den Kopf, halb auf den rechten Arm |

Der Malus auf den Reichweitenmodifikator beschädigt die Waffe selbst, nicht die laufende Probe. Er wirkt ab dem nächsten Schuss und summiert sich bis zur Reinigung oder Reparatur. Es wird ein W6 gewürfelt. Je nach Zeile gibt es für jedes der sechs Bänder eine eigene Formel:

| Zeile | 10 m | 30 m | 60 m | 100 m | 150 m | 210 m |
|---|---|---|---|---|---|---|
| Fehlzündung | W6 − 5 | W6 − 4 | W6 − 3 | W6 − 2 | W6 − 1 | W6 |
| Kugel bleibt stecken | W6 − 3 | W6 − 2 | W6 − 1 | W6 | W6 + 1 | W6 + 2 |
| Lauf beschädigt | W6 × 1 | W6 × 2 | W6 × 3 | W6 × 4 | W6 × 5 | W6 × 6 |

Ist das Ergebnis einer Formel 0 oder kleiner, ist der Abzug an diesem Band 0. Der Reichweitenmodifikator wird nie besser. Der Abzug wird vom Reichweitenmodifikator mit seinem Vorzeichen abgezogen.

## Ausdauerkosten im Fernkampf

Jede Fernkampfhandlung kostet Ausdauer ([[Ausdauer]]). Die Kosten hängen von der Mindeststärke der Waffe ab, einem Wert aus dem Waffenkatalog. Jede Teilung wird aufgerundet.

### Feuerwaffen und Armbrüste

```text
Abschießen = Mindeststärke / 2
Nachladen  = Mindeststärke / 10
Zielen     = Mindeststärke / 20 pro Sekunde (nur freihändig gehalten)
```

Eine aufgelegte Waffe kostet beim Zielen nichts, gleich wie lange gezielt wird. Die Ausdauer regeneriert währenddessen normal ([[Ausdauer]]).

Bei Armbrüsten hängt die Mindeststärke an der Ladetechnik. Der Katalog führt für Hand-, Leichte, Mittelschwere und Schwere Armbrüste die Ladetechniken Hand, Geißfuß und Winde, jeweils mit eigener Mindeststärke. Repetier-Armbrüste haben Repetieren und Repetierer Nachladen. Für Abschießen und Zielen gilt die höchste Mindeststärke, die die Waffe über alle ihre Ladetechniken führt. Für Nachladen gilt die Mindeststärke der Ladetechnik, die der Held tatsächlich wählt.

### Bögen

```text
Be- und Entspannen = Mindeststärke
Spannen            = Mindeststärke / 4
Zielen             = Mindeststärke / 20 pro Sekunde
```

Be- oder Entspannen fällt einmalig an: Der Bogen wird einsatzbereit (aufgezogen) oder transportfähig (entspannt). Es gehört nicht zu jedem einzelnen Schuss.

Jeder Schuss beginnt mit Spannen. Das ist die erste Sekunde des Zielens, der Hüftschuss. Jede weitere Sekunde bis zum Abschuss kostet zusätzlich Zielen. Das Loslassen selbst kostet nichts. Es ist nur das Ende des Zielens, kein eigener Kostenpunkt.

### Wurfwaffen

```text
Zielen = Mindeststärke / 20 pro Sekunde
Werfen = Mindeststärke / 2
```

Werfen fällt am Ende des Zielens beim Wurf an.

### Beispiele zu den Ausdauerkosten

Feuerwaffen, freihändig gehalten:

- Schopkrotz (orkisch, Mindeststärke 12): Abschießen = 12 / 2 = 6. Nachladen = 12 / 10 = 1,2, aufgerundet 2. Zielen = 12 / 20 = 0,6, aufgerundet 1 pro Sekunde.
- Durass (orkisch, Mindeststärke 17): Abschießen = 17 / 2 = 8,5, aufgerundet 9. Nachladen = 17 / 10 = 1,7, aufgerundet 2. Zielen = 17 / 20 = 0,85, aufgerundet 1 pro Sekunde.
- Metnar (orkisch, Mindeststärke 21): Abschießen = 21 / 2 = 10,5, aufgerundet 11. Nachladen = 21 / 10 = 2,1, aufgerundet 3. Zielen = 21 / 20 = 1,05, aufgerundet 2 pro Sekunde.

Bögen, 6 Sekunden gezielt und dann geschossen:

- Kurzbogen (Gnom, Mindeststärke 4): Spannen in der ersten Sekunde = 4 / 4 = 1. Zielen = 4 / 20 = 0,2, aufgerundet 1 pro Sekunde, für die 5 weiteren Sekunden also 5. Zusammen kostet der Schuss 1 + 5 = 6.
- Schwarzfels-Bogen (Indianer, Mindeststärke 15): Spannen = 15 / 4 = 3,75, aufgerundet 4. Zielen = 15 / 20 = 0,75, aufgerundet 1 pro Sekunde, für 5 Sekunden 5. Zusammen 4 + 5 = 9.
- Kriegsbogen (orkisch, Mindeststärke 20): Spannen = 20 / 4 = 5. Zielen = 20 / 20 = 1 pro Sekunde, für 5 Sekunden 5. Zusammen 5 + 5 = 10.
- Derselbe Kriegsbogen, einmaliges Be- oder Entspannen außerhalb eines Schusses: 20.

Armbrüste, freihändig gehalten:

- Hand Armbrust (orkisch) mit den Ladetechniken Hand (Mindeststärke 13), Geißfuß (9) und Winde (7): Abschießen mit der höchsten Mindeststärke (Hand) = 13 / 2 = 6,5, aufgerundet 7. Zielen = 13 / 20 = 0,65, aufgerundet 1 pro Sekunde. Nachladen mit der gewählten Ladetechnik Geißfuß = 9 / 10 = 0,9, aufgerundet 1.
- Repetier Armbrust (orkisch) mit den Ladetechniken Repetieren (Mindeststärke 15) und Repetierer Nachladen (1): Abschießen mit Repetieren = 15 / 2 = 7,5, aufgerundet 8. Zielen = 15 / 20 = 0,75, aufgerundet 1 pro Sekunde. Nachladen mit Repetierer Nachladen = 1 / 10 = 0,1, aufgerundet 1.

Wurfwaffen, 3 Sekunden gezielt und dann geworfen (die Mindeststärken sind angenommene Beispielwerte):

- Messer (Mindeststärke 4): Zielen = 4 / 20 = 0,2, aufgerundet 1 pro Sekunde, für 3 Sekunden 3. Werfen = 4 / 2 = 2. Zusammen 3 + 2 = 5.
- Kurz- oder Wurfspeer (Mindeststärke 10): Zielen = 10 / 20 = 0,5, aufgerundet 1 pro Sekunde, für 3 Sekunden 3. Werfen = 10 / 2 = 5. Zusammen 3 + 5 = 8.
- Kleine Axt (Mindeststärke 14): Zielen = 14 / 20 = 0,7, aufgerundet 1 pro Sekunde, für 3 Sekunden 3. Werfen = 14 / 2 = 7. Zusammen 3 + 7 = 10.
