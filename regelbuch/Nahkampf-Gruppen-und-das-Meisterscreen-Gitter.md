---
title: Nahkampf-Gruppen und das Meisterscreen-Gitter
aliases: [Nahkampf-Gruppen und das Meisterscreen-Gitter, Nahkampf-Gruppe, Nahkampf-Ini-Bubble, NK-Ini-Bubble, Bubble, Ini-Paar, Ini-Paare, Nahkampf-Ini-Differenz, Waffen-Modifikator, Ini-Letzter, Nahkampf-Austausch, Verzichten, Mut-Probe, Sammelplatz, Meisterscreen-Gitter, Nahkampf-Gitter, Gitter, Ini bestimmen, Ini-Wechsel, Angreifer behält Ini, Konter-EA, Rest-Parade, reaktive Parade, Flucht möglich, Fluchtversuch, Fliehen, Fliehen-Probe, Diagonal-Band-Modell, pariert Bruchtest, meisterlicher Treffer]
status: entwurf
---

# Nahkampf-Gruppen und das Meisterscreen-Gitter

Stehen mehrere Teilnehmer im Nahkampf, kämpfen sie nicht mehr nach der Rangfolge der Runde, sondern als Nahkampf-Gruppe. Die Gruppe nimmt in der Runde einen einzigen Platz ein und arbeitet ihre Angriffe Paar für Paar ab. Jeder Angriff und die Antwort des Angegriffenen ergeben zwei Erfolgsstufen, und der Meister liest daraus im Meisterscreen-Gitter den Ausgang ab.

Dieses Kapitel beschreibt, wie eine Nahkampf-Gruppe entsteht und sich auflöst, in welcher Reihenfolge sie kämpft, wie ein einzelner Austausch von Angriff und Antwort läuft, wie ein Teilnehmer den Nahkampf verlassen kann und wie das Gitter zu lesen ist. Die Proben selbst stehen in [[Nahkampf]]. Umwerfen und Klingenbruch stehen in [[Nahkampf-im-Kampf]], die Kampfrunde und die globale Initiative in [[Kampfrunde-Aktionen-Initiative-und-Sicht]].

## Wie eine Nahkampf-Gruppe entsteht

Geraten zwei Teilnehmer durch Bewegung in angrenzende Felder und gehen miteinander in den Nahkampf, bilden sie eine Nahkampf-Gruppe. Drei oder mehr Teilnehmer bilden eine gemeinsame Gruppe und nicht mehrere Paare.

Die Reichweite für Bildung und Auflösung ist fest: das angrenzende Feld des Hexrasters ([[Bewegung]]). Sie hängt nicht von der Reichweite der einzelnen Waffen ab. Wer an einer Feldecke steht (West oder Ost, siehe die Blickrichtung in [[Kampfrunde-Aktionen-Initiative-und-Sicht]]), muss zum Nahkampf erst in ein Nachbarfeld einrücken.

### Der Platz der Gruppe in der Runde

Die Gruppe belegt in der Rangfolge der Runde genau einen Platz. Er hängt am Mitglied mit dem besten Runden-Ini-Wert (Sammelplatz). Erreicht die Gruppe in der Ausführungs-Phase diesen Platz, wird sie in sich vollständig aufgelöst, bevor die Reihenfolge der Runde fortfährt.

## Die Rangfolge in der Gruppe

### Nahkampf-Ini-Wert und Wurf

Innerhalb der Gruppe zählt der Nahkampf-Ini-Wert. Er ist der Runden-Ini-Wert plus der Waffen-Modifikator, also der höchste Ini-Wert der Nahkampfwaffen, die das Mitglied gerade führt ([[Nahkampfwaffen]]). Führt es mehrere Waffen, zählt nur der höchste Wert und nicht die Summe.

Jedes Mitglied würfelt einmal bei der Bildung der Gruppe W30 − W12 auf seinen Nahkampf-Ini-Wert, wie beim Ini-Wurf der Runde:

```text
Nahkampf-Ini-Differenz = Nahkampf-Ini-Wert − Würfelergebnis
```

Die Rangfolge der Gruppe ergibt sich aus der Nahkampf-Ini-Differenz: Der beste Wert steht vorn, der schlechteste hinten.

### Einmal geworfen, dann fest

Die Rangfolge der Gruppe wird nicht jede Kampfrunde neu geworfen. Sie bleibt von der Bildung an unverändert, bis ein Ausgang des Meisterscreen-Gitters sie ändert. Das sind nur „Ini bestimmen“ und „Ini-Wechsel“ (siehe „Initiative-Ausgänge“). Weitere Mitglieder der Gruppe bleiben davon unberührt.

### Späterer Beitritt

Tritt ein Teilnehmer in einer späteren Kampfrunde in eine bestehende Gruppe ein, würfelt er seinen Nahkampf-Ini-Wert und reiht sich ein. Die Rangfolge der übrigen Mitglieder bleibt, und die laufende Runde wird nicht umsortiert. Treten mehrere Teilnehmer in derselben Kampfrunde ein, gilt die Regel zur gleichzeitigen Neubildung (siehe unten).

## Der Ablauf der Gruppe in einer Kampfrunde

Die Gruppe arbeitet Paar für Paar ab, geordnet nach dem Nahkampf-Ini-Wurf des Angreifers. Es gibt keine getrennte Ansage-Phase, keine umgekehrte Ausführungsreihenfolge und keine Liste, in der alle Mitglieder der Reihe nach handeln. Darin unterscheidet sich die Gruppe von der Runde außerhalb.

1. Das Mitglied mit dem besten Wurf sagt seinen Rundenplan an und führt ihn sofort aus. Der Rundenplan ist der komplette Plan für 3 Aktionspunkte ([[Glossar#AP|AP]]), nicht Aktion für Aktion. Meist ist es ein Angriff auf sein Ziel.
2. Unmittelbar danach sagt dieses Ziel an und führt aus, gleich wo es in der Rangfolge steht. Das Ziel ist der Ini-Letzte dieser Paarung. Gemeint ist das Mitglied der Paarung mit dem niedrigsten Wurf und nicht das Mitglied, das zuletzt ansagt. Es entscheidet mit vollem Wissen über den bereits ausgeführten Angriff: verteidigen oder verzichten und selbst angreifen (siehe „Der Nahkampf-Austausch“).
3. Dann kommt das nächste noch nicht behandelte Mitglied nach dem Nahkampf-Ini-Wurf, zusammen mit seinem Ziel. Wieder folgt zuerst der Angriff, dann die Antwort des Ziels.
4. Das geht weiter, bis alle Mitglieder der Gruppe gehandelt haben.

- **Ein Mitglied handelt einmal je Kampfrunde.** Es hat ein Budget von 3 Aktionspunkten und handelt entweder als Angreifer oder als angegriffenes Ziel. Ein bereits behandeltes Ziel bekommt keine zweite Aktivierung.
- **Später Angreifer gegen ein bereits behandeltes Ziel.** Greift ein Angreifer aus Schritt 3 ein Ziel an, das in einer früheren Paarung schon gehandelt und seine 3 Aktionspunkte verbraucht hat, kann sich das Ziel nicht mehr wehren und kassiert den Angriff. Hat es Aktionspunkte zurückbehalten, verteidigt es daraus.
- **Keine vorgezogene Reaktion.** Jeder Angriff wird sofort aufgelöst. Ein Mitglied mit schlechterer Initiative kann auf den Angriff eines besseren nicht mit einem eigenen vorgezogenen Zug reagieren. Es hat nur die Antwort auf genau diesen Angriff oder das Verzichten. Das ist das Gegenstück zum Reaktionsfenster der Runde.
- **Die Ansage ist öffentlich.** Jede Ansage samt Ziel ist den anderen Mitgliedern bekannt.
- **Zielverlust.** Ist das angesagte Ziel bei der Ausführung weg, weil es in Deckung gegangen, außerhalb des Sichtfelds oder tot ist, muss die zielgebundene Handlung nicht ausgeführt werden. Die frei gewordenen Aktionspunkte dürfen nur für eine Drehung oder eine Defensivaktion verwendet werden (Nachsteuern, [[Kampfrunde-Aktionen-Initiative-und-Sicht]]).
- **Sichtkegel.** Die Blickrichtung und der Sichtkegel von 120° gelten auch in der Gruppe. Die Pflicht zur Orientierung entfällt dort.

## Der Nahkampf-Austausch

Ein Austausch besteht aus einem Angriff eines Mitglieds gegen ein anderes und der Antwort des Angegriffenen.

### Waffenklassen-Vergleich: einmal je Paarung

Der Vergleich der Waffenklassen ([[Nahkampf]]) der beiden Waffen einer Paarung wird einmal festgestellt, bei der Bildung der Paarung. Danach gilt er für jede folgende Parade dieser Paarung und wird nicht für jeden Austausch neu berechnet. Er bestimmt, welches Band der Waffenklassen-Differenz für die Paarung gilt, und damit die Erschwerung der Parade und den Auslöser für den Bruchtest ([[Nahkampf-im-Kampf]]). Die Waffenklasse rundet auf halbe Punkte.

### Angriff und Antwort

1. Der Angreifer würfelt seine Attacke für 3 Aktionskosten ([[Glossar#AK|AK]]). Mit dem Wurf steht ihre Erfolgsstufe fest: Patzer, Fehlschlag, normaler (n), guter (g), meisterlicher (m) oder fröhlicher (f) Erfolg ([[Wuerfeln-und-Proben]]). Sie ist der Schlüssel für die Zeile im Gitter.
2. Der Angegriffene wählt eine von drei regulären Antworten. Die Wahl bestimmt, welche der drei Tabellen des Gitters den Austausch regelt:
   - **Parade** für 2 AK,
   - **defensives Ausweichen** (defAW) für 1 AK,
   - **offensives Ausweichen** (offAW) für 3 AK.
3. Der Angegriffene würfelt die gewählte Verteidigungsprobe. Ihre Erfolgsstufe ist der Schlüssel für die Spalte.
4. Der Ausgang wird im Gitter nachgeschlagen: Treffer, pariert, ausgewichen, Ini bestimmen, Ini-Wechsel, Extra-Aktion, Flucht möglich und weitere.

Statt einer dieser drei Antworten hat der Ini-Letzte noch das Verzichten.

### Verzichten: der beidseitige Angriff

Der Ini-Letzte einer Paarung darf auf jede Verteidigung verzichten und selbst eine Attacke ausführen. Der Austausch wird dann ein beidseitiger Angriff. Das Gitter regelt ihn nicht. Das Verzichten ist an eine Mut-Probe gebunden (siehe unten).

- **Schadensreihenfolge.** Die bessere Erfolgsstufe der Attacke macht zuerst Schaden. Sind die Erfolgsstufen genau gleich, schlägt der Teilnehmer mit der besseren Nahkampf-Ini zuerst zu.
- **Abzug der Schadenspunkte.** Die Schadenspunkte (SP) des zuerst auflösenden Angriffs werden von den rohen Schadenspunkten des zweiten Angriffs abgezogen, bevor Schild, Rüstung und die weiteren Minderungen greifen ([[Treffer-und-Schaden]]). Das ist eine Korrektur vor der Minderung und kein eigener Schritt danach.
- **Der zweite Angriff** findet nur statt, wenn es noch einen Ausführenden gibt. Ist sein Angreifer durch den ersten Angriff tot oder handlungsunfähig, entfällt er. Das folgt aus den allgemeinen Regeln, die Handlungen verhindern ([[Zustaende-Grundregeln]]).
- **Der Zustand des zweiten Angreifers** nach dem Treffer ist genau der Zustand, den die gewöhnliche Kette aus Selbstbeherrschungsprobe (SB) und Selbstbeherrschungstabelle für diesen Treffer erzeugt ([[Treffer-und-Schaden]]).

### Die Mut-Probe fürs Verzichten

Will der Ini-Letzte verzichten und selbst angreifen, muss er eine einfache Mut-Probe bestehen.

- **Probe:** eine Eigenschaftsprobe auf Mut ([[Eigenschaften]]), ohne besondere Erschwerung und ohne besondere Schwelle.
- **Auslöser:** Der Ini-Letzte will verzichten und selbst angreifen. Es muss nicht sein, dass beide einen Angriff angesagt haben.
- **Zeitpunkt:** bei der Ansage des Ini-Letzten, im zweiten Schritt des Ablaufs der Gruppe. Er sagt an, dass er verzichtet und angreift, und würfelt sofort.
- **Erfolg:** Die Gegenattacke wird ausgeführt. Es gilt der beidseitige Angriff.
- **Fehlschlag:** Der Ini-Letzte behält seine 3 Aktionspunkte. Er darf sie nur für eine Parade (2 AK) und/oder ein defensives Ausweichen (1 AK) einsetzen. Ein offensives Ausweichen und eine Attacke sind ihm verwehrt.

## Das Meisterscreen-Gitter

Das Meisterscreen-Gitter ist die Schnellreferenz des Meisters für einen einzelnen Austausch. Aus der Erfolgsstufe des Angriffs und der Erfolgsstufe der Verteidigung liest er den Ausgang ab. Das Gitter sagt nicht nur, ob ein Treffer landet. Es sagt auch, ob sich die Initiative der Paarung verschiebt, ob eine Extra-Aktion entsteht, ob ein Bruchtest fällig wird und ob der Verteidiger fliehen kann.

### Die Eingänge

- **Zeile: Erfolgsstufe der Attacke** ([[Glossar#AT|AT]]). Sie lautet Patzer, Fehlschlag (AT miss), nAT, gAT, mAT oder fAT.
- **Tabelle: die Antwort des Angegriffenen.** Die Parade ([[Glossar#PA|PA]]) gehört zu Tabelle A, das defensive Ausweichen zu Tabelle B, das offensive Ausweichen zu Tabelle C ([[Glossar#AW|AW]]).
- **Spalte: Erfolgsstufe der gewählten Verteidigung.** Sie lautet Patzer, Fehlschlag (PA miss oder AW miss), n, g, m oder f. Bei der Parade heißen die Erfolge nPA, gPA, mPA und fPA, beim Ausweichen nAW, gAW, mAW und fAW.

### So schlägt der Meister nach

1. Der Angreifer würfelt seine Attacke. Ihre Erfolgsstufe ist die Zeile.
2. Der Angegriffene wählt Parade, defensives Ausweichen oder offensives Ausweichen und damit Tabelle A, B oder C. Das Verzichten ist die Ausnahme (siehe „Verzichten: der beidseitige Angriff“).
3. Der Angegriffene würfelt die gewählte Verteidigungsprobe. Ihre Erfolgsstufe ist die Spalte. Das defensive Ausweichen wird nur einmal je Kampfrunde gewürfelt und gegen jede eingehende Attacke derselben Kampfrunde abgelesen. Das offensive Ausweichen wird ebenfalls nur einmal gewürfelt, deckt aber wie eine Parade nur einen Angriff (siehe „Mehrere Angreifer in einer Kampfrunde“).
4. Die Zelle aus Zeile und Spalte nennt den Ausgang. Enthält sie mehrere Ausgänge, durch Komma getrennt, gelten alle. Sie werden in der Lesereihenfolge abgearbeitet: zuerst Schaden, „pariert“ oder „ausgewichen“, dann der Ausgang der Initiative, dann Extra-Aktion oder „Flucht möglich“.
5. Was jeder Ausgang bedeutet, steht unter „Was die Ausgänge bedeuten“.

**Ausnahme Umwerfen.** Der Angreifer kann seine Attacke als Umwerfen ansagen, nachdem der Angegriffene seine Antwort gewählt hat ([[Nahkampf-im-Kampf]]). Gelingt die Attacke, ist die Zelle nicht ihr Ausgang. Es entsteht kein Schaden, der Angreifer erhält keine Extra-Aktion, es gibt keinen Bruchtest und die Waffenklasse hat keine Wirkung. Die Verteidigung entscheidet dann nach den Regeln des Umwerfens: bei der Parade durch den Klassenvergleich, beim Ausweichen nach dem Diagonal-Band-Modell (siehe unten). Scheitert das Umwerfen, gelten die Ausgänge der Zelle für den Verteidiger normal: Extra-Aktion, Ausgänge der Initiative und „Flucht möglich“. Misslingt die Attacke, gilt die Zelle normal.

### Die drei Tabellen

Für jede Zeile stehen die Ausgänge je Spalte. „Fehlschlag“ steht für eine misslungene Parade oder ein misslungenes Ausweichen. „EA“ steht für Extra-Aktion (siehe „Extra-Aktionen“).

#### Tabelle A: Attacke gegen Parade

**Angreifer Patzer**

- gegen Patzer: Ini bestimmen
- gegen Fehlschlag: Ini-Wechsel
- gegen nPA: unbewaffnete Konter-EA
- gegen gPA, mPA, fPA: Konter-EA

**Angreifer Fehlschlag (AT miss)**

- gegen Patzer: Angreifer behält Ini
- gegen Fehlschlag: Ini bestimmen
- gegen nPA: Ini-Wechsel
- gegen gPA: unbewaffnete Konter-EA
- gegen mPA, fPA: Konter-EA

**Angreifer nAT**

- gegen Patzer, Fehlschlag: Treffer
- gegen nPA: pariert, Bruchtest!
- gegen gPA: pariert, Ini-Wechsel
- gegen mPA: pariert, unbewaffnete Konter-EA
- gegen fPA: pariert, Konter-EA

**Angreifer gAT**

- gegen Patzer, Fehlschlag: Treffer
- gegen nPA: pariert, unbewaffnete EA
- gegen gPA: pariert
- gegen mPA: pariert, Ini-Wechsel
- gegen fPA: pariert, unbewaffnete Konter-EA

**Angreifer mAT**

- gegen Patzer, Fehlschlag: Treffer
- gegen nPA: pariert, bewaffnete EA
- gegen gPA: pariert, unbewaffnete EA
- gegen mPA: pariert
- gegen fPA: pariert, Ini-Wechsel

**Angreifer fAT**

- gegen Patzer, Fehlschlag: Treffer
- gegen nPA: pariert, meisterlicher Treffer
- gegen gPA: pariert, bewaffnete EA
- gegen mPA: pariert, unbewaffnete EA
- gegen fPA: pariert

Bei einem Patzer des Angreifers ist nichts zu parieren. Deshalb steht in der Zelle Patzer gegen nPA „unbewaffnete Konter-EA“ und nicht „pariert“. Bei nAT gegen gPA, gAT gegen mPA und mAT gegen fPA steht „pariert, Ini-Wechsel“ und nicht bloß „Ini-Wechsel“.

#### Tabelle B: Attacke gegen defensives Ausweichen

**Angreifer Patzer**

- gegen Patzer: Ini bestimmen
- gegen Fehlschlag: Ini-Wechsel
- gegen nAW, gAW, mAW, fAW: Ini-Wechsel, Flucht möglich

**Angreifer Fehlschlag (AT miss)**

- gegen Patzer: Angreifer behält Ini
- gegen Fehlschlag: Ini bestimmen
- gegen nAW: Ini bestimmen, Flucht möglich
- gegen gAW, mAW, fAW: Ini-Wechsel, Flucht möglich

**Angreifer nAT**

- gegen Patzer, Fehlschlag: nur PA (2 AP) sonst Treffer
- gegen nAW: ausgewichen
- gegen gAW: ausgewichen, Ini bestimmen, Flucht möglich
- gegen mAW, fAW: ausgewichen, Ini-Wechsel, Flucht möglich

**Angreifer gAT**

- gegen Patzer, Fehlschlag: nur PA (2 AP) sonst Treffer
- gegen nAW: unbewaffnete EA gg. PA (2 AP)
- gegen gAW: ausgewichen
- gegen mAW: ausgewichen, Ini bestimmen, Flucht möglich
- gegen fAW: ausgewichen, Ini-Wechsel, Flucht möglich

**Angreifer mAT**

- gegen Patzer, Fehlschlag, nAW: nur PA (2 AP) sonst Treffer
- gegen gAW: unbewaffnete EA gg. PA (2 AP)
- gegen mAW: ausgewichen
- gegen fAW: ausgewichen, Ini bestimmen, Flucht möglich

**Angreifer fAT**

- gegen Patzer, Fehlschlag, nAW, gAW: nur PA (2 AP) sonst Treffer
- gegen mAW: unbewaffnete EA gg. PA (2 AP)
- gegen fAW: ausgewichen

Zwei Besonderheiten dieser Tabelle:

- Die Spalte Patzer lautet bei allen gelungenen Angriffen (nAT bis fAT) „nur PA (2 AP) sonst Treffer“ und nicht „Treffer“. Auch nach einem Patzer beim defensiven Ausweichen bleibt der Paradeversuch aus den verbliebenen Aktionspunkten.
- Beim Stufenunterschied von minus 1 steht hier „Ini bestimmen“, bei der Parade in Tabelle A dagegen „pariert, Ini-Wechsel“. Das ist Absicht.

#### Tabelle C: Attacke gegen offensives Ausweichen

**Angreifer Patzer**

- gegen Patzer: Ini bestimmen
- gegen Fehlschlag: Ini-Wechsel
- gegen nAW, gAW, mAW, fAW: Konter-EA

**Angreifer Fehlschlag (AT miss)**

- gegen Patzer: Angreifer behält Ini
- gegen Fehlschlag: Ini bestimmen
- gegen nAW: unbewaffnete Konter-EA
- gegen gAW, mAW, fAW: Konter-EA

**Angreifer nAT**

- gegen Patzer, Fehlschlag: Treffer
- gegen nAW: ausgewichen, Ini-Wechsel
- gegen gAW: ausgewichen, unbewaffnete Konter-EA
- gegen mAW, fAW: ausgewichen, Konter-EA

**Angreifer gAT**

- gegen Patzer, Fehlschlag: Treffer
- gegen nAW: ausgewichen
- gegen gAW: ausgewichen, Ini-Wechsel
- gegen mAW: ausgewichen, unbewaffnete Konter-EA
- gegen fAW: ausgewichen, Konter-EA

**Angreifer mAT**

- gegen Patzer, Fehlschlag, nAW: Treffer
- gegen gAW: ausgewichen
- gegen mAW: ausgewichen, Ini-Wechsel
- gegen fAW: ausgewichen, unbewaffnete Konter-EA

**Angreifer fAT**

- gegen Patzer, Fehlschlag, nAW, gAW: Treffer
- gegen mAW: ausgewichen
- gegen fAW: ausgewichen, Ini-Wechsel

Diese Tabelle ist bewusst so aufgebaut:

- Bei Gleichstand der Erfolgsstufen gilt „ausgewichen, Ini-Wechsel“. Der Ausweichende holt sich die Initiative schon bei Gleichstand.
- Ist der Angreifer eine Stufe besser, weicht der Verteidiger noch aus. Ab zwei Stufen Unterschied trifft der Angriff voll (harter Sprung).
- „Flucht möglich“ gibt es hier nicht. Fliehen geht nur über das defensive Ausweichen.
- Die Konter-EA kommt eine Stufe früher als bei der Parade, weil das offensive Ausweichen den Gegenangreifer voll preisgibt.

### Das Diagonal-Band-Modell

Alle drei Tabellen folgen einem einzigen Modell. Darin ist d die Erfolgsstufe des Angriffs minus die Erfolgsstufe der Verteidigung, gezählt auf dieser Skala:

```text
Patzer = 0, Fehlschlag = 1, n = 2, g = 3, m = 4, f = 5
```

Die Tabellen sind die ausgeschriebene Form dieses Modells. Weicht das Modell von einer ausgeschriebenen Zelle ab, gilt die Zelle.

**Beide Seiten im Erfolgsbereich** (der Angriff mindestens nAT, die Verteidigung mindestens n):

| d | Tabelle A, Parade | Tabelle B, defensives Ausweichen | Tabelle C, offensives Ausweichen |
|---:|---|---|---|
| +3 und mehr | pariert, meisterlicher Treffer | nur PA (2 AP) sonst Treffer | Treffer |
| +2 | pariert, bewaffnete EA | nur PA (2 AP) sonst Treffer | Treffer |
| +1 | pariert, unbewaffnete EA | unbewaffnete EA gg. PA (2 AP) | ausgewichen |
| 0 | pariert (bei nAT gegen nPA zusätzlich Bruchtest!) | ausgewichen | ausgewichen, Ini-Wechsel |
| −1 | pariert, Ini-Wechsel | ausgewichen, Ini bestimmen, Flucht möglich | ausgewichen, unbewaffnete Konter-EA |
| −2 | pariert, unbewaffnete Konter-EA | ausgewichen, Ini-Wechsel, Flucht möglich | ausgewichen, Konter-EA |
| −3 und weniger | pariert, Konter-EA | ausgewichen, Ini-Wechsel, Flucht möglich | ausgewichen, Konter-EA |

**Angreifer im Fehlschlag-Bereich** (Patzer oder Fehlschlag):

- Ist die Verteidigung ebenfalls im Fehlschlag-Bereich, zählt der Schweregrad. Gleich schlecht ergibt „Ini bestimmen“. Ist der Angreifer weniger schlecht (Fehlschlag gegen Patzer der Verteidigung), ergibt es „Angreifer behält Ini“. Ist der Angreifer schlechter (Patzer gegen Fehlschlag der Verteidigung), ergibt es „Ini-Wechsel“.
- Ist die Verteidigung im Erfolgsbereich, gilt dasselbe Band von d wie oben, aber ohne „pariert“ und „ausgewichen“, weil es keinen echten Angriff gab. In Tabelle B kommt „Flucht möglich“ nach derselben Regel hinzu.

**Verteidigung im Fehlschlag-Bereich, Angreifer im Erfolgsbereich:**

- Tabelle A: „Treffer“.
- Tabelle B: „nur PA (2 AP) sonst Treffer“, auch bei einem Patzer der Verteidigung. Der Paradeversuch aus den verbliebenen Aktionspunkten bleibt, es heißt nie glatt „Treffer“.
- Tabelle C: „Treffer“.

**„Flucht möglich“** gilt nur in Tabelle B. Es gilt genau dann, wenn der Verteidiger defensives Ausweichen gewählt hat, mindestens n gewürfelt hat und seine Erfolgsstufe höher ist als die des Angreifers.

### Was die Ausgänge bedeuten

#### Schadens-Ausgänge

- **Treffer.** Der Angriff landet. Es geht weiter mit der Schadensberechnung ([[Treffer-und-Schaden]]): Trefferzone würfeln, Deckung, dann die Schadenspipeline mit magischem Schild, Rüstungsschutz samt Schild, Resistenz oder Anfälligkeit, Leberschutz, Faktor der Zone und Lebensenergie der Zone, danach Gesundheit, Blutung und Behinderung notieren, Selbstbeherrschungsprobe. Das Gitter berechnet keinen Schaden.
- **pariert.** Der Angriff ist abgewehrt, es gibt keinen Schaden. Weitere Ausgänge derselben Zelle (Extra-Aktion, Ini-Wechsel, Bruchtest) gelten zusätzlich.
- **ausgewichen.** Der Angriff geht ins Leere, es gibt keinen Schaden. Weitere Ausgänge derselben Zelle gelten zusätzlich.
- **pariert, Bruchtest!** Steht nur in der Zelle nAT gegen nPA von Tabelle A. Der Angriff ist pariert, es gibt keinen Schaden, und eine Klingenbruch-Probe wird ausgelöst. Beide Waffen können verschleißen oder brechen ([[Nahkampf-im-Kampf]]). Die anderen Auslöser des Bruchtests, der Unterschied der Waffenklassen und das Schild, hängen an Waffe und Ausrüstung und sind nicht an eine Zelle gebunden.
- **pariert, meisterlicher Treffer.** Steht nur in der Zelle fAT gegen nPA von Tabelle A. Die ursprüngliche Attacke ist regulär pariert, aus ihr entsteht kein Schaden. Die bewaffnete Extra-Aktion, die der Angreifer erhält, ist aber ein automatischer meisterlicher Erfolg und braucht keine eigene Attackeprobe. Der meisterliche Treffer läuft dann durch die normale Schadensberechnung.

#### Initiative-Ausgänge

- **Ini bestimmen.** Die Initiative der Paarung wird neu gewürfelt. Beide Parteien der Paarung würfeln einen frischen Nahkampf-Ini-Wurf (Nahkampf-Ini-Wert − (W30 − W12)), und die neue Nahkampf-Ini-Differenz bestimmt die Rangfolge der Paarung neu. Weitere Mitglieder der Gruppe bleiben unberührt.
- **Ini-Wechsel.** Der Ini-Bessere und der Ini-Schlechtere der Paarung tauschen ihre Rangpositionen, ohne Neuwurf. Weitere Mitglieder der Gruppe sind nicht betroffen.
- **Angreifer behält Ini.** Das steht in der Zeile Fehlschlag (AT miss) und der Spalte Patzer aller drei Tabellen. Trotz des misslungenen Angriffs verschiebt sich nichts: Die bestehende Rangfolge der Paarung bleibt.

Die neue Rangfolge gilt ab dem nächsten Austausch der Paarung, der laufende Austausch ist bereits aufgelöst. In einer Gruppe mit drei oder mehr Mitgliedern ändert ein Ausgang der Initiative nur die zwei beteiligten Parteien, und der Ablauf der Gruppe läuft mit der geänderten Reihenfolge weiter.
#### Extra-Aktionen (EA)

Eine Extra-Aktion ([[Glossar#EA|EA]]) ist eine Zusatzaktion, die der Stufenunterschied des Austauschs gewährt. Sie kostet 0 AK und liegt außerhalb des Budgets von 3 Aktionspunkten. Sie steht auch dann zur Verfügung, wenn das Budget schon verbraucht ist. Je Kampfrunde ist höchstens eine Extra-Aktion erlaubt ([[Kampfrunde-Aktionen-Initiative-und-Sicht]]).

**Wer sie bekommt.** Der Gewinner des Stufenunterschieds. „Konter-EA“ und „unbewaffnete Konter-EA“ führt der Verteidiger aus. „EA“, „unbewaffnete EA“ und „bewaffnete EA“ führt der Angreifer aus.

**Womit.** Bei „unbewaffnete …“ ist nur eine unbewaffnete Extra-Aktion erlaubt. Ohne diesen Zusatz oder bei „bewaffnete …“ ist eine bewaffnete Extra-Aktion erlaubt, die bewaffnet oder unbewaffnet ausgeführt werden kann. Je größer der Abstand d, desto stärker ist die Extra-Aktion: erst unbewaffnet, dann bewaffnet.

**Ausführung.**

- Für jede Extra-Aktion legt der Ausführende eine eigene Attackeprobe ab. Ist sie erfolgreich, kann sie nicht pariert werden.
- Die Ausnahme ist die bewaffnete Extra-Aktion aus der Zelle fAT gegen nPA („pariert, meisterlicher Treffer“). Sie ist ein automatischer meisterlicher Erfolg ohne eigenen Wurf.
- Das Talent Kampf mit zwei Waffen erlaubt ab Stufe 1, eine „unbewaffnete EA“ mit der Waffe in der linken Hand statt der bloßen Hand auszuführen ([[Kampf-Talente]]).

Die Ausgänge „nur PA (2 AP) …“ und „… gg. PA (2 AP)“ sind keine Extra-Aktion.

#### Die reaktive Parade „nur PA (2 AP)“

Die Ausgänge „nur PA (2 AP) sonst Treffer“ und „unbewaffnete EA gg. PA (2 AP)“ gibt es nur in Tabelle B. Sie enthalten eine reaktive Parade aus den verbliebenen Aktionspunkten. Diese Parade ist keine Extra-Aktion. Sie kostet 2 AP aus dem regulären Budget.

**Ablauf.**

1. Die Attacke gelingt.
2. Der Verteidiger hat defensives Ausweichen angesagt (1 AP).
3. Der Wurf des defensiven Ausweichens reicht nicht (Zelle „nur PA (2 AP) sonst Treffer“).
4. Der Verteidiger würfelt aus seinen verbliebenen 2 AP eine reguläre Parade gegen genau dieselbe Attacke.

**Auswertung.**

- Die reaktive Parade wird wie eine normale Parade in Tabelle A nachgeschlagen: Erfolgsstufe der Attacke gegen Erfolgsstufe der reaktiven Parade. Der Ausgang aus Tabelle A gilt vollständig. Das ist „pariert“ (kein Schaden), „Ini-Wechsel“ und auch eine Extra-Aktion oder Konter-EA, wenn die Erfolgsstufe der Parade sie gewährt.
- Tabelle A kennt keinen Ausgang „nur PA“. Der Nachschlag endet also nach einem Schritt.
- Reicht die reaktive Parade nicht (Ausgang aus Tabelle A ist „Treffer“) oder fehlen die 2 AP, ist es ein Treffer.
- Die reaktive Parade ist die eine Parade der Kampfrunde und die letzte wählbare Aktion. Danach sind die Aktionspunkte bei 0. Eine daraus gewährte Extra-Aktion kostet trotzdem 0 AK.
- Der Ausgang steht auch in der Spalte Patzer. Nach einem Patzer beim defensiven Ausweichen bleibt der Paradeversuch aus den verbliebenen Aktionspunkten.

**„unbewaffnete EA gg. PA (2 AP)“** gilt bei d = +1. Der Angreifer erhält eine unbewaffnete Extra-Aktion mit eigener Attackeprobe. Der Verteidiger darf gerade diese eine Extra-Aktion mit der reaktiven Parade abwehren. Das ist die einzige Ausnahme des Gitters zur Regel, dass eine erfolgreiche Extra-Aktion nicht pariert werden kann.

#### „Flucht möglich“

Der Ausgang erscheint nur in Tabelle B und eröffnet die Fluchtgelegenheit. Er greift nur, wenn der Verteidiger in derselben Ansage bereits „will fliehen“ gewählt hatte, und er verpflichtet nicht zur Flucht. Der Ablauf steht unter „Den Nahkampf verlassen“.

### Mehrere Angreifer in einer Kampfrunde

Jeder Teilnehmer hat genau ein defensives Ausweichen je Kampfrunde. Es kostet 1 AP und wird gegen jede Attacke in Tabelle B abgelesen. Ein Wurf des Ausweichens wird nie in mehrere kleinere Würfe aufgeteilt.

| Verteidigung | Würfe je Kampfrunde | Kosten | Wirkt gegen |
|---|---|---|---|
| defensives Ausweichen | genau 1 | 1 AP | jeden Angriff der Kampfrunde |
| offensives Ausweichen | genau 1 | 3 AP (ganze Kampfrunde) | nur einen Angriff |
| Parade | höchstens 1 (letzte wählbare Aktion) | 2 AP | nur einen Angriff |

- Beim defensiven Ausweichen ist die Erfolgsstufe des einen Wurfs die Spalte von Tabelle B für jeden Austausch der Kampfrunde. Ein guter Wurf schützt ungeteilt gegen alle Angreifer der Gruppe.
- Das offensive Ausweichen wirkt wie die Parade: ein Wurf, aber nur gegen einen Angriff. Wer gegen mehrere Gegner offensiv ausweicht oder nur pariert, ist gegen alle außer einem ungedeckt. Welcher Angriff gedeckt ist, wählt der Verteidiger oder der Meister.
- Die reaktive Parade aus den verbliebenen Aktionspunkten ist dieselbe einmalige Parade, nur reaktiv statt angesagt.
- Ein Verteidiger kassiert einen weiteren Angriff, wenn er kein defensives Ausweichen angesagt hatte. Das gilt bei voller Offensive, bei offensivem Ausweichen oder Parade gegen mehrere Gegner, wenn er in seinem eigenen Austausch bereits geflohen ist und wenn er nur pariert hat und der Angriff nicht der eine parierte ist.

## Den Nahkampf verlassen: der Fluchtversuch

„Flucht möglich“ ist der einzige reguläre Weg, den Nahkampf zu verlassen. Die Ausnahme ist ein Gegner mit einem Zustand ab Benommenheit ([[Zustaende-Katalog]]).

### Ansage

„Will fliehen“ ist defensives Ausweichen plus Fliehen: 1 AK + 2 AK = 3 AK. Es belegt die ganze Kampfrunde.

### Ausführung: der Wurf des defensiven Ausweichens entscheidet

- **Misslingt das defensive Ausweichen,** kassiert das Ziel den Treffer und flieht nicht.
- **Gelingt das defensive Ausweichen** und liefert das Gitter „Flucht möglich“, folgt die Fliehen-Aktion.

### Fliehen-Aktion und Fliehen-Probe

Die Fliehen-Aktion ist eine Bewegung wie das Joggen. Sie zählt als die eine Laufen-Aktion der Kampfrunde ([[Kampfrunde-Aktionen-Initiative-und-Sicht]]). Die Fliehen-Probe lautet:

```text
Probenwert = Athletik + Fliehen − Behinderung (BE)
Wurf: W30 − W12
```

Athletik ist eine [[Eigenschaften|Eigenschaft]], Fliehen eine [[Sonderfertigkeiten|Sonderfertigkeit]]. Die Behinderung ist in [[Behinderung-und-Erschwernis]] erklärt.

- **Gelingt die Probe,** ist der Teilnehmer weg, um die Distanz des Joggens. Die Gruppe löst sich sofort für den Fliehenden auf, er fällt zurück auf seinen Platz in der Rangfolge der Runde.
- **Misslingt die Probe,** endet die Kampfrunde ohne Flucht. In der nächsten Kampfrunde sinkt die Paradeklasse um 1 (PA-Kl.-1). Das ist dieselbe Herabstufung wie beim Band 12 der Selbstbeherrschungstabelle ([[Treffer-und-Schaden]]) und beim Zustand „entwaffnet“ ([[Zustaende-Katalog]]).

### Mehrere Gegner

- Die Austausche werden in der Reihenfolge der Gruppe abgehandelt, der Beste nach Nahkampf-Ini zuerst.
- Wer in seinem Austausch flieht, hat danach keine Aktionspunkte mehr, um die Attacke eines anderen Gegners der Gruppe abzuwehren. Er kassiert sie.
- Wie viele Angriffe eine Verteidigung deckt, steht unter „Mehrere Angreifer in einer Kampfrunde“.

### Flucht statt Drehung

Nimmt ein überraschtes Ziel den Angriff wahr (Zustand „verfolgt“ oder „visuell“), kann es statt zu drehen und zu kämpfen die Flucht ansagen ([[Kampfrunde-Aktionen-Initiative-und-Sicht]]). Gelingt der Ablauf der Flucht, entgeht es damit auch den Attacken der übrigen Gegner der Gruppe. Für die Gegner, die vor dem Austausch des Fliehens eine bessere Initiative haben, gilt weiterhin die Regel zu mehreren Gegnern.

## Wenn sich die Gruppe verändert

### Auflösung

Bildung und Auflösung der Gruppe sind symmetrisch. Beide sind an die Bewegung in oder aus dem angrenzenden Feld gebunden. Die Auflösung wird für jeden Teilnehmer einzeln geprüft und nicht für die ganze Gruppe auf einmal.

- Bewegt sich ein Mitglied aus dem angrenzenden Feld heraus, verlässt nur dieses die Gruppe. Es fällt auf seinen eigenen ursprünglichen Platz in der Rangfolge der Runde zurück.
- Die Gruppe besteht für die übrigen Mitglieder weiter, solange mindestens zwei von ihnen in gegenseitiger Reichweite stehen, also in angrenzenden Feldern.
- Fällt die Gruppe unter zwei Mitglieder, löst sie sich vollständig auf. Dann fallen alle verbliebenen Mitglieder auf ihren ursprünglichen Platz in der Rangfolge der Runde zurück.
- Ein erfolgreicher Fluchtversuch löst die Gruppe sofort für den Fliehenden auf.

### Gleichzeitige Neubildung innerhalb einer Kampfrunde

Stürmen drei oder mehr Teilnehmer innerhalb einer einzigen Kampfrunde in dieselbe neue Gruppe, obwohl die Rangfolge der Runde schon geworfen und die Ansage-Phase schon gelaufen ist, greift die Gruppe sofort in dieser Kampfrunde. Für einen einzelnen später eintretenden Teilnehmer gilt dagegen der spätere Beitritt.

- Die Gruppe unterbricht die laufende Ausführungs-Phase der Runde und sortiert deren Rest neu.
- Gebunden bleiben nur die Aktionskosten, die für die auslösende Bewegung schon ausgegeben wurden. Der Rest des Budgets von 3 Aktionspunkten dieser Kampfrunde wird frei neu verteilt.
- Unbeteiligte Dritte, die in der Ausführungsreihenfolge zwischen den Mitgliedern der Gruppe standen und schon dran waren, werden übersprungen und nicht wiederholt. Die Umsortierung berührt nur den noch nicht ausgeführten Rest der Runde.

## Grenzfall: die Gruppe aus zwei Parteien

Die Ini-bessere Partei sagt an und führt aus, in aller Regel ein Angriff. Die Ini-schlechtere antwortet oder verzichtet, mit Mut-Probe. Danach wäre die Ini-schlechtere an der Reihe. Hat sie verzichtet und gegenangegriffen, war das ihre Aktion.

## Beispiele zum Gitter

- **gAT gegen gPA (Tabelle A).** Die Zelle lautet „pariert“. Der Angriff ist abgewehrt, es gibt keinen Schaden, keine Verschiebung der Initiative und keine Extra-Aktion. Der Austausch ist beendet, und der Ablauf der Gruppe geht weiter.
- **nAT gegen nPA (Tabelle A).** Die Zelle lautet „pariert, Bruchtest!“. Es gibt keinen Schaden, aber beide Waffen legen eine Klingenbruch-Probe ab.
- **fAT gegen nPA (Tabelle A).** Die Zelle lautet „pariert, meisterlicher Treffer“. Die Attacke ist pariert, aber die bewaffnete Extra-Aktion des Angreifers landet automatisch als meisterlicher Treffer und geht in die Schadensberechnung.
- **Patzer gegen gAW (defensives Ausweichen, Tabelle B).** Die Zelle lautet „Ini-Wechsel, Flucht möglich“. Die beiden tauschen ihre Plätze in der Rangfolge der Gruppe. Hatte der Ausweichende „will fliehen“ angesagt, eröffnet sich der Fluchtversuch.
- **mAT gegen nAW (defensives Ausweichen, Tabelle B).** Die Zelle lautet „nur PA (2 AP) sonst Treffer“. Die Attacke gelingt, der Verteidiger hatte defensives Ausweichen angesagt (1 AP), und sein Wurf reicht nicht. Er würfelt aus seinen 2 AP eine reguläre Parade gegen dieselbe Attacke, nachgeschlagen in Tabelle A (mAT gegen die Erfolgsstufe der Parade). Der Ausgang aus Tabelle A gilt voll: „pariert“, gegebenenfalls mit Extra-Aktion oder Konter-EA, wenn die Erfolgsstufe der Parade sie gewährt. Reicht die Parade nicht oder fehlen die 2 AP, ist es ein Treffer.
- **nAT gegen gAW (offensives Ausweichen, Tabelle C).** Die Zelle lautet „ausgewichen, Ini-Wechsel“. Es gibt keinen Schaden, und die Paarung tauscht ihre Plätze in der Rangfolge der Gruppe.

