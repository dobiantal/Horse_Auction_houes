# Az alkalmazottak entitás

### Hozzáadott osztályok
Az alkalmazottak entitással felüldefiniáltam az alapértelmezett Users
egyedet. Elkészítettem hozzá a serializer.py-t. A convertálás során az 
egyed összes mezőjét nem használom csak a 
['id',
'Fname',
'Lname',
'account_name',
'email',
'password',
'Policy',
'created_at',
'updated_at',
'deleted_at']
mezőket. Készítettm hozzá egy create() metódus mely a kapott jelszavak
Hash titkosítást végzi.
***
###  Alkalmazottak urls.py fájljában 3db útvonalat defináltam. 
* Registrate => regisztráció
* Login => bejelentkezés
* Logout => kijelentkezés
***
### Alkalmazottak views.py fájlában vannak definiálva a válaszlogikák.
* Registrate:
  Post request-et fogad. Serializálja az adatokat majd ellenőrzi a helyességüket.
  Amennyiben nem convertálható kivételt dob. Amennyiben minden rendben van akkor elmenti
  és visszatér sikeres regisztráció üzenettel.
* LogIn:
  Post request-et fogad. A requestből kiveszi a felhasználónév és jelszó mezőket.
  Adatbázis lekérdezést indít hogy létezik e a felhasználó és amennyiben igen a jelszót is validálja.
  Ellenkező esetben kivételt dob. Hitelesítés után a JWT token generátor segítségével
  tokent készít. A token rétegei a felhasználó azonosító a kezdet dátum idő és a kezdet +1 óra a lejárati idő.
  Cookie-ba rakja a tokent és visszatér vele a kliens felé.
* IsLogIn:
  A bejelentkezett kliens hitelességét ellenőrzi. Kikéri a request.COOKIE-ból a tokent dekódolja és megnézi hogy a
  kapott azonosító létezik-e az adatbázisban. Serializálja az adatokat.
* LogOut:
  Pélldányosít egy Response osztályt, majd kitörli a cookie tartalmát.
  Végül beleír a data metőbe egy kilépési üzenetet visszatér vele.
