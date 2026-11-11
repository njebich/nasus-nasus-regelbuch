---
title: Feuerwaffen
aliases: [Feuerwaffen, Feuerwaffe, Gewehr, Pistole, Bauart, Lademechanik, Schloss, Lauf, Verarbeitung, Kaliber, Nachladezeit, Patzermodifikator, Maximalreichweite, Munition, Preis einer Feuerwaffe]
status: entwurf
---

# Feuerwaffen

Eine Feuerwaffe besteht aus acht Bauteilen. Sechs davon stehen bei jeder Waffe des Katalogs fest, zwei wählt der Held beim Kauf. Aus den Einträgen der acht Bauteile ergeben sich Gewicht, Mindeststärke, Schaden, Reichweite, Nachladezeit, Verfügbarkeit und Preis der Waffe.

Wie der Held mit der Waffe schießt, steht in [[Fernkampf]] und [[Fernkampf-im-Kampf]].

## Die acht Bauteile

Der Katalog führt 86 Feuerwaffen. Jede legt sechs Bauteile fest:

- **Volk:** Feuerwaffen gibt es von 6 Völkern: zwergisch, goblinisch, drow, orkisch, dalkinisch und elfisch.
- **Typ:** Gewehr oder Pistole.
- **Bauart:** eine von 21 Bauarten.
- **Lademechanik:** eine von 4 Lademechaniken.
- **Schloss:** eines von 6 Schlössern.
- **Lauf:** einer von 4 Läufen.

Zwei Bauteile wählt der Held beim Kauf:

- **Verarbeitung:** eine von 7 Stufen.
- **Anpassung:** eine von 3 Stufen.

## Die Werte der Waffe

Jeder Wert ist die Summe der Einträge bestimmter Bauteile. Führt ein Bauteil für einen Wert keinen Eintrag, zählt es als 0.

- **Gewicht:** Volk + Typ + Bauart + Lademechanik + Lauf.
- **Mindeststärke:** Volk + Typ + Bauart + Anpassung. Von ihr hängen die Ausdauerkosten ab ([[Fernkampf]]).
- **Erster Würfel, zweiter Würfel und Fixschaden:** jeweils Volk + Typ + Bauart.
- **Rüstungsbrechend (RB):** Volk + Typ + Bauart + Lademechanik.
- **Kaliber:** Volk + Typ + Bauart + Lademechanik.
- **Reichweitenmodifikator** je Entfernungsband (10, 30, 60, 100, 150 und 210 Meter): Volk + Typ + Bauart + Schloss + Lauf + Verarbeitung + Anpassung.
- **Maximalreichweite (RW):** Volk + Typ + Bauart + Lauf.
- **Nachladezeit:** Bauart + Lademechanik + Schloss.
- **Patzermodifikator:** Volk + Bauart + Schloss + Verarbeitung.
- **Verfügbarkeit (Rohwert):** alle acht Bauteile.
- **Herstellungszeit:** Volk + Typ + Bauart + Schloss + Lauf + Verarbeitung + Anpassung.

Der Nachladen-Teiler ist keine Summe. Er kommt allein von der Lademechanik.

Die Werte der Waffe stehen fest, sobald der Held Verarbeitung und Anpassung gewählt hat.

### Die Schadenswürfel

Die Summen für den ersten und den zweiten Würfel sind keine Würfelgrößen, sondern Stufen von −4 bis 5. Jede Stufe steht für einen Würfel:

| Stufe | −4 | −3 | −2 | −1 | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|---|---|---|---|
| Würfel | W2 | W3 | W4 | W6 | W8 | W10 | W12 | W15 | W20 | W30 |

### Die Munition

Welche Munition die Waffe verschießt, wird nicht summiert. Es gilt:

- Bauart Harpunengewehr: Harpune.
- Lademechanik Vorderlader: Blei.
- Lademechanik Hinterlader: Papier Patrone.
- Lademechanik Klapplauf oder Block- oder Scharnierverschluss: Messing Patrone.

In jedem anderen Fall gilt die Munition, die der Katalog bei der Waffe nennt.

### Improvisierter Nahkampf

23 Feuerwaffen des Katalogs führen eigene Werte für den improvisierten Einsatz im Nahkampf. Diese Werte stehen bei der Waffe und entstehen nicht aus den Bauteilen.

## Der Preis

```text
Materialpreis = (Stahlpreis je kg des Typs + Stahlpreis je kg der Verarbeitung)
                × Gewicht Stahl in kg
                + Gewicht Holz in kg

Preis = Lohn pro Tag der Verarbeitung × Herstellungszeit + Materialpreis
```

Das Gewicht Stahl ist die Summe der Einträge von Volk, Typ, Bauart, Lademechanik und Lauf. Das Gewicht Holz ist die Summe der Einträge von Volk, Typ und Bauart. Der Preis steht in Dublonen.

## Die Verfügbarkeit

Aus dem Rohwert der Verfügbarkeit ergibt sich eine Stufe von 1 bis 7 ([[Gueter-Preise-und-Verfuegbarkeit]]). Je niedriger der Rohwert, desto höher die Stufe und desto schwerer ist die Waffe zu bekommen. Ein Rohwert unter 70 ergibt Stufe 7. Ein Rohwert ab 170 ergibt Stufe 1.

## Schießen mit der Feuerwaffe

Die Fernkampfprobe und ihre Erschwerungen stehen in [[Fernkampf]]. Die Waffe liefert dazu drei Dinge.

### Der Reichweitenmodifikator

Bei jedem Schuss gilt der Reichweitenmodifikator des Entfernungsbandes, in dem das Ziel steht. Er wird zum Basiswert des Schützen für Feuerwaffen addiert:

```text
Normalwert = Basiswert Feuerwaffen + Reichweitenmodifikator des Bandes
```

Hat der Held die Spezialisierung gekauft, die zum Typ der Waffe passt, gilt sein Basiswert mit dieser Spezialisierung: Musketen bei einem Gewehr, Pistolen bei einer Pistole.

Aus dem Normalwert ergeben sich die Schwellen für den guten und den meisterlichen Erfolg wie bei Bögen und Armbrüsten:

```text
gut         = 1 + Normalwert / Teiler für gut
meisterlich = 21 + Normalwert / Teiler für meisterlich
```

Beide Teiler gibt das Talent Fernkampfgeschick ([[Talente-die-Werte-veraendern]]). Der Wert für gut gilt nur, wenn er größer als 1 ist, der Wert für meisterlich nur, wenn er größer als 21 ist.

Der Reichweitenmodifikator kann negativ sein. Die Pocket Pistol hat bei 210 Meter zum Beispiel −80. Dann kann auch der Normalwert negativ werden. Er bleibt ein regulärer, schwerer Probenwert.

### Die Maximalreichweite

Die Maximalreichweite geht nicht in die Probe ein. Trifft ein Schuss ein Ziel jenseits der Maximalreichweite, sinkt der Schaden um (Entfernung − Maximalreichweite) / Maximalreichweite ([[Fernkampf-im-Kampf]]).

### Der Patzermodifikator

Bei einem Patzer würfelt der Schütze auf der Patzertabelle des Fernkampfs einen W12 und zählt den Patzermodifikator der Waffe dazu. Einige Ergebnisse der Tabelle verschlechtern die Reichweitenmodifikatoren der Waffe, bis sie repariert ist ([[Fernkampf]]).

## Beispiel

Der Held kauft ein zwergisches Jagdgewehr: Typ Gewehr, Volk Zwergisch, Bauart Jagd, Lademechanik Vorderlader, Schloss Steinschloss, Lauf Gezogen (Gewehr). Er wählt die Verarbeitung Gesellenarbeit und die Anpassung Von der Stange.

```text
Gewicht          = Typ 3,8 + Volk 1 + Bauart 0 + Lademechanik 0 + Lauf 0,3 = 5,1
Mindeststärke    = Typ 10 + Volk 1 + Bauart 0 + Anpassung 0 = 11
Maximalreichweite = Typ 40 + Volk 0 + Bauart 10 + Lauf 60 = 110
Verfügbarkeit    = Typ 100 + Volk 20 + Bauart −15 + Lademechanik 0 + Schloss 0
                   + Lauf −10 + Verarbeitung 0 + Anpassung 0 = 95
```

Der Rohwert 95 ergibt die Verfügbarkeit Stufe 5.

Der Held schießt mit dem Gewehr auf ein Ziel in 10 Meter Entfernung. Sein Basiswert für Feuerwaffen ist 12. Angenommen, der Reichweitenmodifikator des Gewehrs im Band 10 Meter ist +7. Dann ist der Normalwert 12 + 7 = 19. Der Held hat Fernkampfgeschick Stufe 2, sein Teiler für gut ist 3. 19 / 3 ergibt aufgerundet 7, die Schwelle für gut ist 1 + 7 = 8.
