\# Proiect: Clasificare animale (Pisici / Câini) + Atribute multiple



<<<<<<< HEAD
\*\*Disciplina:\*\* Rețele Neuronale  

\*\*Instituție:\*\* POLITEHNICA București – FIIR  

\*\*Student:\*\* Comardici Alexandru  

\*\*Data:\*\* \[Data]  

\*\*Link Repository GitHub:\*\* \[repo-url]



\## 1. Tabel Nevoie Reală → Soluție SIA → Modul Software



| \*\*Nevoie reală concretă\*\* | \*\*Cum o rezolvă SIA-ul\*\*         | \*\*Modul software responsabil\*\* |

|---------------------------|----------------------------------|--------------------------------|

| Identificarea rapidă a animalelor rătăcite | Clasificare imagine în < 1.5 secunde pentru câine/pisică | RN Inference Module + Web UI |

| Estimarea probabilității ca animalul să aibă proprietar | Modelul generează probabilitate 0–100% → alertă la prag 40% | RN Inference + Business Logic Layer |

| Estimarea mărimii unui câine pentru triaj rapid | Clasificare small / medium / big cu latență < 1.5 secunde | Size Classifier + UI Feedback Module |

| Istoric vizual al detecțiilor recente | Salvarea ultimelor 3 imagini într-un mini-dashboard | History Manager + Web UI |



---



\## 2. Contribuția originală la setul de date



\*\*Total observații finale:\*\* 100% originale (toate imaginile au fost colectate manual)  

\*\*Observații originale:\*\* 100%  



\*\*Tipul contribuției:\*\*  

\[x] Date achiziționate manual / etichetate manual  

\[ ] Date generate prin simulare fizică  

\[ ] Etichetare/adnotare manuală  

\[ ] Date sintetice prin metode avansate  



\*\*Descriere detaliată:\*\*  

Am colectat manual imagini cu pisici și câini, etichetând fiecare fișier cu: specie (cat/dog), proprietar (yes/no) și mărimea animalului (small/medium/big). Setul de date a fost preprocesat prin redimensionare la 640×640 px pentru uniformitate, apoi folosit în pipeline-ul nostru de clasificare multi-task.  



\*\*Locația codului:\*\* `src/preprocessing/resize.py`  

\*\*Locația datelor:\*\* `data/raw/`, `data/processed/`



\*\*Dovezi:\*\*    

\- Descriere dataset: `docs/datasets/datasets\_description.md`



---



\## 3. Diagrama State Machine



\*\*Legendă / Justificare:\*\*



Arhitectura aleasă este un \*\*State Machine pentru clasificare vizuală la cerere\*\*, deoarece aplicația permite utilizatorului să încarce o imagine, aceasta este preprocesată și inferența este afișată în UI.  



\*\*Stările principale:\*\*

1\. \*\*INIT:\*\* Încarcă modelul Keras și validează resursele.  

2\. \*\*WAIT\_UPLOAD:\*\* Standby până la încărcarea unei imagini de la utilizator.  

3\. \*\*PREPROCESS:\*\* Imaginea este convertită în RGB, scalată și normalizată.  

4\. \*\*PREDICT:\*\* Modelul rulează inferența pentru specie, proprietar și mărime.  

5\. \*\*DISPLAY\_RESULT:\*\* UI-ul prezintă predicția și actualizează istoricul ultimele 3 detecții.  

6\. \*\*ERROR:\*\* Gestionarea fișierelor invalide sau probleme la inferență.  

7\. \*\*STOP:\*\* Oprirea serverului și eliberarea resurselor.



\*\*Tranziții critice:\*\*

\- `WAIT\_UPLOAD → PREPROCESS`: când utilizatorul selectează o imagine validă  

\- `PREPROCESS → PREDICT`: după procesarea corectă a fișierului  

\- `PREDICT → ERROR`: dacă modelul returnează valori invalide  

\- `DISPLAY\_RESULT → WAIT\_UPLOAD`: când utilizatorul dorește o nouă analiză  



\*\*Starea ERROR\*\* este esențială pentru gestionarea imaginilor corupte sau incompatibile și asigură revenirea controlată la starea de așteptare.



\*\*Diagrama este salvată în:\*\* `docs/state\_machine.png`



---

\#### Detalii per modul:



\#### \*\*Modul 1: Data Logging / Acquisition\*\*



\*\*Funcționalități obligatorii:\*\*

\- \[ ] Cod rulează fără erori: `python src/data\_acquisition/generate.py` sau echivalent LabVIEW

\- \[X] Generează CSV în format compatibil cu preprocesarea din Etapa 3

\- \[X] Include minimum 40% date originale în dataset-ul final

\- \[ ] Documentație în cod: ce date generează, cu ce parametri



\#### \*\*Modul 2: Neural Network Module\*\*



\*\*Funcționalități obligatorii:\*\*

\- \[X] Arhitectură RN definită și compilată fără erori

\- \[X] Model poate fi salvat și reîncărcat

\- \[X] Include justificare pentru arhitectura aleasă (în docstring sau README)

\- \[X] \*\*NU trebuie antrenat\*\* cu performanță bună (weights pot fi random)





\#### \*\*Modul 3: Web Service / UI\*\*



\*\*Funcționalități MINIME obligatorii:\*\*

\- \[X] Propunere Interfață ce primește input de la user (formular, file upload, sau API endpoint)

\- \[X] Includeți un screenshot demonstrativ în `docs/screenshots/`





\## 4. Structura Repository

Sistem inteligent de clasificare a animalelor/
=======
Acest proiect implementează o rețea neuronală convoluțională multi-task capabilă să prezică:

\- specia (cat / dog)

\- dacă animalul are stăpân (yes / no)

\- mărimea animalului (small / medium / big)



Modelul folosește MobileNetV2 ca backbone și este antrenat pe un set de imagini etichetate.



---------------------------------------------------------------------



\## Structura proiectului



project/
>>>>>>> b09f42134bed8fc523d3793b4fa475efb6101989

├── README.md

├── docs/

<<<<<<< HEAD
│ ├── datasets/

│ │ └── datasets\_description.md

│ ├── state\_machine.png

│ └── screenshots/

├── data/

│ ├── raw/

│ ├── processed/

│ ├── train/

│ ├── validation/

│ └── test/

├── src/

│ ├── preprocessing/

│ │ └── resize.py

│ ├── animal\_detector.keras

│ ├── app.ipynb

│ ├── readMe.txt

│ └── ui.py

├── config/

│   ├──config.yaml

│   └──readme.txt

=======
│   └── datasets/

│       └── datasets\_description.md

├── data/

│   ├── raw/

│   ├── processed/

│   ├── train/

│   ├── validation/

│   └── test/

├── src/

│   ├── preprocessing/

│   ├── data\_acquisition/

│   └── neural\_network/

├── config/

>>>>>>> b09f42134bed8fc523d3793b4fa475efb6101989
└── requirements.txt



<<<<<<< HEAD
---



\## 5. Cum rulezi proiectul ##



1\. Clonează repository:

git clone <repo-url>

pip install -r requirements.txt

python src/preprocessing/resize.py

python src/app.ipynb

python src/ui.py



\## 6. Detalii tehnice



\- Model: MobileNetV2 backbone, multi-task output (species, has\_owner, size)

\- Dimensiune input: 224×224×3

\- Preprocesare: scalare la \[0,1]

\- Inferență UI: Flask + Bootstrap 5, preview imagine și istoric ultimele 3 detecții

\- Threshold proprietar: 0.4 (Owner ✅ / Owner ❌)



\*\*Diferențe față de Etapa 3:\*\*

\- Adăugat `data/generated/` pentru contribuția dvs originală

\- Adăugat `src/data\_acquisition/` - MODUL 1

\- Adăugat `src/neural\_network/` - MODUL 2

\- Adăugat `src/app/` - MODUL 3

\- Adăugat `models/` pentru model neantrenat

\- Adăugat `docs/state\_machine.png` - OBLIGATORIU

\- Adăugat `docs/screenshots/` pentru demonstrație UI



---



\### Documentație și Structură

\- \[x] Tabelul Nevoie → Soluție → Modul complet (minimum 2 rânduri cu exemple concrete completate in README\_Etapa4\_Arhitectura\_SIA.md)

\- \[x] Declarație contribuție 40% date originale completată în README\_Etapa4\_Arhitectura\_SIA.md

\- \[x] Cod generare/achiziție date funcțional și documentat

\- \[x] Dovezi contribuție originală: grafice + log + statistici în `docs/`

\- \[x] Diagrama State Machine creată și salvată în `docs/state\_machine.jpg`

\- \[x] Legendă State Machine scrisă în README\_Etapa4\_Arhitectura\_SIA.md (minimum 1-2 paragrafe cu justificare)

\- \[x] Repository structurat conform modelului de mai sus (verificat consistență cu Etapa 3)



\### Modul 1: Data Logging / Acquisition

\- \[ ] Cod rulează fără erori (`python src/data\_acquisition/...` sau echivalent LabVIEW)

\- \[x] Produce minimum 40% date originale din dataset-ul final

\- \[x] CSV generat în format compatibil cu preprocesarea din Etapa 3

\- \[ ] Documentație în `src/data\_acquisition/README.md` cu:

&nbsp; - \[x] Metodă de generare/achiziție explicată

&nbsp; - \[ ] Parametri folosiți (frecvență, durată, zgomot, etc.)

&nbsp; - \[x] Justificare relevanță date pentru problema voastră

\- \[x] Fișiere în `data/generated/` conform structurii



\### Modul 2: Neural Network

\- \[x] Arhitectură RN definită și documentată în cod (docstring detaliat) - versiunea inițială 

\- \[x] README în `src/` cu detalii arhitectură curentă



\### Modul 3: Web Service / UI

\- \[x] Propunere Interfață ce pornește fără erori (comanda de lansare testată)

\- \[x] Screenshot demonstrativ în `docs/screenshots/ui\_demo.png`

\- \[x] README în `src/app/` cu instrucțiuni lansare (comenzi exacte)
=======
---------------------------------------------------------------------



\## Cum rulezi proiectul



1\. Clonează repository-ul:

&nbsp;  git clone <repo-url>



2\. Instalează dependențele:

&nbsp;  pip install -r requirements.txt



3\. Rulează preprocesarea imaginilor (ex: redimensionare, split):

&nbsp;  python src/preprocessing/resize.py

&nbsp;  python src/preprocessing/split.py



4\. Rulează antrenarea:

&nbsp;  python src/app.ipynb



5\. Rulează evaluarea:

&nbsp;  python src/ui.py 



---------------------------------------------------------------------



\## Date de intrare



Dataset-ul trebuie să conțină:

\- imagini în foldere (cat/... , dog/...)

\- un fișier annotations.csv cu:

&nbsp; - filename

&nbsp; - species

&nbsp; - has\_owner

&nbsp; - size



---------------------------------------------------------------------



\## Rezultate



La finalul antrenării se generează:

\- acuratețe pentru clasificarea speciei

\- acuratețe pentru proprietar (0/1)

\- acuratețe pentru mărime (small/medium/big)

\- graficul evoluției loss-ului și acurateții

\- modelul final salvat în .h5



---------------------------------------------------------------------



\## Autor



Comardici Alexandru


