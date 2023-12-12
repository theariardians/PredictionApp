import streamlit as st
import webbrowser
from PIL import Image

st.title("NCT Dream")

image = Image.open("Team logo/NCT_DREAM_logo.png")

new_size = (850, 508)

resized_image = image.resize(new_size)

st.image(resized_image)

# info about the team
st.write("NCT Dream adalah sub-unit ketiga dari boy band asal Korea Selatan NCT, yang khusus beranggotakan remaja dengan usia belasan tahun.")
st.write("Pada awalnya, sub-unit ini memiliki sistem kelulusan di mana anggota yang melampaui usia 20 akan keluar, tapi pada 2020, sistem ini diganti dan menjadikan NCT Dream sebagai unit tetap NCT. Unit ini melakukan debutnya pada 25 Agustus 2016 dengan lagu Chewing Gum.")

st.subheader("Di bawah adalah para anggota")

# for Player
st.header("Anggota")
st.info('Mark Lee, Huang Renjun, Lee Jeno, Lee Haechan, Na Jaemin, Zhong Chenle dan Park Jisung.')
lead = Image.open('Team photos/MMA_2023_NCT_Dream_1.jpg')
size = (1260, 768)
lead_image = lead.resize(size)
st.image(lead_image)

st.subheader("Connect dengan NCT Dream: ")

if st.button("Instagram"):
    webbrowser.open_new_tab("https://www.instagram.com/nct/")

if st.button("Twitter"):
    webbrowser.open_new_tab("https://twitter.com/NCTsmtown_DREAM")

if st.button("Album NCT Dream Spotify"):
    webbrowser.open_new_tab(
        "https://open.spotify.com/intl-id/artist/1gBUSTR3TyDdTVFIaQnc02?si=DzXHjtRjQgiyIjO-GFIH-Q")
