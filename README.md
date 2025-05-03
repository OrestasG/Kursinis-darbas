# Kursinis-darbas

## Įvadas

a. Apie mano programą

Mitybos sekimo program - tai python kalba parasyta progrmam, skirta padėti vartotojams nusistatyti ir pasiekti mitybos tikslus. Ši programa leidžia apskaičiuoti saugų dienos kalorijų kiekį pagal dabartinį svorį, norima pasiekti svorį ir terminą. Vartotojai gali pridėti savo ingredientų ir patiekalų, sekti suvartotas kalorijas bei gauti pasiūlymus pagal turimus ingredientus.

b. Kaip paleisti programą?

1. Įsitikinti kad yra instaliuotas Python 3.
2. Atsisiųsti visus .py failus is GitHub
3. Paleisti pagrindinę programą: app.py

c. Kaip naudotis programa?

- Įveskite informaciją: lytį, amžių, ūgį, esamą svorį, tikslinį svorį ir laikotarpį.
- Pridėkite ingredientų su kalorijų verte.
- Kurkite patiekalus iš pasirinktų ingredientų.
- Registruokite suvalgytus patiekalus ir stebėkite likusias dienos kalorijas.
- Gaukite pasiūlymus pagal namuose turimus ingredientus.

## Analizė

a. Funkciniai reikalavimai

1. Dienos kalorijų skaičiavimas:
   ![image](https://github.com/user-attachments/assets/1b4c11e8-8d2e-4ca3-be56-04c599a98d39)
   Skaičiavimas tikrina, ar apskaičiuotas kalorijų kiekis yra saugus (500–4000 kcal).
2. Ingredientų pridėjimas:
   ![image](https://github.com/user-attachments/assets/18cd2e10-fc02-4244-9e56-ca01ed4020b0)
   Vartotojas gali pridėti bet kokius norimus ingredientus.
3. Patiekalų kūrimas iš sukurtų ingredientų:
   ![image](https://github.com/user-attachments/assets/f717a350-104f-4192-9713-0ceb7b83156c)
   Patiekalai sudaromi iš kelių ingredientų.
4. Suvalgytų patiekalų registravimas:
   ![image](https://github.com/user-attachments/assets/f23f928f-83cc-4798-a847-33b4b4632836)
   Registruojami patiekalai ir atimamos kalorijos iš dienos limito.
5. Patiekalų pasiūlymai pagal turimus ingredientus:
   ![image](https://github.com/user-attachments/assets/a84e2eef-a210-47e9-a5bd-66ec1ed05ea8)
   Filtruoja patiekalus, atitinkančius turimus ingredientus.

b. OOP principai

1. Abstraction:
   Vartotojas naudoja metodus kaip add_iteml() be vidinio mechanizmo žinojimo.
   ![image](https://github.com/user-attachments/assets/bdd6653d-1885-4648-97ab-fb0f7eea0ba7)
2. Encapsulation:
   Kiekviena klasė saugo vidinius duomenis per metodus
   ![image](https://github.com/user-attachments/assets/241084de-0240-4de8-bb5a-42bc8307924f)
3. Inheritance:
   Visos manager klasės paveldi base_manager klasę.
   ![image](https://github.com/user-attachments/assets/2e59a6a4-4714-46b1-9570-53526e6073a2)
   ![image](https://github.com/user-attachments/assets/ac3bb626-a23c-41f4-86f0-33dfe990dae4)
4. Polymorphism:
   Patiekalų siūlymas ir registravimas veikia nepriklausomai nuo ingredientų.
   ![image](https://github.com/user-attachments/assets/5390a77a-91c1-4836-ad92-9e44b17a465e)


   
