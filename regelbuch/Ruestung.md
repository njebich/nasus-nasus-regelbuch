---
title: Rüstung
aliases: [Rüstung, Rüstungsteil, Rüstungsschutz, RS, Rüstungshinderlichkeit, RH, RHg, RBE, Lage, Trageschicht, Verarbeitung, Anpassung einer Rüstung, Schild als Rüstung, Lage Schild, Gepanzert, Umhang, Zusatzmaterial-Rüstung]
status: entwurf
---

# Rüstung

Der Held trägt Rüstung in Schichten übereinander, getrennt für Kopf, Torso, Arme und Beine. Jedes Rüstungsteil schützt mit seinem Rüstungsschutz ([[Glossar#RS|RS]]) und behindert mit seiner Rüstungshinderlichkeit ([[Glossar#RH|RH]]). Ein Rüstungsteil setzt sich aus drei Bausteinen zusammen: dem Rüstungsteil selbst, seiner Verarbeitung und seiner Anpassung.

## Wo der Held Rüstung trägt

Rüstung sitzt auf einer von vier Körpergruppen: Kopf, Torso, Arme oder Beine. Es sind dieselben Gruppen, in denen Schaden weitergeleitet wird ([[Treffer-und-Schaden]]).

Über jeder Gruppe liegen die Schichten, die Lagen:

- **Lage 0** ist die Kleidung. Sie ist kein Platz für Rüstung.
- **Lage 1 bis 4** nehmen die regulären Rüstungsteile auf. Jedes Rüstungsteil gehört im Katalog zu einer bestimmten Lage.
- **Lage 5** nimmt Umhänge auf oder Zusatzmaterial-Rüstung. Zusatzmaterial-Rüstung kann der Held tragen, aber nicht kaufen.

Vier Gruppen mal fünf Lagen ergeben 20 Plätze für Rüstung. Jeder Platz nimmt ein Rüstungsteil auf, nie mehrere. Der Held darf an einer Gruppe mehrere Lagen übereinander tragen. Der Rüstungsschutz und die RH aller getragenen Teile zählen dann zusammen.

## Die Werte eines Rüstungsteils

Ein leerer Eintrag eines Bausteins zählt als 0.

```text
RS    = RS des Rüstungsteils + RS-Modifikator der Verarbeitung

RH    = Hinderlichkeit des Rüstungsteils
        + Modifikator der Verarbeitung + Modifikator der Anpassung
        mindestens die Nummer der Lage (außer auf Lage 5)

Preis = Materialkosten des Rüstungsteils
        + Lohn pro Tag der Verarbeitung
          × (Arbeitszeit des Rüstungsteils + zusätzliche Tage der Anpassung)
```

Die RH eines getragenen Rüstungsteils ist auf Lage 1 bis 4 also nie kleiner als die Nummer seiner Lage. Auf Lage 5 gilt diese Untergrenze nicht: Ein Umhang kann RH 0 haben.

Ein leerer Platz hat immer RH 0, auf jeder Lage. Die Untergrenze gilt nur für ein Teil, das der Held wirklich trägt.

### Verfügbarkeit

Rüstungsteil, Verarbeitung und Anpassung haben je eine Verfügbarkeit für die Alte Welt und eine für die Neue Welt ([[Gueter-Preise-und-Verfuegbarkeit]]). Für das fertige Rüstungsteil gilt je Welt der höchste der drei Werte.

## Der Schild

Ein getragener Schild wird nicht wie ein Rüstungsteil zusammengesetzt, wirkt aber wie eine weitere Schicht:

- Seine Waffenklasse ([[Glossar#WK|WK]], siehe [[Nahkampf]]) zählt zur RH des Trägers dazu.
- Sein RS gilt zusätzlich, aber nur am linken Arm.

An der linken Hand und am linken Ellenbogen zählt der RS des Schildes in voller Höhe, auch wenn Rüstung dort sonst nur halb schützt ([[Treffer-und-Schaden]]).

Das gilt für jeden Schild gleich, unabhängig von seiner Größe. Der Schild wirkt neben der Rüstung: Trägt der Held beides, gilt beides.

## Von der Rüstung zur Behinderung

Die RH aller getragenen Rüstungsteile an allen Körpergruppen wird zur RHg zusammengezählt. Ein Held ohne Rüstung hat RHg 0.

Aus der RHg ergibt sich die RBE:

```text
RBE = (RHg − ((Konstitution / 5 + Stärke) / 2 + Rüstungsmanöver)) / 6
      mindestens 0
```

Konstitution und Stärke sind [[Eigenschaften]]. Jede Teilung wird sofort aufgerundet, bevor der nächste Schritt folgt ([[Wuerfeln-und-Proben]]). Die RBE geht in die Gewichtsbehinderung ein ([[Behinderung-und-Erschwernis]]).

## Gepanzerte Arme und Beine im unbewaffneten Kampf

Trägt der Held an einem Arm oder Bein ein Rüstungsteil der Lage 4, kämpft er mit dieser Gliedmaße unbewaffnet nicht mit den normalen Werten von Unbewaffnet, sondern mit den Werten des Grundtyps „Gepanzert“ aus dem Katalog der [[Nahkampfwaffen]]. Gepanzert gilt für Arm und Bein gleich. Wie die normale Zeile Unbewaffnet trägt Gepanzert das Merkmal „Schnell“ ([[Kampfrunde-Aktionen-Initiative-und-Sicht]]).

Der Held kann das nicht abwählen. Es gibt zwei Ausnahmen:

- Das Rüstungsteil ist ein Lederpanzer oder ein schwerer Lederpanzer. Dann gilt der normale Schaden von Unbewaffnet.
- Der Held sagt ausdrücklich einen Angriff mit einer anderen Gliedmaße an, zum Beispiel einen Tritt statt eines Fauststoßes. Dann zählt die Gliedmaße, die er wirklich benutzt.

Gepanzert wirkt für jede Hand und jedes Bein einzeln. Trägt der Held an beiden Armen Rüstung der Lage 4, wird jede Hand für sich bestimmt. Führt er in derselben Hand eine Waffe, gilt beides zugleich.

Gepanzert ersetzt auch die Werte eines Schlagrings oder einer Veteranenhand, wenn der Held am selben Arm Rüstung der Lage 4 trägt. Das gilt auch dann, wenn Schlagring oder Veteranenhand die besseren Werte hätten.

### Material, Fertigung und Anpassung von Gepanzert

Der Held wählt für Gepanzert nichts aus. Material, Fertigung und Anpassung folgen aus dem getragenen Rüstungsteil. Die Werte dazu stehen in den Listen der Nahkampfwaffen:

- **Material** nach dem Namen des Rüstungsteils: Eisenpanzer ergibt Eisen, Stahlpanzer ergibt Stahl, Faltstahlpanzer ergibt Faltstahl. Der Zusatz „Schwerer“ ändert das Material nicht.
- **Fertigung** nach der Verarbeitung der Rüstung. Beide Stufen heißen gleich: Gesellenarbeit, Meisterarbeit, Großmeisterarbeit und Einzelstück.
- **Anpassung** nach der Anpassung der Rüstung: von der Stange, angepasst und perfekt angepasst gelten unverändert. Die Stufe „völlig unpassend“ der Rüstung zählt bei Gepanzert als Von der Stange.

Bestimmt wird das bei jeder unbewaffneten Kampfhandlung neu, aus dem Rüstungsteil, das der Held dann an der Gliedmaße trägt.

## Beispiele

**Eine Stoffrüstung.** Der Held kauft eine Stoffrüstung als Meisterarbeit und lässt sie anpassen. Sie hat RS 3 und RH 1 und kostet 227. Ihre Verfügbarkeit ist 3 in der Neuen Welt und 2 in der Alten Welt.

**Ein leerer Platz.** Der Held trägt an einer Körpergruppe auf einer Lage kein Rüstungsteil. Der Platz hat RH 0, gleich welche Lage es ist.

**Ein Umhang.** Der Held trägt einen Umhang auf Lage 5. Seine RH kann 0 sein, denn auf Lage 5 gilt die Untergrenze nicht.

**Rüstung und Schild.** Der Held trägt eine Torso-Rüstung mit RH 2 und einen Schild mit Waffenklasse 3. Seine RH ist zusammen 2 + 3 = 5. Der RS des Schildes schützt zusätzlich den linken Arm, an Hand und Ellenbogen ohne die sonst übliche Halbierung.

**Ein Fausthieb im Stahlpanzer.** Der Held trägt am Arm einen Stahlpanzer der Lage 4, Meisterarbeit, angepasst. Schlägt er mit dieser Faust zu, gilt Gepanzert mit dem Material Stahl, der Fertigung Meisterarbeit und der Anpassung angepasst.

**Ein schwerer Lederpanzer.** Der Held trägt am Arm einen schweren Lederpanzer der Lage 4. Sein Fausthieb macht den normalen Schaden von Unbewaffnet.

**Schlagring unter dem Eisenpanzer.** Der Held hat einen Schlagring gewählt und trägt am selben Arm einen Eisenpanzer der Lage 4. Für seinen Fausthieb gilt Gepanzert mit dem Material Eisen, nicht der Schlagring, auch wenn dieser die besseren Werte hätte.
