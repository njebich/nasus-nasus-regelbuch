---
title: Bewegung
aliases: [Bewegung, Hexraster, Hexfeld, Gehen, Schnell Gehen, Dauerlauf, Sprint, Sprinten, Laufen, Hochsprung, Weitsprung, Springen, Sprung, Kampf-Sprung-Probe, Kriechen, Bewegungsgeschwindigkeit, Felder pro Kampfrunde, Ausdauerkosten Bewegung]
status: entwurf
---

# Bewegung

Der Held geht, läuft, sprintet und springt. Seine Geschwindigkeit gilt in Metern pro Sekunde, im Kampf auf dem Hexraster in Feldern pro Kampfrunde. Dieses Kapitel nennt das Raster, die Werte der Fortbewegungsarten und der Sprünge, den Einfluss fehlender Gliedmaßen und die Ausdauerkosten. Klettern und Schwimmen stehen in [[Klettern-und-Schwimmen]], die Traglast in [[Tragen]]. Wie eine Bewegung als Aktion in die Kampfrunde passt, steht in [[Kampfrunde-Aktionen-Initiative-und-Sicht]].

## Das Hexraster

Der Kampf läuft auf einem Raster aus Sechsecken, den Hexfeldern. Ein Feld misst 1 Meter von einer Kante zur gegenüberliegenden. Alle sechs Nachbarfelder eines Feldes sind gleich weit entfernt, nämlich 1 Meter.

Der Held bewegt sich nur über eine volle gemeinsame Kante zweier Felder. Berühren sich zwei Felder nur an einer einzelnen Ecke, darf er darüber nicht ziehen. Das gilt auch, wenn er durch eine Lücke zwischen zwei Hindernissen oder Kreaturen schlüpfen will, die sich nur an dieser Ecke berühren.

Kreaturen, die größer sind als ein Mensch, belegen mehr als ein Feld, zum Beispiel ein Drache.

Eine Kampfrunde dauert zurzeit eine Sekunde ([[Zeit-und-Spielablauf|Zeit und Spielablauf]]).

## Von Metern zu Feldern

Jede Fortbewegungsart hat einen Wert in Metern pro Sekunde. Gerundet wird in zwei Schritten:

1. **Offizieller Wert.** Das fertige Ergebnis der Formel wird einmal auf das nächste Viertel (0,25) aufgerundet. Teilen, Malnehmen und Addieren zählen dabei als ein Rechenschritt. Anders als bei sonstigen Formeln ([[Wuerfeln-und-Proben|Würfeln und Proben]]) wird also nicht nach jeder Teilung gerundet, sondern erst am fertigen Ergebnis. Der offizielle Wert gilt für Reisezeiten über Land und für Sprungweiten außerhalb des Kampfrasters.
2. **Auf dem Raster.** Der offizielle Wert wird durch die Feldgröße von 1 Meter geteilt und auf ganze Felder aufgerundet:

```text
Felder pro Kampfrunde = offizieller Wert in m/s / 1 m, aufgerundet
```

Eine Sprungweite wird ebenso auf eine ganze Zahl von Feldern aufgerundet.

Zum Beispiel hat Langsam Schwimmen ([[Klettern-und-Schwimmen]]) den festen Wert 0,3 m/s und ergibt 1 Feld pro Kampfrunde.

## Die vier Fortbewegungsarten

Gehen, Schnell Gehen, Dauerlauf und Sprint hängen alle vom Helden ab. In die Formeln gehen die vollen Werte der [[Eigenschaften]] ein, nicht die Eigenschaftsboni. Laufen ist eine [[Grundfertigkeiten|Grundfertigkeit]]; ihr Wert steht in der Formel.

```text
Sprint    = (Athletik + Schnelligkeit + Laufen) / 7 + 4     [m/s]
Dauerlauf = (Konstitution + Athletik + Laufen) / 9 + 1      [m/s]
Schnell Gehen = 2/3 des Sprint-Werts
Gehen         = 1/3 des Sprint-Werts
```

Sprint und Dauerlauf werden nach der Formel berechnet und wie oben gerundet. Für Gehen und Schnell Gehen gilt der bereits aufgerundete Sprint-Wert. Dessen Drittel beziehungsweise zwei Drittel wird einmal auf das nächste Viertel aufgerundet und danach wie jeder Wert auf Felder gebracht.

## Sprünge

Der Held kennt vier Sprungarten. Die Weite in Metern ist:

```text
Hochsprung                = (Stärke + Schnelligkeit + Springen) / 40
Weitsprung aus dem Stand  = (Stärke + Schnelligkeit + Springen) / 13 + 1
Weitsprung kurzer Anlauf  = (Stärke + Schnelligkeit + Springen) / 8 + 1
Weitsprung weiter Anlauf  = (Stärke + Athletik + Springen) / 6 + 1
```

Springen ist eine Grundfertigkeit. Auch hier zählen die vollen Eigenschaftswerte. Die Weite wird wie oben auf das nächste Viertel und im Kampf auf ganze Felder aufgerundet.

### Wie viele Kampfrunden ein Sprung dauert

| Sprungart | Dauer | Ablauf |
|---|---|---|
| Hochsprung | 1 Kampfrunde | nur der Sprung |
| Weitsprung aus dem Stand | 1 Kampfrunde | nur der Sprung, kein Anlauf |
| Weitsprung kurzer Anlauf | 2 Kampfrunden | Runde 1: Sprint-Anlauf geradeaus, Runde 2: Sprung |
| Weitsprung weiter Anlauf | 3 Kampfrunden | Runde 1 und 2: Sprint-Anlauf geradeaus, Runde 3: Sprung |

Die Formel gibt nur die Weite des Sprungs selbst an, also die Weite der letzten Kampfrunde. Jede Anlauf-Runde ist eine gewöhnliche Sprint-Aktion. Der Held legt in ihr die Sprint-Strecke des Rasters zurück. Die Gesamtstrecke einer Anlauf-Sprung-Aktion ist die Summe der Sprint-Felder aller Anlauf-Runden plus die Sprungweite der letzten Runde.

### Der Sprung als Aktion

Die Sprung-Kampfrunde zählt zur Aktionskategorie „Laufen“ (neben Gehen, Laufen, Sprint und Fliehen). Sie kostet wie ein Sprint 3 Aktionskosten ([[Glossar#AK|AK]]). Pro Kampfrunde ist höchstens eine Laufen-Aktion erlaubt. Das stört einen Anlauf-Sprung nicht, weil Anlauf-Runden und Sprung-Runde verschiedene Kampfrunden sind.

Eine **Kampf-Sprung-Probe** kann die Aktionskosten der Sprung-Kampfrunde auf 0 senken, so wie die Kampf-Laufen-Probe es für das Laufen tut ([[Kampfrunde-Aktionen-Initiative-und-Sicht|Kampfrunde, Aktionen, Initiative und Sicht]]):

```text
Probenwert = Springen + Athletik − Behinderung (BE)
Wurf: W30 − W12, erschwert um 13 (fest, wie beim vollen Sprint)
```

Die Probe gilt für alle vier Sprungarten gleich, gleich wie lang der Anlauf ist. Die Behinderung ([[Glossar#BE|BE]]) ist in [[Behinderung-und-Erschwerung|Behinderung und Erschwerung]] erklärt.

## Fehlende Gliedmaßen

Welche Merkmale der Held hat, steht in [[Aussehen-Schlaf-Sinne-und-Koerper|Aussehen, Schlaf, Sinne und Körper]]. Auf die Geschwindigkeit wirken sie so:

| Zustand | Fortbewegung |
|---|---|
| Einarmigkeit oder Keine Arme | kein Einfluss auf die Geschwindigkeit |
| Einbeinigkeit oder Keine Beine, ohne Hilfsmittel (Kriechen) | fest 1 Feld pro Kampfrunde (1 m/s) |
| mit einfacher Krücke oder Holzbein | alle vier Fortbewegungsarten, Geschwindigkeit mal 0,5 |
| mit angepasster Gehhilfe oder tatkräftiger fremder Hilfe | alle vier Fortbewegungsarten, Geschwindigkeit mal 0,75 |

Kriechen ist die einzige Geschwindigkeit in diesem Zustand. Gehen, Schnell Gehen, Dauerlauf und Sprint stehen nicht zur Verfügung. Kriechen setzt mindestens zwei funktionsfähige Gliedmaßen voraus. Mit weniger bewegt der Held sich nicht selbst fort, er wird getragen oder geschoben.

Die Faktoren 0,5 und 0,75 wirken auf die Geschwindigkeit in Metern pro Sekunde, nicht auf das Ergebnis in Feldern. Die Reihenfolge ist:

1. Formel berechnen und auf das nächste Viertel aufrunden (offizieller Wert). Bei einem Fixwert entfällt dieser Schritt.
2. Mit dem Faktor malnehmen und das Produkt sofort auf das nächste Viertel aufrunden.
3. Auf ganze Felder aufrunden.

Die Faktoren gelten auch für Sprungweite und Sprunghöhe. Beispiel: Ein Weitsprung aus dem Stand von 3,50 m wird mit Holzbein 3,50 × 0,5 = 1,75 m.

Die Zustände schließen sich je Gliedmaßenklasse gegenseitig aus.

## Ausdauerkosten

Jede Fortbewegung kostet Ausdauer ([[Ausdauer]]):

| Art | Ausdauerkosten |
|---|---|
| Gehen | −2 pro Stunde |
| Schnell Gehen | −1 pro 2 Minuten |
| Dauerlauf | −1 pro Minute |
| Sprint (auch als Anlauf-Runde vor einem Sprung) | −4 pro Sekunde (also pro Kampfrunde) |
| Hochsprung, Weitsprung aus dem Stand | −5, einmalig |
| Weitsprung kurzer Anlauf | −5 für den Sprung, dazu −4 für die eine Anlauf-Runde, zusammen −9 |
| Weitsprung weiter Anlauf | −5 für den Sprung, dazu 2 × −4 für die zwei Anlauf-Runden, zusammen −13 |

Der Sprung kostet bei allen vier Sprungarten −5. Jede Anlauf-Runde kostet zusätzlich die Ausdauer eines Sprints und wird getrennt gebucht.

Stunde, Minute und Sekunde sind Zeiteinheiten der Spielwelt. Sie gelten unabhängig von der Dauer einer Kampfrunde.

## Beispiele

### Ein Held mit lauter Zwölfern

Der Held hat Stärke, Athletik, Schnelligkeit und Konstitution 12, dazu Laufen 8 und Springen 8.

```text
Sprint:        (12+12+8) / 7 + 4 = 8,5714    → 8,75 m/s   → 9 Felder pro Kampfrunde
Dauerlauf:     (12+12+8) / 9 + 1 = 4,5556    → 4,75 m/s   → 5 Felder pro Kampfrunde
Schnell Gehen: 8,75 × 2/3 = 5,8333           → 6,00 m/s   → 6 Felder pro Kampfrunde
Gehen:         8,75 / 3 = 2,9167             → 3,00 m/s   → 3 Felder pro Kampfrunde
```

Seine Sprungweiten:

```text
Hochsprung:               (12+12+8) / 40 = 0,8      → 1,00 m
Weitsprung aus dem Stand: (12+12+8) / 13 + 1 = 3,4615 → 3,50 m
Weitsprung kurzer Anlauf: (12+12+8) / 8 + 1 = 5,00   → 5,00 m (schon auf dem Viertel)
Weitsprung weiter Anlauf: (12+12+8) / 6 + 1 = 6,3333 → 6,50 m
```

### Weitsprung mit Anlauf

Der Held springt mit kurzem Anlauf. Runde 1 ist der Sprint-Anlauf: 9 Felder, Ausdauer −4. Runde 2 ist der Sprung: zusätzlich 5,00 m, also 5 Felder, Ausdauer −5. Zusammen sind das 14 Felder und −9 Ausdauer.

Springt er mit weitem Anlauf, sprintet er in Runde 1 und 2 je 9 Felder, zusammen 18 Felder, und zahlt 2 × −4 = −8 Ausdauer. In Runde 3 springt er 6,50 m, also 7 Felder, und zahlt −5. Zusammen sind das 25 Felder und −13 Ausdauer.

### Einbeinig

Der Held hat ein Holzbein und geht. Seine Geschwindigkeit ist 3,00 × 0,5 = 1,50 m/s, das sind 2 Felder pro Kampfrunde.

Sprintet er mit dem Holzbein, sind es 8,75 × 0,5 = 4,375, aufgerundet 4,50 m/s und damit 5 Felder pro Kampfrunde. Mit einer angepassten Gehhilfe gilt der Faktor 0,75: 8,75 × 0,75 = 6,5625, aufgerundet 6,75 m/s und damit 7 Felder pro Kampfrunde.

Ein einbeiniger Held ohne Hilfsmittel kriecht mit festen 1 Feld pro Kampfrunde, gleich welche Werte er hat. Er hat dafür noch mindestens zwei funktionsfähige Gliedmaßen. Dauerlauf und Sprint sind ihm nicht möglich.
