---
title: Klettern und Schwimmen
aliases: [Klettern, Schwimmen, Freiklettern, Seil Klettern, Leiter Steigen, Langsam Schwimmen, Schnell Schwimmen, Über Wasser bleiben, Ausdauerkosten Klettern, Ausdauerkosten Schwimmen]
status: entwurf
---

# Klettern und Schwimmen

Der Held klettert an Wänden, Seilen und Leitern hinauf und schwimmt durch Wasser. Jede dieser Fortbewegungsarten hat eine Geschwindigkeit in Metern pro Sekunde und Ausdauerkosten. Fehlende Gliedmaßen verlangsamen den Helden oder machen die Bewegung unmöglich.

Beide Geschwindigkeiten werden wie die der übrigen Fortbewegung gerundet ([[Bewegung]]): Das fertige Ergebnis einer Formel wird einmal auf das nächste Viertel (0,25) aufgerundet. Das ist der offizielle Wert in Metern pro Sekunde. Auf dem Hexraster des Kampfes wird er zusätzlich durch die Feldgröße von 1 Meter geteilt und auf ganze Felder pro Kampfrunde aufgerundet. In die Formeln gehen die vollen Werte der [[Eigenschaften]] ein, nicht die Eigenschaftsboni. Der Faktor für fehlende Gliedmaßen wirkt auf den offiziellen Wert. Das Produkt wird sofort auf das nächste Viertel aufgerundet, und erst danach folgt die Rundung auf Felder.

## Klettern

Der Held klettert auf drei Arten: Freiklettern ohne Sicherung, Seil Klettern und Leiter Steigen. Seil Klettern und Leiter Steigen setzen ein Seil beziehungsweise eine Leiter voraus. Klettern ist eine [[Grundfertigkeiten|Grundfertigkeit]], ihr Wert steht in der Formel.

### Geschwindigkeit

Freiklettern hat eine eigene Formel. Seil Klettern ist Freiklettern mit dem Faktor 1,25, Leiter Steigen ist Freiklettern mit dem Faktor 2:

```text
Freiklettern   = (Stärke + Geschicklichkeit + Schnelligkeit + 8 × Klettern) / 75     [m/s]
Seil Klettern  = (Stärke + Geschicklichkeit + Schnelligkeit + 8 × Klettern) / 60     [m/s]
Leiter Steigen = (Stärke + Geschicklichkeit + Schnelligkeit + 8 × Klettern) / 37,5   [m/s]
```

Seil Klettern gilt als erleichtertes, Leiter Steigen als stark erleichtertes Klettern. Jeder der drei Werte wird aus dem fertigen Ergebnis seiner Formel auf das nächste Viertel aufgerundet.

### Ausdauerkosten

| Art | Ausdauerkosten |
|---|---|
| Freiklettern | −4 pro Sekunde (also pro Kampfrunde) |
| Seil Klettern | −3 pro Sekunde |
| Leiter Steigen | −1 pro Sekunde |

Die Ausdauer ist in [[Ausdauer]] erklärt. Fehlende Gliedmaßen ändern die Ausdauerkosten beim Klettern nicht, sondern nur die Geschwindigkeit.

### Fehlende Gliedmaßen

Welche Merkmale der Held hat, steht in [[Aussehen-Schlaf-Sinne-und-Koerper|Aussehen, Schlaf, Sinne und Körper]]. Beim Klettern wirkt der Zustand der Arme anders als der der Beine:

| Zustand | Leiter Steigen | Freiklettern und Seil Klettern |
|---|---|---|
| 2 Arme, 2 Beine | volle Formel | volle Formel |
| Einarmigkeit, 2 Beine | mal 0,75 | unmöglich |
| Keine Arme, 2 Beine | mal 0,5 | unmöglich |
| 2 Arme, Einbeinigkeit | mal 0,5 | mal 0,5 |
| 2 Arme, Keine Beine | mal 0,25 | mal 0,25 |
| Einarmigkeit, Einbeinigkeit | mal 0,25 | unmöglich |
| Einarmigkeit, Keine Beine | ganz unmöglich | unmöglich |
| Keine Arme, Einbeinigkeit | ganz unmöglich | unmöglich |
| Keine Arme, Keine Beine | ganz unmöglich | unmöglich |

Fehlt dem Helden ein Arm oder fehlen ihm beide, kann er weder frei klettern noch am Seil klettern, gleich wie es um seine Beine steht. Leiter Steigen setzt mindestens zwei funktionsfähige Gliedmaßen insgesamt voraus. Mit nur einer oder keiner Gliedmaße ist auch das unmöglich, gleich ob die verbliebene Gliedmaße ein Arm oder ein Bein ist.

Der Faktor je Zustand steht fest in der Tabelle. Er wirkt nur auf die Geschwindigkeit.

### Beispiel

Der Held hat Stärke, Geschicklichkeit und Schnelligkeit 15 und Klettern 12. Die Summe in den Formeln ist 15 + 15 + 15 + 8 × 12 = 141.

```text
Freiklettern:   141 / 75   = 1,88  → 2,00 m/s → 2 Felder pro Kampfrunde
Seil Klettern:  141 / 60   = 2,35  → 2,50 m/s → 3 Felder pro Kampfrunde
Leiter Steigen: 141 / 37,5 = 3,76  → 4,00 m/s → 4 Felder pro Kampfrunde
```

Fehlen dem Helden beide Beine, gilt beim Seil Klettern der Faktor 0,25. Er rechnet 2,50 × 0,25 = 0,625. Das wird auf 0,75 m/s aufgerundet und ergibt 1 Feld pro Kampfrunde.

## Schwimmen

Der Held schwimmt auf drei Arten: Langsam Schwimmen, Schnell Schwimmen und Über Wasser bleiben. Schwimmen ist eine [[Grundfertigkeiten|Grundfertigkeit]].

### Geschwindigkeit

```text
Langsam Schwimmen   = 0,3 m/s (fest)
Schnell Schwimmen   = (Konstitution + Athletik + Schwimmen) / 30    [m/s]
Über Wasser bleiben = 0,00 m/s (fest)
```

Über Wasser bleiben bringt den Helden nicht voran. Er hält sich nur an der Wasseroberfläche. Auf dem Hexraster ergibt Langsam Schwimmen 1 Feld pro Kampfrunde, Über Wasser bleiben 0 Felder.

Nur Schnell Schwimmen ist ein Formelergebnis und wird auf das nächste Viertel aufgerundet. Langsam Schwimmen und Über Wasser bleiben sind feste Werte. Ohne fehlende Gliedmaßen werden sie nur auf Felder gebracht.

### Ausdauerkosten

| Art | Ausdauerkosten |
|---|---|
| Langsam Schwimmen | −4 pro Minute |
| Schnell Schwimmen | −2 pro Sekunde |
| Über Wasser bleiben | wie Langsam Schwimmen |

Minute und Sekunde sind Zeiteinheiten der Spielwelt. Sie gelten unabhängig von der Dauer einer Kampfrunde.

### Fehlende Gliedmaßen

Beim Schwimmen zählt jede fehlende Gliedmaße gleich, ob Arm oder Bein. Die Mindestzahl von zwei funktionsfähigen Gliedmaßen gilt hier nicht.

| Fehlende Gliedmaßen | Geschwindigkeit | Zuschlag auf die Ausdauerkosten |
|---|---|---|
| 0 | mal 1,00 | +0 |
| 1 | mal 0,75 | +1 |
| 2 | mal 0,50 | +2 |
| 3 | mal 0,25 | +3 |
| 4 | ganz unmöglich | keiner |

Der Faktor wirkt bei Schnell Schwimmen auf den aufgerundeten Wert der Formel, bei Langsam Schwimmen und Über Wasser bleiben auf den festen Wert. Das Produkt wird sofort auf das nächste Viertel aufgerundet, danach folgt die Rundung auf Felder.

Der Zuschlag wird zu den Ausdauerkosten in derselben Zeiteinheit addiert. Langsam Schwimmen kostet bei einer fehlenden Gliedmaße −5 pro Minute statt −4. Der Zuschlag gilt auch für Über Wasser bleiben, weil es die Kosten von Langsam Schwimmen teilt.

### Beispiele

Der Held hat Konstitution 12, Athletik 12 und Schwimmen 8. Die Summe in der Formel ist 32.

Ohne fehlende Gliedmaßen:

```text
Schnell Schwimmen:   32 / 30 = 1,0667 → 1,25 m/s → 2 Felder pro Kampfrunde
Langsam Schwimmen:   0,3 m/s → 1 Feld pro Kampfrunde
Über Wasser bleiben: 0,00 m/s → 0 Felder pro Kampfrunde
```

Mit einer fehlenden Gliedmaße schwimmt er schnell: 1,25 × 0,75 = 0,9375, aufgerundet 1,00 m/s, das ist 1 Feld pro Kampfrunde. Die Ausdauerkosten sind −2 − 1 = −3 pro Sekunde.

Mit zwei fehlenden Gliedmaßen schwimmt er langsam: 0,3 × 0,5 = 0,15, aufgerundet 0,25 m/s, das ist 1 Feld pro Kampfrunde. Die Ausdauerkosten sind −4 − 2 = −6 pro Minute.

Mit drei fehlenden Gliedmaßen bleibt er über Wasser: 0,00 × 0,25 = 0,00 m/s, das sind 0 Felder pro Kampfrunde. Die Ausdauerkosten teilt er mit Langsam Schwimmen: −4 − 3 = −7 pro Minute.

Mit vier fehlenden Gliedmaßen kann der Held nicht schwimmen.
