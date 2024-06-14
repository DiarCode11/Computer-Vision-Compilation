import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def draw_line_chart(data):
    # Membuat plot garis
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(data, marker='o', linestyle='-', color='b')

    # Menambahkan judul dan label pada sumbu
    ax.set_title('Diagram Deteksi Stroberi Matang')
    ax.set_xlabel('Frame')
    ax.set_ylabel('Jumlah Stroberi yang Dideteksi')

    # Menambahkan grid
    ax.grid(True)

    # Menampilkan plot menggunakan Streamlit
    st.pyplot(fig)