import streamlit as st
import pandas as pd
import numpy as np

# Configurazione
st.set_page_config(page_title="Smart Inventory", layout="wide")
st.title("📦 Smart Inventory Dashboard")

# 1. Sidebar per i parametri dinamici
st.sidebar.header("⚙️ Parametri Dinamici")
st.sidebar.markdown("Usa lo slider per simulare i picchi di vendita stagionali.")
moltiplicatore_stagione = st.sidebar.slider("Fattore Stagionalità (Es. 1.5 = Picco Estivo)", min_value=0.5, max_value=2.0, value=1.0, step=0.1)

@st.cache_data
def carica_dati():
    return pd.read_csv("dati_magazzino.csv")

df = carica_dati()

# 2. Motore di Calcolo Logistico Dinamico
# Moltiplichiamo la domanda base per il fattore scelto dall'utente
df["Domanda_Attiva"] = df["Domanda_Annua"] * moltiplicatore_stagione

df["EOQ_Dinamico"] = np.sqrt(
    (2 * df["Domanda_Attiva"] * df["Costo_Ordine"]) / df["Costo_Mantenimento"]
).round().astype(int)

domanda_giornaliera = df["Domanda_Attiva"] / 300
df["ROP_Dinamico"] = (domanda_giornaliera * df["Lead_Time_Giorni"]).round().astype(int)

# 3. Interfaccia Grafica e Visualizzazione
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📊 Metriche")
    st.metric("Moltiplicatore Attivo", f"{moltiplicatore_stagione}x")
    prodotti_in_esaurimento = len(df[df["Scorta_Attuale"] <= df["ROP_Dinamico"]])
    st.metric("Allarmi Sottoscorta", prodotti_in_esaurimento, delta_color="inverse")

with col2:
    st.subheader("📈 Scorte vs Punto di Riordino (ROP)")
    # Prepariamo un sotto-dataframe pulito per il grafico nativo di Streamlit
    grafico_dati = df[["Descrizione", "Scorta_Attuale", "ROP_Dinamico"]].set_index("Descrizione")
    st.bar_chart(grafico_dati)

st.divider()
st.subheader("📋 Tabella Operativa e Interventi")

# Mostriamo la tabella aggiornata con i valori dinamici
colonne_visibili = ["SKU", "Descrizione", "Scorta_Attuale", "ROP_Dinamico", "EOQ_Dinamico"]
st.dataframe(df[colonne_visibili], use_container_width=True)

# Avvisi visivi per le rotture di stock
da_ordinare = df[df["Scorta_Attuale"] <= df["ROP_Dinamico"]]
if not da_ordinare.empty:
    for index, row in da_ordinare.iterrows():
        st.error(f"**{row['Descrizione']}** è sotto il limite! Scorta: {row['Scorta_Attuale']} | Ordinare: **{row['EOQ_Dinamico']}** unità.")
else:
    st.success("Tutti i prodotti hanno scorte sufficienti.")
