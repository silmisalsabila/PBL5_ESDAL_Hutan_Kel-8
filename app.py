import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==================================================
# KONFIGURASI HALAMAN
# ==================================================
st.set_page_config(
    page_title="Eco-Forest Valuation",
    page_icon="🌳",
    layout="wide"
)

# ==================================================
# COVER
# ==================================================
col1, col2 = st.columns([1, 5])

with col1:

    logo_path = "logo_unisba.png"

    if os.path.exists(logo_path):
        st.image(logo_path, width=120)

with col2:

    st.markdown("""
    <h1 style='color:#14532d;'>
    ECO-FOREST VALUATION
    </h1>

    <h4 style='color:#166534;'>
    Aplikasi Interaktif Ekonomi Sumber Daya Hutan
    untuk Memahami Nilai Ekonomi dan Keberlanjutan Hutan
    </h4>
    """, unsafe_allow_html=True)

st.markdown("---")

st.write("### Disusun Oleh")

st.write("""
**Kelompok 8**

1. Nadylah Agustinawati (10090224003)

2. Silmi Yusniah Salsabila (10090224020)

3. Siti Annisa Dewanty (10090224033)
""")

st.write("""
**Mata Kuliah:** Ekonomi Sumber Daya Alam dan Lingkungan

**Dosen Pengampu:** Yuhka Sundaya, S.E., M.Si

**Program Studi:** Ekonomi Pembangunan

**Universitas Islam Bandung**
""")

st.markdown("---")

# ==================================================
# SIDEBAR
# ==================================================
menu = st.sidebar.selectbox(
    "Pilih Modul",
    [
        "Beranda",
        "Kalkulator TEV",
        "Trade-off Lahan",
        "Kebijakan PES",
        "Kasus Interaktif",
        "Visualisasi TEV",
        "Tentang Aplikasi"
    ]
)

# ==================================================
# BERANDA
# ==================================================
if menu == "Beranda":

    st.header("🌳 Selamat Datang")

    st.write("""
    Eco-Forest Valuation merupakan aplikasi pembelajaran
    interaktif yang membantu pengguna memahami konsep
    ekonomi sumber daya hutan melalui pendekatan valuasi ekonomi.

    Aplikasi ini terdiri atas empat modul utama:
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.success("📊 Kalkulator Total Economic Value (TEV)")
        st.success("⚖️ Simulasi Trade-off Lahan")

    with col2:
        st.success("💰 Kebijakan PES")
        st.success("📚 Kasus Interaktif")

    st.info("""
    Tujuan aplikasi adalah membantu mahasiswa memahami
    bagaimana hutan memberikan manfaat ekonomi,
    sosial, dan lingkungan secara berkelanjutan.
    """)

# ==================================================
# KALKULATOR TEV
# ==================================================
elif menu == "Kalkulator TEV":

    st.header("📊 Kalkulator Total Economic Value (TEV)")

    st.write("""
    Total Economic Value (TEV) merupakan pendekatan yang digunakan
    untuk menghitung seluruh manfaat ekonomi yang diberikan oleh hutan.
    """)

    luas = st.number_input(
        "Luas Hutan (Ha)",
        min_value=1,
        value=100
    )

    nilai_langsung = st.number_input(
        "Nilai Guna Langsung (Rp/Ha)",
        min_value=0,
        value=500000
    )

    nilai_jasa = st.number_input(
        "Nilai Jasa Lingkungan (Rp/Ha)",
        min_value=0,
        value=900000
    )

    nilai_opsi = st.number_input(
        "Nilai Pilihan Masa Depan (Rp/Ha)",
        min_value=0,
        value=300000
    )

    nilai_eksistensi = st.number_input(
        "Nilai Eksistensi (Rp/Ha)",
        min_value=0,
        value=300000
    )

    tev = luas * (
        nilai_langsung +
        nilai_jasa +
        nilai_opsi +
        nilai_eksistensi
    )

    st.success(
        f"Total Economic Value = Rp {tev:,.0f}"
    )

# ==================================================
# TRADE OFF LAHAN
# ==================================================
elif menu == "Trade-off Lahan":

    st.header("⚖️ Simulasi Trade-off Lahan")

    st.write("""
    Modul ini membandingkan manfaat ekonomi antara
    mempertahankan kawasan hutan dan mengkonversinya
    menjadi penggunaan lain.
    """)

    nilai_hutan = st.slider(
        "Nilai Hutan Lestari (Miliar Rp)",
        0,
        200,
        120
    )

    nilai_pertanian = st.slider(
        "Nilai Konversi Pertanian (Miliar Rp)",
        0,
        200,
        80
    )

    data = pd.DataFrame({
        "Alternatif": [
            "Hutan Lestari",
            "Konversi Pertanian"
        ],
        "Nilai": [
            nilai_hutan,
            nilai_pertanian
        ]
    })

    st.bar_chart(
        data.set_index("Alternatif")
    )

    if nilai_hutan > nilai_pertanian:

        st.success(
            "Rekomendasi: Mempertahankan hutan lebih menguntungkan."
        )

    elif nilai_hutan < nilai_pertanian:

        st.warning(
            "Konversi lahan terlihat lebih menguntungkan secara ekonomi jangka pendek."
        )

    else:

        st.info(
            "Kedua alternatif memiliki nilai yang sama."
        )

# ==================================================
# KEBIJAKAN PES
# ==================================================
elif menu == "Kebijakan PES":

    st.header("💰 Payment for Ecosystem Services (PES)")

    st.write("""
    PES merupakan mekanisme pemberian insentif kepada masyarakat
    atas jasa lingkungan yang dihasilkan dari pelestarian hutan.
    """)

    karbon = st.slider(
        "Serapan Karbon (Ton CO₂)",
        0,
        1000,
        300
    )

    harga = st.number_input(
        "Harga Karbon (Rp/Ton)",
        min_value=0,
        value=150000
    )

    insentif = karbon * harga

    st.metric(
        "Estimasi Insentif PES",
        f"Rp {insentif:,.0f}"
    )

    st.write("""
    Semakin besar jasa lingkungan yang dihasilkan,
    semakin besar pula insentif yang dapat diterima.
    """)

# ==================================================
# KASUS INTERAKTIF
# ==================================================
elif menu == "Kasus Interaktif":

    st.header("📚 Kasus Interaktif")

    kasus = st.selectbox(
        "Pilih Kasus",
        [
            "Penyerbukan Lebah",
            "Karbon Hutan",
            "Ekowisata"
        ]
    )

    if kasus == "Penyerbukan Lebah":

        st.subheader("🐝 Penyerbukan Lebah")

        st.write("""
        Lebah hutan membantu proses penyerbukan tanaman
        pertanian sehingga meningkatkan produktivitas hasil panen.
        Jika habitat hutan rusak maka populasi lebah menurun
        dan hasil pertanian dapat berkurang.
        """)

    elif kasus == "Karbon Hutan":

        st.subheader("🌍 Karbon Hutan")

        st.write("""
        Hutan berperan sebagai penyerap karbon alami
        yang membantu mengurangi dampak perubahan iklim.
        Nilai ekonomi karbon dapat digunakan sebagai dasar
        kebijakan perdagangan karbon.
        """)

    else:

        st.subheader("🏕️ Ekowisata")

        st.write("""
        Ekowisata memberikan manfaat ekonomi kepada masyarakat
        sekitar sekaligus mendorong pelestarian kawasan hutan.
        """)

# ==================================================
# VISUALISASI TEV
# ==================================================
elif menu == "Visualisasi TEV":

    st.header("📈 Visualisasi Komponen TEV")

    data = pd.DataFrame({
        "Komponen": [
            "Nilai Guna Langsung",
            "Jasa Lingkungan",
            "Option Value",
            "Existence Value"
        ],
        "Persentase": [
            25,
            45,
            15,
            15
        ]
    })

    fig, ax = plt.subplots(figsize=(7, 5))

    ax.pie(
        data["Persentase"],
        labels=data["Komponen"],
        autopct="%1.0f%%"
    )

    ax.set_title("Komposisi Total Economic Value")

    st.pyplot(fig)

# ==================================================
# TENTANG APLIKASI
# ==================================================
elif menu == "Tentang Aplikasi":

    st.header("ℹ️ Tentang Aplikasi")

    st.write("""
    Eco-Forest Valuation merupakan media pembelajaran
    yang dirancang untuk membantu mahasiswa memahami
    konsep ekonomi sumber daya hutan melalui simulasi
    interaktif dan pendekatan valuasi ekonomi.

    Konsep utama yang digunakan meliputi:

    • Total Economic Value (TEV)

    • Trade-off penggunaan lahan

    • Payment for Ecosystem Services (PES)

    • Valuasi jasa lingkungan hutan
    """)

st.markdown("---")

st.caption(
    "Sumber: Arsitektur Aplikasi Eco-Forest Valuation dan konsep Ekonomi Sumber Daya Hutan."
)
