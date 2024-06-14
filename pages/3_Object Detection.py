import streamlit as st
from PIL import Image
from utils.detect import detect_strawberries
from utils.diagram import draw_line_chart
import numpy as np
import cv2

def main():
    st.title("🍓Deteksi Stroberi Matang")
    
    toggleOn = st.checkbox('Aktifkan Kamera')

    # Inisialisasi counts dalam session_state jika belum ada
    if 'counts' not in st.session_state:
        st.session_state.counts = []

    # Inisialisasi status awal kamera
    if 'fstStart' not in st.session_state:
        st.session_state.fstStart = True
    
    if toggleOn:
        st.session_state.fstStart = False
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
            if not ret:
                break
            
            # Deteksi stroberi matang
            frame, detection_counts = detect_strawberries(frame)
            print(detection_counts)
            st.session_state.counts.append(detection_counts)
            
            # Tempat kosong untuk menampilkan frame 
            frame_container.image(frame, channels="BGR")
            
    elif not toggleOn and not st.session_state.fstStart:
        st.session_state.fstStart = True
        # Menghitung total stroberi matang yang terdeteksi
        print(st.session_state.counts)
        draw_line_chart(st.session_state.counts)

if __name__ == "__main__":
    main()
