import streamlit as st

st.title("Data Karir Mahasiswa")

nama=st.text_input("Nama")
nim=st.text_input("NIM")
prodi=st.text_input("Prodi")
lulusan=st.text_input("Tahun Lulusan")
bekerja=st.text_input("Bekerja")

send=st.button("Kirim")