---
title: Alchemika
aliases: [Alchemika, Alchemikum, Gift, Trank, Salbe, Parfum, Alchemieresistenz, Alchemieresistenz-Probe, Giftresistenz, Potenz, Zufuhr, Dosis, Antidot, Zeit bis Symptom, Zeit bis Wirkung, Legalität, Verkaufspreis]
status: entwurf
---

# Alchemika

Ein Alchemikum ist ein Gift, ein Trank, eine Salbe oder ein Parfum. Es wirkt erst, wenn es auf seinem Zufuhrweg in den Körper gelangt ist und das Ziel die Alchemieresistenz-Probe nicht bestanden hat. Das gilt für jedes Alchemikum, auch für einen Heiltrank.

## Die Angaben eines Alchemikums

Jedes Alchemikum hat diese Angaben:

- **Zufuhr:** der Weg, auf dem es in den Körper gelangen muss.
- **Zeit bis Symptom:** die Zeit zwischen der Einnahme und der Alchemieresistenz-Probe. Sie entspricht der Vorbereitungsdauer ([[Magie-Wirkungsdauer-und-Konzentration|Magie: Wirkungsdauer und Konzentration]]).
- **Zeit bis Wirkung:** die Zeit zwischen der misslungenen Probe und der vollen Wirkung. Sie entspricht der Effektdauer.
- **Wirkungsdauer:** die Zeit, für die die volle Wirkung anhält.
- **Wirkung:** was das Alchemikum mit den Werten des Ziels tut.
- **Dosierbar:** ja oder nein.
- **Potenz:** wie schwer es ist, dem Alchemikum zu widerstehen.
- **Magisch oder profan.**
- **Legalität:** eine Zahl von 1 bis 7.
- **Verfügbarkeit.**
- **Zutatenpreis und Kaufpreis** in Dublonen.

Es gibt 118 Alchemika in fünf Kategorien: 47 Gifte, 30 Heiltränke, 22 Kampftränke, 14 Zustandstränke und 5 Parfums.

## Zufuhr

Die Zufuhr legt fest, wann ein Alchemikum als eingenommen gilt.

| Zufuhr | Bedingung |
|---|---|
| Nahrung | Das Ziel muss es schlucken. |
| Körper | Es muss in den Körper gelangen: durch einen Treffer, der mindestens 1 [[Glossar#TP\|Trefferpunkt (TP)]] verursacht, oder durch Kontakt mit einer Schleimhaut. |
| Kontakt | Eine Berührung der Haut genügt. Kommt das Alchemikum über einen Treffer, muss der Treffer mehr als 0 TP verursachen. |
| Blut | Es muss in die Blutbahn gelangen: durch einen Treffer über der [[Glossar#TS\|Trefferschwelle (TS)]] oder durch eine Injektion in eine Vene. |
| Gas | Das Ziel muss es einatmen. |

Bei einem Treffer zählen die TP, also der Schaden nach Rüstung und anderem Schutz ([[Treffer-und-Schaden|Treffer und Schaden]]).

Ein Wesen, das nicht atmet, nimmt kein Gas auf, zum Beispiel unter der Wirkung von „Lufttrank“ oder „Luftunabhängigkeit“. Ein Parfum mit der Zufuhr Gas wirkt auf den Träger, der es trägt und einatmet, nicht auf Umstehende.

## Von der Einnahme bis zum Ende der Wirkung

1. **Einnahme.** Das Alchemikum gelangt auf seinem Zufuhrweg in den Körper. Die Zeit bis Symptom verstreicht.
2. **Probe.** Am Ende der Zeit bis Symptom würfelt das Ziel die Alchemieresistenz-Probe. Steht bei Zeit bis Symptom „Sofort“, würfelt es gleich bei der Einnahme.
3. **Erfolg.** Das Alchemikum hat keine Wirkung. Zeit bis Wirkung und Wirkungsdauer entfallen.
4. **Fehlschlag.** Die Zeit bis Wirkung beginnt. Währenddessen wirkt das Alchemikum mit halber Wirkung. Danach wirkt es mit voller Wirkung, die für die Wirkungsdauer anhält. Steht bei Zeit bis Wirkung „Sofort“, tritt die volle Wirkung sofort ein.

Zwei Arten von Wirkungen weichen in Schritt 4 ab:

- **Einmalwirkungen.** Tritt die Wirkung nur einmal ein (Heilung, Gewinn oder Verlust einer Ressource, Schaden, Alterung, Heilung einer Krankheit, eine erzwungene Probe), passiert während der Zeit bis Wirkung nichts. Die Wirkung tritt an ihrem Ende vollständig ein.
- **Wiederkehrende Wirkungen.** Nennt die Wirkung eine Wiederholung, zum Beispiel „W8 pro Minute“, passiert während der Zeit bis Wirkung ebenfalls nichts. Die Wiederholungen beginnen mit der Wirkungsdauer, die erste gleich zu ihrem Beginn. In jedem Intervall tritt die Wirkung einmal ein, und das Ziel würfelt eine neue Alchemieresistenz-Probe. Die erste gelungene Probe beendet die Wirkung sofort und vollständig.

Die halbe Wirkung während der Zeit bis Wirkung gilt also nur für Wirkungen, die anhalten.

Steht bei der Wirkungsdauer „permanent“, endet die volle Wirkung nicht von selbst. Sie endet, wenn sie geheilt wird oder wenn eine spätere Probe durch ein Antidot gelingt.

## Die Alchemieresistenz-Probe

Die Probe entscheidet, ob ein Alchemikum wirkt. Das Ziel würfelt sie bei jeder Einnahme, ob freiwillig oder nicht, ob das Mittel schadet oder nützt. Es kann nicht auf die Probe verzichten.

### Der Alchemieresistenz-Wert

```text
Alchemieresistenz-Wert = Konstitution + 3 × Vitalität + Sonderfertigkeit Alchemieresistenz
```

[[Eigenschaften|Konstitution]] ist eine Eigenschaft, [[Attribute|Vitalität]] ein Attribut. Die [[Sonderfertigkeiten|Sonderfertigkeit]] Alchemieresistenz hat nur, wer den zugehörigen Vorteil besitzt ([[Vor-und-Nachteile|Vor- und Nachteile]]). Ohne ihn ist sie 0.

Wirkungen können den Alchemieresistenz-Wert verändern. Die [[KI|KI-Fähigkeit]] „Abhärtung“ zum Beispiel erhöht ihn.

### Der Probenwert

```text
Probenwert = Alchemieresistenz-Wert − wirksame Potenz − Malus aus Anfälligkeit + Bonus aus Antidot
wirksame Potenz = Potenz × Dosis-Faktor
```

Die wirksame Potenz wird gleich nach der Multiplikation gerundet ([[Wuerfeln-und-Proben|Würfeln und Proben]]).

Körperliche und Mentale [[Behinderung-und-Erschwernis|Behinderung]] werden bei dieser Probe nicht abgezogen.

Der Probenwert hat keine Untergrenze und keine Obergrenze. Er kann 0 oder negativ sein. Dann gelingt die Probe nur noch mit einer gewürfelten 1.

### Dosis

Bei einem dosierbaren Alchemikum erschwert eine höhere Dosis die Probe:

| Dosis | ×2 | ×3 | ×4 | ×5 | ×6 | ×7 | ×8 | ×9 | ×10 |
|---|---|---|---|---|---|---|---|---|---|
| Faktor | 1,5 | 1,75 | 1,87 | 1,93 | 1,96 | 1,97 | 1,97 | 1,97 | 1,97 |

Ohne erhöhte Dosis ist der Faktor 1.

Die Dosis erschwert nur die Probe. Sie erhöht nie die Wirkung.

Acht Alchemika sind nicht dosierbar: die vier Stufen des Waffengifts, die drei Stufen des Nahrungsgifts und die Geruchslossalbe. Ihr Faktor ist immer 1. Man kann darin baden, ohne dass das Gift potenter wird.

### Anfälligkeit gegen Alchemie

Hat der Held den Nachteil „Anfälligkeit gegen Alchemie“, sind alle seine Alchemieresistenz-Proben um einen festen Betrag erschwert:

| Stufe | gering | leicht | mittel | schwer | sehr schwer | extrem |
|---|---|---|---|---|---|---|
| Malus | 5 | 10 | 15 | 20 | 25 | 30 |

Ein Held hat höchstens eine Stufe dieses Nachteils. Wer ihn hat, kann die Sonderfertigkeit Alchemieresistenz nicht steigern.

### Wurf und Ergebnis

Der Held würfelt W30 − W12. Die Probe gelingt, wenn der Wurf höchstens so hoch ist wie der Probenwert. Sie misslingt, wenn der Wurf höher ist.

- Eine gewürfelte 1 ist immer ein Erfolg.
- Ein Patzer ist immer ein Fehlschlag. Eine weitere Folge hat der Patzer nicht.

Die Erfolgsstufe wird wie bei jeder Probe bestimmt. Für das Alchemikum zählt nur, ob die Probe gelingt:

- **Erfolg jeder Stufe:** Das Alchemikum hat keine Wirkung. Das gilt auch für ein nützliches Mittel: Der Heiltrank versagt dann. Ein hoher Alchemieresistenz-Wert ist deshalb zweischneidig.
- **Fehlschlag oder Patzer:** Das Alchemikum wirkt.

Bei einer Wirkung ohne Wiederholung bleibt es bei dieser einen Probe. Eine neue Probe gibt es dann nur durch ein Antidot.

### Antidot

Ein Antidot gibt dem Helden eine neue Probe mit einem Bonus:

| Antidot | Bonus |
|---|---|
| Leichtes Antidot | +25 |
| Antidot | +35 |
| Starke Antidot | +45 |

Das Antidot wirkt selbst erst nach seiner Zeit bis Symptom und seiner Zeit bis Wirkung. 3 Kampfrunden danach würfelt der Held einmal. Der Wurf gilt für alle Alchemika, die gerade auf ihn wirken: Er wird mit dem Probenwert jedes dieser Alchemika verglichen, den Bonus eingerechnet. Jedes Alchemikum, dessen Probenwert der Wurf erreicht, endet. Das gilt auch für eine permanente Wirkung.

### Mehrere Alchemika

Für jedes Alchemikum würfelt das Ziel eine eigene Alchemieresistenz-Probe.

## Die Wirkung

Die Wirkung eines Alchemikums verändert bestimmte Werte des Ziels, zum Beispiel eine Probe, die [[Glossar#LE|Lebensenergie (LE)]], das Mana, den [[Glossar#RS|Rüstungsschutz (RS)]] oder die Trefferschwelle.

### Halbe Wirkung

Während der Zeit bis Wirkung wirkt ein Alchemikum mit halber Wirkung:

- **Die Wirkung hat einen Zahlenwert** (eine Erschwernis, eine Behinderung, einen Zuschlag auf die Trefferschwelle, Schaden, Heilung, einen Bonus auf einen Wert): Dieser Wert wird halbiert.
- **Die Wirkung hat keinen Zahlenwert** (zum Beispiel „artikuliertes Sprechen unmöglich“ oder „fällt in Schlaf“): Der Meister legt eine abgeschwächte Variante fest. Wer stumm werden wird, kann zum Beispiel zeitweise nicht sprechen.

In beiden Fällen tritt die volle Wirkung am Ende der Zeit bis Wirkung ein.

Ein halbierter Wert hat keine Untergrenze außer 0. Aus 2,25 wird 3, aus 1,75 wird 2, aus 4,5 wird 5. Betrifft die Wirkung eine [[Nahkampf|Waffenklasse]], wird sie auf halbe Punkte gerundet.

### Gewürfelte Werte

Steht in der Wirkung oder in der Dauer ein Würfel, wird er einmal gewürfelt, wenn die Wirkung beginnt: am Ende der Zeit bis Symptom nach der misslungenen Probe. Das Ergebnis gilt für die ganze Wirkungsdauer. Während der Zeit bis Wirkung gilt die Hälfte desselben Wurfs. Wiederkehrende Wirkungen würfeln bei jeder Wiederholung neu.

### Blendgift

Ein Blendgift macht das Opfer für die Wirkungsdauer blind. Blind heißt: eine Erschwernis von 18 + K-Mod auf Nahkampf, Fernkampf und Zauber, außer bei Zaubern mit dem Ziel „Selbst“ oder „Berührung“. Der [[Glossar#K-Mod|K-Mod]] ist der Malus aus den Komplementärsinnen des Opfers ([[Aussehen-Schlaf-Sinne-und-Koerper|Aussehen, Schlaf, Sinne und Körper]]). Fernangriffe sind nur als Deutschüsse mit dem Wert 18 + K-Mod möglich ([[Fernkampf-im-Kampf|Fernkampf im Kampf]]). „Blinder Kampf“ verringert die Erschwernis, aber nur gegen Ziele bis 10 m. Diese Erschwernis ist keine Behinderung.

Das Blendgift wirkt nur auf den Zielsinn. Während der Zeit bis Wirkung wird deshalb nur die 18 halbiert, der K-Mod kommt unverändert dazu: Es gilt 9 + K-Mod, danach 18 + K-Mod.

### Giftschaden

Der Schaden von Waffengift und Jagdgift wirkt als TP direkt auf die [[Glossar#TZ|Trefferzone]], durch die das Gift eingedrungen ist. Rüstungsschutz, Trefferzonen-Faktor und Kritisch-Faktor gelten dafür nicht. Der Schaden zählt für die [[Glossar#SB|Selbstbeherrschungs-Probe]] (TP über der Trefferschwelle). Eine Wunde entsteht nicht, wenn die TP nur durch das Gift über die Trefferschwelle steigen.

### Der Alchemieresistenz-Trank

Der Zustandstrank „Alchemieresistenz“ wirkt 2 Stunden. Jede Wirkung eines Alchemikums, die in dieser Zeit eintritt, hat nur den halben Zahlenwert. Aus dem Schaden wird zum Beispiel der halbe Schaden.

- Die Wirkungsdauer halbiert er nicht.
- Wirkungen ohne Zahlenwert verändert er nicht.
- Er halbiert auch nützliche Alchemika.
- Er halbiert auch Alchemika, die nicht dosierbar sind.

Er verändert nicht die Alchemieresistenz-Probe, nur die Wirkung nach einer misslungenen Probe.

### Mehrere Alchemika zugleich

Wirken mehrere Alchemika mit gleichartiger Wirkung, zählt nur das höchste Ergebnis. Die Werte addieren sich nicht. Jeder Wert wird zuerst einzeln bestimmt, Würfel werden einzeln gewürfelt, dann werden die Ergebnisse verglichen. Es zählt also nicht der größere Würfel, sondern der höhere Wurf.

Verschiedenartige Wirkungen gelten nebeneinander.

Einmalwirkungen mehrerer Alchemika addieren sich.

Boni aus Alchemika addieren sich zu Wirkungen aus [[KI]], [[Spruchmagie]] und [[Artefakte|Artefakten]]. Das höchste Ergebnis zählt nur zwischen mehreren Alchemika.

### Zwei Halbierungen

Treffen zwei Halbierungen zusammen (die halbe Wirkung während der Zeit bis Wirkung, der Alchemieresistenz-Trank, „Resistenz gegen magische Heilung“), gilt der Wert × 0,25. Er wird nur einmal gerundet.

## Untote und andere Wesen

Auf Untote wirken nur magische Alchemika. Ein profanes Alchemikum hat auf einen Untoten keine Wirkung, und er würfelt keine Alchemieresistenz-Probe.

Für lebende Tiere und Wesen gelten Zufuhr, Probe und Wirkung wie für Helden.

## Anwendung und Haltbarkeit

Jedes Alchemikum hat eine Anwendung. Auf eine Waffe aufgetragen, wirkt es auf den ersten Treffer, der Haut berührt. Danach ist es verbraucht.

Ein Alchemikum hält 77 Jahre, im Leben eines Helden also praktisch unbegrenzt.

Ein Gift der Waffengift-Familie, das auf eine Waffe aufgetragen ist, hält nur bis zum Ende des nächsten Kampfes, in dem die Waffe eingesetzt wird. Ein Kampf, in dem der Held die Waffe nicht benutzt, verbraucht das Gift nicht.

## Legalität und Verfügbarkeit

Die Legalität reicht von 1 (legal) bis 7 (Todesstrafe). Welche Folgen Besitz und Handel haben, legt der Meister fest. Sie unterscheiden sich von Volk zu Volk. Die Legalität bestimmt außerdem den Preis.

Die Verfügbarkeit folgt derselben Skala wie bei allen Gütern ([[Gueter-Preise-und-Verfuegbarkeit|Güter, Preise und Verfügbarkeit]]): 1 bis 2 ist immer verfügbar, 3 bis 7 wird gewürfelt, darüber ist ein Alchemikum nur über ein Ruhm-Ereignis zu bekommen.

## Preis

Jedes Alchemikum hat einen Zutatenpreis in Dublonen. Der Kaufpreis in der Liste der Alchemika sind die Herstellungskosten des Alchemisten:

```text
Herstellungskosten = Zutatenpreis × Legalität
```

Jeder Käufer zahlt das Doppelte, auch ein Held, auch für legale Ware:

```text
Verkaufspreis = Zutatenpreis × Legalitäts-Faktor × 2
```

Der Legalitäts-Faktor ist die Legalität. Unterwelt-Kontakte des Käufers senken ihn:

| Kontakt des Käufers | Abzug |
|---|---|
| Dealer | −1 |
| Diebesgilde | −2 |
| Kriminelle Organisation | −3 |

- Es zählt nur ein Kontakt des Käufers. Die Abzüge addieren sich nicht.
- Bei Legalität 1 wirkt der Abzug nicht. Der Faktor ist 1.
- Ab Legalität 2 wird der Abzug von der Legalität abgezogen. Der Faktor ist mindestens 1.

Der niedrigste Verkaufspreis ist deshalb Zutatenpreis × 2. Ohne Unterwelt-Kontakt ist der Verkaufspreis das Doppelte des Kaufpreises aus der Liste.

Der Verkaufspreis wird einmal am Ende auf 3 Nachkommastellen gerundet. Zwischenwerte werden nicht gerundet.

Der Preis wird beim Kauf bestimmt, aus dem Kontakt des Helden, der kauft. Alchemika werden nach dieser Rechnung bezahlt, nicht nach der Preisliste der Güter.

## Beispiele

### Probe

Ein Held hat Konstitution 12, Vitalität 5 und die Sonderfertigkeit Alchemieresistenz 8. Sein Alchemieresistenz-Wert ist 12 + 15 + 8 = 35.

- **Behinderungsgift, Potenz 15.** Der Probenwert ist 35 − 15 = 20. Würfelt der Held höchstens 20, wirkt das Gift nicht. Würfelt er mehr oder patzt er, hat er eine Stunde lang eine Behinderung von W6. Bei einer gewürfelten 1 wirkt das Gift nie.
- **Dasselbe Gift in dreifacher Dosis.** Der Faktor ist 1,75. Die wirksame Potenz ist 15 × 1,75 = 26,25, also 27. Der Probenwert ist 35 − 27 = 8.
- **Antidot gegen Blendgift.** Dem Helden misslingt die Probe gegen ein Blendgift (Potenz 15, Wirkungsdauer 1 Stunde). Er trinkt ein Antidot. 7 Kampfrunden nach der Einnahme, 3 Kampfrunden nachdem das Antidot wirkt, würfelt er neu. Der Probenwert ist 35 − 15 + 35 = 55. Der Erfolg ist praktisch sicher, die Blindheit endet.
- **Heiltrank, Potenz 45.** Der Probenwert ist 35 − 45 = −10. Nur bei einer gewürfelten 1 widersteht der Held, dann wirkt der Heiltrank nicht. Bei jedem anderen Wurf wirkt er normal.

### Ablauf und Wirkung

- **Leichtes Managift** (magisch, Potenz 5, Zufuhr Blut, Zeit bis Symptom und Zeit bis Wirkung „Sofort“, Wirkungsdauer permanent, Wirkung: Mana −4W6). Ein Treffer über der Trefferschwelle bringt das Gift ins Blut. Der Getroffene würfelt sofort. Misslingt die Probe, verliert er sofort und permanent 4W6 Mana. Hat er vorher einen Alchemieresistenz-Trank getrunken, verliert er die Hälfte: Bei einer gewürfelten 15 sind das 7,5, also 8.
- **Leichtes Behinderungsgift** (profan, Potenz 5, Zufuhr Körper, Zeit bis Symptom 1 Kampfrunde, Zeit bis Wirkung 2 Kampfrunden, Wirkungsdauer 1 Stunde, Wirkung: Behinderung W4). Ein Treffer mit mindestens 1 TP bringt das Gift in den Körper. Eine Kampfrunde später würfelt der Getroffene. Misslingt die Probe, würfelt er den W4, zum Beispiel eine 3. Zwei Kampfrunden lang hat er die halbe Behinderung, also 2. Danach hat er eine Stunde lang die volle Behinderung 3.
- **Leichtes Blendgift** (profan, Potenz 5, Zufuhr Körper, Zeit bis Symptom 1 Kampfrunde, Zeit bis Wirkung 3 Kampfrunden, Wirkungsdauer 1 Stunde). Misslingt die Probe, hat das Opfer 3 Kampfrunden lang eine Erschwernis von 9 + K-Mod, danach eine Stunde lang 18 + K-Mod. Ein Opfer mit K-Mod 6 hat erst 15, dann 24.
- **Zwei Behinderungsgifte.** Ein Held steht zugleich unter Leichtem Behinderungsgift (Behinderung W4) und Behinderungsgift (Behinderung W6). Für jedes Gift hat er eine eigene Probe gewürfelt. Der W4 zeigt 4, der W6 zeigt 2. Es gilt die Behinderung 4.
- **Waffengift auf der Klinge** (profan, Zufuhr Kontakt, Wirkungsdauer permanent). Die Beschichtung hält bis zum Ende des nächsten Kampfes, in dem der Held die Klinge führt. Trifft die Klinge ein Ziel mit mehr als 0 TP und misslingt dessen Probe, erleidet die getroffene Zone W10 TP durch das Gift.

### Preis

Ein Alchemikum hat den Zutatenpreis 10.

- **Legalität 3, Käufer ohne Kontakt.** Der Faktor ist 3. Die Herstellungskosten sind 10 × 3 = 30. Der Verkaufspreis ist 10 × 3 × 2 = 60 Dublonen.
- **Legalität 3, Käufer mit Kontakt zur Diebesgilde.** Der Faktor ist 3 − 2 = 1. Der Verkaufspreis ist 10 × 1 × 2 = 20 Dublonen.
- **Legalität 6, Käufer mit Kontakt zu einer Kriminellen Organisation.** Der Faktor ist 6 − 3 = 3. Der Verkaufspreis ist 10 × 3 × 2 = 60 Dublonen.
- **Legalität 1, Käufer mit Kontakt zu einem Dealer.** Der Abzug wirkt nicht, der Faktor ist 1. Der Verkaufspreis ist 10 × 1 × 2 = 20 Dublonen.
- **Legalität 2, Käufer mit Kontakt zu einer Kriminellen Organisation.** 2 − 3 = −1, der Faktor ist deshalb 1. Der Verkaufspreis ist 10 × 1 × 2 = 20 Dublonen.
