import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_icon=":bar_chart:", page_title="Tingkat Kenaikan UMP Di Indonesia", layout="centered")
st.markdown("""
<style>
.normal-font {
    font-size:100% !important;
    text-align: justify;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.title-font {
    font-size:260% !important;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)



st.markdown('<h1 class="title-font"> TINGKAT KENAIKAN GAJI TIAP DAERAH DI INDONESIA PADA 2019-2022 </h1>', unsafe_allow_html=True)
st.markdown("Penulis: **Adli Aulia Fattah Harahap**")
st.caption("04 Agustus 2022")
st.markdown("---")


data_final = pd.read_csv("./data/Indonesian Salary by Region (1997-2022)_final.csv")


x_indexes = np.arange(34)
width = 0.25
fig, ax = plt.subplots(figsize = (13, 8)) 
plt.bar(x_indexes-width, data_final['GROWTH RATE (2019-2020) %'][:34], width = width, color='#19b356', label='PERSENTASE TINGKAT KENAIKAN UMP (2019-2020)')
plt.bar(x_indexes, data_final['GROWTH RATE (2020-2021) %'][:34], width = width, color='#1963b3', label='PERSENTASE TINGKAT KENAIKAN UMP (2020-2021)')
plt.bar(x_indexes+width, data_final['GROWTH RATE (2021-2022) %'][:34], width = width, color='#b31919', label='PERSENTASE TINGKAT KENAIKAN UMP (2021-2022)')
plt.xlabel("PROVINSI", fontsize=12)
plt.xticks(x_indexes, data_final['REGION'][:34], rotation = 70)
plt.ylabel("TINGKAT KENAIKAN (%)", fontsize=12)
plt.title("TINGKAT KENAIKAN UMP DI INDONESIA 3 TAHUN TERAKHIR (2019-2022)", fontweight='bold', fontsize=20)
plt.grid()
plt.tight_layout()
plt.legend()
st.pyplot(fig)

st.markdown('''<p class="normal-font">
Tahukah kamu bahwa <b>Upah Minimum Provinsi (UMP)</b> di Indonesia memiliki nilai yang berbeda-beda? dan apakah nilainya akan selalu sama, naik ataukah turun? Sebelum itu, perlu diketahui apa itu Upah Minimum Provinsi. Upah Minimum Provinsi (UMP) atau lebih dikenal UMR adalah standar minimum yang diberikan oleh pekerja dan ditetapkan oleh pemerintah berdasarkan <b>UU No. 11 Tahun 2020 tentang Cipta Kerja</b> yang diturunkan melalui <b>Peraturan Pemerintah (PP) No. 36 tahun 2021 tentang pengupahan</b>. Pada halaman resmi <b>BPS</b> (bps.go.id) besarnya UMP pada setiap daerah berbeda dan sudah ada sejak tahun 1997.
</p>''', unsafe_allow_html=True)

st.markdown('<p style="color:Grey; font-size: 100%;">(Sumber : BPS dan Kementerian Ketenagakerjaan RI)</p>', unsafe_allow_html=True)

st.dataframe(data_final)

st.markdown('<p class="normal-font">Sejak tahun 2019, besarnya UMP di Indonesia mengalami kenaikan walaupun diterjang pandemi <b>COVID-19</b>. Hal ini terjadi karena adanya instruksi <b>Kementerian Ketenagakerjaan (Kemnaker) RI</b> di setiap tahunnya, yaitu:', unsafe_allow_html=True)

st.markdown('''
\n 1. Pada tahun 2020, **kenaikan UMP sebesar 8,51%** untuk semua provinsi di Indonesia. Namun, berdasarkan data yang diperoleh rata-rata kenaikan UMP yang terjadi dari tahun 2019-2020 sebesar **8,84%** 
\n 2. Pada tahun 2021, **tidak ada kenaikan UMP di seluruh Indonesia**. Dikutip dari CNN Indonesia (cnnindonesia.com) didorong oleh pertimbangan bahwa pertumbuhan ekonomi Indonesia akan minus karena **resesi**, walaupun kebijakan tersebut tidak diikuti oleh beberapa daerah. Sehingga, berdasarkan data yang diperoleh rata-rata kenaikan UMP yang terjadi dari tahun 2020-2021 sebesar **0,52%** 
\n 3. Pada tahun 2022, **kenaikan UMP sebesar 1,09%** untuk semua provinsi di Indonesia. Akan tetapi, berdasarkan data yang diperoleh rata-rata kenaikan UMP yang terjadi dari tahun 2021-2022 sebesar **1,49%**''')

width = 0.4
fig, ax = plt.subplots(figsize = (12, 8))
plt.bar(x_indexes, data_final['GROWTH RATE AVG %'][:34], width = width, color='#19b356', label='RATA-RATA PERSENTASE TINGKAT KENAIKAN UMP')
plt.xlabel("PROVINSI", fontsize=12)
plt.xticks(x_indexes, data_final['REGION'][:34], rotation = 70)
ax.get_xticklabels()[-6].set_weight("bold")
ax.get_xticklabels()[10].set_weight("bold")
ax.get_xticklabels()[13].set_weight("bold")
plt.ylabel("TINGKAT KENAIKAN (%)", fontsize=12)
plt.title("RATA-RATA PERSENTASE TINGKAT KENAIKAN UMP DI INDONESIA 3 TAHUN TERAKHIR (2019-2022)", fontweight='bold', fontsize=15)
plt.grid()
plt.tight_layout()
plt.legend()
st.pyplot(fig)

st.markdown('''<p class="normal-font">
Kemudian terlihat dari tiga tahun terkahir, provinsi yang memiliki rata-rata <b>kenaikan UMP tertinggi</b> adalah <b>Provinsi Gorontalo sebesar 5,8 %, DKI Jakarta sebesar 5,63 %, dan DI Yogyakarta sebesar 5,45 %</b>. Rata-rata kenaikan tertinggi yang diperoleh Provinsi Gorontalo disebabkan oleh tingkat <b>kenaikan UMP Gorontalo di tahun 2020 sebesar 16,98%</b>. Dikutip dari Hulondalo.id dan Kumparan di mana tingkat kenaikan tersebut didapatkan dari kebijakan Kemnaker RI mengenai UMP tahun 2020 dan juga <b>Provinsi Gorontalo dinilai belum menerapkan upah sesuai Kondisi Hidup Layak (KHL)</b> di bawah PP No.78 tahun 2015 sehingga kenaikan <b>bertambah sebesar 8,47%</b>. Sementara, rata-rata tingkat <b>kenaikan UMP di Provinsi DKI Jakarta dan DI Yogyakarta disebabkan oleh keputusan gubernur</b> yang tidak melanggar kebijakan Kemnaker RI tiap tahunnya.</p>''', unsafe_allow_html=True)

for i in range(5):
    st.markdown(" ")
st.markdown("---")
st.markdown("---")