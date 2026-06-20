# ==================================================

# BERANDA

# ==================================================

if menu == "Beranda":

st.header("Beranda")

st.write("""
Eco-Forest Valuation merupakan aplikasi pembelajaran interaktif yang dirancang untuk membantu mahasiswa memahami konsep ekonomi sumber daya hutan melalui pendekatan valuasi ekonomi. Aplikasi ini mengintegrasikan konsep Total Economic Value (TEV), trade-off penggunaan lahan, dan Payment for Ecosystem Services (PES) untuk menggambarkan bagaimana sumber daya hutan memberikan manfaat ekonomi, sosial, dan lingkungan secara berkelanjutan.

Sebagai contoh penerapan, aplikasi ini menggunakan pendekatan studi kasus Taman Nasional Gunung Ciremai. Kawasan konservasi ini memiliki peran penting sebagai penyedia jasa lingkungan, penyerap karbon, habitat keanekaragaman hayati, serta sumber manfaat ekonomi melalui kegiatan wisata alam dan pemberdayaan masyarakat sekitar.

Melalui simulasi dan visualisasi yang tersedia, pengguna dapat memahami bahwa nilai suatu kawasan hutan tidak hanya berasal dari hasil hutan yang dapat dimanfaatkan secara langsung, tetapi juga dari berbagai manfaat tidak langsung yang mendukung keberlanjutan lingkungan dan kesejahteraan masyarakat.
""")

st.subheader("Modul Aplikasi")

st.write("""
1. Kalkulator Total Economic Value (TEV)

2. Simulasi Trade-off Penggunaan Lahan

3. Payment for Ecosystem Services (PES)

4. Studi Kasus Interaktif

5. Visualisasi Komponen Nilai Ekonomi Hutan
""")

# ==================================================

# KALKULATOR TEV

# ==================================================

elif menu == "Kalkulator TEV":

st.header("Kalkulator Total Economic Value (TEV)")

st.write("""
Total Economic Value (TEV) merupakan pendekatan yang digunakan untuk menghitung seluruh manfaat ekonomi yang dihasilkan oleh suatu kawasan hutan. Pendekatan ini mencakup nilai guna langsung, nilai jasa lingkungan, nilai pilihan, dan nilai eksistensi.

Dalam konteks Taman Nasional Gunung Ciremai, manfaat tersebut dapat berupa pemanfaatan wisata alam, penyediaan air bersih, penyimpanan karbon, perlindungan keanekaragaman hayati, serta manfaat keberlanjutan yang dapat dinikmati oleh generasi mendatang.

Melalui simulasi ini, pengguna dapat memasukkan nilai dari masing-masing komponen untuk memperoleh estimasi Total Economic Value suatu kawasan hutan.
""")

st.info("""
Contoh Studi Kasus:
Taman Nasional Gunung Ciremai memiliki luas kawasan sekitar 14.841 hektar dan memberikan berbagai manfaat ekonomi serta ekologis bagi masyarakat di sekitarnya.
""")

luas = st.number_input(
    "Luas Hutan (Ha)",
    min_value=1,
    value=14841
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
    "Nilai Pilihan (Rp/Ha)",
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

st.header("Simulasi Trade-off Penggunaan Lahan")

st.write("""
Pengelolaan sumber daya hutan sering menghadapi dilema antara mempertahankan fungsi ekologis kawasan hutan dan mengkonversinya menjadi penggunaan lahan lain yang memberikan keuntungan ekonomi jangka pendek.

Simulasi ini membantu pengguna memahami konsep trade-off dengan membandingkan nilai ekonomi dari hutan lestari dan konversi lahan pertanian. Hasil simulasi dapat digunakan untuk menggambarkan pentingnya mempertimbangkan manfaat jangka panjang dalam pengambilan keputusan pembangunan.
""")

nilai_hutan = st.slider(
    "Nilai Hutan Lestari (Miliar Rupiah)",
    0,
    200,
    120
)

nilai_pertanian = st.slider(
    "Nilai Konversi Pertanian (Miliar Rupiah)",
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
        "Mempertahankan hutan memberikan manfaat ekonomi dan lingkungan yang lebih tinggi dalam jangka panjang."
    )

elif nilai_hutan < nilai_pertanian:

    st.warning(
        "Konversi lahan memberikan keuntungan ekonomi jangka pendek yang lebih besar, namun berpotensi mengurangi jasa lingkungan."
    )

else:

    st.info(
        "Kedua alternatif memiliki nilai ekonomi yang sama."
    )

# ==================================================

# KEBIJAKAN PES

# ==================================================

elif menu == "Kebijakan PES":

st.header("Payment for Ecosystem Services (PES)")

st.write("""
Payment for Ecosystem Services (PES) merupakan mekanisme pemberian insentif kepada masyarakat atau pengelola kawasan yang mampu menjaga dan meningkatkan jasa lingkungan yang dihasilkan oleh hutan.

Dalam praktiknya, jasa lingkungan yang dapat dihargai melalui skema PES meliputi penyimpanan karbon, perlindungan daerah tangkapan air, konservasi keanekaragaman hayati, dan perlindungan ekosistem lainnya.

Simulasi berikut digunakan untuk mengestimasi potensi insentif ekonomi berdasarkan kemampuan hutan dalam menyerap karbon.
""")

karbon = st.slider(
    "Serapan Karbon (Ton CO2)",
    0,
    1000,
    300
)

harga_karbon = st.number_input(
    "Harga Karbon per Ton (Rp)",
    min_value=0,
    value=150000
)

insentif = karbon * harga_karbon

st.metric(
    "Estimasi Nilai Insentif",
    f"Rp {insentif:,.0f}"
)

# ==================================================

# KASUS INTERAKTIF

# ==================================================

elif menu == "Kasus Interaktif":

st.header("Kasus Interaktif")

kasus = st.selectbox(
    "Pilih Kasus",
    [
        "Taman Nasional Gunung Ciremai",
        "Karbon Hutan",
        "Ekowisata"
    ]
)

if kasus == "Taman Nasional Gunung Ciremai":

    st.subheader("Taman Nasional Gunung Ciremai")

    st.write("""
    Taman Nasional Gunung Ciremai merupakan kawasan konservasi yang memiliki nilai ekologis dan ekonomi yang tinggi. Kawasan ini berfungsi sebagai daerah tangkapan air, penyerap karbon, habitat berbagai spesies flora dan fauna, serta destinasi wisata alam yang mendukung perekonomian masyarakat sekitar.

    Dari perspektif ekonomi sumber daya alam, berbagai manfaat tersebut dapat dinilai menggunakan pendekatan valuasi ekonomi agar seluruh manfaat lingkungan dapat dipertimbangkan dalam pengambilan keputusan pembangunan dan konservasi.

    Keberadaan kawasan ini menunjukkan bahwa pelestarian hutan tidak hanya penting bagi lingkungan, tetapi juga memberikan manfaat ekonomi jangka panjang yang sering kali lebih besar dibandingkan pemanfaatan lahan secara eksploitatif.
    """)

elif kasus == "Karbon Hutan":

    st.subheader("Karbon Hutan")

    st.write("""
    Hutan berperan sebagai penyerap karbon alami yang membantu mengurangi konsentrasi gas rumah kaca di atmosfer. Kemampuan ini memberikan manfaat ekonomi melalui skema perdagangan karbon dan berbagai kebijakan mitigasi perubahan iklim.

    Semakin besar kemampuan hutan menyerap karbon, semakin tinggi pula potensi nilai ekonomi jasa lingkungan yang dapat dihasilkan.
    """)

else:

    st.subheader("Ekowisata")

    st.write("""
    Ekowisata merupakan bentuk pemanfaatan sumber daya hutan yang mengedepankan prinsip konservasi dan keberlanjutan. Aktivitas wisata alam dapat menciptakan lapangan kerja, meningkatkan pendapatan masyarakat, serta mendorong pelestarian lingkungan.

    Oleh karena itu, ekowisata sering dianggap sebagai alternatif pemanfaatan hutan yang mampu menyeimbangkan tujuan ekonomi dan konservasi.
    """)

# ==================================================

# VISUALISASI TEV

# ==================================================

elif menu == "Visualisasi TEV":

st.header("Visualisasi Komponen TEV")

st.write("""
Total Economic Value (TEV) terdiri atas berbagai komponen yang secara bersama-sama mencerminkan nilai ekonomi suatu kawasan hutan. Visualisasi berikut menunjukkan proporsi masing-masing komponen dalam membentuk nilai ekonomi total sumber daya hutan.
""")

data = pd.DataFrame({
    "Komponen": [
        "Nilai Guna Langsung",
        "Jasa Lingkungan",
        "Nilai Pilihan",
        "Nilai Eksistensi"
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

ax.set_title(
    "Komposisi Total Economic Value"
)

st.pyplot(fig)

# ==================================================

# TENTANG APLIKASI

# ==================================================

elif menu == "Tentang Aplikasi":

st.header("Tentang Aplikasi")

st.write("""
Eco-Forest Valuation dikembangkan sebagai media pembelajaran untuk mendukung pemahaman mahasiswa terhadap konsep ekonomi sumber daya hutan. Aplikasi ini mengintegrasikan teori dan simulasi interaktif sehingga pengguna dapat mengeksplorasi berbagai aspek valuasi ekonomi lingkungan secara lebih mudah dan aplikatif.

Konsep yang digunakan dalam aplikasi ini meliputi:

• Total Economic Value (TEV)

• Trade-off Penggunaan Lahan

• Payment for Ecosystem Services (PES)

• Valuasi Jasa Lingkungan

• Pengelolaan Hutan Berkelanjutan

Aplikasi ini juga menampilkan contoh penerapan pada Taman Nasional Gunung Ciremai sebagai salah satu kawasan konservasi yang memiliki nilai ekonomi, sosial, dan ekologis yang penting bagi pembangunan berkelanjutan.
""")
