I.	Scopul proiectului si specificul aplicatiei:
    Plantele din apartament sau din casa nu au nevoie de aceeasi cantitate de apa. Nu ii putem pune unui cactus aceeasi cantitate de apa ca plantei Medinilla magnifica, spre exemplu, care are nevoie de extrem de multa apa. Pentru acest lucru ne-am gandit sa facem o aplicatie care citeste semnalele trimise de catre un sensor de umiditate a solului si le prelucreaza in asa fel incat sa ne dam seama daca planta noastra are sau nu nevoie de apa.
    Dupa ce introducem senzorul in sol, aplicatia preia datele de la acesta si le imparte in 4 categorii avertizandu-ne de pozitia senzorului: senzorul se afla in aer, sol uscat, sol umed sau apa. Avem 2 leduri (si un led de pe modul) care reactioneaza diferit la fiecare categorie. Daca avem sol umed ledul verde este aprins, cand acesta devine uscat se stinge ledul verde si se aprinde cel rosu avertizandu-ne ca trebuie sa udam solul. Cand udam planta punem suficienta apa, pana cand se reaprinde becul verde. Cand senzorul este in aer doar ledul de pe modul este aprins informandu-ne ca senzorul este pregatit pentru a fi folosit.

II.	Lista componentelor hardware:
    Pentru proiect noi am folosit urmatoarele componente:
	-	Intel Galileo Gen 2
	-	Breadboard
	-	Senzor de umiditate cu modul
	-	1 led verde de 3 mm cu Lentile Difuze
	-	1 led rosu de 3 mm cu Lentile Difuze
	-	2 rezistori 0.25W 2.2K?
	-	Fire colorate Tata-Tata
	-	4 Fire colorate Mama-Mama (pentru modul (si pentru a putea folosi senzorul la o distanta sigura de placuta :) ))

III.	Prezentarea pachetelor/modulelor folosite:
    Pentru a realiza aplicatia am folosit limbajul de programare Python. Pachetele folosite sunt mraa si time.
