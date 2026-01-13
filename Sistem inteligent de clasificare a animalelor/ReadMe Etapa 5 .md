# 📝 Etapa 5: Configurarea și Antrenarea Modelului RN

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Comardici Alexandru Gabriel  
**Link Repository GitHub:** [https://github.com/alexandrucomardici/Proiect_RN_Comardici_Alexandru.git](https://github.com/alexandrucomardici/Proiect_RN_Comardici_Alexandru.git)  
**Titlul proiectului:** Sistem inteligent de clasificare a animalelor  
**Data predării:** 11.12.2025  

---

## 1️⃣ Scopul Etapei 5

Antrenarea modelului RN definit în Etapa 4, evaluarea performanței pe setul combinat (≥40% date originale) și integrarea acestuia în UI-ul final.

**Context industrial:**  
Sistem aplicat camerelor de supraveghere publice pentru detectarea și clasificarea câinilor vagabonzi și a altor animale fără stăpân. Modelul recunoaște animalele din imagine, verifică dacă au stăpân (prezența zgărzii) și clasifică câinii după mărime.  

**Riscuri industriale:**  
O clasificare eronată poate duce la omiterea câinilor vagabonzi sau la interpretarea greșită a riscului, afectând deciziile operaționale și intervențiile echipelor de control.

---

## 2️⃣ Dataset

- **Număr total de sample-uri:** 1072  
- **Contribuție proprie (≥40%):** DA  
- **Tip date:** imagini  
- **Număr de clase:**  
  - Species: 2 (`cat`, `dog`)  
  - Owner: 2 (`has_owner = 0/1`)  
  - Size: 3 (`small`, `medium`, `big`)  

**Distribuție aproximativă:**

| Clasa           | Număr exemple |
|-----------------|---------------|
| Cat             | 69            |
| Dog             | 82            |
| Small (dog)     | 114           |
| Medium (dog)    | 37            |
| Big (dog)       | rest          |

**Generare date:** descărcare și procesare imagini online, resize la 224x224, normalizare 0–1.  

---

## 3️⃣ Preprocesare

- **Scaler / normalizare:** resize la 224x224 și împărțire RGB / 255 (cod Python propriu)  
- **Feature engineering:** n/a  
- **Split date:**  
  - Train: 80%  
  - Validation: 20%  
  - Test: 20%  
- **Random state:** 42  

---

## 4️⃣ Arhitectura RN

- **Framework:** TensorFlow / Keras  
- **Tip rețea:** CNN + MobileNetV2 (pretrained, top=False)  
- **Straturi principale:**  
  - Base MobileNetV2  
  - GlobalAveragePooling2D  
  - Dropout 0.3  
  - Dense 256 ReLU  
- **Output layers:**  
  - Species: Dense 2 softmax  
  - Owner: Dense 1 sigmoid  
  - Size: Dense 3 softmax  
- **Dimensiune input:** 224×224×3  

---

## 5️⃣ Antrenare – Hiperparametri

| Hiperparametru      | Valoare Aleasă | Justificare |
|--------------------|----------------|------------|
| Learning rate       | 0.001          | Standard pentru Adam, convergență stabilă |
| Batch size          | 16             | Memorie GPU restrânsă, 1072 imagini → 16 per batch asigură stabilitate și timp rezonabil de antrenare |
| Number of epochs    | 30             | Permite early stopping, dar modelul converge rapid (≈25 epoci efectiv) |
| Optimizer           | Adam           | Adaptive learning rate, bun pentru CNN + Multi-task |
| Loss function       | categorical_crossentropy (species & size), binary_crossentropy (owner) | Clasificare multi-class și binary |
| Activation functions| ReLU (hidden), Softmax (species/size), Sigmoid (owner) | ReLU pentru non-linearitate, Softmax/Sigmoid pentru probabilități clase |

- **Early stopping:** NU  
- **LR Scheduler:** NU  

---

## 6️⃣ Augmentări – Nivel 2

- **Tip augmentări:** noise Gaussian, random scaling, slight brightness variation  
- **Relevanță industrială:** simulează variațiile reale din mediul camerelor de supraveghere (distanta față de animal, condiții de iluminare diferite).  

---

## 7️⃣ Rezultate finale

- **Accuracy pe test set (species):** 0.9603  
- **F1-score macro (species):** 0.9601  
- **Precision macro:** 0.9697  
- **Recall macro:** 0.9603  
- **Număr epoci efectiv:** 25  

---

## 8️⃣ Analiză erori – Nivel 2

### 8.1 Clasele confundate cel mai frecvent

**Species:** cat → dog : 6 exemple  
**Size:** small → big : 114 exemple, medium → big : 37 exemple  

### 8.2 Condiții erori

Performanța scade când imaginile sunt surprinse de la distanțe variabile față de animal. Lipsa unei referințe de scară afectează corectitudinea clasificării dimensiunii.

### 8.3 Impact industrial

False positives sunt mai critice decât false negatives: clasificarea greșită a unui câine mare ca fiind mic poate duce la subestimarea riscului și decizii operaționale eronate.

### 8.4 Măsuri corective

1. Colectarea de imagini suplimentare pentru câini de talie medie și mare, surprinși la distanțe variabile.  
2. Aplicarea augmentărilor de tip zoom și random scaling pentru a simula variația distanței camerei.  
3. Prag adaptiv pentru clasificarea dimensiunii, bazat pe probabilitățile de ieșire ale rețelei neuronale.  

---

## 9️⃣ Rezultate grafice

- **Loss vs Val_loss:** `docs/loss_curve.png`  
- **Screenshot inferență UI:** `docs/screenshots/inference_real.png`  
- **Confusion matrix:** opțional (Nivel 3)  

---

## 10️⃣ Procedură rulare rapidă

```bash
# 1. Setup mediu
pip install -r requirements.txt

# 2. Preprocesare
python src/preprocessing/combine_datasets.py
python src/preprocessing/data_cleaner.py
python src/preprocessing/feature_engineering.py
python src/preprocessing/data_splitter.py --stratify --random_state 42

# 3. Antrenare model
python src/neural_network/train.py --epochs 30 --batch_size 16

# 4. Evaluare
python src/neural_network/evaluate.py --model models/trained_model.h5

# 5. UI
streamlit run src/app/main.py
