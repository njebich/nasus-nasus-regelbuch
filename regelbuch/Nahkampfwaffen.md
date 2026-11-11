---
title: Nahkampfwaffen
aliases: [Nahkampfwaffen, Nahkampfwaffe, Waffenbau, Waffenkauf, Grundtyp, Material, Fertigung, Fertigungsstufe, Anpassung, Schaftmaterial, Waffenpreis, Mindeststärke, Rüstungsbrechend, Verfügbarkeit einer Waffe, Anpassungs-Service, Waffe anpassen, Von der Stange, angepasst, Perfekt angepasst]
status: entwurf
---

# Nahkampfwaffen

Der Held kauft eine Nahkampfwaffe nicht als fertiges Stück, er stellt sie zusammen: Er wählt einen Grundtyp, zum Beispiel ein Langschwert, dazu ein Material, eine Fertigungsstufe und eine Anpassung. Bei Waffen mit Schaft kommt das Schaftmaterial hinzu. Aus diesen Bausteinen ergeben sich alle Werte der Waffe und ihr Preis. Eine Waffe, die der Held schon besitzt, kann ein Handwerker später an ihn anpassen.

Wie der Held mit der Waffe kämpft, steht in [[Nahkampf]]. Wie gepanzerte Arme und Beine den unbewaffneten Kampf verändern, steht in [[Ruestung|Rüstung]].

## Die Bausteine

Der Waffenkatalog führt fünf Listen. Andere Bausteine hat eine Nahkampfwaffe nicht.

- **Grundtyp:** die Waffe selbst. Der Katalog kennt 241 Grundtypen in 25 Spezialisierungen.
- **Material:** der Werkstoff. Es gibt 19 Materialien, zum Beispiel Eisen, Stahl, Holz, Leder und Adamantit.
- **Fertigung:** die Güte der Arbeit. Es gibt 7 Fertigungsstufen, von der schlechtesten zur besten:
  Ausschuss, Goblin Massenfab., Massenfabrikation, Gesellenarbeit, Meisterarbeit, Großmeisterarbeit, Einzelstück.
  Jede Stufe hat einen Tageslohn. Je höher die Stufe, desto höher der Lohn.
- **Anpassung:** die Passform für den Träger. Es gibt 3 Stufen: Von der Stange, angepasst und Perfekt angepasst.
- **Schaftmaterial:** nur bei Waffen mit Schaft. Es gibt 15 Schaftmaterialien.

### Wer was wählen darf

Jeder Held darf jeden Grundtyp, jedes Material, jede Fertigung, jede Anpassung und jedes Schaftmaterial wählen. Das Volk, das im Katalog bei einem Baustein steht, schränkt die Wahl nicht ein. Es verändert nur die Verfügbarkeit.

Ein Grundtyp, den der Katalog als nicht aktiv führt, ist nicht wählbar.

Leder und Peitschen gehören fest zusammen. Peitschen (Hauptfertigkeit Unbewaffnet, Spezialisierung Peitschen) bestehen immer aus Leder, eine Materialwahl haben sie nicht. Keine andere Spezialisierung darf Leder als Material wählen.

### Schaftmaterial

Ein Schaftmaterial haben nur die Waffen von 7 der 25 Spezialisierungen:

- bei den Hiebwaffen: Äxte, Beidhand-Hiebwaffen und Stumpfe Hiebwaffen, aber nicht Kettenwaffen,
- alle vier Spezialisierungen der Stangenwaffen: Hellebarden, Lanzen, Speere und Stäbe.

Bei allen anderen Waffen entfällt das Schaftmaterial in jeder Rechnung dieses Kapitels.

Das Schaftmaterial „Standard“ ist ein Schaft aus Hartholz. Es verändert keinen Wert der Waffe.

## Die Werte der Waffe

Jeder Wert ist die Summe der Einträge, die die gewählten Bausteine für ihn führen. Ein leerer Eintrag zählt als 0.

- **Bonus auf die Attacke ([[Glossar#AT|AT]]) und Bonus auf die Parade ([[Glossar#PA|PA]]):** Grundtyp + Material + Anpassung + Schaftmaterial.
- **Waffenklasse ([[Glossar#WK|WK]]):** Grundtyp + Material. Rundung und Gebrauch der Waffenklasse stehen in [[Nahkampf]].
- **Stärke-Malus:** Grundtyp + Material.
- **Klingenbrecher:** Grundtyp + Material + Fertigung.
- **Klingenschutz:** Grundtyp + Material + Fertigung + Schaftmaterial. Klingenbrecher und Klingenschutz braucht die Klingenbruch-Probe ([[Nahkampf-im-Kampf]]).
- **Rüstungsbrechend (RB):** allein der Wert des Grundtyps. Kein anderer Baustein verändert ihn.
- **Rezept-Erschwerung:** Grundtyp + Material. Sie gilt für die Handwerksprobe, mit der die Waffe hergestellt oder nach einem Klingenbruch repariert wird ([[Wissens-Handwerks-und-Kulturfertigkeiten]]).

Bonus auf Attacke und Parade, Stärke-Malus, Klingenbrecher, Klingenschutz und Waffenklasse können negativ werden. Holz hat zum Beispiel beim Klingenbrecher −11 und beim Klingenschutz −7.

Bei 17 der 241 Grundtypen fehlt der Wert für die Rezept-Erschwerung. Für sie ist eine Handwerksprobe erst möglich, wenn der Meister nach eigenem Ermessen einen Wert festlegt.

### Mindeststärke

Jede Waffe hat eine Mindeststärke für den einhändigen und eine für den zweihändigen Griff. Was dem Helden bei zu wenig Stärke geschieht, steht in [[Nahkampf]].

```text
Mindeststärke einhändig  = Mindeststärke einhändig des Grundtyps × Faktor des Materials

Mindeststärke zweihändig = Mindeststärke zweihändig des Grundtyps × Faktor des Materials
                           + Wert der Anpassung + Wert des Schaftmaterials
```

Das Material hat je einen Faktor für den einhändigen und den zweihändigen Griff. Führt es keinen Faktor, gilt 1. Die Faktoren liegen zwischen 0,5 und 1,3, zum Beispiel 0,8, 0,9 oder 1,2.

Das Ergebnis der Malnahme wird sofort auf eine ganze Zahl aufgerundet, bevor Anpassung und Schaftmaterial dazukommen ([[Wuerfeln-und-Proben]]).

## Der Preis

Preise stehen in Dublonen (D), der Silber-Dublone. Kleinere Beträge stehen in Fuffzisch (Ffz.): 1 D = 1000 Ffz. Ein Preis hat die Form „92 D 250 Ffz.“. Die Gold-Dublone (G) ist 10 D wert. Sie ist unüblich und steht auf keiner Preisliste.

```text
Preis = Materialpreis-Faktor des Grundtyps × Preis des Materials
        + Tageslohn der Fertigung × Arbeitstage

Arbeitstage = Arbeitszeit des Grundtyps + Arbeitszeit der Anpassung
```

Der Tageslohn der Fertigung wird also mit der ganzen Bauzeit malgenommen. Die Anpassung verteuert die Waffe, indem sie die Bauzeit verlängert: Von der Stange um 0 Tage, angepasst um 1 Tag, Perfekt angepasst um 2 Tage.

Trägt der Grundtyp das Merkmal „Holzschaft“ oder „Holzschaft, Schnell“, kommt das Schaftmaterial hinzu:

```text
Arbeitstage = Arbeitszeit des Grundtyps + Arbeitszeit der Anpassung
              + Arbeitszeit des Schaftmaterials

Preis       = wie oben
              + Preis des Schaftmaterials je Meter × Länge der Waffe in Metern
```

Der Preis wird anders gerundet als die übrigen Werte: Die ganze Rechnung läuft ohne Rundung durch. Erst das Endergebnis wird einmal auf drei Stellen nach dem Komma aufgerundet, also auf ganze Fuffzisch.

Hat ein Grundtyp keinen Materialpreis-Faktor, hat die Waffe keinen Preis. Das betrifft die unbewaffneten Kampfstile: Ringen, Boxen, Biss, Huftritt und die 7 exotischen Kampfstile einzelner Völker. Ihre übrigen Werte entstehen wie bei jeder anderen Waffe.

## Die Verfügbarkeit

Jeder Baustein hat eine Verfügbarkeit für die Alte Welt und eine für die Neue Welt. Sie sagt, wie schwer er zu beschaffen ist ([[Gueter-Preise-und-Verfuegbarkeit]]). Es gibt die Stufen 1 bis 7, dabei ist 1 die beste und 7 die schlechteste. Dazu kommen zwei Sonderwerte:

- **M (Meisterverfügbarkeit):** Über diese Waffe verfügt allein der Meister.
- **NICHT KAUFBAR.**

Für die fertige Waffe gilt je Welt der schlechteste Wert ihrer Bausteine: Grundtyp, Material, Fertigung, Anpassung und Schaftmaterial. M schlägt jede Zahl, NICHT KAUFBAR schlägt alles.

M haben zurzeit nur Adamantit als Material und die Schaftmaterialien aus Adamantit. NICHT KAUFBAR sind die Grundtypen ohne Materialpreis-Faktor, also die unbewaffneten Kampfstile. Das Schaftmaterial „Standard“ hat in beiden Welten die Verfügbarkeit 1.

## Wann die Werte gelten

Die Werte entstehen beim Bau oder Kauf aus den gewählten Bausteinen. Wählt der Held einen Baustein neu, ändern sie sich mit.

## Schilde

Der Katalog führt 12 der 241 Grundtypen unter der Spezialisierung Schild. Schilde werden nicht nach den Regeln dieses Kapitels zusammengesetzt. Sie teilen mit den Waffen nur die Liste der Anpassungen.

## Eine Waffe anpassen lassen

Die Anpassung gehört zum Träger, nicht zur Waffe. Sie gilt für den, für den die Waffe zuletzt angepasst wurde. Für jeden anderen verhält sich die Waffe wie Von der Stange. Dieselbe Waffe kann so für verschiedene Träger verschiedene Anpassungen haben.

Findet der Held eine Waffe, die für ihren früheren Besitzer Perfekt angepasst wurde, führt er sie also wie Von der Stange. Das bleibt so, bis er sie für sich anpassen lässt. Ob der frühere Besitzer die Waffe noch hat, spielt keine Rolle.

### Das Ziel

Der Held lässt die Waffe auf „angepasst“ oder auf „Perfekt angepasst“ bringen. Von der Stange ist kein Ziel: Diesen Stand hat jede Waffe für einen neuen Träger von selbst, ohne dass ein Handwerker etwas tut.

### Der Handwerker

Der Handwerker muss mindestens die Fertigungsstufe beherrschen, in der die Waffe gefertigt ist. Es gilt die Reihenfolge der sieben Stufen von Ausschuss bis Einzelstück. Findet der Held keinen solchen Handwerker, ist kein Versuch möglich.

Handwerker und Träger dürfen dieselbe Person sein.

### Der Preis der Anpassung

```text
Preis der Anpassung = Tageslohn des Handwerkers × Arbeitszeit der Zielstufe
```

Der Tageslohn ist der Lohn der Fertigungsstufe des Handwerkers. Die Arbeitszeit beträgt 1 Tag für angepasst und 2 Tage für Perfekt angepasst. Weder der Grundtyp noch das Material der Waffe ändern diesen Preis.

Die Arbeitszeit der Zielstufe gilt immer ganz. Ist die Waffe für den Helden schon angepasst und soll Perfekt angepasst werden, zahlt er die vollen 2 Tage. Der eine Tag der früheren Anpassung wird nicht angerechnet.

Die Anpassung kostet mindestens 1 D 500 Ffz. (ein Handwerker der Stufe Ausschuss, Ziel angepasst) und höchstens 284 D (ein Handwerker der Stufe Einzelstück, Ziel Perfekt angepasst). Gerundet wird wie beim Preis der Waffe.

### Die Probe

Der Handwerker würfelt eine Handwerksprobe ([[Wissens-Handwerks-und-Kulturfertigkeiten]]). Zwei Angaben kommen von der Waffe und vom Ziel:

- Die Rezept-Erschwerung ist allein der Wert des Materials der Waffe. Der Wert des Grundtyps zählt hier nicht. Das Material bestimmt also, wie schwer die Anpassung ist, aber nicht, was sie kostet. Der Wert kann negativ sein.
- Die Herstellungszeit ist die Arbeitszeit der Zielstufe.

Preis und Rezept-Erschwerung richten sich nach dem Zeitpunkt, zu dem der Held die Anpassung in Auftrag gibt.

## Beispiele

### Ein Langschwert kaufen

Der Held lässt ein Langschwert aus Eisen bauen. Das Langschwert hat 4 Tage Arbeitszeit und den Materialpreis-Faktor 1. Eisen kostet 50. Ein Geselle nimmt 6 am Tag.

- Gesellenarbeit, Von der Stange: 1 × 50 + 6 × (4 + 0) = 50 + 24 = 74 D.
- Gesellenarbeit, angepasst: 50 + 6 × (4 + 1) = 50 + 30 = 80 D.
- Gesellenarbeit, Perfekt angepasst: 50 + 6 × (4 + 2) = 50 + 36 = 86 D.

Aus Stahl (Preis 125) kostet dasselbe Schwert als Gesellenarbeit Von der Stange 1 × 125 + 6 × (4 + 0) = 125 + 24 = 149 D.

Lässt der Held das Eisenschwert von einem Großmeister bauen (71 am Tag), zahlt er:

- Von der Stange: 50 + 71 × (4 + 0) = 50 + 284 = 334 D.
- angepasst: 50 + 71 × (4 + 1) = 50 + 355 = 405 D.
- Perfekt angepasst: 50 + 71 × (4 + 2) = 50 + 426 = 476 D.

### Eine billige Axt

Der Held kauft eine Axt aus Eisen (Preis 50), Fertigung Ausschuss (1,5 am Tag), Von der Stange, mit dem Schaftmaterial „Standard“. Die Axt hat 1,5 Tage Arbeitszeit und den Materialpreis-Faktor 1,8.

```text
Preis = 1,8 × 50 + 1,5 × (1,5 + 0) = 90 + 2,25 = 92,25
```

Zwischendurch wird nicht gerundet. Das Endergebnis hat schon höchstens drei Stellen nach dem Komma und bleibt 92,250 D, also 92 D 250 Ffz.

### Eine Axt aus Adamantit

Der Held will eine Axt aus Adamantit, Gesellenarbeit, Von der Stange, mit dem Schaftmaterial „Standard“. Grundtyp, Fertigung, Anpassung und Schaftmaterial haben in beiden Welten die Verfügbarkeit 1. Adamantit hat in beiden Welten M. Die Axt hat damit in der Alten und in der Neuen Welt die Verfügbarkeit M: Das Material entscheidet, obwohl jeder andere Baustein die beste Stufe hat.

### Ein Großmeister passt ein Langschwert an

Der Held besitzt ein Langschwert aus Eisen, eine Großmeisterarbeit. Nur ein Großmeister oder ein Handwerker der Stufe Einzelstück darf es anpassen. Der Großmeister nimmt 71 am Tag.

- Ziel angepasst: 71 × 1 = 71 D.
- Ziel Perfekt angepasst: 71 × 2 = 142 D.

### Von angepasst auf Perfekt angepasst

Die Waffe des Helden ist eine Gesellenarbeit und für ihn schon angepasst. Ein Geselle (6 am Tag) soll sie Perfekt anpassen. Der Held zahlt 6 × 2 = 12 D, die vollen 2 Tage.
