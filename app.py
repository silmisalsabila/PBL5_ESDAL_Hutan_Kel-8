import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Forest Value Explorer",
    page_icon="🌳",
    layout="wide"
)

# ================= COVER =================

st.title("🌳 Forest Value Explorer")
st.subheader(
    "Aplikasi Interaktif untuk Memahami Ekonomi dan Keberlanjutan Sumber Daya Hutan Indonesia"
)

st.markdown("---")

st.write("### Disusun Oleh")
st.write("**Kelompok 8**")

st.write("""
1. Nadylah Agustinawati (10090224003)
2. Silmi Yusniah Salsabila (10090224020)
3. Siti Annisa Dewanty (10090224033)
""")

st.write("Program Studi Ekonomi Pembangunan")
st.write("Universitas Islam Bandung")

st.markdown("---")

# ================= PENDAHULUAN =================

st.header("📖 Pendahuluan")

st.write("""
Ekonomi sumber daya hutan merupakan cabang ilmu yang mempelajari
pemanfaatan sumber daya hutan secara optimal untuk meningkatkan
kesejahteraan masyarakat tanpa mengabaikan aspek keberlanjutan.

Berdasarkan tiga jurnal yang digunakan, hutan memiliki nilai ekonomi
yang besar baik dari hasil kayu, hasil non-kayu, jasa lingkungan,
maupun sektor ekowisata.
""")

# ================= MANFAAT EKONOMI HUTAN =================

st.header("🌿 Manfaat Ekonomi Sumber Daya Hutan")

manfaat = pd.DataFrame({
    "Jenis Manfaat":[
        "Hasil Kayu",
        "Hasil Non Kayu",
        "Jasa Lingkungan",
        "Ekowisata"
    ],
    "Keterangan":[
        "Bahan baku industri dan konstruksi",
        "Madu, rotan, getah, tanaman obat",
        "Penyerap karbon dan penyimpan air",
        "Pendakian, wisata alam dan konservasi"
    ]
})

st.dataframe(manfaat)

# ================= PERMASALAHAN =================

st.header("⚠️ Permasalahan Sumber Daya Hutan")

masalah = pd.DataFrame({
    "Permasalahan":[
        "Deforestasi",
        "Penebangan Liar",
        "Kebakaran Hutan",
        "Eksploitasi Berlebihan"
    ],
    "Dampak":[
        "Berkurangnya luas hutan",
        "Kerusakan ekosistem",
        "Pencemaran dan kerugian ekonomi",
        "Penurunan kualitas sumber daya hutan"
    ]
})

st.dataframe(masalah)

# ================= GRAFIK =================

st.header("📊 Tingkat Ancaman terhadap Hutan")

grafik = pd.DataFrame({
    "Kategori":[
        "Deforestasi",
        "Penebangan Liar",
        "Kebakaran",
        "Eksploitasi"
    ],
    "Skor":[40,25,20,15]
})

fig, ax = plt.subplots()

ax.bar(
    grafik["Kategori"],
    grafik["Skor"]
)

ax.set_ylabel("Persentase (%)")
ax.set_title("Ancaman terhadap Sumber Daya Hutan")

st.pyplot(fig)

# ================= STUDI KASUS =================

st.header("🏕️ Studi Kasus Taman Nasional Gunung Ciremai")

st.write("""
Penelitian pada Taman Nasional Gunung Ciremai menggunakan
Contingent Valuation Method (CVM) untuk mengetahui
kesediaan membayar (Willingness To Pay/WTP)
pengunjung terhadap peningkatan pengelolaan kawasan wisata.

Hasil penelitian menunjukkan bahwa wisata alam memiliki
nilai ekonomi yang penting dalam mendukung konservasi
dan pengelolaan sumber daya hutan secara berkelanjutan.
""")

# ================= SIMULASI =================

st.header("💰 Simulasi Nilai Ekonomi Wisata Hutan")

jumlah = st.slider(
    "Jumlah Pengunjung",
    100,
    10000,
    1000
)

wtp = st.number_input(
    "Willingness To Pay per Pengunjung (Rp)",
    value=10000
)

nilai = jumlah * wtp

st.success(
    f"Estimasi Nilai Ekonomi Wisata = Rp {nilai:,.0f}"
)

# ================= KESIMPULAN =================

st.header("📌 Kesimpulan")

st.write("""
1. Hutan memiliki nilai ekonomi yang tinggi melalui hasil kayu,
hasil non-kayu, jasa lingkungan dan ekowisata.

2. Pemanfaatan hutan harus memperhatikan prinsip keberlanjutan
agar fungsi ekologis tetap terjaga.

3. Valuasi ekonomi sumber daya hutan penting sebagai dasar
pengambilan kebijakan pengelolaan hutan.

4. Pengembangan ekowisata dapat menjadi alternatif peningkatan
pendapatan sekaligus mendukung konservasi hutan.
""")

st.markdown("---")
st.caption("Sumber: Hasil sintesis tiga jurnal ekonomi sumber daya hutan.")