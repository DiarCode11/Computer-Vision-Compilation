import streamlit as st
from PIL import Image
from utils.detect import detect_strawberries
import numpy as np
import cv2

def main():
    st.title("🍓Deteksi Strawbery Matang")
    st.write("Silakan berikan gambar strawberry")
    
    
    cap = cv2.VideoCapture(0)
    # Periksa apakah kamera berhasil diinisialisasi
    if not cap.isOpened():
        st.error("Tidak dapat membuka kamera.")
        return
    
    # Menyiapkan wadah kosong untuk menampilkan frame
    frame_container = st.empty()
    # Loop untuk menampilkan frame dari kamera
    while True:
        # Baca frame dari kamera
        ret, frame = cap.read()
        
        # Deteksi stroberi matang
        frame = detect_strawberries(frame)
        
        # Tempat kosong untuk menampilkan frame 
        frame_container.image(frame, channels="BGR")
        
if __name__ == "__main__":
    main()

