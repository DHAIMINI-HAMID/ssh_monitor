import streamlit as st
import pandas as pd

# 1. CONFIGURATION
st.set_page_config(page_title="SSH Monitor Dashboard", page_icon="🛡️", layout="wide")

# 2. CHARGEMENT
@st.cache_data
def load_data():
    data = pd.read_csv('dataset_ssh.csv')
    if 'Timestamp' in data.columns:
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    return data

# 3. INTERFACE
st.title("🛡️ Analyse des tentatives d'intrusion SSH")

try:
    df = load_data()
    
    # --- A. FILTRES ---
    st.sidebar.header("🔍 Filtres")
    
    # Filtre EventId
    if 'EventId' in df.columns:
        all_events = ['Tous'] + list(df['EventId'].unique())
        selected_event = st.sidebar.selectbox("Type d'événement", all_events)
    else:
        selected_event = 'Tous'

    # Filtre IP
    if 'SourceIP' in df.columns:
        all_ips = df['SourceIP'].unique()
        selected_ips = st.sidebar.multiselect("IP Source(s)", all_ips)
    else:
        selected_ips = []

    # Application des filtres
    df_filtered = df.copy()
    if selected_event != 'Tous':
        df_filtered = df_filtered[df_filtered['EventId'] == selected_event]
    if selected_ips:
        df_filtered = df_filtered[df_filtered['SourceIP'].isin(selected_ips)]

    # --- B. FEEDBACK UTILISATEUR (NOUVEAU) ---
    # Si le filtre ne renvoie RIEN, on arrête tout ici et on affiche le warning.
    if df_filtered.empty:
        st.warning("⚠️ Aucune donnée ne correspond à vos filtres actuels. Veuillez élargir votre sélection.")
        # On arrête l'exécution du script ici pour ne pas afficher des graphiques vides
        st.stop()
    
    # Si on arrive ici, c'est qu'il y a des données !
    st.sidebar.success(f"✅ {len(df_filtered)} événements trouvés")

    # --- C. METRICS ---
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Total Événements", len(df_filtered))
    kpi2.metric("IPs Uniques", df_filtered['SourceIP'].nunique())
    kpi3.metric("Attaquant Principal", df_filtered['SourceIP'].mode()[0])

    st.markdown("---")

    # --- D. GRAPHIQUES ---
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🚨 Top IPs")
        st.bar_chart(df_filtered['SourceIP'].value_counts().head(5))

    with col2:
        st.subheader("📈 Chronologie")
        if 'Timestamp' in df_filtered.columns:
            df_time = df_filtered.set_index('Timestamp')
            st.line_chart(df_time.resample('H').size())

    # --- E. LOGS ---
    with st.expander("Voir les logs détaillés"):
        st.dataframe(df_filtered, use_container_width=True)

except FileNotFoundError:
    st.error("Fichier dataset_ssh.csv introuvable.")
