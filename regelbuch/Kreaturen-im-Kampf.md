---
title: Kreaturen im Kampf
aliases: [Kreaturen im Kampf, Kreaturen-im-Kampf, Kreaturen, Kreaturen-Trefferzonen, Untote im Kampf, Untoten-Kampfunfähigkeitsschwelle, UK, Gespenst, niedergestreckt, Trefferzonen bei Kreaturen, Körperteil, Körperteile, Zonenliste, Krit-Zeile, Normalzeile, Rohgewicht, Größenstufe, Segmentnaht, Krit-Dichte, Hexfeld-Tabelle, LE-Faktor, Gesundheit, Maximale Gesundheit, LE-Maximum, Einteiliger Rumpf, Kern, Glied, Angeschlossene Zone, Weiterleitung bei Kreaturen, Magiekorpus, Magiekonstrukt, Dämonide, Geist, Eine-Zone-Kreatur, Blutet, Skelettkategorie, Endoskelett, Exoskelett, Flügelflug, Flugsperre, Flügelverlust, Absturz]
status: entwurf
---

# Kreaturen im Kampf

Jede Kreatur bekommt für jedes Hexfeld, das sie belegt, eine eigene Trefferzonen-Tabelle mit W100. Sie entsteht aus den Körperteilen, die in diesem Feld liegen. Die Tabelle des Helden ist die Vorlage ([[Treffer-und-Schaden]]). Dieses Kapitel sagt, wie die Tabelle einer Kreatur aufgebaut wird, wie viel Lebensenergie ihre Zonen haben, wohin überschüssiger Schaden geht, welche Kreaturen bluten und brechen, wann eine Kreatur nicht mehr fliegen kann und wie ihr Sturz verläuft. Der Held und der Nichtspielercharakter (NSC) folgen denselben Rechnungen, soweit nichts anderes steht.

Teilungen werden nach der allgemeinen Rundungsregel gerundet ([[Wuerfeln-und-Proben|Würfeln und Proben]]). Wo eine Rechnung abweicht, steht es an der Stelle.

## Körperteile und Zonen

Ein Körperteil ist eine anatomische Einheit mit eigener Zone und eigener Lebensenergie ([[Glossar#LE|LE]]). Beispiele sind Kopf, Oberleib, Unterleib, Rumpf, Arm, Bein, Flügel, Schwanz und Tentakel. Jedes Exemplar zählt für sich: Acht Arme sind acht Zonen.

**Körperteiltypen.** Jedes Körperteil gehört genau einem der fünf Typen Kopf, Oberleib, Unterleib, Arm oder Bein. Die Bauform des Körperteils, die der Meister bei der Kreatur festlegt, bestimmt den Typ. Flügel und Tentakel sind vom Typ Arm, wenn die Bauform sie so zuordnet.

**Einteiliger Rumpf.** Eine Kreatur kann Oberleib und Unterleib bewusst zu einer einzigen Zone mit einer gemeinsamen LE zusammenlegen. Das ist der einteilige Rumpf. Ohne diese Entscheidung hat die Kreatur getrennte Zonen für Oberleib und Unterleib.

**Die Zonenliste eines Hexfelds.** Für das angegriffene Hexfeld ([[Bewegung]]) bilden alle Körperteile, die diesem Feld zugeordnet sind, samt ihren Zusatzzeilen die Zonenliste. Mehrfach vorhandene Körperteile zählen mehrfach. Ein Körperteil, das mehreren Feldern zugeordnet ist, bleibt eine Zone mit einer LE. Es steht in jeder dieser Tabellen mit vollem Gewicht. Wo es im Feld liegt und ob es dort erreichbar ist, ändert die Gewichtung nicht. Jede Extremität einer Kreatur, die mehrere Felder belegt, gehört mindestens einem Feld an. Eine Kreatur, bei der eine Extremität keinem Feld zugeordnet ist, ist ungültig.

**Zeilen.** Jede Zeile der Tabelle ist ein W100-Bereich. Jedes Körperteil hat eine Normalzeile. Dazu kann es Krit-Zeilen haben. Das sind Zeilen mit einer Zusatzwirkung, wie beim Auge, beim Hals oder beim Knie des Helden. Eine Krit-Zeile gehört zu einem Körperteil und teilt dessen LE und Zonengruppe. Ein Körperteil ohne Krit-Zeile trägt nur seine Normalzeile. Eine Kreatur mit nur einem Körperteil hat die Normalzeile 1–97 und kein Krit. Trägt ein Körperteil auf einem Feld Krit-Zeilen, die dort nicht erreichbar sind, bleibt es vollständig in der Tabelle dieses Felds.

## Die Tabelle aufbauen

### Rohgewichte

Jede Zeile hat vor dem Ausgleich ein Rohgewicht. Das Rohgewicht eines Körperteils ist N + K. N ist das Rohgewicht der Normalzeile, K die Summe der Rohgewichte seiner Krit-Zeilen. Die Standardwerte sind die des Helden:

- **Kopf.** Normalzeile 8, Auge 1, Hals 2. Zusammen 11.
- **Oberleib.** Normalzeile 21, Herz und/oder Lunge 2, dazu 1 für jedes angesetzte Glied mit Gliedsperre. Zusammen 23 plus die Glieder.
- **Unterleib.** Normalzeile 10, Organ 5. Zusammen 15.
- **Arm.** Normalzeile 10, Ellenbogen 1, Hand 2. Zusammen 13.
- **Bein.** Normalzeile 7, Knie 2, Fuß 1. Zusammen 10.
- **Einteiliger Rumpf.** Normalzeile 31, Herz und/oder Lunge 2, Organ 5, dazu 1 für jedes angesetzte Glied mit Gliedsperre. Zusammen 38 plus die Glieder.

Die Summe der Körperteile des Helden (Kopf, Oberleib, Unterleib, zwei Arme, zwei Beine) beträgt 97.

Das Rohgewicht jeder Krit-Zeile darf je Zeile ganzzahlig zwischen 1 und 5 frei gesetzt werden. Der Standard ist der Wert aus der Liste. Ein Kopf mit normaler Normalzeile (8) und dem Hals auf Rohgewicht 5 hat zum Beispiel die Rohgewichte 8 (Kopf), 1 (Auge) und 5 (Hals).

**Größenstufe.** Die Größenstufe eines Körperteils (klein, normal, groß) multipliziert nur das Rohgewicht seiner Normalzeile, mit 0,5, 1 oder 1,5. Die Faktoren gelten für alle Körperteiltypen gleich. Das Rohgewicht einer Krit-Zeile hängt nicht von der Größenstufe ab.

Ein Rohgewicht ist nur ein Verhältniswert. Die fertige Breite einer Zeile entsteht erst beim Ausgleich auf 97 und ist bei einer Krit-Zeile höchstens 5. Die Ausgleichszeilen der Krit-Dichte (siehe unten) haben ein berechnetes Rohgewicht und sind von dieser Setzung ausgenommen.

### Die Krit-Zeilen prüfen

Jede Krit-Zeile eines vorhandenen Körperteils braucht eine anatomische Voraussetzung. Die Zeilen des Helden sind die Vorlage, jede gehört zu einer von sieben Wirkungsarten:

- **Sehorgan** (Auge). Voraussetzung: ein Sehorgan. Wirkung: Trefferpunkte mal 2 ([[Glossar#TP|TP]]). Kein Ersatz.
- **Blutung** (Hals, Herz und/oder Lunge, Organ). Voraussetzung: Hals beziehungsweise Organ, und die Kreatur kann bluten. Wirkung: bei TP > Trefferschwelle ([[Glossar#TS|TS]]) eine zusätzliche Blutung. Kein Ersatz.
- **Gliedsperre** (Schultergelenk). Voraussetzung: ein Gliedansatz. Wirkung: bei TP > TS ist das Glied W4 + 2 Kampfrunden (KR) nicht benutzbar. Ersatz: Gliedansatz (Armansatz, Flügelansatz).
- **Gelenk** (Ellenbogen, Knie). Voraussetzung: ein Gelenk. Wirkung: TP mal 2. Ersatz: Armmitte oder Segmentnaht (für Körperteile, die in Segmenten gegliedert sind).
- **Greifen** (Hand). Voraussetzung: ein Greiforgan. Wirkung: bei misslungener Selbstbeherrschungsprobe ist die Waffe entwaffnet. Ersatz: Armspitze, Klaue oder Greifzange.
- **Stand** (Fuß). Voraussetzung: ein Standorgan am Boden. Wirkung: Eine Probe aus Körperbeherrschung und Athletik, erschwert um TP. Misslingt sie, folgt der Sturz nach „Der Sturz am Fuß“. Kein Ersatz.
- **Flug** (Hand eines Flügels). Voraussetzung: ein Flügel. Wirkung: Bei misslungener Selbstbeherrschungsprobe ist der Flügel W4 KR nicht benutzbar. Ersatz: Flügelspitze.

Wirkungen, die eine Ersatzzeile von der Zeile des Helden übernimmt, gelten unverändert. Die Normalzeile des Kopfes behält bei jedem Kopf ihre Wirkung: Die Selbstbeherrschungsprobe ist um TP mal 2 erschwert.

Jede Krit-Zeile wird in dieser Reihenfolge geprüft:

1. **Direkt übertragbar.** Die Voraussetzung der Wirkungsart ist erfüllt. Die Zeile bleibt unverändert.
2. **Funktional übertragbar.** Die Voraussetzung fehlt, aber das Körperteil hat eine Struktur, die dieselbe Wirkungsart erfüllt. Die Zeile wird durch die Ersatzzeile mit gleichem Rohgewicht ersetzt.
3. **Nicht übertragbar.** Die Zeile entfällt. Ihr Rohgewicht fließt in den Ausgleich ein und verteilt sich dort anteilig auf die vorhandenen Zeilen.

Entfallende Zeilen vergrößern den Streiftreffer-Bereich nicht.

### Der Ausgleich auf 97

Die Zeilen werden auf eine Summe von 97 gebracht. Der Streiftreffer belegt 98–100.

1. Jede Zeile hat mindestens die Breite 1, jede Krit-Zeile höchstens die Breite 5. Eine Zeile, deren anteiliger Wert unter 1 läge, wird auf 1 festgesetzt. Eine Krit-Zeile, deren anteiliger Wert über 5 läge, wird auf 5 festgesetzt. Die übrigen Zeilen werden auf 97 minus die Summe der festgesetzten Breiten neu verteilt. Das wiederholt sich, bis keine Zeile mehr eine Grenze verletzt.
2. Jede Zeile, die nicht festgesetzt ist, erhält den abgerundeten Wert ihres anteiligen Werts. Die fehlenden Punkte gehen an die Zeilen in der Reihenfolge der größten Nachkommareste.
3. Zeilen mit demselben Nachkommarest bilden eine Gruppe. Reichen die übrigen Punkte für die ganze Gruppe, erhält jede Zeile einen Punkt. Reichen sie nicht, erhalten die Zeilen in der Reihenfolge der Tabelle je einen Punkt, bis die Punkte aufgebraucht sind. Gleichartige Körperteile können dadurch um höchstens einen Punkt voneinander abweichen.
4. Die Zeilen erhalten ihre W100-Bereiche lückenlos in der Reihenfolge nach „Die Reihenfolge der Zeilen“.

Hier wird nicht aufgerundet, sondern abgerundet. Die Verteilung nach den größten Nachkommaresten sorgt dafür, dass die Summe nie über 100 liegt.

Die Tabelle gilt, wenn die Summe aller Zeilenbreiten 97 beträgt, der Streiftreffer 98–100 belegt und es keine Lücken oder Überschneidungen gibt.

### Der Streiftreffer

Der Bereich des Streiftreffers beträgt 3 Punkte (98–100). Er wächst nur, wenn die Zahl der Zeilen größer wäre, als 97 Punkte aufnehmen können. Dann werden zuerst Zeilen zusammengefasst. Erst danach darf der Bereich wachsen, höchstens auf 6 Punkte (95–100). Eine Tabelle mit mehr als 6 Punkten für den Streiftreffer ist ungültig. Entfallende Zeilen und fehlende Körperteile vergrößern den Bereich nie.

Die Wirkung ist wie beim Helden ([[Treffer-und-Schaden]]): Die Zone wird neu gewürfelt, und der Schaden wird durch W6 Schadenspunkte ersetzt. Der Neuwurf gilt auf der Tabelle desselben Hexfelds.

### Die Krit-Dichte

K ist die Summe der Breiten aller Krit-Zeilen der Tabelle. Die Normalzeile des Kopfes zählt nicht dazu. Der Referenzwert ist K = 24. Die Grenzen sind 20 und 25.

- **K ab 20.** Es gibt keinen Ausgleich.
- **K unter 20.** Für jedes Körperteil, das in Segmenten gegliedert ist und dessen Normalzeile ein Rohgewicht von mindestens 10 hat, wird eine Ausgleichszeile „Segmentnaht“ ergänzt (Wirkung: TP mal 2, wie beim Gelenk). Alle Ausgleichszeilen haben dasselbe Rohgewicht x. x ist der kleinste Wert, bei dem nach dem Ausgleich auf 97 K mindestens 20 beträgt. Ist das nicht erreichbar, ist x der Wert, bei dem alle Ausgleichszeilen die Breite 5 erreichen.
- **K bleibt unter 20.** Die Tabelle erhält die Warnung „W-KD“. Sie bleibt gültig. Die Warnung entfällt bei Kreaturen mit nur einer Zone, die ein Magiekorpus sind.
- **K über 25.** Die Tabelle erhält einen Prüfhinweis. Sie wird nicht verändert.

### Die Reihenfolge der Zeilen

Die Reihenfolge ist Kopf, dann Rumpf (Oberleib, Unterleib, einteiliger Rumpf), dann die Glieder in der Reihenfolge ihres Körperteiltyps: Arme, Beine, übrige Glieder. Gleichartige Glieder stehen in der Reihenfolge ihrer Nummerierung. Innerhalb eines Körperteils stehen die Krit-Zeilen vor der Normalzeile. Für den Körperbau des Helden ergibt das genau die Reihenfolge der Tabelle in [[Treffer-und-Schaden]].

### Jedes Hexfeld für sich

Jede Tabelle eines Hexfelds wird für sich nach diesen Regeln aufgebaut und ist für sich vollständig von 1 bis 100. Hat eine Kreatur ein Körperteil in mehreren Hexfeldern, steht es in jeder dieser Tabellen.

## Der Sturz am Fuß

Die Zahl der noch vorhandenen Beine der Kreatur entscheidet, was ein misslungener Wurf der Zeile mit dem Standorgan bewirkt. Jedes Bein zählt als ein Bein, gleich welcher Art die Kreatur ist und welchen Bau sie hat. Amputierte Beine zählen nicht.

- **0 Beine.** Die Fuß-Zeile entfällt. Stürzt die Kreatur aus einer anderen Quelle, tritt der Zustand Sturz wie beim Helden ein.
- **1 bis 3 Beine.** Der Sturz verläuft wie beim Helden, bei der Fuß-Zeile wie bei jeder anderen Quelle.
- **Mehr als 3 Beine.** Statt Sturz tritt Straucheln ein, bei der Fuß-Zeile wie bei jeder anderen Quelle. Eine Ausnahme ist der Sturz durch ein Weltereignis des Meisters, etwa ein Einsturz oder ein Klippensturz: Er löst auch bei mehr als drei Beinen den Zustand Sturz samt Sturzschaden aus.

Straucheln ist der Zustand aus dem Band 6 bis 9 der Selbstbeherrschungstabelle ([[Treffer-und-Schaden]], [[Zustaende-Katalog]]). Bei Straucheln entfällt der Sturzschaden-Wurf.

## Lebensenergie und Gesundheit

Jedes Körperteil mit eigener Zone hat eine maximale Lebensenergie und einen Behinderungswert. Beide ergeben sich aus dem Körperteiltyp und einem Faktor der Bauform. Der Körperbau des Helden behält seine Werte unverändert. Die Lebensenergie jeder Zone ist auf ihr Maximum gedeckelt, und ihre Regeneration folgt [[Gesundheit-und-Mana-Regeneration]].

### Die Gesundheit

Die Gesundheitsformel gilt für jedes Wesen mit Gesundheit: für den Helden, den NSC und jede Kreatur. Es gilt ein Satz Regeln für alle; Ausnahmen stehen nur, wo sie ausdrücklich genannt sind (Magiekorpi haben keine Gesundheit). Unterschiede bei Kreaturen entstehen durch Vor- und Nachteile und durch Talente. Es gibt keinen LE-Faktor. Bei der Erschaffung ist der aktuelle Wert gleich dem Maximum.

```text
Gesundheit = (Willenskraft + Konstitution + Kreis) / 3 + Vitalität
```

Die Division wird sofort aufgerundet, danach wird die Vitalität addiert. Willenskraft und Konstitution sind [[Eigenschaften]], die Vitalität ein [[Attribute|Attribut]], den Kreis erklärt [[Stufe-Kreis-Macht-und-Rerolls]]. Beispiele:

- Willenskraft 7, Konstitution 7, Kreis 0, Vitalität 0: 14 / 3 = 4,67, aufgerundet 5. Gesundheit 5.
- Willenskraft 11, Konstitution 11, Kreis 1, Vitalität 1: 23 / 3 = 7,67, aufgerundet 8. 8 + 1 = Gesundheit 9.
- Willenskraft 36, Konstitution 36, Kreis 7, Vitalität 8 (Maximum): 79 / 3 = 26,33, aufgerundet 27. 27 + 8 = Gesundheit 35.
- Willenskraft 43, Konstitution 43, Kreis 7, Vitalität 11 (Maximum, magisch): 93 / 3 = 31. 31 + 11 = Gesundheit 42.
- Willenskraft 20, Konstitution 24, Kreis 3, Vitalität 4 (mittlerer Wert): 47 / 3 = 15,67, aufgerundet 16. 16 + 4 = Gesundheit 20.

### Die LE einer Zone

Der Grundwert hängt vom Körperteiltyp ab:

```text
Kopf              = Konstitution / 4 + Vitalität + 4
Oberleib          = (Stärke × 2 / 5 + Konstitution + Vitalität) / 2 + 10
Unterleib         = (Konstitution + Vitalität) / 2 + 8
Arm               = (Konstitution / 2 + Stärke) / 2 + 5
Bein              = Konstitution + 8
einteiliger Rumpf = Grundwert Oberleib + Grundwert Unterleib
```

Jede Division im Grundwert wird einzeln sofort aufgerundet. Additionen und Malnahmen mit ganzen Zahlen ändern daran nichts. Beispiel Oberleib mit Stärke 36, Konstitution 36 und Vitalität 8: 36 × 2 = 72, 72 / 5 = 14,4, aufgerundet 15. 15 + 36 + 8 = 59, 59 / 2 = 29,5, aufgerundet 30. 30 + 10 = 40.

Mit Konstitution 12, Stärke 10 und Vitalität 5 ergeben sich diese Grundwerte:

- **Kopf.** 12 / 4 + 5 + 4 = 3 + 5 + 4 = 12.
- **Oberleib.** (10 × 2 / 5 + 12 + 5) / 2 + 10 = (4 + 12 + 5) / 2 + 10 = 11 + 10 = 21.
- **Unterleib.** (12 + 5) / 2 + 8 = 9 + 8 = 17.
- **Arm.** (12 / 2 + 10) / 2 + 5 = 8 + 5 = 13.
- **Bein.** 12 + 8 = 20.
- **Einteiliger Rumpf.** 21 + 17 = 38.

### Der Faktor

Die LE der Zone ist der Grundwert mal dem LE-Faktor, aufgerundet. Der Standardfaktor ist 1. Der Faktor gehört zur Bauform des Körperteils und gilt für jedes Exemplar einzeln. Bezahlt wird er je Körperteil in Entwicklungspunkten ([[Abenteuer-Entwicklungs-und-Talentpunkte]]):

- Faktor 1 kostet 0 Entwicklungspunkte.
- Ein Faktor unter 1 kostet 0 Entwicklungspunkte und gibt keine Gutschrift.
- Ein Faktor über 1 kostet 200 × Faktor − 200 Entwicklungspunkte.

Bei mehreren gleichartigen Körperteilen, etwa acht Armen, fallen die Kosten für jedes einzeln an. Der Faktor ändert nur die LE, nicht die Behinderung.

Beispiele mit dem Grundwert 13 für einen Arm: Faktor 1,5 ergibt 13 × 1,5 = 19,5, aufgerundet 20 LE, bei Kosten von 200 × 1,5 − 200 = 100 Entwicklungspunkten je Arm. Faktor 0,5 ergibt 13 × 0,5 = 6,5, aufgerundet 7 LE, bei Kosten von 0. Ein Kopf mit Faktor 2 hat 24 LE und kostet 200 Entwicklungspunkte.

### Die Behinderung der Zonen

Fällt die LE einer Zone auf 0, entsteht eine Behinderung ([[Behinderung-und-Erschwerung]]). Ihr Wert hängt vom Körperteiltyp ab:

- Kopf: 5
- Oberleib, Unterleib und einteiliger Rumpf: 2
- Arm: 3
- Bein: 4

Fällt die Zone durch einen einzigen Treffer von ihrer vollen LE auf 0, verdoppelt sich der Wert. Alle Krit-Zeilen eines Körperteils teilen denselben Wert. Mehrere Zonen mit LE 0 addieren ihre Werte, jede zählt einzeln, auch wenn sie vom selben Körperteiltyp ist. Der Wert gilt vollständig als Körperliche und als Mentale Behinderung.

### Weitere Regeln

- Ein Körperteil ohne eigene Zone hat keine LE und keine Behinderung.
- Der Leberschutz ist nicht Teil der LE einer Zone. Er ist ein Puffer der Kreatur, der vor jeder Zone verrechnet wird. Er hängt weder von Körperteilen noch von LE-Faktoren ab ([[Treffer-und-Schaden]]).
- Ein Magiekorpus, der durch einen Zauber entsteht, etwa ein Feuerball, hat keine Körperteile und bekommt keine LE aus dieser Rechnung. Seine LE bestimmt der Zauber. Er hat nicht zwingend welche, ein Feuerball hat keine.

### Beispiel Oktopus

Der Oktopus hat Kopf, einteiligen Rumpf und acht Arme, alle mit Faktor 1. Mit den Werten oben hat der Kopf 12 LE, der Rumpf 38 LE und jeder Arm 13 LE. Die Behinderung beträgt am Kopf 5, am Rumpf 2 und an jedem Arm 3. Fallen alle acht Arme auf LE 0, ergibt das 8 × 3 = 24 Behinderung aus den Armen. Fällt ein Arm durch einen einzigen Treffer von voller LE auf 0, zählt er 6.

## Wohin der Überschuss geht

Übersteigt ein Treffer die LE einer Zone, wird der Überschuss weitergeleitet. Beim Körperbau des Helden regelt das [[Treffer-und-Schaden]]. Bei Kreaturen ist jede Zone entweder Kern oder Glied.

**Begriffe.**

- **Kern.** Ein Körperteil vom Typ Kopf, Oberleib, Unterleib oder einteiliger Rumpf. Jeder Kopf ist ein Kern.
- **Glied.** Ein Körperteil vom Typ Arm oder Bein. Flügel, Schwanz, Tentakel und Flossen sind Glieder, wenn die Bauform sie dem Typ Arm oder Bein zuordnet.
- **Angeschlossene Zone.** Die Zone des Kerns, an der ein Glied ansetzt. Jedes Glied verweist auf eine oder zwei Kern-Zonen derselben Kreatur.
- **Magiekorpus.** Ein Wesen, dessen Aura von der Basis-Aura abweicht oder das aus Magie besteht oder sie enthält. Das hängt nicht davon ab, ob das Wesen lebt oder untot ist. Auch Lebende können Magiekorpus sein.
- **Magiekonstrukt.** Eine Form des Magiekorpus mit genau einer LE und einer Zone. Es ist zweckgebaut, unbeseelt und hat keine Gesundheit.
- **Dämonide.** Eine übernommene Kreatur, die den Korpus und die Zonen ihres Wirts hat.
- **Geist.** Ein Magiekorpus, der untot ist. Er hat keine Gesundheit und keine weitere Zone, an die er weiterleiten könnte.
- **Untot.** Der Lebensstatus untot. Der Status untotenkrank gehört nicht dazu.
- **Ohne Gesundheit.** Zweckgebaute, unbeseelte Magiekorpi, darunter die Magiekonstrukte, und Geister haben keine Gesundheit. Jede andere Kreatur hat Gesundheit.

### Kern, Glied und erschöpftes Glied

- **Kern.** Der Überschuss eines Kerns geht bei Nahkampf und Fernkampf unmittelbar an die Gesundheit.
- **Glied im Nahkampf.** Der Überschuss geht an die angeschlossene Zone, wenn der Angriffstreffer gut, meisterlich oder fröhlich war (gAT, mAT, fAT). Ohne einen solchen Treffer ist er verloren.
- **Glied im Fernkampf.** Es gibt keine Weiterleitung. Solange das Glied noch LE hat, ist jeder Überschuss verloren, gleich wie gut der Treffer war.
- **Zwei angeschlossene Zonen.** Verweist das Glied auf zwei Kern-Zonen, ist die angeschlossene Zone die Kern-Zone, die in der Tabelle des angegriffenen Hexfelds steht. Stehen beide in dieser Tabelle, ist es die Kern-Zone, die in der Reihenfolge der Tabelle zuerst steht.
- **Erschöpftes Glied.** Hat ein Glied zu Beginn eines neuen, eigenständigen Treffers schon LE 0, weil es ausgeschöpft oder amputiert ist, geht der gesamte Schaden dieses Treffers an die angeschlossene Zone. Das gilt unabhängig von Nahkampf, Fernkampf und Güte des Treffers. Für diesen Treffer zählt der Rüstungsschutz der angeschlossenen Zone, nicht der des Gliedes. Die Behinderung des Gliedes bleibt davon unberührt.
- **Kern mit LE 0.** Ein Kern, der selbst LE 0 hat, leitet jeden weiteren Treffer unverändert an die Gesundheit.
- **Wie weit.** Die angeschlossene Zone wird nicht neu gewürfelt. Weiter als bis zu ihr wird nicht weitergeleitet, außer mit ihrem eigenen Überschuss nach der Regel für Kerne.
- **Verlorenes Glied.** Verliert die Kreatur das Glied durch Amputation, bleibt der Anschluss bestehen, und der Schaden geht nach der Regel für das erschöpfte Glied an die angeschlossene Zone.

### Kreaturen mit nur einer Zone

Hat eine Kreatur nur eine Zone, gibt es keine angeschlossene Zone und keine Sonderweiterleitung. Der Überschuss geht an die Gesundheit, wenn die Kreatur Gesundheit hat. Hat sie keine, verfällt der Überschuss.

### Heiliger Schaden

Trägt der Schaden eines Treffers den Zusatz „Heilig“, „Gesegnet“ oder „Rein“, wird der Überschuss eines Gliedes immer vollständig an die angeschlossene Zone weitergeleitet. Das gilt unabhängig von Schadensart, Nahkampf oder Fernkampf und Güte des Treffers, die Regeln für das Glied oben gelten dann nicht. „Gesegnet“ ist der Name des Zusatzeffekts der Weihestufe geweiht bei Wundern ([[Artefakte]]). Die Sonderweiterleitung gilt nur bei diesen Zielen:

- **Untote.** Immer.
- **Magiekorpus.** Nur, wenn die Kreatur mehr als eine Zone hat.
- **Magiekonstrukt.** Nur, wenn die Kreatur mehr als eine Zone hat. Ein Magiekonstrukt hat genau eine, also nie.
- **Dämonide.** Wie ein Magiekonstrukt: nur bei mehr als einer Zone. Bei Dämoniden mit den Zonen des Wirts ist das in der Regel gegeben.
- **Alle übrigen Lebenden.** Keine Sonderweiterleitung, es gelten die Regeln für das Glied.

Gegen Kerne ändert „Heilig“ nichts, denn deren Überschuss geht ohnehin an die Gesundheit.

### Beispiele

- **Oktopusarm.** Der Arm ist ein Glied am Rumpf. Ein Nahkampftreffer mit Überschuss, ohne gAT: Der Überschuss ist verloren. Mit gAT geht er an den Rumpf. Ein Fernkampftreffer leitet nie weiter.
- **Oktopusarm mit LE 0.** Der nächste Treffer geht vollständig an den Rumpf, mit dem Rüstungsschutz des Rumpfes.
- **Spinnenbein.** Ein Glied am Kopfbruststück, wie der Oktopusarm.
- **Schwanz** an Oberleib und Unterleib. Ein Nahkampftreffer mit gAT auf den Schwanz in einem Hexfeld, in dem nur der Unterleib steht: Der Überschuss geht an den Unterleib. Stehen beide Kern-Zonen im Feld, geht er an die, die in der Tabelle zuerst steht, also an den Oberleib.
- **Drache.** Er belegt 4 Hexfelder. Kopf und Oberleib liegen in den vorderen Feldern, Unterleib und Schwanz in den hinteren. Er hat zwei Flügel, deren Anschluss auf Oberleib und Unterleib liegt. Der linke Flügel liegt auf dem linken vorderen und dem linken hinteren Feld. Er ist eine Zone mit einer LE und steht in beiden Tabellen mit vollem Gewicht. Ist seine LE erschöpft oder steht sie auf 0, geht der Überschuss oder der gesamte Schaden bei einem Angriff auf das linke vordere Feld an den Oberleib, bei einem Angriff auf das linke hintere Feld an den Unterleib. Ein Treffer aus dem einen Feld zieht dieselbe LE des Flügels ab wie ein Treffer aus dem anderen.
- **Untoter mit Armen** (mehr als eine Zone). Ein heiliger Fernkampftreffer auf den Arm mit Überschuss: Der Überschuss geht an die angeschlossene Zone, die Brust. Bei einem körperlichen Untoten mit UK 12 am Arm und 18 Trefferpunkten ist der Überschuss 6, und er kommt auf die Rundensumme der Brust.
- **Magiekonstrukt** (eine Zone, keine Gesundheit). Ein heiliger Treffer mit Überschuss: Der Überschuss verfällt, denn das Konstrukt hat weder eine andere Zone noch Gesundheit.
- **Geist** (Magiekorpus, untot, eine Zone, keine Gesundheit). Ein heiliger Treffer mit Überschuss: Der Überschuss verfällt, aus demselben Grund.
- **Dämonide** (Wirt mit zwei Armen, zwei Beinen und Rumpf). Ein heiliger Nahkampftreffer auf ein Bein mit Überschuss, ohne gAT: Der Überschuss geht an die angeschlossene Zone, weil der Dämonide wie ein Magiekonstrukt mit mehr als einer Zone behandelt wird.
- **Lebende Kreatur** mit heiligem Schaden: kein Unterschied zum normalen Treffer.

## Bluten, Brechen, Amputieren

Die Zustände Blutung, Wunde, Gebrochen, Heilender Knochen und Amputiert beschreibt [[Zustaende-Katalog]]. Bei Kreaturen hängen sie von zwei Eigenschaften ab: ob die Kreatur blutet und welche Skelettkategorie sie hat.

### Standardwerte je Kreaturentyp

Jede Kreatur hat die Eigenschaft „blutet“ (ja oder nein) und genau eine Skelettkategorie: Endoskelett, Exoskelett, kein Skelett, immateriell oder Konstrukt. Der Standard folgt dem Kreaturentyp. Der Meister überschreibt ihn bei der Kreatur oder ihrer Bauform, wenn der Entwurf es verlangt.

- **Blutet, Endoskelett.** Säugetier, Vogel, Reptil, Amphib, Fisch, Stachelhäuter, Drache, Feenwesen.
- **Blutet, Exoskelett.** Insekt, Spinnentier, Krebstier.
- **Blutet, kein Skelett.** Weichtier, Wurm, Nesseltier.
- **Blutet nicht, kein Skelett.** Pflanze, Pilz, Schleimwesen.
- **Blutet nicht, immateriell.** Dämon, Geist.
- **Blutet nicht, Endoskelett.** Elementar.
- **Blutet nicht, Konstrukt.** Konstrukt.

Kreaturen mit dem Lebensstatus untot bluten nie, gleich welchen Typ sie haben. Der Status untotenkrank ändert nichts daran. Eine Dämonide übernimmt Eigenschaft und Skelettkategorie ihres Wirts. Ein Magiekorpus ohne Kreaturentyp, etwa ein Feuerball, hat keinen Standard, der Meister setzt beides bei der Kreatur.

### Blutung

Kann eine Kreatur nicht bluten, bekommt sie aus keiner Quelle eine Blutung: nicht aus einer Wunde, nicht aus den Blutungs-Zeilen der Tabelle, nicht aus Blutmagie und nicht aus der Waffeneigenschaft „Starke Blutung“. Die Krit-Zeilen der Wirkungsart Blutung (Hals, Herz und/oder Lunge, Organ) entfallen. Ihr Rohgewicht wird verteilt wie bei jeder nicht übertragbaren Zeile. Blutet die Kreatur, gelten Blutung und Wunde unverändert. Blutungen, die bestanden, bevor sich die Eigenschaft änderte, bleiben bis zu ihrer Entfernung bestehen. Zauber, die eine Blutung stoppen, wirken bei einer Kreatur, die nicht blutet, auf ihre anderen Effekte unverändert.

### Bruch

Gebrochen und Heilender Knochen gibt es nur bei den Skelettkategorien Endoskelett, Exoskelett und Konstrukt.

Bei den Kategorien „kein Skelett“ und „immateriell“ entfällt der Bruch, und der Heilende Knochen kann nicht entstehen. Fällt eine Zone durch einen einzigen Treffer von ihrer vollen LE auf 0, trägt sie die verdoppelte Behinderung, solange ihre LE 0 beträgt. Steht die LE wieder über 0, endet die Behinderung. Ein Heilzauber, der einen Bruch heilen würde, heilt nur die Wunde oder wirkt wie sonst auf LE und Gesundheit.

Die Sonderschwelle für Hand und Fuß (Bruch bereits ab der halben maximalen LE der Gruppe, aufgerundet) gilt für jede Krit-Zeile der Wirkungsarten Greifen und Stand, auch für deren Ersatzzeilen (Armspitze, Klaue, Greifzange). Die Flügelspitze hat keine Sonderschwelle.

### Amputation

Amputiert gilt für jedes Glied, gleich welche Skelettkategorie die Kreatur hat. Auslöseschwelle, Schadensart und Entfernung bleiben wie beim Helden. Die Sonderschwelle für Hand und Fuß (Amputation bereits ab der maximalen LE der Gruppe, ohne den Anteil der Gesundheit) gilt für jede Krit-Zeile der Wirkungsarten Greifen und Stand, auch für deren Ersatzzeilen.

### Beispiele

- **Oktopus** (Weichtier: blutet, kein Skelett). Ein Treffer über der Trefferschwelle erzeugt Wunde und Blutung. Fällt ein Arm durch einen einzigen Treffer von der vollen LE auf 0, trägt er die verdoppelte Behinderung, solange seine LE 0 beträgt. Gebrochen entsteht nicht.
- **Spinne** (Spinnentier: blutet, Exoskelett). Gebrochen und Heilender Knochen gelten wie bei einem Endoskelett.
- **Schleim** (blutet nicht, kein Skelett). Ein Treffer über der Trefferschwelle erzeugt keine Blutung. Es gibt keine Zeilen der Wirkungsart Blutung und keinen Bruch.
- **Untoter Wolf** (Typ Säugetier, untot). Er blutet nicht. Er hat ein Endoskelett, also ist Gebrochen möglich.
- **Konstrukt** (blutet nicht, Skelett Konstrukt). Kein Blut, aber Gebrochen ist möglich.
- **Armspitze eines Oktopus** (Ersatzzeile der Wirkungsart Greifen). Ein einzelner Treffer auf die Armspitze mit TP ab der halben maximalen LE des Armes löst bei einem Skelett einen Bruch aus. Beim Oktopus ohne Skelett entfällt der Bruch, es gilt die verdoppelte Behinderung.

## Flug und Flügelverlust

Flügel sind Glieder. Treffer auf Flügelzeilen und der Verlust der LE eines Flügels können einer Kreatur das Fliegen sperren. Das gilt für den Flug mit Flügeln. Der Flug durch einen Zauber oder einen Vorteil folgt [[Gaben-und-Schwaechen]].

**Begriffe.**

- **Flügel.** Ein Glied vom Typ Arm, das die Bauform als Flügel ausweist.
- **Trägt den Flug.** Die Kreatur fliegt mithilfe dieses Flügels. Nur solche Flügel zählen für die Sperre.
- **Flügelflug.** Die Fortbewegungsart Fliegend, soweit Flügel sie tragen, die den Flug tragen.

### Nicht benutzbarer Flügel

Ein Flügel, der den Flug trägt, ist nicht benutzbar, solange einer dieser Fälle gilt:

- Die Zeile seines Flügelansatzes (Gliedsperre) hat bei einem Treffer mit TP > TS W4 + 2 KR gesperrt.
- Die Zeile seiner Flügelspitze (Flug) hat bei misslungener Selbstbeherrschungsprobe W4 KR gesperrt.
- Seine Zone hat LE 0.
- Er ist amputiert.

Ein Treffer auf die Flügelgelenk-Zeile hat keine Wirkung auf den Flug. Er wirkt als TP mal 2.

### Die Flugsperre

Der Flügelflug ist gesperrt, sobald mindestens die Hälfte der Flügel, die den Flug tragen, nicht benutzbar ist. Die Hälfte wird aufgerundet: Bei einem Flügel genügt dieser eine, bei zwei Flügeln einer, bei drei Flügeln zwei, bei vier Flügeln zwei. Die Sperre endet, sobald weniger als die Hälfte der Flügel nicht benutzbar ist.

Solange der Flügelflug gesperrt ist, kann die Kreatur nicht durch Flügel fliegen und sich nicht durch Flügel in die Luft erheben. Fliegt sie gleichzeitig durch einen Zauber oder einen Vorteil, ist dieser Flug nicht betroffen.

Ein Flügel, der den Flug nicht trägt, zählt weder für die Hälfte noch für die Sperre. Bei einer Kreatur mit nur einem tragenden Flügel sperrt jede Sperre dieses Flügels den Flug. Steigt die LE eines Flügels, der sonst nicht gesperrt ist, über 0, ist er wieder benutzbar. Ein amputierter Flügel bleibt nicht benutzbar, bis die Amputation entfernt wird.

### Der Absturz

Wird der Flügelflug gesperrt, während die Kreatur in der Luft ist, entscheidet der Meister über einen Absturz. Ein Absturz ist ein Weltereignis: Der Meister legt die Fallhöhe frei fest, der Zustand Sturz und der Sturzschaden folgen den Regeln für den Sturz ([[Treffer-und-Schaden]]). Das gilt unabhängig von der Zahl der Beine der Kreatur. Einen automatischen Absturz gibt es nicht.

### Beispiele

- **Drache** (zwei Flügel, die den Flug tragen). Ein Treffer mit TP > TS auf den linken Flügelansatz sperrt den linken Flügel für W4 + 2 KR. Die Hälfte von zwei Flügeln ist einer, der Flügelflug ist gesperrt. Ist der Drache in der Luft, entscheidet der Meister über den Absturz.
- **Vogelartige** (zwei Flügel). Ein Treffer auf die Flügelspitze mit misslungener Selbstbeherrschungsprobe sperrt den Flügel für W4 KR und damit den Flügelflug. Nach Ablauf der W4 KR ist der Flügel wieder benutzbar, die Sperre endet.
- **Libelle** (vier Flügel, die den Flug tragen). Ein gesperrter Flügel genügt nicht, denn die Hälfte von vier ist zwei. Sind zwei Flügel gesperrt, ist der Flügelflug gesperrt.
- **Fledermaus** (zwei Flügel) mit LE 0 an einem Flügel. Der Flügel ist nicht benutzbar, solange seine LE 0 beträgt. Der Flügelflug ist gesperrt, bis die LE über 0 steht.
- **Kreatur mit Flügeln und Zauberflug.** Der Flügelflug ist gesperrt, der Flug durch den Zauber besteht weiter.

## Untote im Kampf

Untote haben keine Gesundheit und keine Todesschwelle. Wie ihr Schaden gezählt wird, hängt davon ab, ob sie einen materiellen Körper haben.

### Körperliche Untote

Ein körperlicher Untoter hat keine Lebensenergie je Zone. Stattdessen hat jede Zone einen eigenen Schwellenwert, die Untoten-Kampfunfähigkeitsschwelle (UK). Der Meister legt ihn bei der Kreatur fest. Einen Standardwert gibt es nicht.

Die getroffene Zone wird wie üblich ausgewürfelt. Die Trefferpunkte jedes Treffers kommen auf die Rundensumme dieser Zone. Dazu zählen die Trefferpunkte nach Rüstung und nach dem Faktor, den ein geweihter Gegenstand gegen Untote bringt ([[Treffer-und-Schaden]]). Erreicht oder übersteigt die Rundensumme einer Zone ihre UK, gilt:

- **Kopf:** Der Kopf gilt als abgetrennt. Der Untod endet erst, wenn jeder Kopf der Kreatur abgetrennt ist ([[Tod-und-Wiederbelebung]]).
- **Arm oder Bein:** Das Glied ist abgetrennt, und der Untote ist niedergestreckt.
- **Jede andere Zone:** Der Untote ist niedergestreckt.

Mit der nächsten Kampfrunde beginnt jede Zone wieder bei 0. Der Schaden bleibt nicht stehen.

Heiliger Schaden gegen ein Glied: Was über die UK hinausgeht, kommt auf die Rundensumme der angeschlossenen Zone. Der Überschuss ist die Rundensumme des Glieds nach dem Treffer minus seine UK.

Ein niedergestreckter Untoter ist nicht tot. Er bleibt bis Sonnenuntergang liegen und steht dann wieder auf, mit der vollen UK für jede Zone, die er noch hat. Abgetrennte Glieder wachsen nicht nach.

**Beispiel.** Ein Untoter hat am rechten Arm die UK 12 und an der Brust die UK 20. In der ersten Kampfrunde treffen zwei Schläge den Arm mit 5 und 4 Trefferpunkten. Die Rundensumme ist 9 und bleibt unter der UK. In der zweiten Kampfrunde treffen 5 und 7 den Arm. Die Summe ist 12, der Arm ist abgetrennt, und der Untote ist niedergestreckt. Bei Sonnenuntergang steht er wieder auf, mit UK 20 an der Brust und ohne rechten Arm.

### Gespenster

Ein Gespenst hat keinen Körper. Es geht durch jede unmagische Materie, also auch durch Boden, Decken, verschlossene Türen, andere Körper und Gelände. Magische Wände und andere magische Hindernisse halten es auf. Es hat keine UK, sondern einen gemeinsamen Pool an Lebensenergie. Die Trefferzone wird ausgewürfelt, der Schaden aber vom Pool abgezogen.

- **Profane Waffe:** Die Angriffsprobe findet normal statt, der Schaden ist aber immer 0.
- **Magischer Schaden:** wirkt normal. Sinkt der Pool auf 0, ist das Gespenst besiegt, aber nicht getötet: Es verschwindet und bleibt untot. Bei Sonnenuntergang erscheint es am Ort des früheren Körpers wieder, mit vollem Pool und ohne Zustände.
- **Geweihter, heiliger oder reiner Schaden:** wirkt normal. Sinkt der Pool auf 0, ist der Untod beendet ([[Tod-und-Wiederbelebung]]).

Der Untod eines Gespensts endet außerdem, wenn der Kopf des früheren Körpers abgetrennt oder der Leichnam vollständig zerstört wird. Die Angriffe eines Gespensts zählen als magisch. Ob und wie man ein Gespenst ohne Anzeichen bemerkt, entscheidet der Meister.

## Beispiele für Tabellen

Alle Beispiele haben Körperteile in normaler Größe. Der Streiftreffer belegt überall 98–100.

**Der Mensch** ist die Vorlage: Die Zeilen und Breiten sind die der Tabelle in [[Treffer-und-Schaden]], K = 24.

**Der Wurm** hat einen Kopf ohne Augen und Hals, einen Vorderrumpf als Oberleib und einen Hinterrumpf als Unterleib, beide in Segmenten gegliedert. Die Rohgewichte sind Kopf 8, Herz und/oder Lunge 2, Vorderrumpf 21, Organ 5 und Hinterrumpf 10. Das Organ erreicht die Grenze 5. Ohne Ausgleich wäre K = 10. Der Ausgleich ergänzt zwei Segmentnähte, beide erreichen die Grenze 5.

- Kopf: 1–16, Breite 16
- Herz und/oder Lunge: 17–20, Breite 4
- Segmentnaht (Vorderrumpf): 21–25, Breite 5
- Vorderrumpf: 26–67, Breite 42
- Organ: 68–72, Breite 5
- Segmentnaht (Hinterrumpf): 73–77, Breite 5
- Hinterrumpf: 78–97, Breite 20
- Streiftreffer: 98–100, Breite 3

K = 4 + 5 + 5 + 5 = 19 und damit unter 20. Die Tabelle erhält die Warnung „W-KD“ und bleibt gültig. Die Zeilen ergeben 97, mit dem Streiftreffer 100.

**Der Oktopus** hat einen Kopf mit Auge, einen einteiligen Rumpf und acht Arme. Armansatz, Armmitte und Armspitze sind seine Ersatzzeilen. Die Tabelle hat 37 Zeilen.

- Auge: 1, Breite 1
- Kopf: 2–5, Breite 4
- Herz und/oder Lunge: 6, Breite 1
- Organ: 7–9, Breite 3
- Armansatz 1 bis 8: 10–17, je Breite 1
- Rumpf: 18–34, Breite 17
- Arm 1 (Armmitte 35, Armspitze 36, Arm 37–42): 35–42, Breite 8
- Arm 2 bis Arm 7: je 8 Felder von 43 bis 90, je Breite 8
- Arm 8 (Armmitte 91, Armspitze 92, Arm 93–97): 91–97, Breite 7
- Streiftreffer: 98–100, Breite 3

K = 29 und damit über 25: Die Tabelle erhält einen Prüfhinweis und wird nicht verändert. Arm 8 ist durch Schritt 3 des Ausgleichs einen Punkt schmaler als die anderen Arme.

**Der Schleim** hat ein einziges Körperteil, nicht in Segmenten gegliedert. Der Körper belegt 1–97, der Streiftreffer 98–100, K = 0. Die Tabelle erhält die Warnung „W-KD“.
