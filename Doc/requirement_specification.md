# Requirement Specification for Horse Auction Houes
## 1. Leader report about the project
The best of racehorse versenylovakkal foglalkozó cég megkeresett engem,
hogy lovardája számára fejlesszünk egy webapplikációt mely a vilgon bárhonnan
elérhető aukciós platformot biztosít a versenylovakkal történő kereskedelemben.

## 2. Jelenlegi helyzet leírása
* Az istálló tulajdonosa a munkatársaival együtt a kapcsolatrendszerén alapulóan
az ügyfelek számára privát megkeresésések alapján ajánlanak ki lovakat. Szeretnék nemcsak
a meglévő ügyfelek számára értékesíteni a lovakat hanem kiszélessíteni a piacot és 
a világ minden részére értékesíteni állataikat.
* Jelenleg az állatok adatait digitálisan táblázatkezelőben tárolják. Az adatok módosítása
nehézkes, mivel egyszerre csak egy ember képes módosítani, illetve az adatok aktuális állapota
mindig csak egy számítógépen érhető el.
.....

## 3. Vágyálomrendszer leírása
A tulajdonosok szeretnének egy többfelhasználós, több jogosultsági rendszerrel rendelkező
teljes igényt kielégítő applikációt, melyben a kereskedelemmel foglalkozó kollégák, a tulajdonosok, 
és a licitálók képesek belépni és különböző lehetőségekhez hozzáférni. A tulajdonosi jogkörben legyen
rálátás és jogosultság mindenre amire a program képes. A kereskedelemmel foglalkozó kollégák képesek
legyenek új licit tételeket feltölteni, a licitet elindítani és leállítani. A lovak eladási státuszát 
módosítani. Képesek legyenek lekérni a licitálók releváns adatait a kapcsolatfelvétel miatt. A licitálók
jogköre terjedjen ki a regisztrációra, a regisztrációt követően képesek legyenek az éppen futó aukciós tételekre
licitálni. Képesk legyenek saját adataikat módosítani és saját döntésre képesk legyenek törölni fiókjukat a
rendszerből. Az program legyen platformfüggetlen és bárhonnan leérhető, hogy a piac a világ bármely pontjára
kiterjeszthető legyen. Az weboldal elérésekor automatikusan listázza ki a licit alatt álló tételeket és azokat is 
melyek még a jövőben fognak kalapács alá kerülni. Egy tétel leütése után a rendszer küldjön automatikusan egy
e-mailt az ügyfélenek a sikeres vásárlásról és csatolja hozzá mellékletben a tanusítványt mely bizonyítja a
vásárlás tényét.

## 4. Jelenlegi üzleti modell
#### Üzleti munkatársak:
* Kereskedelni asszisztens
* Üzletkötő
* Kapcsolattartó
#### Üzleti entitások:
* Licitáló
* Tenyésztő
* Versenyló
#### Jelenlegi üzleti folyamatok:

## 5. Igényelt üzleti folyamat modellje
#### Üzleti folyamatok
* Bejelentkezés nélkül:
  * Listázni tudjuk azokat az aukciós tételeket amik éppen licit alatt vannak, vagy licitre lesznek bocsátva.
* Tulajdonosok:
  * Az oldal megnyitása és az autentikációt követően hozzáférnek minden funkciót elérnek amire a program lehetőséget ad.
* Keseskedelmi asszisztens:
  * Belejentkezést követően az új aukciós tétel hozzáadása gomb megnyomásával be tudja vinni az adatokat majd véglegesíti a tranzakciót.
  * Belejentkezést követően adatok felülírása gomb megnyomásával képes felülírni a tételek adatait módosítani az eladási státuszukat.
  * Belejentkezést követően tétel törlése gombra kattintva logikai törléssel deaktiválja a tételt.
  * Belejentkezést követően képes generálni eladási tanusítványt
  * Belejentkezést követően képes lekérni adatokat bármely regisztrált licitálóról a kapcsolatfelvétel végett.
* Licitáló:
  * Belejentkezést követően tudja listázni az éppen folyó liciteket és tud licitálni is ezekre. 
  * Belejentkezést követően saját adatait tudja módosítani, törölni is tudja fiókját.
## 6. Követelménylista

| ID | Verzió | Név | Kifejtés |
| -- | ------ | --- | -------- |
| K01 | V1.0 | Felület | platformtól független módon elérhető legyen az alkalmazás a világ bármely részéről. |
| K02 | V1.0 | Jogosultságok | A rendszer kezelje le az üzleti folyamatokban felsorolt üzleti szereplőket megfelelő funkciókkal. |
| K03 | V1.0 | Új tétel | A kereskedelmi asszisztens és a vezető jogosultsággal legyen lehetőség új tétel hozzáadására. |
| K04 | V1.0 | Tétel felülírása | A kereskedelmi asszisztens és a vezető jogosultsággal rendelkező felhasználók tudják felülírni a tétele rögzített adatait. |
| K05 | V1.0 | Tétel törlése | A kereskedelmi asszisztens és a vezető jogosultsággal rendelkező felhasználók tudjanak tételt törölni a rendszerből. |
| K06 | V1.0 | Eladási tanusítvány | A kereskedelmi asszisztens és a vezető jogosultsággal rendelkező felhasználók tudjanak eladási tanusítványt generálni. |
| K07 | V1.0 | Ügyféladat kezelés | A kereskedelmi asszisztens és a vezető jogosultsággal rendelkező felhasználók férjenek hozzá bizonyos ügyféladatokhoz a kapcsolattartás szükségessége miatt. |
| K08 | V1.0 | Regisztrációs | Az weboldal biztosítson regisztrációs platformot a licitálók számára.
| K09 | V1.0 | Ügyféladat módosítás | A weboldal adjon lehetőséget a licitálók saját adatainak módosítására, illetve a fiók törlésére.
