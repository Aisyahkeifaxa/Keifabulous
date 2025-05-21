import streamlit as st

st.title("🎈 KEIFAKEREN")
st.write(
    "Hello welcome to my world [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.image("IMG_20250421_151939.jpg")
st.image("IMG-20250514-WA0001.jpeg", width=100) 
st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
