# Data Science-Induviduel projekt: Faktorer som påverkar studenters prestationer (SPF)

## Projektbeskrivning

Detta projekt [SPF](main_spf.ipynb) syftar till att undersöka vilka faktorer som har störst påverkan på studenters akademiska resultat. Genom att analysera dataset **StudentPerformanceFactors.csv**, som omfattar data från 6 378 studenter, har projektet identifierat mönster kring studietid, närvaro, föräldrainvolvering och tillgång till resurser.

Analysen har genomförts med hjälp av Python-bibliotek som **Pandas**, **Seaborn** och **Matplotlib** för att visualisera samband och statistiska fördelningar.
Centrala resultat från analysen:

   -  Genomsnittligt provresultat: Studenterna har ett genomsnittligt resultat på ca 67,25 poäng.

   -  Resultatfördelning: Majoriteten av studenterna presterar inom intervallet 65 till 75 poäng.

   -  Närvaro och studietid: Projektet visar att studietid är mest effektiv när den kombineras med hög närvaro. En student med "lagom" studietid (ca 20 timmar) men hög närvaro presterar ofta bättre än en student med mer studietid men lägre disciplin.

   -  Samverkande faktorer: Kombinationen av hög föräldrainvolvering och god tillgång till resurser ger de högsta genomsnittliga resultaten (69,1 poäng), medan låga värden på båda leder till de lägsta resultaten (65,3 poäng).


Analysen är strukturerad för att besvara följande frågor rörande studenters framgång:

   1. Hur ser fördelningen av provresultat ut bland studenterna?

        Svar: Genom histogram och KDE-kurvor visas att de flesta studenter ligger nära medelområdet.

   2. Vilka är drivande faktorer bakom studenternas prestationer?
        
        Svar: Studietid(0.45) och närvaronde(0.58) identifierats som mest drivande faktorer. 

   3. Vilken roll spelar studietid kontra närvaro för slutresultatet?

        Svar: Studietid är en viktig faktor, men disciplin i form av hög närvaro fungerar som en förstärkande faktor för bättre resultat.

   4. Hur påverkar socioekonomiska faktorer (resurser och föräldrastöd) resultaten?

        Svar: Rapporten visar tydligt hur materiellt stöd och föräldrainvolvering samverkar för att skapa en mer gynnsam lärmiljö.
        

    