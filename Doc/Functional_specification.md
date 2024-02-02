# Functional specification for Racehorse auction house

## 1. A rendszer célja és nem célja
A  fejlesztés célja, hogy a megrendelő által képviselt kereskedelni ágazat és piac a világ minden részére kiterjeszthető
legyen. A fejlesztés folyamán szemelőtt tartjuk, hogy a jelenlegi rendszerhez nagyon hasonló felépítésű és üzleti folyamatú
rendszert fejlesszünk. Célja hogy a jelenleg dolgozó kollégák könnyel és gyorsan betaníthatóak legyenek. Fontos célja a szoftvernek
az adatok biztonságos és jól visszakövethető tárolása. Az ügyfelek számára egyszrű licitálási lehetőséget biztosítson.
## 2. Használati esetek
##### A rendszert használók:
* Vezetők
* Kereskedelmi asszisztensek
* Licitálók
* Értékesítők
* Kapcsolattartók
* Adminisztrátor
##### A rendszernek a következő funkciókat kell ellátnia:
* Az adminisztrátorok tudjanak új munkatársakat regisztrálni a rendszerbe.
* A Kereskedelni asszisztensek és tulajdonosok tudjanak új licitálási tételt hozzáadni.
* A Kereskedelni asszisztensek és tulajdonosok tudjanak az eladás alatt lévő tételek adatain módosítani.
* A Kereskedelni asszisztensek és tulajdonosok tudjanak tételeket törölni az adatbázisból.
* A Kereskedelni asszisztensek és tulajdonosok tudjanak tudjanak eladási tanusítványt generálni, illetve a rendszer
magától is generáljon egy tétel eladása alkalmával.
* Küldjön e-mailt a vásárlónak amennyiben sikeres volt a vásárlás.
* Regisztrálási lehetőség az oldalon licitálók számára.
* A regisztrált licitálók saját adatainak módosítás és saját fiók törlésének lehetősége.
* Csak a bejelentkezett licitálók tudjanak licitálni egy tételre. 
* Bejelentkezés nékül csak listázni lehessen az aktuálisan futó tételeket és azokat a tételeket melyek később következnek
* Az adatokat jól skálázottan biztonságosan tároltan kell kezelni.
* Minden adatmódosító funkcióhoz kötelező a jelszavas hitelesítés.

![usecase_dia]()

