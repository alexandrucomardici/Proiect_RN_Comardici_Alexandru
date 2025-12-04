# Proiect: Clasificare animale (Pisici / Câini) + Atribute multiple

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Comardici Alexandru  
**Data:** [Data]  
**Link Repository GitHub:** [repo-url]

## 1. Tabel Nevoie Reală → Soluție SIA → Modul Software

| **Nevoie reală concretă** | **Cum o rezolvă SIA-ul**         | **Modul software responsabil** |
|---------------------------|----------------------------------|--------------------------------|
| Identificarea rapidă a animalelor rătăcite | Clasificare imagine în < 1.5 secunde pentru câine/pisică | RN Inference Module + Web UI |
| Estimarea probabilității ca animalul să aibă proprietar | Modelul generează probabilitate 0–100% → alertă la prag 40% | RN Inference + Business Logic Layer |
| Estimarea mărimii unui câine pentru triaj rapid | Clasificare small / medium / big cu latență < 1.5 secunde | Size Classifier + UI Feedback Module |
| Istoric vizual al detecțiilor recente | Salvarea ultimelor 3 imagini într-un mini-dashboard | History Manager + Web UI |

---

## 2. Contribuția originală la setul de date

**Total observații finale:** 100% originale (toate imaginile au fost colectate manual)  
**Observații originale:** 100%  

**Tipul contribuției:**  
[x] Date achiziționate manual / etichetate manual  
[ ] Date generate prin simulare fizică  
[ ] Etichetare/adnotare manuală  
[ ] Date sintetice prin metode avansate  

**Descriere detaliată:**  
Am colectat manual imagini cu pisici și câini, etichetând fiecare fișier cu: specie (cat/dog), proprietar (yes/no) și mărimea animalului (small/medium/big). Setul de date a fost preprocesat prin redimensionare la 640×640 px pentru uniformitate, apoi folosit în pipeline-ul nostru de clasificare multi-task.  

**Locația codului:** `src/preprocessing/resize.py`  
**Locația datelor:** `data/raw/`, `data/processed/`

**Dovezi:**    
- Descriere dataset: `docs/datasets/datasets_description.md`

---

## 3. Diagrama State Machine

**Legendă / Justificare:**

Arhitectura aleasă este un **State Machine pentru clasificare vizuală la cerere**, deoarece aplicația permite utilizatorului să încarce o imagine, aceasta este preprocesată și inferența este afișată în UI.  

**Stările principale:**
1. **INIT:** Încarcă modelul Keras și validează resursele.  
2. **WAIT_UPLOAD:** Standby până la încărcarea unei imagini de la utilizator.  
3. **PREPROCESS:** Imaginea este convertită în RGB, scalată și normalizată.  
4. **PREDICT:** Modelul rulează inferența pentru specie, proprietar și mărime.  
5. **DISPLAY_RESULT:** UI-ul prezintă predicția și actualizează istoricul ultimele 3 detecții.  
6. **ERROR:** Gestionarea fișierelor invalide sau probleme la inferență.  
7. **STOP:** Oprirea serverului și eliberarea resurselor.

**Tranziții critice:**
- `WAIT_UPLOAD → PREPROCESS`: când utilizatorul selectează o imagine validă  
- `PREPROCESS → PREDICT`: după procesarea corectă a fișierului  
- `PREDICT → ERROR`: dacă modelul returnează valori invalide  
- `DISPLAY_RESULT → WAIT_UPLOAD`: când utilizatorul dorește o nouă analiză  

**Starea ERROR** este esențială pentru gestionarea imaginilor corupte sau incompatibile și asigură revenirea controlată la starea de așteptare.

**Diagrama este salvată în:** `docs/state_machine.png`

---
#### Detalii per modul:

#### **Modul 1: Data Logging / Acquisition**

**Funcționalități obligatorii:**
- [ ] Cod rulează fără erori: `python src/data_acquisition/generate.py` sau echivalent LabVIEW
- [X] Generează CSV în format compatibil cu preprocesarea din Etapa 3
- [X] Include minimum 40% date originale în dataset-ul final
- [ ] Documentație în cod: ce date generează, cu ce parametri

#### **Modul 2: Neural Network Module**

**Funcționalități obligatorii:**
- [X] Arhitectură RN definită și compilată fără erori
- [X] Model poate fi salvat și reîncărcat
- [X] Include justificare pentru arhitectura aleasă (în docstring sau README)
- [X] **NU trebuie antrenat** cu performanță bună (weights pot fi random)


#### **Modul 3: Web Service / UI**

**Funcționalități MINIME obligatorii:**
- [X] Propunere Interfață ce primește input de la user (formular, file upload, sau API endpoint)
- [X] Includeți un screenshot demonstrativ în `docs/screenshots/`


## 4. Structura Repository
Sistem inteligent de clasificare a animalelor/
├── README.md
├── docs/
│ ├── datasets/
│ │ └── datasets_description.md
│ ├── state_machine.png
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
│ ├── animal_detector.keras
│ ├── app.ipynb
│ ├── readMe.txt
│ └── ui.py
├── config/
│   ├──config.yaml
│   └──readme.txt
└── requirements.txt

---

## 5. Cum rulezi proiectul ##

1. Clonează repository:
git clone <repo-url>
pip install -r requirements.txt
python src/preprocessing/resize.py
python src/app.ipynb
python src/ui.py

## 6. Detalii tehnice

- Model: MobileNetV2 backbone, multi-task output (species, has_owner, size)
- Dimensiune input: 224×224×3
- Preprocesare: scalare la [0,1]
- Inferență UI: Flask + Bootstrap 5, preview imagine și istoric ultimele 3 detecții
- Threshold proprietar: 0.4 (Owner ✅ / Owner ❌)

**Diferențe față de Etapa 3:**
- Adăugat `data/generated/` pentru contribuția dvs originală
- Adăugat `src/data_acquisition/` - MODUL 1
- Adăugat `src/neural_network/` - MODUL 2
- Adăugat `src/app/` - MODUL 3
- Adăugat `models/` pentru model neantrenat
- Adăugat `docs/state_machine.png` - OBLIGATORIU
- Adăugat `docs/screenshots/` pentru demonstrație UI

---

### Documentație și Structură
- [x] Tabelul Nevoie → Soluție → Modul complet (minimum 2 rânduri cu exemple concrete completate in README_Etapa4_Arhitectura_SIA.md)
- [x] Declarație contribuție 40% date originale completată în README_Etapa4_Arhitectura_SIA.md
- [x] Cod generare/achiziție date funcțional și documentat
- [x] Dovezi contribuție originală: grafice + log + statistici în `docs/`
- [x] Diagrama State Machine creată și salvată în `docs/state_machine.jpg`
- [x] Legendă State Machine scrisă în README_Etapa4_Arhitectura_SIA.md (minimum 1-2 paragrafe cu justificare)
- [x] Repository structurat conform modelului de mai sus (verificat consistență cu Etapa 3)

### Modul 1: Data Logging / Acquisition
- [ ] Cod rulează fără erori (`python src/data_acquisition/...` sau echivalent LabVIEW)
- [x] Produce minimum 40% date originale din dataset-ul final
- [x] CSV generat în format compatibil cu preprocesarea din Etapa 3
- [ ] Documentație în `src/data_acquisition/README.md` cu:
  - [x] Metodă de generare/achiziție explicată
  - [ ] Parametri folosiți (frecvență, durată, zgomot, etc.)
  - [x] Justificare relevanță date pentru problema voastră
- [x] Fișiere în `data/generated/` conform structurii

### Modul 2: Neural Network
- [x] Arhitectură RN definită și documentată în cod (docstring detaliat) - versiunea inițială 
- [x] README în `src/` cu detalii arhitectură curentă

### Modul 3: Web Service / UI
- [x] Propunere Interfață ce pornește fără erori (comanda de lansare testată)
- [x] Screenshot demonstrativ în `docs/screenshots/ui_demo.png`
- [x] README în `src/app/` cu instrucțiuni lansare (comenzi exacte)