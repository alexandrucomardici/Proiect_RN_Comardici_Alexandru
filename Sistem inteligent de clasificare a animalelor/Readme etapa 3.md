# 📘 README – Etapa 3: Analiza și Pregătirea Setului de Date pentru Rețele Neuronale

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Comardici Alexandru Gabriel  
**Data:** 11.12.2025  

---

## Introducere

Acest document descrie activitățile realizate în **Etapa 3**, în care se analizează și se preprocesează setul de date necesar proiectului „Sistem inteligent de clasificare a animalelor". Scopul etapei este pregătirea corectă a datelor pentru instruirea modelului RN, respectând bunele practici privind calitatea, consistența și reproductibilitatea datelor.

---

## 1. Structura Repository-ului Github (versiunea Etapei 3)

Proiect_RN_Comardici_Alexandru/
├── README.md
├── docs/
│ └── datasets/ # descriere seturi de date, surse, diagrame
├── data/
│ ├── raw/ # date brute (imagini originale și etichete)
│ ├── generated/ # date generate / augmentate (peste 40%)
│ ├── processed/ # date curățate și transformate (redimensionate)
│ ├── train/ # set de instruire
│ ├── validation/ # set de validare
│ └── test/ # set de testare
├── src/
│ ├── preprocessing/ # funcții pentru preprocesare (resize, scalare)
│ ├── data_acquisition/ # colectare / generare date noi
│ └── neural_network/ # implementarea RN (în etapa următoare)
├── config/ # fișiere de configurare (scaler etc.)
└── requirements.txt # dependențe Python


---

## 2. Descrierea Setului de Date

### 2.1 Sursa datelor

* **Origine:** Imagini descărcate de pe internet și capturate din mediul urban  
* **Modul de achiziție:** Fișier extern + generare programatică (peste 40% din date)  
* **Perioada / condițiile colectării:** Noiembrie 2024 – Ianuarie 2025, imagini cu câini și pisici în medii urbane variate

### 2.2 Caracteristicile dataset-ului

* **Număr total de sample-uri (după combinare):** 1,072  
* **Tip date:** Imagini  
* **Format fișiere:** PNG / JPG  

* **Număr de clase principale:** 2 (specie: cat / dog)  
* **Clase secundare:** 3 (marime caini: small / medium / big)  
* **Etichetare proprietar:** binary (has_owner: 0 / 1)

### 2.3 Distribuția pe clase

| **Clasă** | **Număr exemple** | **Procent aproximativ** |
|-----------|-----------------|------------------------|
| cat       | 69              | 6.4%                   |
| dog       | 82              | 7.7%                   |
| small     | 120             | 11.2%                  |
| medium    | 75              | 7.0%                   |
| big       | 150             | 14.0%                  |

### 2.4 Generarea datelor noi (peste 40%)

* **Metodă:** Descărcare de imagini de pe internet, ajustare dimensiuni și balansare clase  
* **Script:** `src/data_acquisition/generate_data.py`  
* **Tipuri de augmentări:** resize, flip orizontal, ajustări minore de contrast

---

## 3. Analiza Exploratorie a Datelor (EDA)

### 3.1 Statistici descriptive

* **Număr total imagini:** 1,072  
* **Dimensiuni originale:** variabile, toate redimensionate la 224x224 pixeli  
* **Distribuție pe clase principale:** cat / dog: aproape echilibrat, mici discrepanțe  
* **Distribuție pe marimea cainilor:** small/medium/big, clasă dominantă „small”  

### 3.2 Probleme identificate

* Unele imagini cu pisici au fost etichetate incorect ca „dog” (corectate manual)  
* Dimensiuni inițiale variabile → nevoie de resize uniform 224x224  
* Discrepanțe în iluminare și background → vor fi tratate la etapa de augmentare

---

## 4. Preprocesarea Datelor

### 4.1 Curățarea datelor

* Eliminarea imaginilor duplicate  
* Eliminarea imaginilor corupte  
* Verificarea consistenței etichetelor (`species`, `size`, `has_owner`)

### 4.2 Transformarea imaginilor

* **Redimensionare:** 224x224 pixeli  
* **Normalizare:** scalare pixel values 0–1 (division by 255)  
* **Encoding etichete:**  
  * `species` → one-hot encoding 2 clase  
  * `size` → one-hot encoding 3 clase  
  * `has_owner` → binary (0/1)  

### 4.3 Structurarea seturilor de date

* **Train:** 80%  
* **Validation:** 10%  
* **Test:** 10%  
* **Stratificare:** pe `species` pentru menținerea proporțiilor claselor  
* **Random state:** 42 (reproducibilitate)

### 4.4 Salvarea rezultatelor

* Seturi procesate salvate în `data/processed/` și `data/train/validation/test/`  
* Parametri de preprocesare salvați în `config/preprocessing_params.pkl`  

---

## 5. Fișiere generate în această etapă

* `data/raw/` – imagini brute și fișier CSV cu etichete  
* `data/generated/` – date noi generate (peste 40%)  
* `data/processed/` – date curățate și normalizate  
* `data/train/`, `data/validation/`, `data/test/` – seturi finale  
* `src/preprocessing/` – codul de preprocesare (resize + scalare)  

---

## 6. Concluzii Etapa 3

* Dataset-ul este pregătit complet pentru antrenarea modelului RN  
* Distribuțiile de clase sunt echilibrate pentru training și validare  
* Toate imaginile au dimensiune uniformă (224x224) și valori scalate  
* Etichetele sunt validate și encode corect  
* Structura repository-ului este pregătită pentru Etapa 4  

---

## 7. Stare Etapă (Checklist student)

- [x] Structură repository configurată  
- [x] Dataset analizat (EDA realizată)  
- [x] Date preprocesate și normalize  
- [x] Seturi train/val/test generate  
- [x] Documentație actualizată în README  

---
