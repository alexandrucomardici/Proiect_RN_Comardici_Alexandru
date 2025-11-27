\# Proiect: Clasificare animale (Pisici / Câini) + Atribute multiple



Acest proiect implementează o rețea neuronală convoluțională multi-task capabilă să prezică:

\- specia (cat / dog)

\- dacă animalul are stăpân (yes / no)

\- mărimea animalului (small / medium / big)



Modelul folosește MobileNetV2 ca backbone și este antrenat pe un set de imagini etichetate.



---------------------------------------------------------------------



\## Structura proiectului



project/

├── README.md

├── docs/

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

└── requirements.txt



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



