# 📦 Smart Inventory Dashboard

Una web application interattiva sviluppata in Python per digitalizzare e ottimizzare la gestione delle scorte in ambito retail. Il tool calcola dinamicamente i volumi di riordino ideali applicando modelli matematici logistici, colmando il divario tra l'operatività di negozio e l'analisi avanzata dei dati.

Questo progetto dimostra l'applicazione pratica di logiche di digital transformation per prevenire rotture di stock e minimizzare i costi di magazzino.

## ✨ Funzionalità Principali
* **Calcolo EOQ Dinamico:** Determinazione automatica dell'Economic Order Quantity per bilanciare e minimizzare i costi di ordine e di mantenimento a scaffale.
* **Reorder Point (ROP):** Calcolo del livello critico di scorte che fa scattare l'allarme di riordino, calcolato sul lead time dei fornitori.
* **Simulazione Stagionalità:** Un pannello laterale interattivo permette di applicare moltiplicatori di domanda in tempo reale per simulare picchi di vendita (es. festività o stagioni ad alto traffico).
* **Data Visualization:** Grafici a barre reattivi e metriche dinamiche per confrontare a colpo d'occhio le giacenze attuali con i limiti critici calcolati.
* **Alerting Visivo:** Sistema di notifiche condizionali che segnala esattamente quali referenze (SKU) necessitano di un intervento immediato, suggerendo le quantità esatte da ordinare.

## 🛠️ Stack Tecnologico
* **Linguaggio:** Python 3
* **Librerie Core:** `pandas` (manipolazione dataset), `numpy` (calcolo algebrico)
* **Interfaccia Web:** `streamlit`

## 🚀 Come avviare il progetto

1. **Clona il repository e installa le dipendenze:**
   ```bash
   git clone [https://github.com/TUO_USERNAME/inventory_dashboard.git](https://github.com/TUO_USERNAME/inventory_dashboard.git)
   cd inventory_dashboard
   pip install pandas numpy streamlit
