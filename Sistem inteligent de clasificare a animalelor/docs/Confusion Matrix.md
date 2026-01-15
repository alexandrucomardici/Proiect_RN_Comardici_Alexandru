### Interpretare Confusion Matrix (Species)

Modelul obține performanță foarte bună pentru clasificarea speciilor.

- **Pisică (cat):**
  - 63 clasificate corect
  - 6 clasificate greșit ca dog
  - Recall = 0.91
  - Cauză: unele imagini conțin pisici în poziții sau dimensiuni atipice

- **Câine (dog):**
  - 82 clasificate corect
  - 0 clasificate greșit
  - Recall = 1.00
  - Clasa este bine separată datorită caracteristicilor vizuale clare

**Confuzia principală:** cat → dog (6 exemple)
Această eroare este acceptabilă în context industrial, deoarece nu produce risc major.
