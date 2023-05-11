import streamlit as st
tab1,tab2 = st.tabs(["Mengisi Form Data Karir Mahasiswa","Data Karir Mahasiswa"])
with tab1 :
    st.title("Data Karir Mahasiswa")
    nama=st.text_input("Nama")
    nim=st.text_input("NIM")
    prodi=st.text_input("Prodi")
    lulusan=st.text_input("Tahun Lulusan")
    bekerja=st.text_input("Bekerja")
    send=st.button("Kirim")
    if send :
        st.success("Terkirim")
    if send:
        with tab2 :
            yang_terkirim1 = nama
            yang_terkirim2 = nim
            yang_terkirim3 = prodi
            yang_terkirim4 = lulusan
            yang_terkirim5 = bekerja
            st.text("===============================================================================")
            (f"Nama    : {yang_terkirim1}")
            (f"NIM     : {yang_terkirim2}")
            (f"Prodi   : {yang_terkirim3}")
            (f"Lulusan : {yang_terkirim4}")
            (f"Bekerja : {yang_terkirim5}")
            st.text("===============================================================================")

