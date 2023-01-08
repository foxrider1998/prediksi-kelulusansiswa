import pickle
import numpy as np
import streamlit as st

#load save model
model = pickle.load(open('kelulusan_siswa.sav', 'rb'))

#judul web
st.title('Prediksi Kelulusan Siswa')


col1, col2,  = st.columns(2)

st.text ('Nurlaela , 191351068')
with col1 :
    decile3 = st.number_input('Peringkat sekolah berdasarkan hukum desil tahun ketiga')
with col2 :
    decile1 = st.number_input('Peringkat sekolah berdasarkan hukum desil tahun pertama')
with col1 :
    sex = st.number_input('Jenis Kelamin')
with col2 :
    isat = st.number_input('Skor dari setiap Kandidat tahun pertama')
with col1 :
    ugpa = st.number_input('Skor dari setiap Kandidat tahun ketiga')
with col2 :
    grad = st.number_input('Siswa berdasarkan lulusan')
with col1 :
    fulltime = st.number_input('Siswa penuh waktu')
with col2 :
    fam_inc = st.number_input('Pendapatan keluarga berdasarkan kuintil')
with col1 :
    partime = st.number_input('Pekerja Keras')
with col2 :
    male = st.number_input('Kategori pria')
with col1 :
    race1 = st.number_input('Kategori siswa berdasarkan ras')
with col2 :
    tier = st.number_input('Tingkatan sekolah hukum')
with col1 :
    decileb1 = st.number_input('Satuan untuk mengukur intesitas suara')
# code for prediction
kelulusan_siswa_data =''

# membuat tombol prediksi 
if st.button('Prediksi Kelulusan Siswa'):
    kelulusan_siswa_prediction = model.predict([[decile3, decile1, sex, isat, ugpa, grad, fulltime, fam_inc, partime, male, race1, tier, decileb1]])

    if (kelulusan_siswa_prediction[0]==1):
        kelulusan_siswa_data = 'Siswa Lulus Ujian'
    else :
        kelulusan_siswa_data = 'Siswa Tidak Lulus Ujian'
st.success(kelulusan_siswa_data)
