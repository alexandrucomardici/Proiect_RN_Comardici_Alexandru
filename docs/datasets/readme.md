\# 📚 Dataset – Sistem Inteligent de Clasificare a Animalelor



Acest proiect utilizează un dataset de imagini cu \*\*pisici și câini\*\*, necesar pentru clasificarea:

\- 🐱 pisică / câine  

\- 🐶 talia câinelui: mică / medie / mare  

\- 🐕‍🦺 prezența zgărzii: da / nu  



\## 📌 Sursa dataset-ului

Dataset principal: \*\*Zenodo DOGS\_AND\_CATS\_LIGHT\*\*  

Link: https://zenodo.org/records/5226945?utm\_source=chatgpt.com



Opțional completare:

\- TensorFlow Cats vs Dogs  

\- Adnotări manuale pentru zgardă (dacă este necesar)



\## 📊 Structură

\- ~550 imagini pisici

\- ~550 imagini câini  

\- Rezoluții variate  

\- Diverse rase, poziții și fundaluri



\## 📝 Caracteristici

| Label | Tip | Valori |

|-------|------|----------|

| species | categorial | cat / dog |

| size | categorial | small / medium / large |

| collar\_present | categorial | yes / no |



\## 🔧 Preprocesare realizată

\- redimensionare la 224×224 px  

\- normalizare 0–1  

\- split train/val/test  

\- augmentări (flip, rotație, zoom)



