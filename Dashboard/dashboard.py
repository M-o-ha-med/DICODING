import streamlit as st
import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns
plt.rcParams.update({'font.size': 15})

st.title(
"""
Dashboard analisis data
"""
)

st.text("""oleh Mohamed""")

st.header("""Cuaca dan keadaan cuaca""")
fig , axis  = plt.subplots(nrows = 1 , ncols  = 2 , figsize = (20 , 8))
data_hour = pd.read_csv("data_hour.csv")
sns.barplot(x = data_hour.season , y = data_hour.cnt , ax = axis[0] )
sns.barplot(x = data_hour.weathersit, y = data_hour.cnt , ax = axis[1] )
axis[0].set_xlabel("Musim" , fontsize = (20))
axis[1].set_xlabel("Kondisi cuaca" , fontsize = (20))
axis[0].set_ylabel("penyewa ( casual + registered) " , fontsize = (20))
axis[1].set_ylabel(None)
plt.ylim(0, 250)
plt.suptitle("Cuaca dan keadaan cuaca terhadap jumlah sewa sepeda" , fontsize = (20))
st.pyplot(fig)

st.write(
"""
pada grafik diatas , terlihat bahwa musim gugur merupakan musim dengan jumlah sewa sepeda
terbanyak diiringi dengan kondisi cuaca 1.

keterangan untuk grafik kondisi cuaca:

"""
)

st.text("1: Cerah, Sedikit awan, Sebagian berawan, Sebagian berawan")
st.text("2: Kabut + Mendung, Kabut + Awan pecah, Kabut + Sedikit awan, Kabut")
st.text("3: Salju ringan, Hujan ringan + Badai petir + Awan terpisah, Hujan ringan + Awan terpisah")
st.text("4: Hujan lebat + Pecahan es + Badai petir + Kabut, Salju + Kabut")

st.header("""Temperatur , kelembapan dan kecepatan angin""")

figure,axis  = plt.subplots(nrows = 1 , ncols = 3 ,  figsize=(40, 10))
sns.lineplot(x  = data_hour.temp , y = data_hour.cnt ,ax= axis[0])
sns.lineplot(x  = data_hour.hum , y = data_hour.cnt ,ax= axis[1])
sns.lineplot(x  = data_hour.windspeed , y = data_hour.cnt ,ax= axis[2])
plt.ylim(0,500)
plt.suptitle("perbandingan antara temperatur , kelembapan dan kecepatan angin  terhadap jumlah sewa sepeda",fontsize = 40)
st.pyplot(figure)

st.write(
"""
pada grafik diatas , terlihat bahwa kelembapan , kecepatan angin dan temperatur lingkungan berpengaruh
terhadap banyak jumlah sewa sepeda.
"""
)

st.header("""Jam sewa sepeda""")
figs , axiss = plt.subplots( figsize = (20 , 8))
axiss.bar(x = data_hour.hr ,height = data_hour.cnt)
axiss.set_xlabel("waktu (jam)")
axiss.set_ylabel("Jumlah sewa")
st.pyplot(figs)


st.write(
"""
pada grafik diatas , terlihat bahwa rentang  jam 18:00  - 19:00 merupakan waktu yang paling
banyak terjadinya peminjaman sepeda.
"""
)

st.header("""hari biasa , hari libur , dan hari kerja""")
fig  ,axis = plt.subplots(nrows = 1 , ncols = 3 , figsize = (15 , 8))
sns.barplot(x = data_hour["weekday"] , y = data_hour.cnt , ax = axis[0])
sns.barplot(x = data_hour["holiday"] , y = data_hour.cnt , ax = axis[1])
sns.barplot(x = data_hour["workingday"] , y = data_hour.cnt , ax = axis[2])
axis[1].set_ylabel(None)
axis[2].set_ylabel(None)
plt.suptitle("perbandingan antara hari biasa , hari libur dan hari kerja  terhadap jumlah sewa sepeda",fontsize = 10)
st.pyplot(fig)

st.write(
"""
pada grafik diatas , jumlah sewa sepeda memiliki jumlah tertinggi pada hari ke 4 dan 5 , lalu jumlah sewa
juga biasanya lebih banyak pada hari selain liburan dan lebih banyak di hari kerja dan hari biasa.
"""
)

st.header("""perbandingan penyewa casual dan registered""")
fig , axis = plt.subplots(nrows = 1 , ncols = 2 , figsize = (20 ,8))
sns.barplot(x = data_hour.hr , y = data_hour.casual , ax = axis[0])
sns.barplot(x = data_hour.hr , y = data_hour.registered , ax = axis[1])
axis[0].set_ylim(top = 400)
st.pyplot(fig)

st.write(
"""
pada grafik diatas , terlihat bahwa penyewa sepeda yang telah teregistrasi lebih banyak daripada
penyewa sepeda kasual dengan jarak yang cukup jauh terutama pada jam tertentu seperti jam 18:00 hingga 19:00.
"""
)
