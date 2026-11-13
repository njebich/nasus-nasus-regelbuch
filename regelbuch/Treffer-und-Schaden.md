---
title: Treffer und Schaden
aliases: [Treffer und Schaden, Treffer-und-Schaden, Trefferzonen, Trefferzonen-Tabelle, Trefferzone, Streiftreffer, Schadenspipeline, Schadensberechnung, Leberschutz, Weiterleitung, Weiterleitung an die Gesundheit, Sturzschaden, Schadensart, Scharf, Durchbohrend, Stumpf, Trefferzonen-Rerolls, TZ-Rerolls, Trefferzonen-Rerolls, Rerolls, Rerolls im Kampf, Rerolls im Kampf, Selbstbeherrschung, SB-Probe, Selbstbeherrschungsprobe, Selbstbeherrschungstabelle, Trefferschwelle, TS, Konzentrationsprobe, Blutrausch, Todesschwelle im Kampf, Untoten-Kampfunfähigkeitsschwelle, Verlorenen Gegenstand aufheben]
status: entwurf
---

# Treffer und Schaden

Landet ein Treffer, würfelt der Spieler mit einem W100, welche Trefferzone er trifft. Deckung, Schild und Rüstung mindern den Schaden, der Rest fällt von der Lebensenergie der Zone ab und, wenn die Zone leer ist, von der Gesundheit. Ist der Treffer schwer genug, muss der Getroffene eine Selbstbeherrschungsprobe würfeln. Dieses Kapitel beschreibt die Trefferzonen, die Schadensart, die Berechnung des Schadens, den Sturzschaden, die Selbstbeherrschungsprobe, den Blutrausch und die Rerolls, mit denen Spieler Würfe im Kampf verändern.

Zwischenergebnisse der Schadensberechnung werden an den benannten Stellen sofort auf eine ganze Zahl aufgerundet ([[Wuerfeln-und-Proben|Würfeln und Proben]]). Wo eine Rechnung abweicht, steht es an der Stelle.

## Der Weg eines Treffers

Ein Treffer im Nahkampf ist der Ausgang „Treffer“ des Meisterscreen-Gitters ([[Nahkampf-Gruppen-und-das-Meisterscreen-Gitter]]), ein Treffer im Fernkampf oder mit einem Zauber ist die Wirkung, die die Verteidigung nicht verhindert hat ([[Fernkampf-im-Kampf]], [[Magie-im-Kampf]]). Danach läuft immer dieselbe Kette ab:

1. **Trefferzone würfeln.** Ein W100 bestimmt die Zone. Wer die Zone lenken darf, steht unter „Die Zone lenken“.
2. **Deckung.** Ist die getroffene Zone gedeckt, wird zuerst der Deckungs-Rüstungsschutz vom rohen Schaden abgezogen ([[Deckung]]).
3. **Schadenspipeline.** Schild, Rüstungsschutz, Schaden, Lebensenergie und Gesundheit durchlaufen sieben feste Schritte („Die Schadenspipeline“ und „Weiterleitung an die Gesundheit“).
4. **Blutung notieren.** Manche Zonen verursachen bei einem schweren Treffer eine Blutung ([[Zustaende-Katalog]]).
5. **Behinderung notieren.** Fällt die Lebensenergie einer Zonengruppe auf 0, entsteht eine Behinderung („Die Trefferzonen“).
6. **Selbstbeherrschungsprobe.** Übersteigt der Schaden die Trefferschwelle, würfelt der Getroffene diese Probe.
7. **Konzentrationsprobe.** Misslingt die Selbstbeherrschungsprobe, während der Getroffene etwas aufrechterhält, das Konzentration verlangt, folgt die Probe auf den Mentalen Fokus ([[Magie-Wirkungsdauer-und-Konzentration|Magie: Wirkungsdauer und Konzentration]]).

Was nach einer misslungenen Selbstbeherrschungsprobe in den folgenden Kampfrunden geschieht, steht in [[Kampfrunde-Aktionen-Initiative-und-Sicht]]. Zustände wie Benommenheit, Straucheln, Sturz, Kampfunfähigkeit und Bewusstlosigkeit beschreibt [[Zustaende-Katalog]].

## Die Trefferzonen

Jeder Treffer wird mit einem einzigen W100 einer Trefferzone zugeordnet. Die Tabelle gilt für Nahkampf und Fernkampf gleichermaßen. Es gibt keine getrennten Tabellen. Die Zonen gehören zu sieben Gruppen: Kopf, Brust, Unterleib, rechter Arm, linker Arm, rechtes Bein und linkes Bein. Auf diese Gruppen beziehen sich die Lebensenergie ([[Glossar#LE|LE]]), die Weiterleitung des Überschusses und die Selbstbeherrschungsprobe.

| W100 | Zone | Gruppe | Behinderung bei LE 0 |
|---|---|---|---:|
| 1 | Auge | Kopf | 5 |
| 2–3 | Hals | Kopf | 5 |
| 4–11 | Kopf | Kopf | 5 |
| 12–13 | Herz und/oder Lunge | Brust | 2 |
| 14 | Linkes Schultergelenk | Brust | 2 |
| 15 | Rechtes Schultergelenk | Brust | 2 |
| 16–36 | Brust | Brust | 2 |
| 37–41 | Organe (Unterleib) | Unterleib | 2 |
| 42–51 | Unterleib | Unterleib | 2 |
| 52 | Rechter Ellenbogen | Rechter Arm | 3 |
| 53–54 | Rechte Hand | Rechter Arm | 3 |
| 55–64 | Rechter Arm | Rechter Arm | 3 |
| 65 | Linker Ellenbogen | Linker Arm | 3 |
| 66–67 | Linke Hand | Linker Arm | 3 |
| 68–77 | Linker Arm | Linker Arm | 3 |
| 78–79 | Rechtes Knie | Rechtes Bein | 4 |
| 80 | Rechter Fuß | Rechtes Bein | 4 |
| 81–87 | Rechtes Bein | Rechtes Bein | 4 |
| 88–89 | Linkes Knie | Linkes Bein | 4 |
| 90 | Linker Fuß | Linkes Bein | 4 |
| 91–97 | Linkes Bein | Linkes Bein | 4 |
| 98–100 | Streiftreffer | neu gewürfelt | – |

Kreaturen mit anderem Körperbau haben eigene Tabellen ([[Kreaturen-im-Kampf]]).

### Zusatzeffekte der Zonen

Die Trefferpunkte (TP, [[Glossar#TP|TP]]) sind der Schaden nach der Rüstung, die Trefferschwelle ([[Glossar#TS|TS]]) erklärt der Abschnitt zur Selbstbeherrschungsprobe. Die Kampfklasse (KK) fasst die Attacke-, Parade-, Ausweich- und Fernkampf-Klasse zusammen. Senkt ein Effekt die KK, sinken alle vier gleichermaßen.

- **Auge, Ellenbogen, Knie.** Die Trefferpunkte werden mit 2 malgenommen. Das gilt für das Auge (1), den rechten Ellenbogen (52), den linken Ellenbogen (65), das rechte Knie (78–79) und das linke Knie (88–89).
- **Hals.** Bei TP > TS entsteht eine zusätzliche Blutung.
- **Kopf.** Die Selbstbeherrschungsprobe ist zusätzlich um TP × 2 erschwert.
- **Herz und/oder Lunge, Organe (Unterleib).** Bei TP > TS entsteht eine zusätzliche Blutung.
- **Schultergelenk.** Bei TP > TS kann der Arm auf der Seite des Gelenks W4 + 2 Kampfrunden (KR) nicht benutzt werden. Alle zweihändigen Nahkampf- und Fernkampf-Fähigkeiten sind in dieser Zeit gesperrt. Zusätzlich sinken die Attackeklasse und die Paradeklasse um je 1. Der Wurf 14 betrifft den linken, der Wurf 15 den rechten Arm.
- **Hand.** Misslingt die Selbstbeherrschungsprobe, ist die Waffe entwaffnet: Die Paradeklasse sinkt für den Rest der laufenden Kampfrunde um 1. Danach braucht der Held W4 Kampfrunden, um die Waffe zu lokalisieren, und nimmt sie in der Kampfrunde danach auf. Das gilt für die rechte (53–54) wie für die linke Hand (66–67).
- **Fuß.** Bei TP > TS würfelt der Getroffene eine Probe aus Körperbeherrschung und Athletik, erschwert um die Trefferpunkte. Misslingt sie, stürzt er: Die Kampfklasse sinkt um 2, und der Zustand hat keine feste Dauer. Der Sturz ist derselbe Zustand wie im Band 10 bis 11 der Selbstbeherrschungstabelle, nur hier über einen eigenen Auslöser erreicht. Jeder Eintritt von Sturz löst einen Sturzschaden-Wurf aus. Das gilt für den rechten (80) und den linken Fuß (90).
- **Brust, Unterleib, Arme, Beine.** Kein Zusatzeffekt.

### Behinderung bei Lebensenergie 0

Fällt die Lebensenergie einer Zonengruppe auf 0, entsteht eine Behinderung in Höhe des Werts der letzten Spalte. Geschieht das durch einen einzigen Treffer, der die volle Lebensenergie der Gruppe auf 0 bringt, verdoppelt sich der Wert. Alle Zeilen einer Gruppe haben denselben Wert. Der Wert wirkt als Körperliche (KBE) und als Mentale Behinderung (MBE) ([[Behinderung-und-Erschwerung]]).

### Streiftreffer

Ein Wurf von 98 bis 100 ist ein Streiftreffer. Er hat keinen eigenen Zusatzeffekt. Die Trefferzone wird neu gewürfelt. Der Schaden, den der Angriff ursprünglich erzielt hat, wird durch W6 Schadenspunkte (SP, [[Glossar#SP|SP]]) ersetzt. Dieser Wert durchläuft die Schadenspipeline für die neu gewürfelte Zone wie jeder andere Treffer. Die Behinderung bei Lebensenergie 0 gilt für diese neue Zone, ein Streiftreffer hat keinen eigenen Wert.

## Die Zone lenken: Trefferzonen-Rerolls

Ein Trefferzonen-Reroll wiederholt ausschließlich den W100-Wurf der Trefferzone. Er lenkt einen Treffer, der schon gelungen ist, auf eine angesagte Zone, zum Beispiel „auf den Kopf“. Ob der Angriff gelingt, ändert er nicht, nur wohin er trifft. Bezahlt wird er nicht aus dem [[Stufe-Kreis-Macht-und-Rerolls|Vorrat des Helden an Rerolls]], er kommt aus eigenen Quellen.

### Woher die Rerolls kommen

- **Ansage-Tabelle der guten, meisterlichen und fröhlichen Erfolge.** Die Zeile „3 Trefferzonen-Rerolls“ gibt 3 Rerolls je Ansagepunkt. Ein guter Erfolg (gAT) bringt 1 Ansagepunkt, ein meisterlicher (mAT) 2, ein fröhlicher (fAT) 3. Die Zeilen der Tabelle sind kombinierbar. Bei einem fröhlichen Erfolg sind aus dieser Zeile bis zu 9 Rerolls möglich.
- **Freiwillige Selbst-Erschwerung der Angriffsprobe** (Nahkampf-Attacke, Fernkampf, Zauber): 2 Rerolls je +3 Erschwerung. Bei schlechter Sicht gibt es nur 1 je +3. Bei der Nahkampf-Attacke mindern überzählige Pool-Punkte die Senkung des Normalwerts, die aus der gewählten Erschwerung folgt ([[Nahkampf]]).
- **Die Talente Gezielter Schuss** (Fernkampf, 50 TaP) **und Gezielter Schlag** (Nahkampf, 75 TaP). Sie geben keine eigenen Rerolls, denn die 2 je +3 der Selbst-Erschwerung hat jeder Held. Das Talent erlaubt „auf kritisch weiterwürfeln“ bei jedem Treffer mit Ansage, auch bei einem normalen Erfolg (nFK, nAT) ([[Kampf-Talente]]).
- **Die Zauberform Blitz** (Form 4, in allen fünf Elementen und in der Magiebeschwörung): 2 Rerolls. Schlechte Sicht ändert daran nichts, denn die Wirkung des Zaubers ist fest.
- **Die Zauberform Strahl** (Form 5) **und der Materie-Strahl** der Materiebeschwörung: 1 Reroll ([[Magie-im-Kampf]]).

Weitere Quellen sind möglich. Alle Quellen eines Angriffs bilden zusammen ein einziges Bündel, und die Regeln sind für Nahkampf, Fernkampf und Magie dieselben. Eine Obergrenze gibt es nicht. Ohne Ansage der Zone gibt es keine Rerolls.

Als schlechte Sicht gelten Nebel, Nacht, Dämmerung, absolute Dunkelheit, Geblendetsein und alle Wetter-Modifikatoren ([[Fernkampf]]). Sie wirkt nur auf die Selbst-Erschwerung. Die Ansage-Tabelle bleibt unberührt.

### Ansage

Der Angreifer sagt eine der sieben Hauptzonen an: Kopf, Brust, Unterleib, rechter Arm, linker Arm, rechtes Bein oder linkes Bein. Eine feine Unterzone wie das Auge kann er nicht ansagen. Für Kreaturen gelten eigene Zonen ([[Kreaturen-im-Kampf]]).

Eine freiwillige Selbst-Erschwerung muss er vor dem Wurf ansagen, denn sie ändert die Angriffsprobe. Der Malus bleibt, auch wenn der Angriff misslingt. Wie viele Rerolls zur Verfügung stehen, steht erst fest, wenn der Treffer aufgelöst ist: Erst dann ist bekannt, ob die Probe gelungen ist und mit welcher Erfolgsstufe.

Der Schritt beginnt erst nach einem bestätigten Treffer. Misslingt die Angriffsprobe oder gelingt die Verteidigung (Parade, Ausweichen, Glück), gibt es keine Rerolls.

### Der erste Treffer der Zone gilt

Der W100-Wurf der Trefferzone und die Rerolls werden nacheinander geworfen. Der erste Wurf, der die angesagte Hauptzone trifft, gilt, mit seiner genauen Unterzone und deren Zusatzeffekt. Sobald er fällt, verfallen alle weiteren Rerolls. Trifft schon der erste W100 die angesagte Zone, wird kein Reroll gebraucht.

Trifft kein Wurf die angesagte Zone, gilt der Wurf, dessen Zone der angesagten am nächsten liegt, mit seiner genauen Unterzone. Bei gleicher Entfernung gilt der zuerst geworfene.

**Entfernung der Zonen.** Die Zonen bilden diesen Plan. Die Entfernung ist die Zahl der Schritte auf dem kürzesten Weg. Das Gelenk (Ellenbogen, Knie) zählt zum Knoten, der näher am Rumpf liegt:

```text
Kopf — Brust — Unterleib
Brust     — [Arm und Ellenbogen]  — [Hand]   (je links und rechts)
Unterleib — [Bein und Knie]       — [Fuß]    (je links und rechts)
```

Ellenbogen und die glatte Armzone sind der Knoten „Arm und Ellenbogen“, die Hand ist der Knoten „Hand“. Knie und die glatte Beinzone sind der Knoten „Bein und Knie“, der Fuß ist der Knoten „Fuß“. Ein Streiftreffer kommt als nächstliegende Zone nie infrage. Ist „Kopf“ angesagt, haben die Zonen diese Entfernungen: Brust 1, Unterleib und die Arm-Knoten 2, Hand und die Bein-Knoten 3, Fuß 4.

### Auf kritisch weiterwürfeln

Der Angreifer darf statt der Reihenfolge oben alle Rerolls werfen. Unter allen Würfen, die die angesagte Hauptzone treffen, zählt dann die schlimmste Unterzone dieser Zone. Trifft kein Wurf die Zone, gilt die Regel für die nächstliegende Zone. Bei Gleichstand zwischen einer linken und einer rechten Unterzone (zum Beispiel Schultergelenk) gilt rechts.

Das ist nur erlaubt bei

- jeder guten, meisterlichen oder fröhlichen Probe, bei der auf die Trefferzone gewürfelt wird, oder
- dem Talent Gezielter Schuss (Fernkampf) beziehungsweise Gezielter Schlag (Nahkampf).

Es ist eine Option und kein Zwang. Der Angreifer darf auch bei einer guten, meisterlichen oder fröhlichen Probe die Reihenfolge von oben wählen, zum Beispiel, um eine kritische Zone gerade nicht zu treffen.

**Die schlimmste Unterzone** jeder Hauptzone, von der schlimmsten zur mildesten:

- **Kopf:** Auge (Trefferpunkte × 2), Hals (1 zusätzliche Blutung), Kopf (Selbstbeherrschungsprobe um TP × 2 erschwert).
- **Brust:** Schultergelenk (bei TP > TS ist der Arm W4 + 2 Kampfrunden nicht benutzbar), Herz und/oder Lunge (1 zusätzliche Blutung), Brust (kein Zusatzeffekt).
- **Unterleib:** Organe (1 zusätzliche Blutung), Unterleib (kein Zusatzeffekt).
- **Arm** (links und rechts): Ellenbogen (Trefferpunkte × 2), Hand (bei misslungener Selbstbeherrschungsprobe zusätzlich entwaffnet), Arm (kein Zusatzeffekt).
- **Bein** (links und rechts): Knie (Trefferpunkte × 2), Fuß (bei TP > TS eine Probe aus Körperbeherrschung und Athletik, erschwert um TP, sonst Sturz mit Kampfklasse −2), Bein (kein Zusatzeffekt).

### Streiftreffer im Bündel

Ein Streiftreffer (98 bis 100) wird nicht sofort neu geworfen, sondern zurückgestellt. Trifft am Ende kein regulärer Wurf des Bündels die angesagte Zone, wird der zurückgestellte Streiftreffer neu auf eine echte Trefferzone geworfen. Er wird wiederholt, bis kein Streiftreffer mehr fällt. Fällt diese Zone in die angesagte Hauptzone, gilt der Streiftreffer dort, mit seinem eigenen geringeren Schaden von W6 Schadenspunkten statt dem Schaden des Angriffs. Die W6 durchlaufen die Schadenspipeline, der Rüstungsschutz greift. Fällt der Neuwurf nicht in die angesagte Zone, gilt die Regel für die nächstliegende Zone.

### Der Neuwurf aus dem Vorrat

Der Held kann einen Reroll aus seinem Vorrat auch auf die Trefferzone ausgeben. Dann wird einmal neu mit einem W100 auf die Zone gewürfelt. Dieser Wurf gilt und ersetzt das gesamte Ergebnis des Bündels, auch eine schon ermittelte schlimmste Unterzone. Jeder weitere Reroll aus dem Vorrat bringt wieder einen neuen W100, der gilt, bis der Vorrat leer ist. Ein solcher Reroll wird nicht Teil des Bündels.

### Beispiele

Der Angreifer sagt „Kopf“ an. Die Kopf-Gruppe umfasst die Würfe 1 bis 11. Er würfelt ohne „auf kritisch weiterwürfeln“ nacheinander:

- **2, dann 14.** Der erste Wurf trifft den Hals und liegt in der Kopf-Gruppe. Er gilt sofort, die 14 verfällt.
- **43, 80, 53.** Keiner trifft den Kopf. Die 43 ist der Unterleib (Entfernung 2), die 53 die rechte Hand (3), die 80 der rechte Fuß (4). Die nächste Zone ist der Unterleib, die 43 gilt.
- **92, 82.** Keiner trifft den Kopf. Die 92 ist das linke Bein, die 82 das rechte Bein, beide haben die Entfernung 3. Bei Gleichstand gilt der zuerst geworfene, die 92.
- **3, 1, 4.** Der erste Wurf trifft den Hals und liegt in der Kopf-Gruppe. Er gilt sofort. Das Auge (1) und der Kopf (4) danach zählen nicht, denn es wurde nicht „auf kritisch“ weitergewürfelt.
- **53, 90, 98, danach 4.** Die 53 (rechte Hand) und die 90 (linker Fuß) verfehlen den Kopf. Die 98 ist ein Streiftreffer und wird zurückgestellt. Er wird neu geworfen und ergibt 4: Kopf, also die Kopf-Gruppe. Der Streiftreffer gilt in der Zone Kopf, mit W6 Schadenspunkten statt des Schadens des Angriffs.

## Die Schadensart

Jede Schadensquelle hat genau eine von drei Schadensarten: Scharf, Durchbohrend oder Stumpf. Das gilt für Waffen und Sturz ebenso wie für Zauber und Wunder. Die Schadensart ändert sich nie. Sie steuert zwei Dinge der Zustände ([[Zustaende-Katalog]]):

- **Wunde.** Bei Stumpf liegt die Schwelle, ab der eine Wunde entsteht, bei der Trefferschwelle mal 1,5, aufgerundet. Bei einer Trefferschwelle von 5 ist das 7,5, aufgerundet 8: Eine Wunde entsteht ab TP > 8, also ab TP ≥ 9. Bei einer Trefferschwelle von 4 ist es 6, eine Wunde entsteht ab TP ≥ 7.
- **Amputation.** Eine Gliedmaße trennt nur scharfer Schaden ab. Das Auge ist davon ausgenommen: Dort können auch andere Schadensarten amputieren.

### Waffen und Sturz

- **Nahkampfwaffen.** Jede Nahkampfwaffe hat genau eine Schadensart, gleich unter wie vielen Spezialisierungen sie trainierbar ist. Mehrere Spezialisierungen betreffen nur das Training und die Werte für Attacke und Parade, nicht die Schadensart. Das gilt auch für das orkische Bat’leth, die Doppelsense und die Armklingen ([[Nahkampfwaffen]]).
- **Armklingen und Kampfstile.** Die vier Klauen-Zeilen der Armklingen (Drei Langklauen, Klaue, Pranke, Zwei Klauen) sind Scharf. Die übrigen fünf Armklingen-Zeilen behalten ihre Schadensart aus dem Waffenkatalog. Die sieben exotischen Kampfstile (Boxen, Elfische Kunst der Selbstverteidigung, Goblinische Kampfkunst, Katzenmenschen Kampfkunst, Orkisch’ Raufen, Ringen, Schattenkampf) sind Stumpf.
- **Schusswaffen.** Jede reine Schusswaffe (Bogen, Armbrust, Feuerwaffe, Blasrohr) ist Durchbohrend. Das Blasrohr richtet also wie alle Fernkampfwaffen durchbohrenden Schaden an. Einzige Ausnahme ist die Balläster, eine Armbrust, die eine murmelgroße Stahlkugel statt eines Bolzens schießt: Sie ist Stumpf.
- **Wurfwaffen.** Eine geworfene Waffe behält auf Distanz ihre Schadensart als Nahkampfwaffe. Ein Wurfmesser ist Scharf, im Nahkampf wie im Wurf.
- **Sturz.** Sturzschaden ist immer Stumpf.

### Zauber und Wunder

Ein Schadenszauber hat die Schadensart seiner Zauberform. Schule, Element und Gottheit spielen keine Rolle: Dieselbe Form liefert über alle Elemente und Quellen dieselbe Schadensart.

- **Stumpf:** Faust (Elementarschaden auf die eigenen Fäuste) und Ball, auch in den Salve-Varianten.
- **Durchbohrend:** Bolzen, Schuss und Geschoss, auch in den Salve-Varianten.
- **Scharf:** Wand, Aura, Strahl, Blitz oder Entladung (eine Kugel, die um das Ziel beschworen wird) sowie Sturm oder Explosion (unausweichlich, trifft jede Trefferzone).
- **Keine eigene Schadensart:** die Verzauberung von Klinge oder Pfeil. Sie übernimmt die Schadensart der Waffe oder Munition, die schon geführt wird, gleich ob sie aus der Elementarbeschwörung, der Verzauberung, einem Artefakt oder dem Segen eines Wunders stammt.

Diese neun Formen decken die fünf Schulen der Elementarbeschwörung (Erd-, Feuer-, Luft-, Wasser- und Magiebeschwörung) ab, ebenso die gleich gebauten Zauber der Verzauberung, etwa die Klingen und Pfeile mit „(V)“, und die Zauber der Artefakte (Flammen-, Frost-, Sturm-, Splitter- und Schock-Pfeil und -Klinge).

Ein Effekt, der Schaden zurückwirft, zum Beispiel Rache der Lloth, übernimmt die Schadensart des Treffers, den er zurückwirft.

Einzelne Fälle außerhalb der neun Formen:

- Stumpf: ein Golem-Konstrukt der Verzauberung und das Antimagische Feld der Antimagie.
- Scharf: die Explosionsfalle der Verzauberung, der Kontaktschaden von Weihwasser, Heiliger Blitz, Heiliges Land und Rache der Lügen (Verbrennungsfluch) der Wunder.

### Heiliger und Gesegneter Schaden

Heiliger und Gesegneter Schaden ist eine eigene Achse neben Scharf, Durchbohrend und Stumpf. Er gilt für Wunder und geweihte Gegenstände und wirkt als Verstärkung gegen Untote und Dämonen ([[Artefakte]]). Er ersetzt die Schadensart einer Quelle nie, er kommt dazu. Gegen Untote und Dämonen hat er außerdem eine eigene Regel für die Weiterleitung (siehe dort).

### Beispiele

- Steinkugel (Erdbeschwörung), Feuerball, Sturmball, Eisball und Magischer Ball sind alle Stumpf. Sie haben dieselbe Zauberform Ball und unterscheiden sich nur im Element.
- Ein Heiliger Bolzen (Wunder) ist Durchbohrend, wie jeder Bolzen und jeder Schuss, gleich welcher Schule oder Gottheit.
- Ein Golem-Konstrukt schlägt mit Stumpf zu.
- Die Balläster schießt eine murmelgroße Stahlkugel statt eines Bolzens und ist deshalb Stumpf, obwohl jede andere Armbrust Durchbohrend ist.
- Ein Wurfmesser ist im Nahkampf Scharf und bleibt es beim Wurf auf Distanz, nicht das übliche Durchbohrend einer Schusswaffe.

## Die Schadenspipeline

Aus den Schadenspunkten (SP) einer Angriffsprobe werden die Trefferpunkte (TP), die auf einer Zonengruppe ankommen. Die Kette hat sieben Schritte. Nach der Bildung in Schritt 1 dürfen die Schadenspunkte nur noch verringert werden, nie erhöht, bis Schritt 4 sie in Trefferpunkte umwandelt. Ist die getroffene Zone gedeckt, kommt davor der Deckungs-Rüstungsschutz dazu ([[Deckung]]).

1. **Schadenspunkte.** Eine erfolgreiche Angriffsprobe ergibt Schadenspunkte: gewürfelter Schaden plus Bonus.
2. **Magischer Schild.** Ist ein magischer Schild vorhanden, verringert sein eigener Rüstungsschutz (RS) die Schadenspunkte.
3. **Rüstungsschutz.** Die verbleibenden Schadenspunkte werden gegen den gesamten Rüstungsschutz verrechnet. Natürliche, magische und getragene Rüstung addieren sich, ebenso ein getragener Schild.
4. **Resistenz oder Anfälligkeit.** Die Resistenz verringert den Wert, die Anfälligkeit vervielfacht ihn ([[Anfaelligkeit-und-Resistenz]]). Hier werden aus den Schadenspunkten die Trefferpunkte. Jede Multiplikation wirkt nur auf Trefferpunkte, nie auf rohe Schadenspunkte. Das Ergebnis wird sofort aufgerundet.
5. **Leberschutz.** Der Leberschutz ist ein Puffer aus Trefferpunkten. Er muss ganz verbraucht sein, bevor eine Trefferzone selbst Schaden nimmt. Reicht er nicht aus, geht der überschießende Betrag im selben Treffer an die getroffene Trefferzone.
6. **Faktor der Zone.** Der Wert, der nach dem Leberschutz bleibt, wird mit dem eigenen Faktor der getroffenen Zone malgenommen (Trefferpunkte × 2 bei Auge, Ellenbogen und Knie). Das Ergebnis wird sofort aufgerundet.
7. **Lebensenergie.** Der so ermittelte Wert wird auf die Lebensenergie der getroffenen Zonengruppe angewendet. Übersteigt er die verbleibende Lebensenergie, wird der Überschuss weitergeleitet.

An Schritt 4 steht höchstens ein Faktor. Ein verringernder und ein vervielfachender Faktor treffen nie denselben Schaden. Treffen zwei verringernde Faktoren denselben Wert, gilt der stärkere allein. So gibt es höchstens zwei Aufrundungen je Schaden: nach Schritt 4 und nach Schritt 6.

### Der Leberschutz

Leberschutz hat genau zwei Quellen: die KI-Fähigkeit Abhärtung ([[KI]]) und Wunder ([[Wunder]]). Er stapelt unterschiedlich. Bei der KI zählt nur der höchste aktuelle Wert. Der Leberschutz eines Wunders kommt additiv obendrauf. Er regeneriert nie.

Übersteigt der Wert eines einzelnen Treffers den Leberschutz, der zu diesem Zeitpunkt noch übrig ist, geht der überschießende Anteil noch im selben Treffer an die Trefferzone. Schaden, den der Leberschutz ganz aufnimmt, erreicht die Trefferzone nicht, gleich wie groß er vorher war.

### Beispiel

Ein Angriff bringt 9 Schadenspunkte. Das Ziel hat Rüstungsschutz 2 und eine Anfälligkeit mit Faktor 1,5, aber keinen Leberschutz. Der Treffer fällt auf das rechte Knie.

```text
9 − 2          = 7 Schadenspunkte
7 × 1,5        = 10,5, aufgerundet 11 Trefferpunkte
11 × 2 (Knie)  = 22 Trefferpunkte auf das Knie
```

Hätte das Ziel stattdessen eine Resistenz mit Faktor 0,5, ergibt sich 7 × 0,5 = 3,5, aufgerundet 4 Trefferpunkte, und 4 × 2 = 8 Trefferpunkte auf das Knie.

## Weiterleitung an die Gesundheit

Übersteigt der Wert aus Schritt 7 die verbleibende Lebensenergie der Zonengruppe, wird der Überschuss weitergeleitet. Wohin, hängt von der Zone ab.

- **Kopf, Brust, Unterleib.** Der Überschuss geht bei Nahkampf wie bei Fernkampf direkt an die Gesundheit.
- **Rechter und linker Arm, Nahkampf.** Der Überschuss geht nur bei einem guten, meisterlichen oder fröhlichen Angriffstreffer (gAT, mAT, fAT) an die Brust. Ohne einen solchen Treffer ist er verloren.
- **Rechter und linker Arm, Fernkampf.** Es gibt keine Weiterleitung. Solange die Zone noch Lebensenergie hat, ist jeder Überschuss verloren, gleich wie gut der Treffer war.
- **Rechtes und linkes Bein.** Wie der Arm, aber mit dem Unterleib statt der Brust als Ziel.
- **Bereits erschöpfte Arm- oder Beinzone.** Hat eine Arm- oder Beinzone zu Beginn eines neuen, eigenständigen Treffers schon Lebensenergie 0, weil sie ausgeschöpft oder amputiert ist, geht der gesamte Schaden dieses Treffers auf eine feste Ersatzzone: jede Armzone auf die Brust (Würfe 16 bis 36), jede Beinzone auf den Unterleib (Würfe 42 bis 51). Das gilt unabhängig von Nahkampf oder Fernkampf und von der Güte des Treffers. Es zählt der Rüstungsschutz der Ersatzzone, nicht der der ursprünglichen Zone. Die Behinderung der ursprünglichen Zone ist davon unberührt und entsteht normal. Eine Zone mit Lebensenergie 0 nimmt nie wieder direkt Schaden. Jeder neue Treffer auf sie geht vollständig an die Ersatzzone, auch wenn diese noch volle Lebensenergie hat.
- **Heiliger Schaden.** Trägt der Schaden eines Treffers den Zusatz „Heilig“, „Gesegnet“ oder „Rein“, wird der Überschuss eines Gliedes bei bestimmten Zielen immer vollständig an die angeschlossene Zone weitergeleitet: bei Untoten immer, bei Magiekorpi und Dämonen nur, wenn sie mehr als eine Zone haben, bei den übrigen Lebenden nicht. Bei der Anatomie des Helden ist das Ziel die Brust beim Arm und der Unterleib beim Bein. Die Einschränkung durch die Güte des Treffers und die Regel, dass ein Fernkampf-Überschuss am Arm oder Bein verloren ist, gelten dann nicht.
- **Kreaturen mit anderer Anatomie.** Welche Zonen Kern und Glied sind, welche Zone angeschlossen ist und wie Kreaturen mit nur einer Zone behandelt werden, steht in [[Kreaturen-im-Kampf]].

## Sturzschaden

Jeder Eintritt von Sturz löst zusätzlich zur Senkung der Kampfklasse einen Sturzschaden-Wurf aus. Sturzschaden ist immer Stumpf.

### Wann der Wurf fällig wird

Der Wurf folgt auf jeden Eintritt von Sturz, gleich woher er kommt:

- aus den Fuß-Zeilen der Trefferzonen-Tabelle (Würfe 80 und 90),
- aus der Selbstbeherrschungstabelle, Band 10 bis 11,
- aus einem fehlgeschlagenen Rückstoß des Zaubers Luftbeschwörung,
- aus dem Umwerfen im Kampf ([[Nahkampf-im-Kampf]]),
- aus einem Sturz, den der Meister auslöst, etwa durch einen Einsturz, einen Klippensturz oder einen Fall von einer Erhöhung. Die Fallhöhe legt der Meister frei fest.

Es gibt keine schadensfreie Mindesthöhe. Auch ein Sturz ohne reale Fallhöhe, wie ein Niederwurf im Kampf, löst mindestens einen Wurf aus. Für Kreaturen gelten Besonderheiten ([[Kreaturen-im-Kampf]]).

### Der Wurf

Aus der Fallhöhe ergibt sich ein Band: Fallhöhe in Metern geteilt durch 3, aufgerundet, mindestens 1.

- **Band 1** (0 bis 3 m oder ohne Höhe): 1W6.
- **Band 2** (4 bis 6 m): 2W8.
- **Band 3** (7 bis 9 m): 3W10.
- **Band 4 und höher** (ab 10 m, je weitere 3 m ein Band): n×W12, wobei n die Nummer des Bands ist.
- **Band 33** (ab 99 m, die Obergrenze): immer 33W12.

Jeder Würfel erhält einen eigenen W100-Wurf auf die Trefferzone, es sei denn, die Zonenwahl (siehe unten) greift. Ergebnisse auf dieselbe Zonengruppe werden zu einer Summe addiert.

### Die zweite Gegenprobe

Ab Band 2 (ab 4 m) darf der Gestürzte zusätzlich zur ursprünglichen Verteidigungsprobe des auslösenden Vorgangs eine zweite, eigenständige Gegenprobe aus Körperbeherrschung und Athletik würfeln. In Band 1 gibt es sie nicht. Dort ist der Sturzschaden immer voll, ungemildert und zufällig verteilt.

Gelingt die Gegenprobe, gelten beide Vorteile zugleich:

1. **Schaden mindern.** Bei der Marge X der Probe entsteht ein Vorrat von X ÷ 2 Schadenspunkten, aufgerundet. Jeder dieser Punkte wird einzeln von der Zonensumme abgezogen, die gerade am höchsten ist. Das ist dasselbe Verteilungsprinzip wie bei der Heilung nach der Regenerationsstufe, nur umgekehrt ([[Gesundheit-und-Mana-Regeneration]]). Bei Gleichstand gilt die Reihenfolge: Kopf, Brust, Unterleib, rechter Arm, linker Arm, rechtes Bein, linkes Bein.
2. **Zonen wählen.** Der Gestürzte wählt statt der zufälligen Verteilung ausdrücklich Beine, Arme oder Arme und Beine. Die Würfel werden gleichmäßig auf die gewählten Zonen verteilt, ein Rest wird zufällig verteilt. Kopf, Brust, Organe, Hals und die übrigen Zonen bleiben stets ausgenommen.

Misslingt die zweite Gegenprobe, gilt wie in Band 1 der volle, ungeminderte und zufällig verteilte Schaden. Für Kreaturen gelten die Reihenfolge der Zonen bei Gleichstand und die Zählung von Flügeln und Tentakeln als Arme nach [[Kreaturen-im-Kampf]].

**Stehen oder liegen.** Wählt der Gestürzte Arme oder Arme und Beine, bleibt oder wird er im Zustand Sturz, mit der vollen Kette Sturz, Straucheln, Benommenheit, erholt. Wählt er nur die Beine, wird der bereits ausgelöste Sturz auf Straucheln herabgestuft.

### Weiterverarbeitung

Nach einer möglichen Minderung durchläuft jede Zonensumme die Schadenspipeline. Der Rüstungsschutz der Zone gilt einmal gegen die gestapelte Summe, nicht gegen jeden Würfel einzeln. Übersteigt das Ergebnis die verbleibende Lebensenergie, wird der Überschuss weitergeleitet. Übersteigt es die Trefferschwelle dieser Gruppe, wird eine reguläre Selbstbeherrschungsprobe fällig. Sturzschaden ist ein gewöhnlicher Schadenseintrag.

## Die Selbstbeherrschungsprobe

Die Selbstbeherrschungsprobe (SB-Probe, [[Glossar#SB|SB]]) klärt, wie der Held auf schweren Trefferschaden reagiert. Sie entscheidet, ob ein Treffer über den Verlust von Lebensenergie und Gesundheit hinaus einen Kontrollverlust auslöst, von Benommenheit bis Bewusstlosigkeit, und zusätzliche Behinderung erzeugt. Sie ist eine Tabellenprobe: Ein misslungener Wurf wird nach seinem Betrag in der Selbstbeherrschungstabelle nachgeschlagen.

### Die Trefferschwelle

Die Trefferschwelle (TS) ist Vitalität + 5 plus die Summe aller Modifikatoren, die gerade wirken. Es gibt keine feste Liste dieser Modifikatoren: Jede Quelle, die die Trefferschwelle erhöht oder senkt, wirkt mit, auf welchem Weg auch immer. Bekannte Quellen sind

- das Talent Zäher Bursche, Stufe 2 und 3 (+1 und +2, [[Talente-die-Werte-veraendern]]),
- die Spruchmagie-Heilung „Trefferschwelle erhöhen“ (anhaltend, plus Magie, [[Spruchmagie]]),
- die KI-Fähigkeit Konzentration (Trefferschwelle +1 pro +2 gewählter Erschwerung, [[KI]]),
- Wunder ([[Wunder]]).

### Wann die Probe fällig wird

Die Probe ist nicht automatisch. Sie wird nur gewürfelt, wenn die Trefferpunkte (TP) einer Zonengruppe die Trefferschwelle übersteigen (TP > TS). Sonst gibt es weder eine Probe noch eine Auswirkung. Die einzige Ausnahme: Eine Fähigkeit des Angriffs verlangt die Probe ausdrücklich unabhängig davon, zum Beispiel bestimmte Effekte der Magiebeschwörung in der Spruchmagie.

Maßgeblich sind die Trefferpunkte nach dem Leberschutz. Was der Leberschutz aufnimmt, löst keine Probe aus und zählt nicht zur Summe. Erschöpft sich der Leberschutz mitten in einem Treffer, zählt für Auslösung und Summe nur der Teil dieses einen Treffers, der über den Leberschutz hinausgeht.

- **Summe je Zonengruppe und Kampfrunde.** Die Trefferpunkte mehrerer Treffer auf dieselbe Gruppe addieren sich innerhalb derselben Kampfrunde zu einer laufenden Summe. Treffer auf verschiedene Gruppen addieren sich nicht, eine Gesamtsumme über die ganze Kampfrunde gibt es nicht. Übersteigt die Summe die Trefferschwelle, wird eine Probe fällig. Jeder weitere Treffer auf dieselbe Gruppe in derselben Kampfrunde löst eine neue Probe aus, mit dem jeweils größeren Wert. Jede dieser Proben wird für sich ausgewertet.
- **Mehrere Gruppen.** Überschreiten mehrere Gruppen in derselben Kampfrunde unabhängig voneinander die Trefferschwelle, wird für jede eine eigene Probe gewürfelt. Jede zieht ihre Erschwerung nur aus den Trefferpunkten und der Behinderung der eigenen Gruppe, nie aus einer anderen.

### Der Probenwert

```text
Probenwert = (Mut + Willenskraft + Konstitution + Stärke + Selbstbeherrschung) / 7
           + Vitalität + 12 + TS − TP
```

Mut, Willenskraft, Konstitution und Stärke sind [[Eigenschaften]]. Selbstbeherrschung ist eine [[Sonderfertigkeiten|Sonderfertigkeit]]. Vitalität ist ein [[Attribute|Attribut]]. Sie geht doppelt ein, als eigener Term und in der Trefferschwelle.

Im Zähler stehen fünf Werte, der Teiler ist 7. Die Division wird sofort aufgerundet, erst dann werden die übrigen Terme addiert. Übersteigen die Trefferpunkte die Trefferschwelle, ist TS − TP negativ. Die Erschwerung ist also nur so groß wie der Betrag, um den die Trefferpunkte die Trefferschwelle übersteigen, nicht so groß wie die Trefferpunkte selbst. Der Probenwert kann bei hohem Schaden negativ werden. Eine Untergrenze gibt es nicht.

Zusätzlich erschwert:

- **Kopf.** Trifft der auslösende Treffer die Zone Kopf, ist die Probe zusätzlich um TP × 2 erschwert. Für Kreaturen mit mehreren Köpfen gilt das für die Kopf-Zeile jedes Kopfes ([[Kreaturen-im-Kampf]]).
- **Behinderung der Gruppe.** Ist in derselben Zonengruppe die Lebensenergie auf 0 gefallen und hat dabei eine Behinderung erzeugt, zählt für diese eine Probe nur der höhere der beiden Werte von Körperlicher und Mentaler Behinderung (KBE, MBE), nicht ihre Summe. Jede andere Behinderung des Helden zählt wie bei jeder Probe zusätzlich ([[Behinderung-und-Erschwerung]]).

Gewürfelt wird W30 − W12. Die Probendifferenz ist der Probenwert minus der Wurf.

### Die Auswertung

Nur eine negative Probendifferenz, also ein Wurf über dem Probenwert, hat eine Wirkung. Ihr Betrag wird in der Selbstbeherrschungstabelle nachgeschlagen. Eine Differenz von 0 oder mehr bringt keine Wirkung über das Ergebnis der Probe hinaus ([[Wuerfeln-und-Proben|Würfeln und Proben]]).

| Betrag | Behinderung | Zustand |
|---:|---|---|
| 1–5 | KBE +1 und MBE +1 | Benommenheit: Kampfklasse −1, 1 Kampfrunde |
| 6–9 | KBE +2 und MBE +2 | Straucheln: Kampfklasse −1. Nach 1 Kampfrunde wechselt der Zustand automatisch zu Benommenheit |
| 10–11 | KBE +3 und MBE +3 | Sturz: Kampfklasse −2, keine feste Dauer. Mit einer erfolgreichen Athletik-Probe oder Körperbeherrschungs-Probe, in jeder Kampfrunde versuchbar, wechselt der Zustand zu Straucheln |
| 12 | KBE +4 und MBE +4 | Waffe verloren (entwaffnet): Paradeklasse −1 für den Rest der laufenden Kampfrunde, danach der Zustand „Verlorenen Gegenstand aufheben“ (siehe unten) |
| 13–16 | KBE +5 und MBE +5 | Kampfunfähig: Kampfklasse −2 für W15 + W6 Kampfrunden. Danach wechselt der Zustand automatisch zu Sturz |
| 17 und mehr | KBE +7 und MBE +7 | Bewusstlos: Sofort wird ein W30 gewürfelt. Er gibt die Kampfrunden bis zur ersten Konstitutions-Probe an; nach jeder Probe wird für den Abstand zur nächsten ein neuer W30 gewürfelt. Gelingt eine Probe, wechselt der Zustand zu Kampfunfähig |

Die Kampfklasse umfasst Attacke-, Parade-, Ausweich- und Fernkampf-Klasse. Alle vier sinken um den genannten Wert, außer in Zeile 12, die ausdrücklich nur die Paradeklasse nennt und sie bewusst nicht auf die Kampfklasse erweitert, solange die Kampfrunde dauert. Eine Dauer von X Kampfrunden zählt vom Eintritt bis zum Ende der X-ten Kampfrunde.

Die Zustände folgen einander in dieser Reihe: Bewusstlos, Kampfunfähig, Sturz, Straucheln, Benommenheit, erholt. Kampfunfähig und Bewusstlos enden nicht in voller Genesung, sondern in der nächstmilderen Stufe. Wie die Zustände im Einzelnen wirken, steht in [[Zustaende-Katalog]].

**Bewusstlos im Band 17 und mehr.** Beispiel: Der sofort gewürfelte W30 ergibt 12. Nach 12 Kampfrunden folgt die erste Konstitutions-Probe. Misslingt sie, wird ein neuer W30 gewürfelt, zum Beispiel 20; die nächste Probe folgt dann 20 Kampfrunden später.

**Die Behinderung.** Der Wert der Tabelle wird in voller Höhe sowohl zur Körperlichen als auch zur Mentalen Behinderung addiert. Er stapelt mit jeder anderen Behinderung und wirkt ab seinem Entstehen auf jede folgende Probe jeder Art ([[Behinderung-und-Erschwerung]]). Er fließt nicht in die Behinderung der Gruppe zurück, die oben für die Probe gilt. Die Behinderung gehört zur Tabellenzeile und nicht zum Zustand: Straucheln und Sturz aus einer anderen Quelle, etwa dem Umwerfen ([[Nahkampf-im-Kampf]]) oder einem Sturz durch den Meister, geben keine Behinderung. Bewusstlos ist die Ausnahme: Der Zustand trägt die Behinderung 7 aus jeder Quelle, beim Band 17 und höher einmal und nicht zusätzlich zur Tabellenzeile ([[Zustaende-Katalog]]).

**Die Reihenfolge.** Die Probe wird gleich nach dem Treffer gewürfelt: Treffer, Zonenwurf, Prüfung, ob die Lebensenergie der Gruppe auf 0 fällt, Behinderung der Gruppe eintragen, Selbstbeherrschungsprobe, bei negativer Differenz die Tabelle. Die Trefferschwelle, die Eigenschaften und die Sonderfertigkeit zählen so, wie sie zum Zeitpunkt der Probe sind.

Misslingt die Probe, kann der Held in manchen Fällen mit dem Mentalen Fokus eine zweite Chance bekommen ([[Magie-Wirkungsdauer-und-Konzentration|Magie: Wirkungsdauer und Konzentration]]). Gelingen zwei Proben nacheinander gut, kann der Held in Blutrausch verfallen (siehe unten).

### Der Zustand „Verlorenen Gegenstand aufheben“

Der Zustand folgt auf einen Waffenverlust. Quellen sind die Zeile 12 der Selbstbeherrschungstabelle und die Fähigkeit Entwaffnen ([[Kampf-Talente]]). Er gilt für die Waffe der Haupthand. Ist die Haupthand leer, gilt er für die Waffe der Nebenhand.

- **Beginn.** Beim Entwaffnen mit dem Verlust. Bei Zeile 12 nach Ablauf der laufenden Kampfrunde, in der die Paradeklasse −1 gilt. Hat der Entwaffnete den Gegenstand bewusst aufgegeben, wird der Zustand nicht vergeben.
- **Würfe des Meisters.** Bei einem Verlust würfelt der Meister verdeckt je Gegenstand einen W4 und den Landeort. Der W4 ist die Zahl s der Such-Kampfrunden bis zum Finden. Der Landeort ist eine Richtung mit W8 (bei 8 neu würfeln): 1 gleiches Feld, 2 Nord, 3 Nordost, 4 Südost, 5 Süd, 6 Südwest, 7 Nordwest. Die Entfernung zählt ab dem Feld des Entwaffneten: Beim Entwaffnen sind es 1, 2, 3 oder 4 Felder, je nachdem, ob die Probe der Fähigkeit n, g, m oder f war. Bei Zeile 12 ist es immer 1 Feld. Bei „gleiches Feld“ gibt es keine Entfernung. Den Landeort nennt der Meister erst, wenn der Gegenstand gefunden ist.
- **Suchen.** Suchen ist eine Ansage. In jeder Kampfrunde entscheidet der Held, ob er sucht. In dieser Kampfrunde gilt Kampfklasse −1. Das Suchen kostet keine AK und gibt keine Behinderung.
- **Suchzeit.** Sie zählt nur in Kampfrunden, in denen der Held sucht. Nach s Such-Kampfrunden ist der Gegenstand gefunden.
- **Sinnesschärfe-Probe.** In einer Such-Kampfrunde darf der Held eine Sinnesschärfe-Probe würfeln, erschwert um 10 × (s − bisherige Such-Kampfrunden einschließlich der aktuellen). Gelingt sie, ist der Gegenstand in derselben Kampfrunde gefunden. In der letzten, der s-ten Such-Kampfrunde, ist er ohnehin gefunden, die Probe entfällt.
- **Erschwerung nach s.** Bei s = 1 ist der Gegenstand in der ersten Such-Kampfrunde automatisch gefunden. Bei s = 2 ist die Probe in der ersten Such-Kampfrunde um 10 erschwert, in der zweiten ist er automatisch gefunden. Bei s = 3 sind es 20 und 10, danach automatisch. Bei s = 4 sind es 30, 20 und 10, danach automatisch.
- **Gefunden.** Der Meister nennt den Landeort. Der Held geht mit einer normalen Bewegung dorthin und nimmt den Gegenstand mit „Gegenstand: Aufnehmen“ auf (2 Aktionskosten, [[Kampfrunde-Aktionen-Initiative-und-Sicht]]). Kampfklasse −1 gilt dafür nicht.
- **Abbruch.** Der Held kann das Suchen in jeder Kampfrunde lassen. Der Gegenstand bleibt dann liegen, und der Held kämpft unbewaffnet oder zieht eine Zweitwaffe. Sucht er später weiter, zählen die schon gesuchten Kampfrunden mit, solange der Kampf am selben Ort weiterläuft.
- **Mehrere Gegenstände.** Jeder verlorene Gegenstand hat sein eigenes s. Die Gegenstände werden nacheinander gesucht, nie gleichzeitig.
- **Ende.** Der Zustand endet mit der Aufnahme.

**Beispiel Entwaffnen.** Der Held wurde mit einer Entwaffnen-Probe der Klasse g entwaffnet. Der Meister würfelt W4 = 3, die Richtung 3 (Nordost) und die Entfernung 2 Felder. In Kampfrunde 1 sucht der Held (Kampfklasse −1), seine Sinnesschärfe-Probe, erschwert um 20, misslingt. In Kampfrunde 2 kämpft er, ohne zu suchen, kein Malus. In Kampfrunde 3 sucht er wieder (Kampfklasse −1). Die Kampfrunde 1 zählt mit, es ist also seine zweite Such-Kampfrunde, die Probe ist um 10 erschwert und gelingt, und der Gegenstand ist gefunden. Der Meister nennt „zwei Felder nach Nordost“. In Kampfrunde 4 geht der Held dorthin und nimmt den Gegenstand auf.

**Beispiel Zeile 12.** Der Wurf ergibt den Betrag 12. Die Paradeklasse sinkt für den Rest der laufenden Kampfrunde um 1, dazu kommen KBE +4 und MBE +4. Danach beginnt der Zustand mit W4 = 1 und der Entfernung 1 Feld. In Such-Kampfrunde 1 (Kampfklasse −1) ist der Gegenstand gefunden.

### Beispiele zur Selbstbeherrschungsprobe

Der Held hat Trefferpunkte nach dem Leberschutz von 15 und die Trefferschwelle 12 (Vitalität 7 + 5). Weil 15 größer als 12 ist, wird die Probe fällig. Seine Werte sind Mut 8, Willenskraft 6, Konstitution 10, Stärke 9, Selbstbeherrschung 4 und Vitalität 7.

```text
(8 + 6 + 10 + 9 + 4) / 7 = 37 / 7 = 5,29, aufgerundet 6
Probenwert = 6 + 7 + 12 + 12 − 15 = 22
Wurf = 25, Probendifferenz = 22 − 25 = −3, Betrag 3
```

Der Betrag 3 liegt in der Zeile 1–5: KBE +1, MBE +1, Benommenheit (Kampfklasse −1, 1 Kampfrunde).

Traf derselbe Treffer zusätzlich die Zone Kopf, wäre der Probenwert um TP × 2 = 30 erschwert.

Zwei Treffer auf die Brust in derselben Kampfrunde: Der erste bringt TP 8, das liegt unter der Trefferschwelle 12, es gibt keine Probe. Der zweite bringt TP 6, die Summe ist 14 und übersteigt 12. Die erste Probe fällt erst beim zweiten Treffer, mit dem Wert 14.

## Todesschwelle

### Das Band der Todesschwelle

Liegt die Gesundheit des Helden im Band von 0 bis −Vitalität (0 ≥ Gesundheit ≥ −Vitalität), löst jeder Treffer eine Selbstbeherrschungsprobe aus. Der Ausgang ist rein binär: Bei meisterlichem oder fröhlichem Erfolg bleibt der Held voll handlungsfähig, bei jedem anderen Ergebnis wird er sofort bewusstlos. Die Selbstbeherrschungstabelle wird in diesem Fall nicht herangezogen. Ab Gesundheit −Vitalität − 1 ist der Held tot ([[Tod-und-Wiederbelebung]]). Die Stelle im Ablauf der Kampfrunde steht in [[Kampfrunde-Aktionen-Initiative-und-Sicht]].

Für Untote gilt statt der Todesschwelle die Untoten-Kampfunfähigkeitsschwelle ([[Kreaturen-im-Kampf]]).

## Der Blutrausch

Im Blutrausch muss der Held keine Selbstbeherrschungsproben mehr würfeln, er hat unbegrenzte Ausdauer, und die Behinderung aus geschlagenen oder abgetrennten Gliedmaßen wird halbiert. Der Blutrausch hat zwei Wege, ihn auszulösen.

### Wie er beginnt

- **Natürlich.** Gelingt eine Selbstbeherrschungsprobe mit einem guten oder besseren Erfolg, darf der Spieler eine zweite, bestätigende Probe würfeln. Wird auch sie mit einem guten oder besseren Erfolg bestanden, ist die erste bestätigt, und der Held verfällt in Blutrausch. Gelingt die zweite Probe nicht oder nur normal, wird ihr Ergebnis ignoriert. Sie hat keine Folge, der Held bleibt nur nicht im Blutrausch.
- **Magisch.** Das Wunder Berserker des Gottes Khartazh versetzt den Helden bei erfolgreichem Wirken in denselben Blutrausch. Es braucht mindestens Karma 3, hat den Malus 14, kostet 60 Karma-Pool-Punkte ([[Glossar#KPP|KPP]]), hat die Vorbereitungsdauer 1 Sekunde (Stoß) und die Wirkungsdauer Karma × Minuten ([[Wunder]]).

### Was er bewirkt

- **Keine Selbstbeherrschungsproben.** Solange der Blutrausch anhält, muss der Held keine weiteren Selbstbeherrschungsproben ablegen, auch keine erzwungenen, gleich ob er über der Trefferschwelle getroffen wird, Gliedmaßen verliert oder aus einem anderen Grund eine Probe fällig würde. Die einzige Ausnahme steht unter „Gesundheit unter 0“.
- **Halbierte Behinderung.** Die Behinderung, die aus Gliedmaßen mit Lebensenergie 0 und aus abgetrennten Gliedmaßen entsteht, wird für die Dauer des Blutrauschs halbiert und dabei abgerundet. Das ist eine der wenigen Ausnahmen von der allgemeinen Rundungsregel ([[Wuerfeln-und-Proben|Würfeln und Proben]]). Die Halbierung wirkt auf den Gesamtwert der Behinderung dieser Gliedmaßen, nicht auf einzelne Quellen vor der Summierung, und wird bei jeder Berechnung neu angewendet, solange der Blutrausch anhält. Eine Behinderung von 4 aus einer Beinzone mit Lebensenergie 0 wird zu 2, eine von 5 wird zu 2. Aus einer Behinderung von 1 wird 0. Jede andere Behinderung bleibt unverändert, zum Beispiel die Behinderung bei Ausdauer 0, die Frost-Behinderung und die Behinderung aus der Selbstbeherrschungstabelle ([[Behinderung-und-Erschwerung]]).
- **Unbegrenzte Ausdauer.** Kampfaktionen kosten keine Ausdauer, auf beiden Wegen und für die ganze Dauer des Blutrauschs ([[Ausdauer]]). Das Budget von 3 AK pro Kampfrunde bleibt.
- **Andere Verletzungen bleiben möglich.** Der Blutrausch verhindert weder Blindheit noch den Verlust einer Gliedmaße. Nur die Behinderung aus der Halbierung ist verringert, nicht die Verletzung selbst.

### Wie er endet

- **Natürlicher Blutrausch.** Er endet, sobald der Held so viele Kampfrunden, wie seine Konstitution beträgt, außerhalb des gesamten Kampfes verbracht hat. Eine einzelne Kampfrunde genügt nicht, und das bloße Verlassen des Nahkampfs auch nicht. „Außerhalb des Kampfes“ ist weiter gefasst als „außerhalb des Nahkampfs“: Läuft der Held mehrere Kampfrunden auf einen neuen Gegner zu, gilt er weiter als im Kampf, auch ohne Schlagabtausch, und diese Kampfrunden zählen nicht. Der Zähler läuft erst, wenn die Kampfsituation insgesamt vorbei ist. Als Richtwert dafür gilt das Ende der Initiative-Verfolgung, nicht ein fester Zeitpunkt für jeden Grenzfall.
- **Magischer Blutrausch.** Er endet mit dem Ablauf der Wirkungsdauer von Berserker, gleich ob der Held dann noch im Kampf ist. Die Bedingung des natürlichen Blutrauschs gilt hier nicht zusätzlich.

### Beide Wege zugleich

Wird Berserker gewirkt, während ein natürlicher Blutrausch läuft, oder umgekehrt, addieren sich die Wirkungen nicht. Der Bonus der Ausdauer und die halbierte Behinderung gelten einfach, nicht doppelt. Die höhere der beiden Dauern ist maßgeblich. Eine laufende, längere Dauer wird durch einen neuen, kürzeren Auslöser nicht verkürzt, und ein neuer, längerer Auslöser überschreibt eine kürzere, schon aktive Instanz.

### Gesundheit unter 0

Sinkt die Gesundheit des Helden im Blutrausch unter 0, wird trotz der Immunität die Selbstbeherrschungsprobe des Todesschwelle-Bands fällig (siehe „Das Band der Todesschwelle“). Ein meisterliches oder besseres Ergebnis lässt den Blutrausch bestehen. Jedes andere Ergebnis beendet ihn sofort, und der Held wird unmittelbar bewusstlos. Die gestaffelte Selbstbeherrschungstabelle kommt dabei nicht zur Anwendung. Das gilt auf beiden Wegen gleich.

### Beispiele

- Ein Held besteht eine Selbstbeherrschungsprobe mit „gut“, legt die bestätigende zweite Probe ab und besteht auch diese, mit „meisterlich“. Der Blutrausch tritt ein. Hätte er die zweite Probe nur normal bestanden, gäbe es keinen Blutrausch und keine weitere Folge.
- Ein Held im Blutrausch hat eine Beinzone auf Lebensenergie 0, nicht abgetrennt. Ihre reguläre Behinderung wäre 4. Wirksam sind 4 ÷ 2 = 2.
- Ein Held wirkt erfolgreich Berserker. Der Blutrausch tritt ein, und für die Dauer Karma × Minuten fallen keine Ausdauerabzüge durch Kampfaktionen an.
- Ein Held mit Konstitution 8 im natürlichen Blutrausch sprintet 3 Kampfrunden lang auf einen neuen Gegner zu. Der Blutrausch bleibt aktiv, denn er ist weiter im Kampf. Der Zähler läuft nicht. Verlässt er danach die Kampfsituation ganz, ohne Gegner in Reichweite oder Sicht und ohne geplante Handlung, endet der Blutrausch nach 8 Kampfrunden außerhalb des Kampfes.
- Ein Held besteht die doppelte gute Selbstbeherrschungsprobe, ohne dass Berserker gewirkt wurde. Zusätzlich zur Halbierung der Behinderung gilt der Ausdauer-Bonus, bis der Blutrausch nach der Regel für den natürlichen Weg endet.
- Berserker wird gewirkt, die Wirkungsdauer ist bei Karma 6 sechs Minuten. Der Held bleibt danach 10 Minuten ununterbrochen im Kampf. Der Blutrausch endet nach 6 Minuten mit dem Ablauf der Wirkungsdauer, obwohl der Held noch im Kampf ist.
- Ein Held hat einen natürlichen Blutrausch, dessen Zähler noch nicht abgelaufen ist, und wirkt zusätzlich erfolgreich Berserker mit sechs Minuten Wirkungsdauer. Es gibt keinen doppelten Ausdauer-Bonus und keine doppelte Halbierung. Maßgeblich ist die höhere Dauer, hier die neu hinzukommenden 6 Minuten, wenn sie länger sind als der laufende Zähler.

## Rerolls im Kampf

Der Vorrat an Rerolls hängt vom Kreis des Helden ab. Was ein einzelner Reroll bewirkt, für welche Würfe er gilt und wie sich der Vorrat füllt, steht im Kapitel [[Stufe-Kreis-Macht-und-Rerolls|Stufe, Kreis, Macht und Rerolls]]. Dieser Abschnitt sagt, wann im Kampf ein Reroll ausgegeben wird, welche Würfe einer Kampfrunde er erreicht und was danach neu gewürfelt wird.

### Austausch und Beteiligung

Ein Austausch ist die kleinste abgeschlossene Einheit einer Kampfrunde. Das ist entweder eine Paarung innerhalb einer Nahkampf-Gruppe, die paarweise abgehandelt wird ([[Nahkampf-Gruppen-und-das-Meisterscreen-Gitter]]), oder ein einzelner Fernkampf- oder Zauber-Angriff der Runde ([[Kampfrunde-Aktionen-Initiative-und-Sicht]]). Auch ein Angriff auf mehrere Ziele oder ein Flächenzauber bleibt ein einziger Austausch. Die Wirkung tritt für alle betroffenen Ziele gleichzeitig am Beginn der Effektdauer oder Wirkungsdauer ein, an einem festen Punkt der Rundenreihenfolge ([[Magie-Wirkungsdauer-und-Konzentration|Magie: Wirkungsdauer und Konzentration]]).

Ein Held ist an einem Austausch beteiligt, wenn er in dieser Kampfrunde

- in der betreffenden Nahkampf-Gruppe kämpft,
- in sie hineingewirkt hat (Fernkampf, Zauber) oder
- Ziel einer Fernkampf- oder Zauber-Aktion dieses Austauschs ist.

### Wann und welche Würfe

- **Der Zeitpunkt.** Die Entscheidung fällt bei Abschluss des Austauschs: sobald die Paarung fertig abgehandelt ist oder der Fernkampf- oder Zauber-Angriff aufgelöst ist. Der Spieler kann sie nicht bis zum Ende der Kampfrunde aufschieben. Lässt er das Fenster eines Austauschs verstreichen, ist es danach zu.
- **Die Reichweite.** Erreichbar sind nur Austausche dieser Kampfrunde, an denen der Held beteiligt war. Frühere Kampfrunden sind nicht erreichbar.
- **Welche Würfe.** In einem solchen Austausch darf der Spieler seine eigenen Würfe wiederholen und alle nicht geheimen Würfe der Nichtspielercharaktere, offen oder verdeckt. Nicht wiederholbar sind die Würfe anderer Spieler, außer durch das gemeinsame Opfer der Gruppe, und geheime Würfe des Meisters.
- **Ein Wurf je Reroll.** Ein Reroll betrifft genau einen Wurf. Mehrere Würfe zu bündeln ist ausgeschlossen: Der Spieler wiederholt nicht Attacke und Parade zusammen, um danach das bessere Paket zu wählen, sondern entweder die Attacke oder die Parade.
- **Mehrere Stellen.** Im Fenster eines Austauschs darf der Spieler nacheinander beliebig viele Stellen wiederholen, bis der Vorrat 0 ist. Jede Entscheidung wird samt ihrer Folgen vollständig abgeschlossen, bevor die nächste beginnt.
- **Die Kosten.** Ein Reroll kostet nur 1 aus dem Vorrat. Er kostet keine AK, keine Aktion und kein anderes Budget.

Die Würfe eines Austauschs folgen einer festen Kette: Angriffswurf, Verteidigungswurf, Schadenswurf (Schadenspunkte, daraus Trefferpunkte), W100-Wurf der Trefferzone mit einem möglichen Bündel von Trefferzonen-Rerolls, danach die Folgeproben (Klingenbruch, Selbstbeherrschungsprobe, Zustands- und Patzerauswertung). Dazu kommt der Initiative-Wurf der Nahkampf-Gruppe, sofern er in dieser Kampfrunde bestimmt wurde.

### Was nach einem Reroll neu gewürfelt wird

Ein Reroll entwertet genau die nachfolgenden Würfe desselben Austauschs, deren Eingaben sich durch den neuen Wert geändert haben. Sie werden neu ausgewertet, alles andere bleibt bestehen. Welche Würfe das sind, ergibt sich zwingend aus der Kette. Der Meister entscheidet nichts über Umfang oder Reihenfolge der Neuwürfe. Er passt nur Erzählfolgen und Positionen an, die ein geänderter Ausgang gegenstandslos macht, zum Beispiel „der Nichtspielercharakter war tot“, der jetzt lebt. Neu gewürfelte Würfe darf der Spieler seinerseits wiederholen, solange er Vorrat hat.

**Angriffswurf.** Das Gitter ([[Nahkampf-Gruppen-und-das-Meisterscreen-Gitter]]) wird mit der neuen Erfolgsstufe der Attacke und dem vorhandenen Verteidigungswurf neu abgelesen. Das ergibt Treffer ja oder nein und den Ausgang der Zelle. Der Verteidigungswurf bleibt. Der W100-Wurf der Trefferzone bleibt auch, außer bei der Wahl unter a). Fehlschlag und Patzer zählen hier auch als andere Stufe, nicht nur n, g, m und f untereinander.

- **a) Weiterhin Treffer, andere Stufe.** Der Schadenswurf wird neu geworfen, die Schadenspunkte neu, die Trefferpunkte neu berechnet. Der W100-Wurf der Trefferzone wird nicht neu geworfen, die getroffene Zone bleibt. Ausnahme: Schaltet die neue Stufe über die Ansage-Tabelle zusätzliche Ansagepunkte frei und wählt der Spieler jetzt Trefferzonen-Rerolls, wird das gesamte Bündel neu aufgesetzt: alle schon geworfenen Rerolls plus die neu hinzukommenden, zusammen, in einer frischen Auflösung mit der neuen Gesamtzahl. Die Zone darf dabei nachträglich angesagt werden, auch wenn der ursprüngliche Angriff keine Ansage hatte. Eine freiwillige Selbst-Erschwerung als Quelle kann nicht nachträglich ergänzt werden, denn sie verlangt die Ansage vor dem Wurf.
- **b) Jetzt Fehlschlag oder Patzer.** Schadenswurf, Zonenwurf und alle Trefferfolgen entfallen ersatzlos. Ein neu gewürfelter Patzer löst die Patzerauswertung der Probenart aus (für den Nahkampf [[Nahkampf]]).
- **c) Vorher Fehlschlag oder Patzer, jetzt Treffer.** Schadenswurf und Zonenwurf werden zum ersten Mal geworfen, mit der Stufe des neuen Treffers. Trefferzonen-Rerolls gibt es nur, wenn eine Quelle sie stellt.
- **d) Unveränderte Stufe, weiterhin Treffer.** Schadenswurf und Zonenwurf bleiben unverändert.

**Verteidigungswurf** (Parade oder Ausweichen). Dasselbe Gitter wird mit der vorhandenen Erfolgsstufe der Attacke und dem neuen Verteidigungswurf abgelesen. Kippt der Austausch zwischen Treffer und kein Treffer, folgt die Kette aus Schaden und Trefferzone wie oben. Der Angriffswurf bleibt. Bleibt der Ausgang des Gitters gleich, bleibt alles Nachfolgende.

**Schadenswurf.** Die Schadenspunkte werden neu geworfen, und die Trefferpunkte werden mit den Schritten der Schadenspipeline neu berechnet, mit denselben Rundungen. Schadensgekoppelte Folgeproben wie der Klingenbruch folgen. Angriff, Verteidigung und der Zonenwurf bleiben, die Zone ändert sich nicht.

**Zonenwurf.** Ein Reroll aus dem Vorrat auf die Zone ersetzt das gesamte Ergebnis des Bündels durch einen neuen W100. Der Zusatzeffekt der neuen Zone gilt. Angriff, Verteidigung und die Höhe der Schadenspunkte bleiben, nur Zone und Zusatzeffekt ändern sich. Die Neuaufsetzung des Bündels unter a) ist davon verschieden: Sie wird nicht aus dem Vorrat bezahlt, sondern von den Trefferzonen-Rerolls, die die neue Stufe über die Ansage-Tabelle freischaltet.

**Initiative-Wurf der Nahkampf-Gruppe** (nur wenn in dieser Kampfrunde bestimmt). Die Rangfolge innerhalb der Gruppe wird ab der geänderten Position neu bestimmt, ebenso alle danach noch nicht abgehandelten Paarungen. Paarungen vor der geänderten Position bleiben.

**Sonstiger Wurf** (Klingenbruch, Zauberprobe, Selbstbeherrschungsprobe, Probe auf einen Zustand). Neu ausgewertet wird nur die Folge, die unmittelbar an den Wurf gekoppelt ist. Alles Parallele bleibt.

**Der gegnerische Angriffswurf.** Der Angriffswurf des Gegners in einer Paarung, an der der Held beteiligt ist, ist ein nicht geheimer Wurf des Meisters und damit wiederholbar. Die Folgen gelten aus der Sicht des Verteidigers: Das Gitter wird mit der neuen Stufe der gegnerischen Attacke und dem vorhandenen eigenen Verteidigungswurf neu abgelesen, danach folgt je nach Ergebnis die gegnerische Kette aus Schaden und Zone. Der eigene Verteidigungswurf bleibt. Nur der Ausgang des Gitters und das Nachfolgende werden neu bestimmt.

### Initiative

- **Der Wurf der Kampfrunde.** Der Initiative-Wurf der ganzen Runde wird einmal zu Kampfbeginn geworfen. Wiederholbar ist er nur im Fenster vor Beginn von Kampfrunde 1, nicht über die Regeln dieses Abschnitts. Nach Kampfbeginn ist der einzige weitere Initiative-Wurf der eines Teilnehmers, der später hinzukommt. Auch er ist nicht wiederholbar. Der Gitter-Ausgang „Ini bestimmen“ wirkt nicht für die ganze Runde.
- **Der Wurf der Nahkampf-Gruppe.** Der Initiative-Wurf einer Nahkampf-Gruppe bei ihrer Bildung, bei einem späteren Beitritt oder beim Gitter-Ausgang „Ini bestimmen“ ist wiederholbar, wenn er in dieser Kampfrunde bestimmt wurde. Das geschieht im Fenster des Austauschs, an dem der Held in dieser Gruppe beteiligt ist. Der neue Wurf ordnet die Abfolge der Gruppe ab der geänderten Position neu.

### Beispiele

Zwei Helden, A und B, und zwei Nichtspielercharaktere stehen in zwei Nahkampf-Gruppen. Held A ist in Gruppe A und hat die beste Initiative der Runde, deshalb wird Gruppe A zuerst abgehandelt. Held B ist in Gruppe B.

- **Die eigene Paarung.** Held A und sein Gegner, der Nichtspielercharakter 1, tauschen Schläge. Bei Abschluss ihrer Paarung darf A seine eigenen Würfe und alle nicht geheimen Würfe des Nichtspielercharakters 1 aus dieser Paarung wiederholen: Attacke, Parade, Schaden, Trefferzone. Die Würfe von Held B darf er nicht wiederholen. Danach ist das Fenster zu, A kann nicht bis zum Ende der Kampfrunde warten.
- **Eine fremde Gruppe.** Held A hat in dieser Kampfrunde nicht in Gruppe B gewirkt. Er darf dort gar nichts wiederholen, auch keine Würfe der Nichtspielercharaktere. Hätte er mit einem Fernkampf oder einem Zauber in Gruppe B hineingewirkt oder wäre er selbst Ziel eines Fernkampfs oder Zaubers aus Gruppe B, wäre er dort beteiligt. Er dürfte im Fenster dieses Austauschs die nicht geheimen Würfe der Nichtspielercharaktere wiederholen, nicht die von Held B.
- **Eine bessere Stufe.** Ein Held trifft im Nahkampf mit nAT, ohne Ansage der Zone. Schaden und Trefferzone sind gefallen. Bei Abschluss der Paarung wiederholt er den Angriffswurf und erhält mAT. Die Schadenspunkte werden neu geworfen, die Trefferpunkte neu berechnet. Der Zonenwurf bliebe stehen. Der Held wählt aber die Ansagepunkte der mAT für Trefferzonen-Rerolls und sagt „Kopf“ an: Das Bündel wird komplett neu aufgesetzt. Der Vorrat sinkt um 1.
- **Der Treffer kippt.** Ein gAT-Treffer steht, Schaden und Zone auch. Der Held wiederholt den Angriffswurf und erhält einen Fehlschlag. Schadenswurf, Zonenwurf und alle Trefferfolgen entfallen ersatzlos. Der Vorrat sinkt um 1.
- **Die Initiative der Gruppe.** In dieser Kampfrunde ist Gruppe A neu entstanden. Held A hat seinen Initiative-Wurf für die Gruppe gewürfelt und liegt hinter dem Nichtspielercharakter 1, der zuerst zuschlug. Im Fenster seines Austauschs wiederholt er den Initiative-Wurf und erhält eine bessere Differenz. Die Abfolge der Gruppe wird ab der geänderten Position neu abgewickelt. Der Vorrat sinkt um 1. Ein Initiative-Wurf der ganzen Runde wäre hier nicht wiederholbar.

### Grenzfälle

- Ein Reroll, der einen schon verrechneten Treffer in einen Fehlschlag oder Patzer verwandelt, ist zulässig. Der neue Wert zählt bedingungslos, und die Entscheidung liegt beim Spieler, der den Reroll ausgibt.
- Reicht der Vorrat für die gewünschte Tiefe der Neuwürfe nicht, bleibt das bis dahin erwürfelte Ergebnis stehen.
- Mehrere Stellen im Fenster eines Austauschs werden streng nacheinander wiederholt. Die erste ist samt Folgen abgeschlossen, bevor die zweite beginnt.
