# 📘 README – Etapa 3: Analiza și Pregătirea Setului de Date pentru Rețele Neuronale

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Comardici Alexandru  
**Data:** 20.11.2025  

---

## 🚀 Introducere

Acest document descrie activitățile realizate în **Etapa 3**, în care se analizează și se preprocesează setul de date necesar proiectului „Rețele Neuronale: Sistem Inteligent de Clasificare a Animalelor”.  
Scopul etapei este pregătirea corectă a datelor pentru instruirea modelului RN, respectând bunele practici privind calitatea, consistența și reproductibilitatea datelor.

---

## 📂 1. Structura Repository-ului Github (Etapa 3)

```
project-name/
├── README.md
├── docs/
│   └── datasets/          # descriere seturi de date, surse, diagrame
├── data/
│   ├── raw/               # date brute
│   ├── processed/         # date curățate și transformate
│   ├── train/             # set de instruire
│   ├── validation/        # set de validare
│   └── test/              # set de testare
├── src/
│   ├── preprocessing/     # funcții pentru preprocesare
│   ├── data_acquisition/  # generare / achiziție date (dacă există)
│   └── neural_network/    # implementarea RN (în etapa următoare)
├── config/                # fișiere de configurare
└── requirements.txt       # dependențe Python (dacă aplicabil)
```

---

## 🐾 2. Descrierea Setului de Date

### 2.1 📌 Sursa datelor

* **Origine:** Imagini cu animale (pisici și câini), necesare pentru clasificare.  
* **Modul de achiziție:** ✔ Fișier extern + ✔ Posibile completări programatice  
* **Condițiile colectării:** Seturi de imagini în scenarii diverse: interior/exterior, calitate variabilă, talie diferită a câinilor, cu/ fără zgardă.

### 2.2 🧬 Caracteristicile dataset-ului

* **Număr total de imagini:** ~10.000 (exemplu)
* **Tipuri de date:** ✔ Imagini  
* **Format fișiere:** ✔ PNG / ✔ JPG  

### 2.3 📝 Caracteristici

| Caracteristică | Tip | Descriere | Domeniu valori |
|----------------|-----|-----------|----------------|
| label_species | categorial | pisică / câine | {cat, dog} |
| label_size | categorial | talia câinelui | {small, medium, large} |
| collar_present | categorial | detectarea zgărzii | {yes, no} |

---

## 🔍 3. Analiza Exploratorie a Datelor (EDA)

### 3.1 📊 Statistici aplicate

* Distribuția claselor  
* Raport între imagini cu zgardă / fără zgardă  
* Identificarea dataset-ului dezechilibrat  
* Verificarea rezoluțiilor și calității imaginilor  

### 3.2 ♻️ Calitatea datelor

* Imagini corupte eliminate  
* Detectarea duplcicatelor  
* Analiza distribuției pe categorii  

### 3.3 ⚠️ Probleme identificate

* Dezechilibru de clase (ex: prea puține imagini cu zgardă)  
* Diferențe mari în rezoluție  
* Clase suprapuse vizual (ex: câini mici vs. pisici mari)

---

## 🧹 4. Preprocesarea Datelor

### 4.1 Curățare

* Eliminarea imaginilor corupte  
* Uniformizarea dimensiunii imaginilor (ex: 224×224 px)  
* Eliminarea duplicatelor  

### 4.2 🔧 Transformări

* Normalizare pixel intensities  
* Augmentări: flip, rotiri, zoom pentru diversificarea datelor  
* One-hot encoding pentru etichete  

### 4.3 ✂️ Structurare

Împărțire:  
* 70–80% – train  
* 10–15% – validation  
* 10–15% – test  

Principii:  
* Stratificare  
* Fără scurgere de informație  
* Transformări calculate doar pe train  

---

## 💾 5. Fișiere Generate

* `data/raw/` – dataset brut  
* `data/processed/` – imagini procesate  
* Seturile finale: `train/`, `validation/`, `test/`  
* Codul: `src/preprocessing/`  
* Documentație dataset: `data/README.md`

---

## ✅ 6. Stare Etapă

- [ ] Structură repository configurată  
- [ ] Dataset analizat (EDA realizată)  
- [ ] Date preprocesate  
- [ ] Seturi train/val/test generate  
- [ ] Documentație actualizată  

---

✨ **Succes în etapa următoare – implementarea rețelei neuronale!**  
