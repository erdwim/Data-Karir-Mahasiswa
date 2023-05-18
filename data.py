import streamlit as st

st.title("Data Karir Mahasiswa")

# Initialize an empty list to store the data entries
data_entries = []

while True:
    nama = st.text_input("Nama")
    nim = st.text_input("NIM")
    prodi = st.text_input("Prodi")
    lulusan = st.text_input("Tahun Lulusan")
    bekerja = st.text_input("Bekerja")

    # Create a dictionary to store the data for this entry
    data_entry = {
        "Nama": nama,
        "NIM": nim,
        "Prodi": prodi,
        "Tahun Lulusan": lulusan,
        "Bekerja": bekerja
    }

    # Add the data entry to the list of entries if the user clicks the "Kirim" button
    if st.button("Kirim"):
        data_entries.append(data_entry)
        st.success("Terkirim")

    # Ask the user if they want to enter another data entry
    if not st.write("Terima Kasih"):
        break

# Display the table with all of the data entries
if data_entries:
    st.write("Data Karir Mahasiswa:")
    st.table(data_entries)
else:
    st.write("Belum ada data yang dimasukkan.")