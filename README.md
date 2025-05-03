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
   ![image](https://github.com/user-attachments/assets/c446e3e6-9803-42f6-9d06-1428a777e308)
   Filtruoja patiekalus, atitinkančius turimus ingredientus.
