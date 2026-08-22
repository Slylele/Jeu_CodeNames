import streamlit as st
import pandas as pd
import random

# --------------------------
# Paramètres
# --------------------------

NB_LIGNES = 5
NB_COLONNES = 5

COULEUR_DEFAUT = "#C9C9C9"
COULEUR_BLEU = "#1268FF"
COULEUR_ROUGE = "#E60032"
COULEUR_BEIGE = "#d6c6a5"
COULEUR_GRIS = "#5A5A5A"

# --------------------------
# Initialisation
# --------------------------

def nouvelle_grille(varFile, vatTitle):
    df = pd.read_csv(varFile)

    mots = random.sample(
        df[vatTitle].tolist(),
        NB_LIGNES * NB_COLONNES
    )

    st.session_state.mots = mots

    st.session_state.couleurs = [
        COULEUR_DEFAUT
        for _ in range(NB_LIGNES * NB_COLONNES)
    ]


if "mots" not in st.session_state:
    nouvelle_grille()


# --------------------------
# Titre
# --------------------------
st.set_option("client.toolbarMode", "minimal")      # Permet de cacher le menu streamlit en haut à droite

st.set_page_config(
    page_title="JEU CodeNames",
    page_icon="🎲",
    layout= "wide"
)
st.title("CodeNames")

# if st.button("🔄 Nouvelle grille"):
#     nouvelle_grille("mots_FR.csv", "Mot")
#     st.rerun()
nouvelle_grille("mots_FR.csv", "Mot")

col1, col2, col3 = st.columns([20, 20, 60])

with col1:
    if st.button("🇫🇷 🔄 Nouvelle grille"):
        st.session_state.langue = "fr"
        nouvelle_grille("mots_FR.csv", "Mot")
        st.rerun()

with col2:
    if st.button("🇬🇧 🔄 New grid"):
        st.session_state.langue = "en"
        nouvelle_grille("mots_EN.csv", "Word")
        st.rerun()

# --------------------------
# CSS
# --------------------------

st.markdown("""
<style>
/* Hide the Streamlit header and menu */
//header {visibility: hidden;}
//header.stAppHeader {display: none;}
//header.stAppHeader {background: #00325F;}
header.stAppHeader {background: transparent;}
//header[data-testid="stHeader"] {display: none;}
iframe[title="streamlit_autorefresh.st_autorefresh"] {display: none !important;}

/* Reduce space on top of the page */
.block-container {
    padding-top: 0rem;
    padding-bottom: 1rem;
}
/* Couleur de fond principale */
.stApp {
    background-color: #000000 !important;
    color: white !important;
}

/* Titres */
h2, h3, h4, h5, h6 {color: white !important;}
h1 {
    color: #dfe3e8 !important;
    text-align: center;
    font-size: 46px !important;
    font-weight: 1700;
    margin-top: 0 !important;
    padding-top: 0 !important;
    margin-bottom: 0.3rem !important;
    line-height: 1;
}
.stButton > button {
    //width: 100%;
    height: 10px;
    min-height: 12px;
    padding: 0px;
    font-size: 8px;
    border: 0px solid #999;
}

.case {
    border: 1px solid #999;
    border-radius: 8px;
    height: 110px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-weight: bold;
    text-align: center;
    padding: 4px;
    margin-bottom: 2px;
}

.zone-btn button {
    height: 22px !important;
    min-height: 25px !important;
    padding: 0px !important;
}


.blue-btn button {
    background-color:#5b9bd5 !important;
}

.beige-btn button {
    background-color:#d6c6a5 !important;
}

.gray-btn button {
    background-color:#666666 !important;
    color:white !important;
}


</style>
""", unsafe_allow_html=True)

# --------------------------
# Affichage
# --------------------------

for ligne in range(NB_LIGNES):

    cols = st.columns(NB_COLONNES)

    for col in range(NB_COLONNES):

        index = ligne * NB_COLONNES + col

        with cols[col]:
            couleur = st.session_state.couleurs[index]
            mot = st.session_state.mots[index]
            mot = mot[:1].upper() + mot[1:]

            st.markdown(
                f"""
                <div style="
                    background-color:{couleur};
                    border:1px solid #999;
                    border-radius:5px 5px 5px 5px;
                    height:120px;
                    display:flex;
                    justify-content:center;
                    align-items:center;
                    font-weight:bold;
                    text-align:center;
                    font-size:30px;
                ">
                    {mot}
                </div>
                """,
                unsafe_allow_html=True
            )

            aa, b0, b1, b2, b3, b4, xx = st.columns([7, 1, 1, 1, 1, 1, 7])

            with b0:
                if st.button("☒", width="stretch", key=f"xx_{index}"):
                    st.session_state.couleurs[index] = COULEUR_DEFAUT
                    st.rerun()

            with b1:
                if st.button("🟦", width="stretch", key=f"hg_{index}"):
                    st.session_state.couleurs[index] = COULEUR_BLEU
                    st.rerun()

            with b2:
                if st.button("🟥", width="stretch", key=f"hd_{index}"):
                    st.session_state.couleurs[index] = COULEUR_ROUGE
                    st.rerun()

            with b3:
                if st.button("🟨", width="stretch", key=f"bg_{index}"):
                    st.session_state.couleurs[index] = COULEUR_BEIGE
                    st.rerun()

            with b4:
                if st.button("⬛", width="stretch", key=f"bd_{index}"):
                    st.session_state.couleurs[index] = COULEUR_GRIS
                    st.rerun()
