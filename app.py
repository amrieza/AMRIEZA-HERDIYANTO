import streamlit as st
import pandas as pd

# Load data (replace with the correct CSV file name and location)
data = pd.read_csv("employee_data.csv")

# Function to predict income category
def predict_category(gaji_pokok, total_tunjangan, golongan, jenis_jabatan, tahun_formasi_pppk):
    if total_tunjangan > 500000:
        return "Kategori Penghasilan: Tinggi, Tidak mendapatkan kas koperasi"
    elif gaji_pokok > 2000000:
        return "Kategori Penghasilan: Sedang, Tidak mendapatkan kas koperasi"
    else:
        return "Kategori Penghasilan: Rendah, Mendapatkan kas koperasi"

# Function to predict based on employee ID (nip)
def predict_by_nip(nip, golongan, jenis_jabatan, tahun_formasi_pppk, gaji_pokok, total_tunjangan):
    employee_data = data[data['nip'] == int(nip)].iloc[0]

    gaji_pokok_data = employee_data['gaji_pokok']
    total_tunjangan_data = employee_data['total_tunjangan']
    golongan_data = employee_data['golongan']
    jenis_jabatan_data = employee_data['jenis_jabatan']
    tahun_formasi_pppk_data = employee_data['tahun_formasi_pppk']

    return predict_category(gaji_pokok_data, total_tunjangan_data, golongan_data, jenis_jabatan_data, tahun_formasi_pppk_data)

# Streamlit input page
def input_page():
    st.title("Prediksi Kategori Penghasilan Karyawan")

    # Input form
    nip = st.text_input("Masukkan NIP Karyawan:")
    golongan = st.text_input("Masukkan Golongan P3K:")
    jenis_jabatan = st.text_input("Masukkan Jenis Jabatan (1 : Guru, 2 : Nakes, 3 : Teknis):")
    tahun_formasi_pppk = st.text_input("Masukkan Tahun Formasi PPPK:")
    gaji_pokok = st.number_input("Masukkan Gaji Pokok:", min_value=0)
    total_tunjangan = st.number_input("Masukkan Total Tunjangan:", min_value=0)

    submit_button = st.button("Prediksi")

    # Process input when the button is pressed
    if submit_button:
        try:
            result = predict_by_nip(nip, golongan, jenis_jabatan, tahun_formasi_pppk, gaji_pokok, total_tunjangan)
            st.success(result)
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Run Streamlit application
if __name__ == '__main__':
    input_page()
