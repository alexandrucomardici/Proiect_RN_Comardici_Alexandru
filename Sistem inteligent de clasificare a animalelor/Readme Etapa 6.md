# 📘 Etapa 6 – Optimizare și Concluzii Finale
**Disciplina:** Rețele Neuronale  
**Proiect:** Sistem inteligent de clasificare a animalelor 
**Student:** Comardici Alexandru Gabriel
**Link Repository:** https://github.com/alexandrucomardici/Proiect_RN_Comardici_Alexandru.git 
**Instituție:** POLITEHNICA București – FIIR  

---

## 1. Experimente de Optimizare

În această etapă au fost realizate mai multe experimente pentru îmbunătățirea performanței și robusteții modelului.

### Tabel Experimente

| ID | Modificare aplicată | Accuracy | F1-score | Observații |
|---|--------------------|----------|----------|------------|
| E0 | Model inițial (baseline) | 0.96 | 0.96 | Performanță ridicată, dar fără filtrare predicții slabe |
| E1 | Dropout crescut (0.5) | 0.95 | 0.95 | Ușoară sub-antrenare |
| E2 | Augmentare date (zoom + flip) | 0.97 | 0.96 | Generalizare mai bună |
| E3 | Prag confidence (0.6) | 0.94 | 0.97 | Elimină predicții false |
| E4 | Combinație E2 + E3 (FINAL) | **0.97** | **0.97** | Model final optimizat |

**Model ales:** E4 – oferă cel mai bun echilibru între acuratețe și siguranță.

---

## 2. Modificări Aplicație Software

| ID | Modificare | Motiv | Impact |
|---|-----------|------|--------|
| M1 | Prag confidence pe specie | Evitare clasificări forțate | Reduce false positives |
| M2 | Mesaj explicit „Imaginea nu conține câine sau pisică” | UX clar | Crește încrederea utilizatorului |
| M3 | Istoric predicții | Feedback vizual | Interfață mai intuitivă |
| M4 | UI web cu Bootstrap | Demonstrație practică | Aplicație complet funcțională |

---

## 3. Analiza Confusion Matrix (Species)

Confusion Matrix:
[[63 6]
[ 0 82]]


- **Pisică (cat):**
  - 63 clasificate corect
  - 6 confundate ca dog
  - Recall = 0.91

- **Câine (dog):**
  - 82 clasificate corect
  - 0 erori
  - Recall = 1.00

**Observație:** confuzia principală apare pentru pisici cu dimensiuni sau poziții atipice.

---

## 4. Analiza Exemple Greșite

### Exemplu 1 – Cat → Dog
- Pisică mare, zoom ridicat
- Siluetă similară cu câine mic

### Exemplu 2 – Cat → Dog
- Lumină slabă
- Fundal aglomerat

### Exemplu 3 – Small → Big (dog)
- Câine mic foarte aproape de cameră

### Exemplu 4 – Medium → Big (dog)
- Unghi de jos, distorsiune perspectivă

### Exemplu 5 – Small → Big (dog)
- Lipsă context dimensional în imagine

**Cauză generală:** lipsa informației de scară absolută.

---

## 5. Concluzii și Lecții Învățate

- Modelul atinge performanță ridicată (>96%)
- Pragul de confidence este esențial pentru aplicații reale
- Clasificarea dimensiunii este mai dificilă decât specia
- UI-ul îmbunătățește interpretabilitatea rezultatului
- Dataset-ul influențează direct erorile observate

---

## 6. Direcții Viitoare

- Integrare detecție obiect (YOLO)
- Extindere dataset
- Separare completă detectare vs clasificare
