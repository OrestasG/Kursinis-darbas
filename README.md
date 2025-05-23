# Kursinis-darbas

## Įvadas

### a. Apie mano programą

Mitybos sekimo program - tai python kalba parasyta progrmam, skirta padėti vartotojams nusistatyti ir pasiekti mitybos tikslus. Ši programa leidžia apskaičiuoti saugų dienos kalorijų kiekį pagal dabartinį svorį, norima pasiekti svorį ir terminą. Vartotojai gali pridėti savo ingredientų ir patiekalų, sekti suvartotas kalorijas bei gauti pasiūlymus pagal turimus ingredientus.

### b. Kaip paleisti programą?

1. Įsitikinti kad yra instaliuotas Python 3.
2. Atsisiųsti visus .py failus is GitHub
3. Paleisti pagrindinę programą: app.py

### c. Kaip naudotis programa?

- Įveskite informaciją: lytį, amžių, ūgį, esamą svorį, tikslinį svorį ir laikotarpį.
- Pridėkite ingredientų su kalorijų verte.
- Kurkite patiekalus iš pasirinktų ingredientų.
- Registruokite suvalgytus patiekalus ir stebėkite likusias dienos kalorijas.
- Gaukite pasiūlymus pagal namuose turimus ingredientus.

## Analizė

### a. Funkciniai reikalavimai

1. Dienos kalorijų skaičiavimas:
   Skaičiavimas tikrina, ar apskaičiuotas kalorijų kiekis yra saugus (500–4000 kcal)
   
   ![image](https://github.com/user-attachments/assets/1b4c11e8-8d2e-4ca3-be56-04c599a98d39)
   .
4. Ingredientų pridėjimas:
   Vartotojas gali pridėti bet kokius norimus ingredientus.
   
   ![image](https://github.com/user-attachments/assets/18cd2e10-fc02-4244-9e56-ca01ed4020b0)

5. Patiekalų kūrimas iš sukurtų ingredientų:
   Patiekalai sudaromi iš kelių ingredientų.
   
   ![image](https://github.com/user-attachments/assets/f717a350-104f-4192-9713-0ceb7b83156c)
   
6. Suvalgytų patiekalų registravimas:
   Registruojami patiekalai ir atimamos kalorijos iš dienos limito.
   ![image](https://github.com/user-attachments/assets/f23f928f-83cc-4798-a847-33b4b4632836)
   
7. Patiekalų pasiūlymai pagal turimus ingredientus:
   Filtruoja patiekalus, atitinkančius turimus ingredientus.
   
   ![image](https://github.com/user-attachments/assets/a84e2eef-a210-47e9-a5bd-66ec1ed05ea8)

### b. OOP principai

1. Abstraction:
   Abstrakcija leidžia dirbti su objektais jų vidinės veiklos nežinant – naudotojui matoma tik svarbi informacija, o vidinis įgyvendinimas lieka paslėptas.
   Vartotojas naudoja metodus kaip add_iteml() be vidinio mechanizmo žinojimo.

   ![image](https://github.com/user-attachments/assets/bdd6653d-1885-4648-97ab-fb0f7eea0ba7)
   
2. Encapsulation:
   Inkapsuliacija paslepia duomenis klasėje, kad jie būtų apsaugoti nuo neleistino keitimo ir užtikrintu kontroluojamą priėjimas per metodus.
   Kiekviena klasė saugo vidinius duomenis nuo kitų klasių.

   ![image](https://github.com/user-attachments/assets/241084de-0240-4de8-bb5a-42bc8307924f)
   
3. Inheritance:
   Paveldėjimas leidžia kurti naujas klases remiantis jau esamomis, taip išvengiant kodo dubliavimo ir skatinant pakartotinį naudojimą.
   Visos manager(vaikų) klasės paveldi base_manager(tėvų) klasę.

   ![image](https://github.com/user-attachments/assets/2e59a6a4-4714-46b1-9570-53526e6073a2)
   ![image](https://github.com/user-attachments/assets/ac3bb626-a23c-41f4-86f0-33dfe990dae4)
   
4. Polymorphism:
   Polimorfizmas leidžia iškviesti tą patį metodą skirtingiems objektams, o kiekvienas objektas jį įgyvendina savaip.
   Patiekalų siūlymas ir registravimas veikia nepriklausomai nuo ingredientų.

   ![image](https://github.com/user-attachments/assets/5390a77a-91c1-4836-ad92-9e44b17a465e)

### c. Naudotas dizaino modelis

Klasėje BaseManager Template Method dizaino modelis yra naudojamas kartu su abstraction principu. Jis padeda nustatyti bendrą veiksmų eigą bazinėje (abstrakčioje) klasėje, tačiau leidžia konkrečioms paveldėtoms klasėms įgyvendinti detales. 

![image](https://github.com/user-attachments/assets/9a01c917-fcea-418c-9a3d-1575fcb27687)

### d. Kompozicija ir agregacija

Kompozicija:
jei ištrinsim NutritionApp, visi komponentai šioje klasėje irgi išnyks

![image](https://github.com/user-attachments/assets/a3152a54-f486-4447-a9a6-feb2da3913fc)

Agregacija:
jei sunaikinsim MealManager, IngredientManager funkcija niekur nedings ir galima bus naudoti kitoje vietoje.

![image](https://github.com/user-attachments/assets/0a566f7a-9bca-4af0-bc52-0be7fe7ba90f)


## Rezultatai ir apibendrinimas

### a. Rezultatai 

- Pasiekti visi išsikelti tikslai.
- Tinkamai pritaikyti OOP principai ir dizaino modeliai.
- Patikrinami visi klaidingai įvedami duomenys.
- Sėkmingai atlikti visi testai.

### b. Apibendrinimas

Kursinio darbo metu buvo sukurta programą, leidžiančią vartotojams valdyti savo mitybą pagal tikslus ir galimybes. Įgyvendinti visi funkcionalūs reikalavimai ir objektinio programavimo principai. Kodas aiškiai suskirstytas į atskirus failus pagal klases. 

### c. Kaip galima būtų patobulinti programą?

Ateityje galima būtų naudoti tikra duomenų bazė vietoj JSON failų. Pridėti papildomus mitybos aspektus – baltymus, riebalus, angliavandenius. Padaryti programą pasiekiama daugiau žmonių.
Leisti pasirinkti vartotojui sporto lygį ir šia informaciją naudoti skaičiuojant dienos kalorijų limitą 




















