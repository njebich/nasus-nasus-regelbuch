---
title: Kampfrunde, Aktionen, Initiative und Sicht
aliases: [Kampfrunde, Kampfrunde-Aktionen-Initiative-und-Sicht, KR, Initiative, Ini, Runden-Ini-Wert, Ini-Wurf, Ini-Differenz, Nahkampf-Ini-Wert, Ansage, Rundenplan, Reaktionsfenster, Zielverlust, Nachsteuern, Aktionskosten, AK, Aktionsliste, Aktionsbudget, Kampf-Laufen-Probe, Kampf-Sprung-Probe, Extra-Aktion, EA, Extra-Aktion, Warten, Rufen, Waffe ziehen, Zielen, Nachladen, Sichtfeld, Facing, Blickrichtung, Sichtkegel, toter Winkel, Drehung, Orientierung, Überraschungsangriff, Gefahreninstinkt-Probe, Positions-Modifikator, Todesschwelle]
status: entwurf
---

# Kampfrunde, Aktionen, Initiative und Sicht

In einer Kampfrunde handeln alle Teilnehmer nach demselben Ablauf: Erst wird die Reihenfolge ausgewürfelt, dann sagen alle ihre Handlungen an, dann führen alle sie aus. Jeder Teilnehmer hat dafür ein festes Budget an Aktionskosten, und jeder blickt in eine bestimmte Richtung. Dieses Kapitel beschreibt den Ablauf der Runde, die Initiative, die Kosten aller Aktionen und das Sichtfeld mit den Überraschungsangriffen im Nahkampf. Die einzelnen Kampfhandlungen stehen in [[Nahkampf-im-Kampf]], [[Fernkampf-im-Kampf]] und [[Magie-im-Kampf]].

## Die Kampfrunde im Überblick

Eine Kampfrunde (KR) dauert zurzeit eine Sekunde ([[Zeit-und-Spielablauf|Zeit und Spielablauf]]). Sie läuft für alle Teilnehmer in drei Phasen ab:

1. Die Initiative legt die Reihenfolge fest.
2. Alle Teilnehmer sagen ihre Handlung verbindlich an, in aufsteigender Reihenfolge: der Schlechteste zuerst.
3. Alle führen ihre Handlungen aus, in absteigender Reihenfolge: der Beste zuerst.

Die Ansage ist öffentlich. Wer später ansagt, kennt also jede frühere Ansage samt Ziel. Weil die Ausführung in umgekehrter Reihenfolge läuft, entscheidet die Initiative darüber, wer in derselben Runde noch auf eine gegnerische Handlung reagieren kann.

Geraten zwei oder mehr Wesen in angrenzende Felder, bilden sie eine Nahkampf-Gruppe. Die Gruppe belegt in der Reihenfolge der Runde einen einzigen Platz, und zwar den des Mitglieds mit der besten Initiative. Innerhalb der Gruppe gilt ein eigener Ablauf: Das Mitglied mit der besten Initiative sagt zuerst an und führt sofort aus. Sein Ziel antwortet unmittelbar danach, dann kommt das nächste noch nicht behandelte Mitglied mit seinem Ziel. Wie das im Einzelnen geht, steht in [[Nahkampf-Gruppen-und-das-Meisterscreen-Gitter]]. Die Regeln für Ansage und Ausführung in diesem Kapitel gelten für die Runde außerhalb einer solchen Gruppe.

## Die Initiative

### Der Runden-Ini-Wert

Jeder Teilnehmer hat einen Runden-Ini-Wert. Er ergibt sich aus fünf [[Eigenschaften]]:

```text
Runden-Ini-Wert = (Mut + Schnelligkeit) / 2
                + (Intelligenz + Geschicklichkeit + Athletik) / 6
```

Jede der beiden Teilungen wird einzeln aufgerundet, bevor die beiden Ergebnisse zusammengezählt werden ([[Wuerfeln-und-Proben|Würfeln und Proben]]). Es wird nicht erst die Summe gerundet.

### Der Ini-Wurf

Der Teilnehmer würfelt W30 − W12. Seine Ini-Differenz ist der Runden-Ini-Wert minus das Würfelergebnis:

```text
Ini-Differenz = Runden-Ini-Wert − Würfelergebnis
```

Die Rangfolge aller Teilnehmer ergibt sich aus der Ini-Differenz. Wer die schlechteste Differenz hat, sagt in der Ansage-Phase zuerst an. Wer die beste hat, führt in der Ausführungs-Phase zuerst aus.

Haben zwei oder mehr Teilnehmer dieselbe Ini-Differenz, würfeln nur diese Teilnehmer noch einmal W30 − W12, mit unverändertem Runden-Ini-Wert, bis ihre Differenzen verschieden sind. Die Plätze aller anderen bleiben.

### Der Nahkampf-Ini-Wert

Innerhalb einer Nahkampf-Gruppe gilt statt des Runden-Ini-Werts der Nahkampf-Ini-Wert. Er ist der Runden-Ini-Wert plus der Waffen-Modifikator. Der Waffen-Modifikator ist der höchste Ini-Wert der Nahkampfwaffen, die der Held gerade führt ([[Nahkampfwaffen]]). Führt er mehrere Waffen, zählt nur der höchste Wert. Die Werte werden nicht addiert.

### Wann und wie oft gewürfelt wird

- Ein Wesen bestimmt seine Initiative erst, wenn es weiß, dass ein möglicher Gegner da ist.
- Die Rangfolge wird einmal zu Kampfbeginn bestimmt. Sie wird nicht jede Runde neu geworfen.
- Kommt in einer späteren Runde ein neuer Gegner hinzu, würfelt nur er seine Initiative und reiht sich in die bestehende Rangfolge ein. Die übrige Rangfolge bleibt.
- Das Meisterscreen-Gitter ändert die Rangfolge der Runde nicht. Seine Ausgänge „Ini bestimmen“ und „Ini-Wechsel“ wirken nur innerhalb einer Nahkampf-Gruppe, und zwar auf deren Rangfolge im Nahkampf. Die Neubestimmung dort folgt dem eigenen Takt der Gruppe ([[Nahkampf-Gruppen-und-das-Meisterscreen-Gitter]]).
- Treten mehrere Wesen innerhalb einer Runde gleichzeitig in eine Nahkampf-Gruppe ein, ist das ein Sonderfall der Gruppe.

## Aktionskosten

### Das Budget

Jede Aktion hat einen Preis in Aktionskosten ([[Glossar#AK|AK]]). Pro Runde kannst du Aktionen mit Gesamtkosten von höchstens 3 AK ausführen.

- Jede Aktion kann nur einmal je Kampfrunde ausgeführt werden. Einzige Ausnahme ist der Tausch einer angesagten Drehung gegen eine andere Drehung (siehe „Drehung“ im Abschnitt zur Sicht). Die Extra-Aktion ist keine reguläre Aktion.
- Nicht genutzte AK verfallen am Ende der Kampfrunde. Sie werden nicht übertragen.
- Kommunikation („Rufen“) kostet keine Aktionskosten. Sie ist auf den Inhalt begrenzt, der in einer Kampfrunde, also einer Sekunde, übermittelt werden kann. Während der Vorbereitungszeit eines Zaubers ([[Magie-Wirkungsdauer-und-Konzentration|Magie: Wirkungsdauer und Konzentration]]) ist sie nicht möglich.
- Pro Kampfrunde ist höchstens eine Aktion der Kategorie „Laufen“ erlaubt. Dazu gehören Gehen, Laufen, Sprint, Sprung und Fliehen. Das gilt auch dann, wenn eine erfolgreiche Kampf-Laufen-Probe die Aktionskosten auf 0 senkt.
- Pro Kampfrunde ist höchstens eine Extra-Aktion erlaubt.

Aktionskosten und Ausdauer sind getrennt. Die Ausdauerkosten einer Kampfaktion stehen bei der Aktion selbst ([[Nahkampf]], [[Fernkampf]]). Im Blutrausch entfallen nur die Ausdauerabzüge der Kampfaktionen. Das Budget von 3 AK bleibt.

### Die Aktionsliste

**Bewegung**

| Aktion | AK |
|---|---:|
| Gehen (bis zu einem Drittel der Sprintdistanz) | 1 |
| Laufen (zwischen einem und zwei Dritteln der Sprintdistanz) | 2 |
| Sprint (volle Sprintdistanz) | 3 |
| Sprung (Hochsprung oder Weitsprung, die Sprung-Kampfrunde) | 3 |
| Fliehen | 2 |
| Drehung um 60° (1 Schritt) | 0 |
| Drehung um 120° (2 Schritte) | 1 |
| Drehung um 180° (3 Schritte) | 2 |
| In Deckung gehen oder aus der Deckung gehen | 0 |

**Kampf**

| Aktion | AK |
|---|---:|
| Waffe ziehen | 2 |
| Attacke (Nahkampf oder Fernkampf) | 3 |
| Umwerfen | 3 |
| Ausweichen, offensiv | 3 |
| Ausweichen, defensiv | 1 |
| Parade | 2 |
| Unbewaffnete Extra-Aktion | 0 |
| Bewaffnete Extra-Aktion | 0 |
| Zielen | 3 |
| Nachladen | 3 |

**Magie, KI und Psi**

| Aktion | AK |
|---|---:|
| KI-Fähigkeit einsetzen | nach der Staffel unten |
| Psi-Zauber wirken | nach der Staffel unten |
| Spruchzauber wirken | nach der Staffel unten |
| Spruchzauber halten | 1 |

**Gegenstände**

| Aktion | AK |
|---|---:|
| Aufnehmen | 2 |
| Benutzen | 2 |
| Artefakt aktivieren | 0 |
| Ablegen | 2 |
| Einstecken | 3 |
| Fallen lassen | 0 |
| Finden | 3 |

Keine Aktionskosten haben Warten, Rufen, Orientierung und Gegner identifizieren.

**Gegner identifizieren** (Arbeitsname, 0 AK). Der Held macht einen Angreifer im toten Winkel für den Gewarnten bekannt: Dessen Zustand wechselt auf „verfolgt“. Die Aktion steht neben dem Rufen und setzt voraus, dass der Rufende den Angreifer sieht. Je Kampfrunde kann ein Held einen Gegner identifizieren. Der Ruf gilt für alle Verbündeten in Hörweite. Die Hörweite ist nicht beziffert und gilt pauschal wie bei jedem Zielsinn; im Moment entscheidet der Meister.

Attacke, Parade und Fernkampf-Attacke sind jeweils die letzte Aktion der Kampfrunde. Danach tut der Teilnehmer in dieser Runde nichts mehr, auch nichts für 0 AK. Ein Zauber beendet die Runde nicht. Aktionen für 0 AK vor der Attacke bleiben möglich, etwa eine Drehung, eine Bewegung mit gelungener Kampf-Laufen-Probe oder ein Zauber für 0 AK. Die Extra-Aktion aus dem Gitter bleibt unberührt.

**Umwerfen.** Umwerfen ist eine Nahkampf-Attacke und kostet 5 Ausdauer ([[Nahkampf-im-Kampf]]).

**In Deckung gehen.** Das ist eine Haltungsänderung und keine Bewegung. Sie lässt sich mit einer Laufen-Aktion in Richtung Deckung verbinden. Je Kampfrunde ist sie höchstens einmal möglich, entweder hinein oder heraus. Das Herausgehen kann teilweise sein: Schießt der Held aus Volldeckung mit einer einhändigen Waffe, liegen nur Kopf, Brust und Arme frei, die unteren Trefferzonen bleiben gedeckt ([[Deckung]]).

**Fliehen.** Fliehen ist die eine Laufen-Aktion der Kampfrunde. Die Bewegung entspricht dem Dauerlauf. Wie sich der Held damit aus einem Nahkampf löst, steht in [[Nahkampf-Gruppen-und-das-Meisterscreen-Gitter]].

**Gegenstände.**

- Aufnehmen gilt für einen Gegenstand vom Boden, aus der Ausrüstung oder aus einem abgesetzten Rucksack.
- Benutzen setzt voraus, dass der Gegenstand bereits aufgenommen ist.
- Ein abgelegter Gegenstand ist ohne Probe wieder aufnehmbar.
- Der Rucksack wird mit Ablegen abgesetzt und mit Einstecken aufgesetzt. Eine Waffe aus dem Rucksack zu holen heißt also: Rucksack absetzen (Ablegen), Waffe herausnehmen (Aufnehmen), Rucksack aufsetzen (Einstecken).
- Einen fallen gelassenen Gegenstand muss der Held erst lokalisieren, bevor er ihn aufheben kann.
- Finden entscheidet der Meister. Ist der Gegenstand durch Entwaffnen oder durch die Selbstbeherrschungstabelle verloren gegangen, entfällt der Meisterentscheid. Dann ist das Suchen eine Ansage ohne AK. In der Such-Kampfrunde gilt die Herabstufung KK −1 ([[Behinderung-und-Erschwerung]]). Suchzeit und Sinnesschärfe-Probe richten sich nach dem Zustand „Verlorenen Gegenstand aufheben“ ([[Treffer-und-Schaden]]). Der gefundene Gegenstand wird am Landeort aufgenommen. Die Herabstufung KK −1 gilt dafür nicht.

### Laufen und die Kampf-Laufen-Probe

Gehen, Laufen und Sprint kosten 1, 2 und 3 AK. Eine Probe kann die Kosten einer Laufen-Bewegung auf 0 senken. Diese Probe heißt Kampf-Laufen-Probe. Sie ist eine Probe auf die [[Grundfertigkeiten|Grundfertigkeit]] Laufen. Die Eigenschaft ist hier immer Schnelligkeit, der Meister wählt sie nicht:

```text
Probenwert = Laufen + Schnelligkeit − Behinderung (BE)
Wurf: W30 − W12, erschwert um 0 (Gehen), 7 (Laufen) oder 13 (Sprint)
```

Die Probe wird vor der Ansage gewürfelt. Der Held sagt seinen Rundenplan also mit bekanntem Bewegungspreis an, entweder 0 oder voll. Es gibt kein Nachsteuern, weil der Preis feststeht.

0 AK sind 0 AK. Ein auf 0 gesenktes Laufen oder Sprinten lässt sich mit jeder anderen Aktion verbinden, auch mit einer Attacke für 3 AK. Die einzige Grenze ist die eine Laufen-Aktion je Kampfrunde.

Wie weit der Held bei Gehen, Laufen und Sprint kommt, steht in [[Bewegung]].

**Kampf-Sprung-Probe.** Auch die Sprung-Kampfrunde lässt sich auf 0 AK senken. Die Probe ist eine Grundfertigkeitsprobe auf Springen mit der Eigenschaft Athletik:

```text
Probenwert = Springen + Athletik − Behinderung (BE)
Wurf: W30 − W12, erschwert um 13 (fest, für jede Sprungart)
```

Sie gilt nur für die Sprung-Kampfrunde selbst. Die Anlauf-Kampfrunden vor einem Weitsprung mit kurzem oder weitem Anlauf sind gewöhnliche Sprint-Aktionen in den Kampfrunden davor. Für sie gilt die Kampf-Laufen-Probe. Auch hier sind 0 AK 0 AK.

### Waffe ziehen

Waffe ziehen kostet 2 AK. Die Dauer hängt von der Waffe und dem Aufbewahrungsort ab und beträgt mindestens eine Kampfrunde.

- Mit dem Talent Schnellziehen kostet das Ziehen 0 AK ([[Kampf-Talente]]).
- Mit Schnellziehen und dem passenden Talent, dem Kampf mit zwei Waffen oder bei Pistolen dem Beidhändig Pistolenschießen, zieht der Held beide Waffen gleichzeitig für 0 AK.
- Wird der Held während des Ziehens zu einem Ausweichen gezwungen, verzögert sich das Ziehen um 1 Kampfrunde. Das gilt nicht für eine Waffe, für deren Waffenart der Held das Schnellziehen hat.

### Zielen und Nachladen

Zielen kostet 3 AK und belegt die ganze Kampfrunde. Zielen und Attacke passen nicht in dieselbe Kampfrunde, denn beide kosten 3. Zielen ist eine Vorbereitung, die eine oder mehrere Kampfrunden vor der eigentlichen Attacke dauert. Den Bonus, den abgeschlossenes Zielen für die folgende Attacke bringt, regelt [[Fernkampf-im-Kampf]].

Nachladen kostet 3 AK und belegt immer die volle Kampfrunde. Wie viele Kampfrunden das Nachladen dauert, richtet sich nach der Nachladezeit der Waffe ([[Fernkampf]]). Wird der Held während des Ladens zu einem Ausweichen gezwungen, verzögert sich das Laden um 1 Kampfrunde.

### Ausweichen, defensiv und offensiv

Der Verteidiger wählt bei jedem Angriff eine von drei Antworten: Parade, defensives Ausweichen oder offensives Ausweichen. Die Werte der Proben stehen in [[Nahkampf]]. Hier stehen die Kosten:

- **Defensives Ausweichen** kostet 1 AK und lässt 2 AK frei, zum Beispiel für eine Parade als Rückfall oder für eine Bewegung. Im Meisterscreen-Gitter bringt es die Ausgänge „Flucht möglich“ und die Rückfall-Parade ([[Nahkampf-Gruppen-und-das-Meisterscreen-Gitter]]).
- **Offensives Ausweichen** kostet 3 AK, belegt die ganze Kampfrunde und beendet sie: Danach tut der Held in dieser Runde nichts mehr. Das defensive Ausweichen beendet die Runde nicht. Es schaltet im Gitter die Gegenangriffs-Ausgänge frei, etwa die Konter-Extra-Aktion.

### Warten

Warten kostet keine AK. Der Wartende darf als Reaktion trotzdem defensives Ausweichen (1 AK), offensives Ausweichen (3) oder eine Parade (2) einsetzen. Er bezahlt sie aus seinem zurückbehaltenen Budget von 3 AK.

### Aktionskosten von Zaubern

Wie viele AK ein neuer Spruchzauber, eine neue KI-Fähigkeit oder ein neuer Psi-Zauber kostet, hängt davon ab, wie viel der Held von seinem jeweiligen Attribut noch frei hat. Jede Disziplin hat ihren eigenen freien Wert, und die drei sind unabhängig voneinander ([[Magie-Wirkungsdauer-und-Konzentration|Magie: Wirkungsdauer und Konzentration]]):

- **KI:** freie Aura = Aura − Anzahl der aktiven KI-Fähigkeiten
- **Psi:** freie Magie = Magie − Summe der gewählten Psi-Stufen
- **Spruchmagie:** verfügbare Weisheit = Weisheit − Summe aus dem halben Grad jedes Anhaltend-Zaubers und dem vollen Grad jedes Bipolar-Zaubers

Ist die verfügbare Weisheit eine Bruchzahl, zählt für die Staffel ihr ganzzahliger Anteil.

| freier Wert | Aktionskosten des Zaubers |
|---:|---:|
| 1 bis 2 | 3 |
| 3 bis 4 | 2 |
| 5 bis 6 | 1 |
| 7 und mehr | 0 |

- Bei 3 AK belegt der Zauber die volle Kampfrunde. Daneben ist nur beiläufige Bewegung möglich, aber kein zweiter Schritt, der Aktionskosten hat.
- Bei 2 AK bleibt 1 AK für eine Aktion zu 1 AK.
- Bei 1 AK bleiben 2 AK frei.
- Bei 0 AK läuft der Zauber neben einem vollen Rundenplan von 3 AK mit, zum Beispiel Attacke und Zauber.
- Die übrigen AK werden nach den normalen Budgetregeln verwendet.
- Für einen neuen Effekt braucht der Held während der Vorbereitungszeit mindestens 1 Punkt im freien Wert seiner Disziplin. Sonst entsteht kein neuer Effekt.
- Einen bereits laufenden Zauber zu halten („Spruchzauber halten“) kostet 1 AK. Das ist unabhängig von der Staffel, denn es wirkt keinen neuen Zauber.

Wie stark jede aktive Wirkung den freien Wert senkt, steht bei [[KI]], [[Psi]] und [[Spruchmagie]].

### Extra-Aktionen

Eine Extra-Aktion ist eine Extra-Aktion, die ein Unterschied der Kampfklassen gewährt. Im Meisterscreen-Gitter heißt sie auch Konter-Extra-Aktion, unbewaffnete Extra-Aktion oder bewaffnete Extra-Aktion. Für die Aktionskosten gilt:

- Die Extra-Aktion kostet 0 AK.
- Sie wird nicht aus dem Budget von 3 AK bezahlt. Sie steht auch dann zur Verfügung, wenn das Budget schon verbraucht ist, etwa direkt nach einer Attacke für 3 AK.
- Je Kampfrunde ist höchstens eine Extra-Aktion erlaubt.
- Die „PA-Extra-Aktion“ des Gitters ist keine Extra-Aktion. Sie ist eine gewöhnliche Parade als Reaktion, die vollständig aus den tatsächlich verbliebenen AK der Kampfrunde bezahlt wird (Parade = 2 AK). Hat der Verteidiger nach seiner angesagten Aktion keine 2 AK mehr, ist keine spontane Parade möglich.

Welche Gitter-Ausgänge eine Extra-Aktion gewähren, wer sie ausführt und welche Proben sie braucht, steht in [[Nahkampf-Gruppen-und-das-Meisterscreen-Gitter]].

**Waffen mit dem Tag „Schnell“.** Eine Extra-Aktion, die sonst unbewaffnet ausgeführt werden muss, darf mit einer Waffe ausgeführt werden, die den Tag „Schnell“ trägt, solange der Held sie als Primärwaffe führt. Die übrigen Regeln der Extra-Aktion bleiben gleich: 0 AK, höchstens eine je Kampfrunde, eine eigene Attackeprobe. Den Tag tragen zurzeit:

- Armklingen und Armklingen elfisch
- Florett
- mehrere Stab-Waffen (die Kampfstab-Varianten und Zweililien)
- Doppelsense
- Bat’leth orkisch
- die Grundzeile Unbewaffnet sowie die Zeilen Gepanzert, Schlagring und Veteranenhand

### Grenzfälle der Aktionskosten

- Eine Attacke (3 AK) füllt das Budget und beendet die Kampfrunde. Vorher sind Aktionen für 0 AK möglich, danach kommt nur noch die Extra-Aktion aus dem Gitter.
- Defensives Ausweichen (1) und Parade (2) ergeben zusammen 3 und sind zulässig. Die Parade deckt auch die spontane Parade der „PA-Extra-Aktion“ ab.
- Zwei verschiedene Bewegungen, zum Beispiel Gehen und Sprint, schließt die Grenze von einer Laufen-Aktion je Kampfrunde aus. Eine Drehung gehört zu einer eigenen Kategorie und ist zusätzlich möglich.
- Zauber und volle Attacke in einer Kampfrunde gehen nur bei einem freien Wert von 7 oder mehr, denn dann kostet der Zauber 0 AK. Bei einem freien Wert von 5 bis 6 kostet der Zauber 1 AK. Es bleiben 2, genug für defensives Ausweichen plus Drehung oder für eine Parade, aber nicht für eine Attacke.
- Bildet sich in derselben Kampfrunde gleichzeitig eine Nahkampf-Gruppe neu, bleiben nur die Aktionskosten gebunden, die für die auslösende Bewegung schon ausgegeben sind. Die übrigen AK der Kampfrunde werden neu verteilt ([[Nahkampf-Gruppen-und-das-Meisterscreen-Gitter]]).

## Ansage und Ausführung

### Die Ansage

Wer an der Reihe ist, sagt seinen kompletten Rundenplan an. Das sind alle Aktionen, die er in dieser Kampfrunde im Budget von 3 AK ausführen will. Er sagt sie gebündelt in einer Ansage an und nicht Aktion für Aktion einzeln. Zu jeder Aktion gehört das Ziel.

- Die Ansage ist bindend. In der Ausführungs-Phase wird jede Handlung exakt wie angesagt ausgeführt. Die einzige Ausnahme ist das Nachsteuern bei Zielverlust (siehe unten).
- Die Ansage ist öffentlich. Wer später ansagt, kennt jede frühere Handlung samt Ziel.
- Die Reihenfolge ist aufsteigend: Wer die schlechteste Initiative hat, sagt zuerst an, wer die beste hat, zuletzt.

### Das Reaktionsfenster

Auf eine angesagte gegnerische Handlung kann ein Teilnehmer in derselben Kampfrunde nur dann noch reagieren, zum Beispiel mit einer Drehung, wenn seine Initiative besser ist als die der handelnden Partei. Nur dann sagt er nach ihr an, kennt also ihr Ziel, und führt vor ihr aus.

Ein Teilnehmer mit schlechterer Initiative sagt gegenüber diesem Angreifer blind an. Er führt erst aus, wenn die Handlung des Angreifers bereits aufgelöst ist. Dann greift stattdessen das Nachsteuern bei Zielverlust.

### Die Ausführung

Die Reihenfolge ist absteigend, also umgekehrt zur Ansage: Wer die beste Initiative hat, führt zuerst aus, wer die schlechteste hat, zuletzt. Jede Handlung läuft wie angesagt ab.

Erreicht eine Nahkampf-Gruppe in dieser Reihenfolge ihren Platz, wird sie in sich vollständig aufgelöst, bevor die Reihenfolge der Runde fortfährt ([[Nahkampf-Gruppen-und-das-Meisterscreen-Gitter]]).

### Nachsteuern bei Zielverlust

Ist das angesagte Ziel zum Zeitpunkt der Ausführung weg, weil es in Deckung gegangen, außerhalb des Sichtfelds oder tot ist, gilt:

- Die Handlung, die an das Ziel gebunden ist, muss nicht ausgeführt werden. Das sind die Nahkampf-Attacke, der Fernkampf-Schuss und die Vollendung eines Zaubers.
- Die dadurch frei gewordenen AK dürfen nur für eine Drehung oder eine Defensivaktion verwendet werden, für keine andere neue Handlung.
- Eine angesagte Laufen-Bewegung darf wahlweise ausgeführt oder unterlassen werden. Unterlässt der Teilnehmer sie, erlauben die frei gewordenen AK keine neue Bewegung. Auch dann sind nur Drehung oder Defensivaktion möglich.
- Das gilt gleichermaßen für Nahkampf, Fernkampf und Magie.

Wann ein Ziel „außerhalb des Sichtfelds“ ist, steht im Abschnitt zur Sicht. Zu Deckung siehe [[Deckung]].

### Beispiele

**Ini-Wert.** Ein Held hat Mut 12, Schnelligkeit 13, Intelligenz 11, Geschicklichkeit 12 und Athletik 13:

```text
(12 + 13) / 2        = 12,5, aufgerundet 13
(11 + 12 + 13) / 6   = 6
Runden-Ini-Wert      = 13 + 6 = 19
```

Mit Intelligenz 11, Geschicklichkeit 11 und Athletik 11 (Mut und Schnelligkeit wie oben) ist der zweite Teil 33 / 6 = 5,5, aufgerundet 6. Der Runden-Ini-Wert ist 13 + 6 = 19.

**Ini-Wurf und Reaktionsfenster.** A hat den Runden-Ini-Wert 19, B hat 14. Beide stehen nicht in Nahkampf-Reichweite. A würfelt W30 − W12 und erhält 8, seine Ini-Differenz ist 19 − 8 = 11. B würfelt 12, seine Ini-Differenz ist 14 − 12 = 2. A hat die bessere Initiative.

- Ansage, B vor A: B sagt blind „Fernkampf-Schuss auf A“ an. A sagt danach an, kennt also das Ziel von B, und wählt „Drehung plus Defensivaktion“.
- Ausführung, A vor B: A dreht sich und verteidigt, dann schießt B.

Hätte B die bessere Ini-Differenz geworfen, hätte A auf den später angesagten Schuss von B in dieser Kampfrunde nicht mehr reagieren können.

**Nachsteuern bei Zielverlust.** C hat „Fernkampf-Schuss auf D“ angesagt, das kostet 3 AK. In der Ausführungs-Phase ist D vor C an der Reihe und geht in Deckung. C muss nicht schießen. Die frei gewordenen AK darf C nur für eine Drehung oder eine Defensivaktion nutzen.

## Die zehn Schritte der Kampfrunde

Jede Kampfrunde läuft in dieser Reihenfolge ab:

1. **Initiative bestimmen.** Siehe „Die Initiative“.
2. **Umgebung bestimmen (Meister).** Der Meister legt fest: a) die Bedingungen und die generellen Erschwerungen ([[Behinderung-und-Erschwerung]], [[Fernkampf]]), b) den Kampfplatz und die Deckungsmöglichkeiten ([[Deckung]]), c) die Entfernungen. Er platziert und beschreibt jedes Ziel, das gesehen werden kann.
3. **Ansage der Aktionen.** Siehe „Ansage und Ausführung“.
4. **Aktionen ausführen.** Siehe „Ansage und Ausführung“. Die Aktionen sind a) Warten, b) Rufen (auch Gegner identifizieren), c) Orientierung, d) Bewegung, e) Waffe ziehen, f) Waffe laden, g) Nahkampf ([[Nahkampf-Gruppen-und-das-Meisterscreen-Gitter]]; das Umwerfen wird als Nahkampf-Attacke gewürfelt, [[Nahkampf-im-Kampf]]), h) Fernkampf ([[Fernkampf-im-Kampf]]), i) Magie ([[Magie-im-Kampf]]).
5. **Bruchtest.** Siehe die Klingenbruch-Probe in [[Nahkampf-im-Kampf]]. Beim Umwerfen entfällt der Bruchtest.
6. **Wirkung und Schaden.** In dieser Reihenfolge: Trefferzone würfeln, Deckung, Schild, Rüstungsschutz, Schaden, Lebensenergie, Gesundheit, Blutung notieren, Behinderung notieren, Selbstbeherrschungsprobe, gegebenenfalls Konzentrationsprobe ([[Treffer-und-Schaden]]).
7. **Kampfunfähigkeit.** Misslingt die Selbstbeherrschungsprobe ausreichend, dauert die Kampfunfähigkeit W15 + W6 Kampfrunden. Fehlen kampfnötige Gliedmaßen, werden Art und Zeit bestimmt ([[Zustaende-Katalog]]).
8. **Blutungen und Wunden.** Jeder Treffer über der Trefferschwelle führt zu einer Blutung. Sie kostet 1 Gesundheit pro Minute.
9. **Todesschwelle.** Siehe unten.
10. **Weiter bei Schritt 1** mit der nächsten Kampfrunde.

### Bewegungs-Rampe

In der 1. Kampfrunde ist die Höchstgeschwindigkeit Dauerlauf, ab der 2. Kampfrunde Sprint. Darunter ist die Geschwindigkeit frei wählbar. Wie die Bewegung auf dem Raster gezählt wird, steht in [[Bewegung]].

### Die Todesschwelle (Schritt 9)

Für lebende Helden gilt die Todesschwelle. Untote haben stattdessen die Untoten-Kampfunfähigkeitsschwelle, einen Schwellenwert je Trefferzone. Die Untoten-Kampfunfähigkeitsschwelle steht in [[Kreaturen-im-Kampf]], die Todesschwelle in [[Treffer-und-Schaden]]. Hier steht, wie die Todesschwelle in den Ablauf der Kampfrunde passt:

- **Gesundheit von 0 bis −Vitalität** (0 ≥ Gesundheit ≥ −Vitalität): Der Treffer löst eine Selbstbeherrschungsprobe aus. Der Ausgang ist rein binär. Bei einem meisterlichen oder fröhlichen Ergebnis ist der Held voll handlungsfähig. Bei jedem anderen Ergebnis ist er sofort bewusstlos. Die gestaffelte Selbstbeherrschungstabelle wird in diesem Fall nicht herangezogen.
- **Gesundheit −Vitalität − 1 oder weniger:** Der Held ist tot ([[Tod-und-Wiederbelebung]]).

Zur Wechselwirkung mit dem Blutrausch siehe [[Treffer-und-Schaden]].

### Dauer der Kampfrunde

Eine Kampfrunde dauert zurzeit eine Sekunde. Im Ablauf der Kampfrunde zählt jede Zeitangabe in Sekunden als Angabe in Kampfrunden. So steht die Angabe „W30 Sekunden“ bei der Kampfunfähigkeit in Schritt 7 für W15 + W6 Kampfrunden. Außerhalb des Kampfes bleiben Sekunde, Minute, Stunde und Tag reale Zeit. Sie werden nur ausdrücklich über die Dauer der Kampfrunde umgerechnet ([[Zeit-und-Spielablauf|Zeit und Spielablauf]]).

## Blickrichtung, Sichtfeld und Drehung

### Die Blickrichtung

Auf dem Hexraster ([[Bewegung]]) blickt jeder Teilnehmer in genau eine von sechs Richtungen. Sie liegen 60° auseinander und zeigen auf die sechs Nachbarfelder. Ein Zwischenwert ist nicht möglich. Jede Änderung der Blickrichtung springt um ein Vielfaches von 60°.

### Der Sichtkegel

Der Sichtkegel ist 120° breit und liegt symmetrisch um die Blickrichtung. Gesehen werden die Richtung geradeaus und die zwei Richtungen daneben, zusammen 3 der 6 Richtungen. Die Kante bei ±60° zählt voll als gesehen. Die übrigen 3 Richtungen bei ±120° und 180° bilden den toten Winkel.

Die sechs Nachbarrichtungen heißen N, NO, SO, S, SW und NW, wobei N die Blickrichtung ist. Bezogen auf das Ziel, das angegriffen wird, teilen sie sich in vier Klassen:

| Klasse | Richtungen | Winkel | im Sichtkegel des Ziels |
|---|---|---:|---|
| frontal | N | 0° | ja |
| seitlich | NO, NW | ±60° | ja, voll gesehen |
| hintere Flanke | SO, SW | ±120° | nein |
| direkt hinten | S | 180° | nein |

„Seitlich“ gilt als voll gesehen. Es gibt keine halbe Wahrnehmung. Die Klasse wird zum Zeitpunkt der Attacke bestimmt, bezogen auf die Blickrichtung, die das Ziel dann hat. Dreht sich das Ziel, verschieben sich die Klassen.

W und O liegen an Ecken des Feldes. Dort gibt es kein angrenzendes Feld. Wer bei W oder O steht, muss zum Nahkampf erst in ein Nachbarfeld einrücken. Für die Klasse zählt das Feld, in dem der Angreifer bei seiner Attacke steht.

„In Sicht“ ist ein Ziel, wenn es in einer der drei gesehenen Richtungen steht und nicht durch Deckung verdeckt ist.

### Drehung

Die Drehung ändert die Blickrichtung um 1, 2 oder 3 Schritte:

| Drehung | Schritte | Winkel | AK |
|---|---:|---:|---:|
| klein | 1 | 60° | 0 |
| mittel | 2 | 120° | 1 |
| groß | 3 | 180° | 2 |

- Eine Drehung um 3 Schritte kehrt die Blickrichtung um. Weiter als 180° gibt es nicht, denn die Gegenrichtung ist aus beiden Drehrichtungen in höchstens 3 Schritten erreichbar.
- Die Drehrichtung ist frei. Ein Schritt im Uhrzeigersinn und ein Schritt dagegen kosten beide 0 AK.
- Je Kampfrunde wird höchstens eine Drehung ausgeführt, gleich welcher Stufe. Eine angesagte Drehung darf in der Ausführungs-Phase gegen eine andere Stufe getauscht werden, zum Beispiel 120° gegen 180°, wenn das Budget reicht. Zwei kleine Drehungen hintereinander sind nicht zulässig. Wer 120° drehen will, sagt die Stufe 120° an.

Nach einer Drehung folgt der Sichtkegel der neuen Blickrichtung. Ein Ziel im toten Winkel kommt durch eine ausreichende Drehung ins Sichtfeld: Nach 1 Schritt ist das Feld bei 120° sichtbar, nach 2 Schritten das Feld bei 180°.

### Orientierung

Orientierung heißt, ein neues Ziel zu wählen. Die Blickrichtung ändert sich dabei nicht. Sie kostet keine AK.

- Ein Ziel, das schon im Sichtfeld steht, braucht keine Orientierung. Der Wechsel ist dann frei.
- Im Nahkampf gegen mehrere Gegner ist sie ebenfalls nicht nötig. Die Gegner in den angrenzenden Feldern gelten als durchgehend gegenwärtig.
- Steht das neue Ziel außerhalb des Sichtfelds, muss der Held sich zuerst hindrehen, damit es in den Sichtkegel kommt. Die Drehung kostet nach der Tabelle oben 0 bis 2 AK.

Orientierung ist also entweder gratis oder zieht eine Drehung nach sich.

### Was sichtbar ist

- **Meister-Setup.** Der Meister platziert und beschreibt nur Ziele, die gesehen werden können. Ein Gegner im toten Winkel eines Teilnehmers wird für diesen nicht angesagt. Daraus entstehen Überraschungsangriffe.
- **Außerhalb des Sichtfelds beim Zielverlust.** Das Ziel steht zum Zeitpunkt der Ausführung in einer der drei Richtungen des toten Winkels (SO, S, SW) des Handelnden. Das passiert zum Beispiel, wenn das Ziel sich seitlich vorbeibewegt hat oder wenn der Handelnde durch eine erzwungene Reaktion seine Blickrichtung verloren hat. Ein Ziel, das ein Hindernis verdeckt, ist in Deckung. Das ist ein eigener Auslöser des Nachsteuerns, siehe oben.
- **Deckung.** Sie verdeckt das Ziel: Es gilt als nicht mehr sichtbar ([[Deckung]]).

### Grenzfälle

- **Das Ziel bewegt sich seitlich vorbei.** Es kann vom Sichtfeld (±60°) in den toten Winkel (±120°) wechseln, ohne dass der Handelnde etwas tut. Zum Zeitpunkt der Ausführung ist das ein Zielverlust, es sei denn, der Handelnde hat die bessere Initiative und dreht sich hin.
- **Erzwungene Reaktion.** Muss der Held während des Ziehens oder Ladens einer Waffe ausweichen, verzögert sich diese Handlung. Eine Drehung wird ohne Verzögerung ausgeführt. Sie kostet 0 bis 2 AK.
- **Mehrere Gegner um den Helden.** Nur die Gegner in den drei gesehenen Richtungen sind in Sicht. In der Nahkampf-Gruppe entfällt die Pflicht zur Orientierung.
- **180°-Drehung bei einem Ziel genau hinter dem Helden.** Danach steht das Ziel frontal und ist voll im Sichtfeld.
- **Drehung als Nachsteuer-Option.** Beim Zielverlust erlauben die frei gewordenen AK nur Drehung oder Defensivaktion. Eine Drehung um bis zu 180° ist fast immer noch möglich, denn sie kostet 0 bis 2 AK.
- **Eine Drehung ändert die Lage zu allen Gegnern.** Die Klasse nach der Tabelle oben wird für jeden Angriff nach der Blickrichtung bei dessen Attacke neu bestimmt. Dreht sich ein überraschtes Ziel zum Angreifer hin, kommen dadurch andere Gegner aus dem toten Winkel in den Sichtkegel, und ein frontaler Gegner kann herausgedreht werden. Beispiel: Zwei Angreifer haben beide eine bessere Initiative als das Ziel. Der mit der besten Initiative greift überraschend aus S an, ein zweiter steht in SO. Dreht sich das Ziel um 180° zum Angreifer aus S, steht der zweite danach seitlich im Sichtkegel. Sein folgender Angriff ist „visuell“ (siehe unten), und das Ziel kann voll ausweichen.
- **Flucht statt Drehung.** Nimmt das überraschte Ziel den Angriff wahr, weil seine Gefahreninstinkt-Probe gelingt oder weil die Drehung den Angreifer in Sicht bringt, kann es statt zu drehen und zu kämpfen die Flucht ansagen: defensives Ausweichen plus Fliehen, zusammen 3 AK. Gelingt der Ablauf der Flucht, entgeht das Ziel den Attacken der übrigen Gegner der Gruppe. Die Gruppe löst sich für den Fliehenden auf ([[Nahkampf-Gruppen-und-das-Meisterscreen-Gitter]]).

## Überraschungsangriffe im Nahkampf

Wer im Nahkampf aus dem toten Winkel angreift, hat einen Vorteil, und der Verteidiger verteidigt sich schlechter. Zwei Dinge wirken zusammen: der Positions-Modifikator, der immer gilt, und der Wahrnehmungs-Zustand des Ziels, der darüber entscheidet, ob es noch ausweichen kann. Beides gilt nur für Nahkampf-Attacken, nicht für Fernkampf und Magie.

### Der Positions-Modifikator

Entscheidend ist das Feld, in dem der Angreifer im Moment seiner Attacke steht, bezogen auf die Blickrichtung, die das Ziel dann hat. Hat sich das Ziel in derselben Kampfrunde gedreht, zählt die neue Blickrichtung. Der Modifikator besteht aus zwei getrennten Verschiebungen der Erfolgsstufe ([[Behinderung-und-Erschwerung]]): Die Attacke-Klasse des Angreifers steigt um N Stufen, und die Parade-Klasse des Verteidigers sinkt um N Stufen. Die Erfolgsstufe der jeweiligen Probe rutscht also um N Stufen.

| Feld des Angreifers | Attacke-Klasse des Angreifers | Parade-Klasse des Verteidigers |
|---|:---:|:---:|
| N, frontal (0°) | – | – |
| NO und NW, seitlich (±60°) | – | −1 |
| SO und SW, hintere Flanke (±120°) | +1 | −1 |
| S, direkt hinten (180°) | +1 | −2 |

- Das +1 des Angreifers bei SO, SW und S ist sein Winkelvorteil. Es gilt immer, gleich ob das Ziel den Angriff wahrnimmt und wie es sich verteidigt, auch gegen ein Ausweichen.
- Der Malus trifft nur die Parade des Verteidigers. Das Ausweichen hängt nicht von der Blickrichtung ab und trägt nie einen solchen Malus.

### Der Wahrnehmungs-Zustand

Für jeden Nahkampf-Angriff hat das Ziel einen von drei Zuständen:

- **Visuell.** Der Angreifer steht bei seiner Attacke im Sichtkegel des Ziels (N, NO oder NW).
- **Verfolgt.** Der Angreifer steht im toten Winkel (SO, SW oder S), ist dem Ziel aber bekannt: Er hat in einer früheren Kampfrunde schon angegriffen, er war vorher in Sicht, oder ein Verbündeter hat ihn durch einen Ruf lokalisiert (Rufen kostet 0 AK). Verfolgt ist der Zustand auch, wenn das Ziel in dieser Kampfrunde seine Gefahreninstinkt-Probe besteht.
- **Überrascht.** Der Angreifer steht im toten Winkel, ist dem Ziel unbekannt (der Meister hat ihn nicht platziert) und das Ziel verfehlt seine Gefahreninstinkt-Probe.

Überrascht ist der eigentliche Überraschungsangriff. Ab der folgenden Kampfrunde ist der Angreifer bekannt.

### Die Gefahreninstinkt-Probe

Die Probe fällt in zwei Fällen: Bei einem Angriff aus dem toten Winkel von einem unbekannten Angreifer, das ist der Regelfall des echten Überraschungsangriffs, und bei jedem Entdecken, wenn dem Entdeckenden oder einem Schützling Gefahr droht. Das Zweite entscheidet der Meister.

Die Probe ist eine einfache Probe auf eine [[Grundfertigkeiten|Grundfertigkeit]], und zwar auf Sinnesschärfe plus der [[Sonderfertigkeiten|Sonderfertigkeit]] Gefahreninstinkt (zusammen „Sinnesschärfe + Gefahreninstinkt“).

- Jeder unbekannte Angreifer aus dem toten Winkel bekommt eine eigene Probe. Gelingt sie, ist der Zustand „verfolgt“. Misslingt sie, ist er „überrascht“.
- Im Standardfall ist die Probe nicht modifiziert. Der Meister darf sie für besondere Umstände erschweren, zum Beispiel bei einem vorbereiteten Hinterhalt. Er darf sie auch erleichtern.
- Ruft ein Verbündeter, der den Angreifer sieht, eine Warnung, ist der Angreifer dem Ziel bekannt (verfolgt). Eine Gefahreninstinkt-Probe ist dann nicht nötig.
- Der Spruch Unsichtbarkeit erschwert die Probe.
- Ab der Kampfrunde nach seinem ersten Angriff ist der Angreifer bekannt. Der Zustand ist dann „verfolgt“, und es gibt keine weitere Probe.

### Die Verteidigung je nach Zustand

| Zustand | Parade | Ausweichen (defensiv und offensiv) |
|---|---|---|
| visuell oder verfolgt | Positions-Malus der Tabelle oben | voll, ohne Erschwerung |
| überrascht | Positions-Malus plus ein weiteres −1, das bleibt | kein Ausweichen |

Der Angreifer behält in jedem Fall sein +1 bei SO, SW und S.

Einem Angriff, den es nicht kommen spürt, weicht das Ziel nicht aus. Es bleibt nur die zusätzlich erschwerte Parade, sofern das Budget an AK dafür reicht. Das Ausweichen ist entweder voll verfügbar oder gar nicht. Einen verminderten Ausweichmodus gibt es nicht.

### Die Reaktion auf einen Überraschungsangriff

- Das Ziel hat gegen einen unbekannten Angreifer aus dem toten Winkel nichts angesagt. Es reagiert mit seinem vollen Budget von 3 AK, unabhängig von der Initiative. Es kann eine Drehung (0, 1 oder 2 AK für 60°, 120° oder 180°, höchstens eine je Kampfrunde) und eine Verteidigung beliebig im Budget verbinden. Der Preis für das kalte Reagieren sind die Positions-Mali und, nach misslungener Gefahreninstinkt-Probe, das bleibende −1.
- Gezielt zum Angreifer hindrehen kann sich das Ziel nur nach bestandener Gefahreninstinkt-Probe, sonst kennt es die Richtung nicht. Die Spieler sollen kein Wissen nutzen, das ihr Held nicht hat. Nach einem Fehlschlag bleibt es beim Zustand „überrascht“: kein gezieltes Hindrehen, kein Ausweichen, nur die durch die Position erschwerte Parade mit dem bleibenden −1.
- Bringt eine Drehung den Angreifer bis zu seiner Attacke in den Sichtkegel, wird der Zustand „visuell“. Das Ausweichen ist wieder voll möglich, und der Positions-Modifikator richtet sich nach der neuen Richtung. Das bleibende −1 an der Parade bleibt, wenn die Probe vorher misslungen war. Es bleibt auch dann, wenn die Drehung aus einem anderen Grund erfolgt, etwa zu einem anderen, sichtbaren Gegner.
- Ab der nächsten Kampfrunde ist der Angreifer bekannt: Der Zustand ist „verfolgt“, es gibt keine Gefahreninstinkt-Probe und kein bleibendes −1. Ein weiterer Angriff aus dem toten Winkel trägt nur noch den Positions-Modifikator. Drehen und Verteidigen folgen dem normalen Ablauf der Kampfrunde.

### Beispiel: Angreifer aus S, Gefahreninstinkt gelungen

Das Ziel besteht die Gefahreninstinkt-Probe. Der Zustand ist „verfolgt“, das Ausweichen deshalb durchgehend voll. Das Ziel hat die vollen 3 AK.

- **Keine Drehung** (0 AK, 3 AK übrig): Der Angreifer steht bei S. Attacke-Klasse +1, Parade-Klasse −2. Ausweichen voll.
- **Drehung um 60°** (0 AK, 3 AK übrig): Der Angreifer steht bei SO oder SW. Attacke-Klasse +1, Parade-Klasse −1. Ausweichen voll.
- **Drehung um 120°** (1 AK, 2 AK übrig): Der Angreifer steht bei NO oder NW. Parade-Klasse −1. Ausweichen voll.
- **Drehung um 180°** (2 AK, 1 AK übrig): Der Angreifer steht bei N, frontal. Kein Positions-Modifikator. Ausweichen voll, aber mit nur 1 AK bleibt nur das defensive Ausweichen (1 AK). Eine Parade (2 AK) ist nicht mehr möglich.

Die Drehung um 60° ist umsonst: Sie kostet 0 AK und senkt den Malus der Parade von −2 auf −1. Größere Drehungen kosten AK, die dann für die Verteidigung fehlen, senken den Malus aber weiter.

Misslingt die Gefahreninstinkt-Probe, entfällt diese ganze Leiter. Es gibt keine gezielte Drehung und kein Ausweichen, nur die Parade: mit Attacke-Klasse +1 und Parade-Klasse −3 bei S, mit Attacke-Klasse +1 und Parade-Klasse −2 bei SO oder SW.

## Sichtfeld und Sichtqualität

Das Sichtfeld sagt, wohin der Held schaut. Wie gut er sieht, ist unabhängig davon. Ein Ziel kann im Sichtfeld stehen und trotzdem durch Nebel oder Blindheit erschwert sein.

- **Blindheit.** Ein Blinder bekommt eine Erschwerung von 18 plus den Malus aus den Komplementärsinnen ([[Aussehen-Schlaf-Sinne-und-Koerper]]). Sie gilt für Attacke, Parade, Ausweichen und Fernkampf und für Magie und Zauber mit einem anderen Ziel als Selbst oder Berührung. Blindheit ist eine eigene Erschwerung und keine Behinderung.
- **Nebel, Dämmerung, Nacht, absolute Dunkelheit, Geblendetsein, Fackel- und Laternenlicht.** Sie wirken als Sicht-Erschwerungen der Fernkampf-Modifikatoren ([[Fernkampf]]).
- **Sichthilfen** (Dämmerungssicht, Nachtsicht, Astralsicht). Sie ersetzen den Modifikator der Sicht-Erschwerung durch einen eigenen Wert ([[Fernkampf]], [[Aussehen-Schlaf-Sinne-und-Koerper]]).
