---
title: "Magie: Wirkungsdauer und Konzentration"
aliases: [Vorbereitungsdauer, Vorbereitungszeit, Effektdauer, Wirkungsdauer, VD, ED, WD, VD/ED/WD, Mentaler Fokus, MF, MF-Probe, Konzentrationsprobe, Freie Aura, Freie Magie, Verfügbare Weisheit, Tätigkeitsleiter, Pool, Aurabann, kein Aurabann, Zauber halten]
status: entwurf
---

# Magie: Wirkungsdauer und Konzentration

Wer zaubert, KI einsetzt oder Psi wirkt, braucht Zeit und Konzentration. Jede Wirkung mit Dauer läuft in drei Phasen ab. Wird der Held unterbrochen, kann ihn der Mentale Fokus retten. Wie viel er gleichzeitig aufrechterhalten kann, begrenzt ein Vorrat, und der Aurabann regelt, welche Gegenstände ein Zauber erfassen darf.

## Die drei Phasen: Vorbereitung, Effekt, Wirkung

Das Zeitmodell gilt für jede Wirkung mit Dauer, die an eine Probe gebunden ist. Es gilt für Spruchmagie ([[Spruchmagie]]) und für KI ([[KI]]).

Die kleinste Zeiteinheit ist die Kampfrunde (KR). Zurzeit gilt 1 KR = 1 Sekunde (siehe [[Zeit-und-Spielablauf]]).

- **Vorbereitungsdauer (VD, auch Vorbereitungszeit):** die Zeit vor der entscheidenden Probe. Der Held muss sich durchgehend konzentrieren.
- **Effektdauer (ED):** die Zeit zwischen der gelungenen Probe und der vollen Wirkung.
- **Wirkungsdauer (WD):** die Zeit, für die die volle Wirkung danach anhält.

Die Reihenfolge ist immer dieselbe:

1. Die VD verstreicht.
2. Der Held würfelt die Probe.
3. Gelingt sie, beginnt die ED.
4. Ist die ED abgeschlossen, beginnt die WD. Bei der ED „sofort“ beginnt die WD sofort. Sonst beginnt sie, wenn die ED ihre eigene Anlaufphase beendet hat.

### „Sofort“ als Effektdauer

„Sofort“ ist ein gültiger Wert für die ED: Die Wirkung tritt unmittelbar ein, ohne Anlaufphase. Spruchmagie und KI nutzen ihn verschieden.

- **Spruchmagie:** Ohne andere Angabe baut sich die Wirkung während der ED halbiert auf und beginnt erst in der Kampfrunde nach dem Ende der Vorbereitungszeit. „Sofort“ überspringt diese Verzögerung. Einzelne Zauber geben „sofort“ an.
- **KI:** Jede KI-Fähigkeit hat immer die ED „sofort“. Eine Anlaufphase gibt es bei KI nie.

### Zauber halten

Der Held darf nur einen Zauber halten, dessen VD schon abgeschlossen ist. Seine Probe war dann bereits erfolgreich. Das Einsetzen des gehaltenen Zaubers beginnt seine ED. ED und WD laufen also nicht während der Haltezeit.

### Formeln der Kategorien

Wie sich VD verkürzen und WD verlängern lässt, regelt jede Kategorie selbst.

- KI tauscht Erschwerungspunkte gegen kürzere VD und längere WD (siehe [[KI]]).
- Spruchmagie teilt die VD nach der Zauberstufe 1, 2 oder 3 und kennt die Schnell-Zaubern-Talente (siehe [[Spruchmagie]]).

Auch das Aufrechterhalten während der WD regelt die Kategorie. Bei der Spruchmagie ist es die verfügbare Weisheit, siehe unten.

## Mentaler Fokus

Der Mentale Fokus (MF) ist eine zweite Chance. Er rettet die Konzentration, wenn die Selbstbeherrschungs-Probe ([[Glossar#SB|SB]]) misslingt, die der Held zum Halten der Konzentration ablegen muss. Er gilt für Spruchmagie, Psi und KI gleichermaßen.

### Der Wert

```text
MF = Willenskraft + Mentaler Fokus
```

Willenskraft ist die [[Eigenschaften|Eigenschaft]]. Mentaler Fokus ist der Wert der gleichnamigen [[Sonderfertigkeiten|Sonderfertigkeit]].

### Wie die MF-Probe abläuft

Die MF-Probe heißt auch Konzentrationsprobe. Sie läuft nach diesen Regeln ab:

1. Der Held versucht unter Beschuss etwas, das Konzentration verlangt. Der Meister verlangt eine Selbstbeherrschungs-Probe (siehe [[Treffer-und-Schaden]]).
2. Misslingt sie, würfelt der Held die MF-Probe als Zweitchance.
3. Die MF-Probe ist doppelt gemindert, und beide Abzüge gelten zugleich:
   - um die Verrissgröße der misslungenen SB-Probe, also darum, wie weit sie verfehlt wurde,
   - um die Behinderung (BE).

Die MF-Probe wird nie von selbst ausgelöst. Der Auslöser ist immer die misslungene Selbstbeherrschungs-Probe, nicht der Treffer.

### Wann der Meister die Selbstbeherrschung verlangt

Der Meister verlangt die konzentrationserhaltende Selbstbeherrschungs-Probe nach eigenem Ermessen, wann immer der Held unter Beschuss etwas versucht, das Konzentration erfordert. Eine feste Liste dieser Effekte gibt es nicht.

**Pflicht in zwei Fällen:** Läuft eine VD von KI, Psi oder Spruchmagie, oder ist der Zauber bipolar, ist die Selbstbeherrschungs-Probe nach einem Treffer über der Trefferschwelle ([[Glossar#TS|TS]]) Pflicht. Misslingt sie, folgt die MF-Probe. Das gilt auch für andere konzentrationspflichtige Effekte, nicht nur für Zauber. Ein Beispiel ist eine KI-Fähigkeit während der VD. Bei jedem anderen konzentrationspflichtigen Effekt entscheidet der Meister.

### Welche Proben eine Selbstbeherrschung auslösen dürfen

**Immer, unabhängig von ihrer Formel:**

- jede Spruchmagie-Probe,
- jede KI-Probe,
- jede Psi-Probe.

**Außerdem jede weitere Probe mit einem geistigen Term.** Ein geistiger Term ist eine der fünf geistigen Eigenschaften (Intelligenz, Mut, Sinnesschärfe, Willenskraft, Ausstrahlung) oder ein von ihnen abgeleiteter Eigenschaftsbonus. Dass ein solcher Term in der Formel steht, genügt. Eine gemischte Formel mit körperlichen und geistigen Termen zählt als geistig. Einziges Kriterium ist der geistige Term. Beispiele:

- Ein Medikus legt unter Feuer einen Verband an. Die Formel enthält den Eigenschaftsbonus der Intelligenz, den Wert der WHK-Fertigkeit und die Spezialisierung.
- Der Held legt im Kampf eine Probe auf die Grundfertigkeit Orientierung plus Sinnesschärfe ab, um Fluchtweg oder Gegnerrichtung zu bestimmen.
- Der Held versucht, Angst durch eine Willenskraft-Probe zu beherrschen.

**Nie, egal was ihre Formel enthält:**

- die Selbstbeherrschungs-Probe selbst, denn sie ist der Auslöser des Mentalen Fokus und kann sich keine Zweitchance verschaffen,
- die Attacke ([[Glossar#AT|AT]]),
- die Parade ([[Glossar#PA|PA]]),
- das Ausweichen ([[Glossar#AW|AW]]),
- der Fernkampf ([[Glossar#FK|FK]]).

Der Ausschluss gilt auch für den Fernkampf, obwohl seine Probe auf Sinnesschärfe zieht.

## Freie Aura, freie Magie, verfügbare Weisheit

Drei Vorräte begrenzen, was der Held gleichzeitig aufrechterhalten kann. Jede Disziplin hat ihren eigenen Vorrat auf einem eigenen Attribut:

| Disziplin | Vorrat | Attribut |
|---|---|---|
| KI | freie Aura | Aura |
| Psi | freie Magie | Magie |
| Spruchmagie | verfügbare Weisheit | Weisheit |

Die Vorräte sind unabhängig voneinander. Eine aktive KI-Fähigkeit senkt nur die freie Aura, nicht die freie Magie und nicht die verfügbare Weisheit, und umgekehrt. Ein Held mit allen drei Disziplinen führt drei getrennte Zählungen. Der Verbrauch eines Vorrats ändert nie den Attributwert selbst. Siehe [[Attribute]].

### Wie die Vorräte berechnet werden

```text
freie Aura          = Aura − Anzahl der aufrechterhaltenen KI-Fähigkeiten
freie Magie         = Magie − Summe der gewählten Psi-Stufen
                      aller aufrechterhaltenen Psi-Fähigkeiten
verfügbare Weisheit = Weisheit
                      − halber Zaubergrad je aufrechterhaltenem Anhaltend-Zauber
                      − voller Zaubergrad je aufrechterhaltenem Bipolar-Zauber
```

- **Freie Aura:** Jede aktive KI-Fähigkeit kostet 1, egal wie stark sie ist.
- **Freie Magie:** Jede aktive Psi-Fähigkeit kostet die Psi-Stufe, die der Held beim Einsatz gewählt hat (1 bis 7).
- **Verfügbare Weisheit:** Anhaltend-Zauber kosten den halben Zaubergrad, Bipolar-Zauber den vollen. Der Wert wird nie gerundet. Er beginnt bei der ganzzahligen Weisheit (Kreis + 1), jede Kostenstufe ist ein halber oder ganzer Zaubergrad, und deshalb liegt jeder Wert auf einem Schritt von 0,5.

Ohne aufrechterhaltene Effekte ist der Vorrat so groß wie das Attribut. Mehrere aufrechterhaltene Effekte einer Disziplin summieren sich. Nur aufrechterhaltene Effekte kosten. Eine KI- oder Psi-Wirkung mit abgelaufener Wirkungsdauer und ein Einmalig-Zauber verbrauchen nichts. Bei der Spruchmagie zehren nur Anhaltend- und Bipolar-Zauber an der Weisheit. Die Zauberarten erklärt das Kapitel [[Spruchmagie]].

### Der Vorrat begrenzt einen neuen Effekt

Ein Vorrat wird nie negativ. Ein neuer Effekt ist nur wählbar, wenn er den Vorrat nicht ins Minus treibt. Das wird zu Beginn der Vorbereitungszeit des neuen Effekts geprüft:

- **KI:** Der Held braucht während der Vorbereitungszeit mindestens 1 freie Aura. Danach kostet die Fähigkeit 1.
- **Psi:** Die gewählte Psi-Stufe darf höchstens so groß sein wie die freie Magie. Danach kostet die Fähigkeit die Stufe.
- **Spruchmagie:** Der Zaubergrad darf höchstens so groß sein wie die verfügbare Weisheit. Verglichen wird mit dem vollen Grad, nicht mit den halben Kosten. Danach kostet der Zauber den halben Grad (Anhaltend) oder den vollen Grad (Bipolar).

### Was der Held währenddessen tun kann

Der Wert des Vorrats bestimmt, was der Held beim Wirken und Aufrechterhalten körperlich nebenbei tun kann:

- 1: steht oder sitzt still und konzentriert sich.
- 2: geht, redet, schießt, wirft, reitet langsam, fährt langsam.
- 3: läuft, reitet zügig, fliegt, fährt schnell.
- 4: sprintet, klettert, galoppiert, fliegt riskant, fährt riskant.
- 5: wirft laufend, schießt schnell fahrend.
- 6: schießt sprintend, wirft riskant fahrend.
- 7: kämpft im Nahkampf.

Bei einer verfügbaren Weisheit mit Bruchteil gilt der ganzzahlige Anteil: 5,5 entspricht 5.

Diese Liste beschreibt, was zu welchem Wert passt. Sie begrenzt die Aktionspunkte nicht selbst. Im Kampf kostet es Aktionspunkte ([[Glossar#AP|AP]]), in einer Kampfrunde einen neuen Zauber zu wirken. Der Preis hängt vom Vorrat der Disziplin ab (siehe [[Kampfrunde-Aktionen-Initiative-und-Sicht]]):

- Vorrat 1 oder 2: 3 AP.
- Vorrat 3 oder 4: 2 AP.
- Vorrat 5 oder 6: 1 AP.
- Vorrat 7 oder mehr: 0 AP.

### Freigabe

Der Vorrat füllt sich nicht allmählich wieder auf. Der Beitrag eines Effekts wird sofort und vollständig frei,

- sobald der Effekt endet, weil der Wirker ihn ablegt oder seine Wirkungsdauer abläuft, oder
- sobald ein Zauber die Wirkungsdauer „permanent“ hat: Es gibt nichts aufrechtzuerhalten, der Vorrat ist unmittelbar nach dem Wirken wieder frei. Die Zugangsgrenze (Zaubergrad höchstens so groß wie die verfügbare Weisheit) gilt beim Wirken trotzdem.

### Beispiele

- Der KI-Adept hat Aura 5 und hält 2 KI-Fähigkeiten. Die freie Aura ist 5 − 2 = 3. Er kann ein neues KI-Wirken beginnen, denn 3 ist mindestens 1. Bei Wert 3 passt „läuft oder reitet zügig“. Ein neuer Zauber kostet 2 AP.
- Der Psi-Adept hat Magie 6 und hält eine Psi-Fähigkeit auf Stufe 3. Die freie Magie ist 6 − 3 = 3. Eine zweite Psi-Fähigkeit kann er bis Stufe 3 wählen. Wählt er Stufe 3, ist die freie Magie danach 0, und er kann nichts weiter aufrechterhalten.
- Der Magus hat Weisheit 7 und hält einen Anhaltend-Zauber vom Grad 3. Er kostet 1,5, die verfügbare Weisheit ist 5,5. Ein weiterer Zauber ist bis Grad 5 wählbar (5,5 ≥ 5), ein Zauber vom Grad 6 nicht. Es wird nichts gerundet.
- Derselbe Held hält 1 KI-Fähigkeit und einen Anhaltend-Zauber vom Grad 2. Die freie Aura ist Aura − 1, die verfügbare Weisheit Weisheit − 1. Die freie Magie bleibt unberührt.
- Entspricht die verfügbare Weisheit genau dem Grad eines gewünschten Zaubers, ist er wirkbar.
- Hat der KI-Adept genau 1 freie Aura, darf er den Effekt in der Vorbereitungszeit beginnen. Danach ist seine freie Aura 0, und er kann keine weitere KI-Fähigkeit beginnen, bis eine endet.
- Ein Effekt einer anderen Disziplin ändert die verfügbare Weisheit nicht. Eine KI-Fähigkeit senkt sie also nie.

## Aurabann

Der Aurabann regelt, ob ein Effekt mit dem Ziel „Gegenstand“ einen Gegenstand erfassen darf, der im Besitz oder Griff eines fremden belebten oder beseelten Wesens liegt. Normalerweise gilt ein solcher Gegenstand als belebte Materie und ist als Ziel „Gegenstand“ nicht wählbar, es sei denn, ein Zauber sagt ausdrücklich etwas anderes. Der Aurabann ist diese Ausnahme, hier als feste Regel.

Jeder Effekt trägt einen von zwei Werten. Der Wirkungstext nennt ihn in Klammern:

- **(Aurabann):** Der Effekt ist eingeschränkt.
- **(kein Aurabann):** Der Effekt ist uneingeschränkt.

Zwei Dinge entscheiden, ob der Gegenstand gewählt werden darf:

- Zu welcher Aura gehört er? Zur eigenen Aura des Wirkenden, zu keiner Aura (neutral) oder zu einer fremden Aura.
- Hat der Inhaber der fremden Aura aktiv zugestimmt? Das zählt nur bei fremder Aura und nur bei Effekten mit (Aurabann).

### Die Regeln

**Wunder sind ausgenommen.** Der Aurabann gilt nie für [[Wunder]]. Das ist eine Ausnahme ohne Einzelfallprüfung, auch für künftige, noch nicht erfasste Wunder. Göttlich gewirkte Effekte unterliegen dieser Einschränkung nicht. Alle 60 erfassten Wunder tragen (kein Aurabann).

Die folgenden Regeln gelten für Spruchmagie und Psi.

**Ziel ist nicht „Gegenstand“.** Dann gilt automatisch (kein Aurabann). Der Effekt weist es trotzdem ausdrücklich als (kein Aurabann) aus, denn ausdrückliche Angaben fördern das Verständnis und vermeiden Unsicherheit.

**(kein Aurabann).** Der Gegenstand darf gewählt werden, zu welcher Aura er auch gehört.

**(Aurabann).** Der Gegenstand darf nur gewählt werden, wenn eine dieser drei Bedingungen erfüllt ist:

- Er liegt in der eigenen Aura des Wirkenden.
- Er ist neutral, gehört also zu keiner Aura.
- Der Inhaber der fremden Aura stimmt aktiv zu.

**Zustimmung.** Sie gilt nur für (Aurabann)-Effekte gegen einen Gegenstand in fremder Aura. Sie hebt die Einschränkung vollständig auf, nicht nur teilweise. Sie muss eine aktive Handlung sein. Eine bloß erklärte Zustimmung oder eine Entscheidung des Meisters genügt nicht.

**Jeder Spruchmagie-Effekt mit dem Ziel „Gegenstand“ trägt einen der beiden Werte.** Das sind 49 Effekte.

**Wann geprüft wird.** Der Aurabann wird bei der Zielwahl geprüft, also wenn der Held das Ziel des Effekts ansagt. Danach wird er nicht noch einmal geprüft.

### Beispiele

- **Material schwächen** (Spruchmagie, Aurabann): Der Zauber darf nicht heimlich das Schwert eines Gegners schwächen. Er darf das eigene Schwert schwächen, einen neutralen Gegenstand oder mit aktiver Zustimmung das Schwert eines Verbündeten.
- **Kleine Telekinese** und **Große Telekinese** (Spruchmagie, kein Aurabann): Sie bewegen jeden Gegenstand, unabhängig vom Besitzer.
- **Psi:** Alle Effekte mit dem Ziel „Aura“ oder „Selbst“ tragen (kein Aurabann). Nur Effekte mit dem Ziel „Gegenstand“ tragen (Aurabann). Der Wert folgt also eins zu eins aus dem Ziel.
- **Wasser weihen** (Geweihte, Wunder, Ziel „Gegenstand“): Der Effekt trägt (kein Aurabann), obwohl ein Spruchmagie-Effekt mit demselben Ziel (Aurabann) tragen würde. Die Wunder-Ausnahme greift, bevor das Ziel überhaupt geprüft wird.
