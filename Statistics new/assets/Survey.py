import streamlit as st
import pandas as pd
from scipy.stats import pearsonr, spearmanr
import matplotlib.pyplot as plt
import seaborn as sns

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Survey Analysis - Kelompok 11",
    layout="wide"
)

# =====================================================
# SIDEBAR LANGUAGE SELECTION
# =====================================================
language = st.sidebar.selectbox(
    "Pilih Bahasa / Select Language",
    ["Indonesia", "English"]
)

# =====================================================
# TEXT DI BASED ON LANGUAGE
# =====================================================
if language == "Indonesia":
    texts = {
        "home_title": "Aplikasi Analisis Survei",
        "home_subtitle": "Kelompok 11 — President University",
        "pendahuluan_title": "📘 Pendahuluan",
        "pendahuluan_text": "Aplikasi ini dirancang untuk membantu pengolahan dan analisis data survei menggunakan pendekatan statistik secara sistematis dan informatif.",
        "deskriptif_title": "📊 Analisis Deskriptif",
        "deskriptif_text": "Analisis deskriptif digunakan untuk menggambarkan karakteristik data survei, seperti mean, median, standar deviasi, nilai minimum, dan maksimum.",
        "asosiasi_title": "🔗 Analisis Asosiasi",
        "asosiasi_text": "Analisis asosiasi bertujuan untuk mengetahui hubungan antar variabel numerik. Aplikasi ini menggunakan korelasi Pearson atau Spearman secara otomatis.",
        "tujuan_title": "🎯 Tujuan",
        "tujuan_text": "Membantu mahasiswa dalam memahami data survei serta menyajikan hasil analisis statistik yang mudah dipahami.",
        "upload_file": "Upload File Excel",
        "desc_stats": "📈 Statistik Deskriptif",
        "scatter_plot": "📉 Visualisasi Scatter Plot",
        "variable_x": "Variabel X",
        "variable_y": "Variabel Y",
        "method": "Metode",
        "corr_coef": "Koefisien Korelasi",
        "p_value": "P-value",
        "significant": "Hubungan signifikan ditemukan.",
        "not_significant": "Tidak ditemukan hubungan signifikan.",
        "about_title": "President University",
        "about_subtitle": "Kelompok 11"
    }
else:  # English
    texts = {
        "home_title": "Survey Analysis Application",
        "home_subtitle": "Group 11 — President University",
        "pendahuluan_title": "📘 Introduction",
        "pendahuluan_text": "This application is designed to help process and analyze survey data using a systematic and informative statistical approach.",
        "deskriptif_title": "📊 Descriptive Analysis",
        "deskriptif_text": "Descriptive analysis is used to describe survey data characteristics, such as mean, median, standard deviation, minimum, and maximum values.",
        "asosiasi_title": "🔗 Association Analysis",
        "asosiasi_text": "Association analysis aims to identify relationships between numeric variables. The app automatically uses Pearson or Spearman correlation.",
        "tujuan_title": "🎯 Purpose",
        "tujuan_text": "Helps students understand survey data and present statistical analysis results in an easy-to-understand way.",
        "upload_file": "Upload Excel File",
        "desc_stats": "📈 Descriptive Statistics",
        "scatter_plot": "📉 Scatter Plot Visualization",
        "variable_x": "Variable X",
        "variable_y": "Variable Y",
        "method": "Method",
        "corr_coef": "Correlation Coefficient",
        "p_value": "P-value",
        "significant": "Significant relationship found.",
        "not_significant": "No significant relationship found.",
        "about_title": "President University",
        "about_subtitle": "Group 11"
    }

# =====================================================
# CSS — FULL COLOR THEME
# =====================================================
st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: linear-gradient(180deg, #fdeaff 0%, #e8f0ff 100%);
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ff7eb3, #8ec5fc);
    padding-top: 30px;
}

section[data-testid="stSidebar"] * {
    color: white !important;
    font-weight: 500;
}

div[data-testid="stRadio"] > div,
div[data-testid="stSelectbox"] > div {
    background: rgba(255,255,255,0.18);
    padding: 15px;
    border-radius: 16px;
    margin-bottom: 20px;
}

/* HEADER */
.header-box {
    background: linear-gradient(135deg, #ff7eb3, #8ec5fc);
    padding: 55px;
    border-radius: 0 0 45px 45px;
    text-align: center;
    color: white;
    margin-bottom: 60px;
    box-shadow: 0 15px 30px rgba(0,0,0,0.12);
}

/* HOME SECTION CARD */
.section-card {
    background: white;
    padding: 30px;
    border-radius: 24px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.1);
    margin-bottom: 35px;
}

.section-title {
    font-size: 26px;
    font-weight: bold;
    color: #ff6fae;
    margin-bottom: 12px;
}

.section-text {
    font-size: 18px;
    color: #444;
    line-height: 1.7;
}

/* PROFILE CARD */
.profile-wrapper {
    max-width: 900px;
    margin: auto;
}

.profile-card {
    background: linear-gradient(180deg, #ffffff, #f7f9ff);
    border-radius: 26px;
    padding: 30px;
    box-shadow: 0 14px 35px rgba(0,0,0,0.12);
    margin-bottom: 45px;
}

.profile-name {
    font-size: 28px;
    font-weight: bold;
    color: #ff6fae;
}

.profile-text {
    font-size: 18px;
    color: #444;
}

.profile-quote {
    margin-top: 10px;
    font-style: italic;
    color: #7aa2ff;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR NAVIGATION
# =====================================================
page = st.sidebar.radio(
    "Navigasi",
    ["🏠 Home", "📊 Analisis Survei", "👥 About Us"]
)

# =====================================================
# HOME — PENDAHULUAN & MATERI
# =====================================================
if page == "🏠 Home":

    st.markdown(f"""
    <div class="header-box">
        <h1>{texts['home_title']}</h1>
        <h3>{texts['home_subtitle']}</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="section-card">
        <div class="section-title">{texts['pendahuluan_title']}</div>
        <div class="section-text">{texts['pendahuluan_text']}</div>
    </div>

    <div class="section-card">
        <div class="section-title">{texts['deskriptif_title']}</div>
        <div class="section-text">{texts['deskriptif_text']}</div>
    </div>

    <div class="section-card">
        <div class="section-title">{texts['asosiasi_title']}</div>
        <div class="section-text">{texts['asosiasi_text']}</div>
    </div>

    <div class="section-card">
        <div class="section-title">{texts['tujuan_title']}</div>
        <div class="section-text">{texts['tujuan_text']}</div>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# ANALISIS SURVEI
# =====================================================
elif page == "📊 Analisis Survei":

    st.title("📊 Analisis Data Survei")

    file = st.file_uploader(texts["upload_file"], type=["xlsx"])

    if file:
        df = pd.read_excel(file)
        st.dataframe(df)

        st.subheader(texts["desc_stats"])
        st.write(df.describe())

        numeric = df.select_dtypes(include="number").columns

        if len(numeric) >= 2:
            x = st.selectbox(texts["variable_x"], numeric)
            y = st.selectbox(texts["variable_y"], numeric)

            # Pilih metode korelasi
            if df[x].nunique() > 10 and df[y].nunique() > 10:
                corr, p = pearsonr(df[x], df[y])
                method = "Pearson"
            else:
                corr, p = spearmanr(df[x], df[y])
                method = "Spearman"

            st.write(f"**{texts['method']}:** {method}")
            st.write(f"**{texts['corr_coef']}:** {corr:.3f}")
            st.write(f"**{texts['p_value']}:** {p:.4f}")

            if p < 0.05:
                st.success(texts["significant"])
            else:
                st.warning(texts["not_significant"])

            # ===========================
            # SCATTER PLOT
            # ===========================
            st.subheader(texts["scatter_plot"])
            fig, ax = plt.subplots(figsize=(7,5))
            sns.scatterplot(data=df, x=x, y=y, ax=ax, s=80, color="#FF6FAE")
            sns.regplot(data=df, x=x, y=y, scatter=False, ax=ax, color="#7AA2FF")  # garis regresi
            ax.set_title(f"{x} vs {y}", fontsize=16)
            ax.set_xlabel(x, fontsize=12)
            ax.set_ylabel(y, fontsize=12)
            st.pyplot(fig)

# =====================================================
# ABOUT US
# =====================================================
elif page == "👥 About Us":

    st.markdown(f"""
    <div class="header-box">
        <h1>{texts['about_title']}</h1>
        <h3>{texts['about_subtitle']}</h3>
    </div>
    """, unsafe_allow_html=True)

    members = [
        ("Alya Mukhbita", "004202400003", "Project Leader & Documentation", "assets/alya.jpg", "Leading with grace"),
        ("Nabila Maharani Yudhistiro", "004202400116", "UI/UX Designer", "assets/Nabila.jpg", "Beauty in every pixel"),
        ("Talytha Belva Clarisa", "004202400020", "Data Analyst", "assets/talytha.jpg", "Data tells the story"),
        ("Zahra Aulia Al Madani", "004202400087", "Programmer", "assets/Zahra.jpg", "Code with purpose")
    ]

    st.markdown('<div class="profile-wrapper">', unsafe_allow_html=True)

    for i, m in enumerate(members):
        col1, col2 = st.columns(2, gap="large")

        if i % 2 == 0:
            with col1:
                st.image(m[3], use_container_width=True)
            with col2:
                st.markdown(f"""
                <div class="profile-card">
                    <div class="profile-name">{m[0]}</div>
                    <div class="profile-text"><b>NIM:</b> {m[1]}</div>
                    <div class="profile-text"><b>Role:</b> {m[2]}</div>
                    <div class="profile-quote">"{m[4]}"</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            with col1:
                st.markdown(f"""
                <div class="profile-card">
                    <div class="profile-name">{m[0]}</div>
                    <div class="profile-text"><b>NIM:</b> {m[1]}</div>
                    <div class="profile-text"><b>Role:</b> {m[2]}</div>
                    <div class="profile-quote">"{m[4]}"</div>
                </div>
                """, unsafe_allow_html=True)
            with col2:
                st.image(m[3], use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)
