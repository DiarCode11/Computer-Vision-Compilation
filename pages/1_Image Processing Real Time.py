import cv2
import numpy as np
import streamlit as st
from utils.processing_real_time import *

def main():
    st.title("🖼️ Image Processing Real Time")
    # Inisialisasi kamera
    cap = cv2.VideoCapture(0)

    # Periksa apakah kamera berhasil diinisialisasi
    if not cap.isOpened():
        st.error("Tidak dapat membuka kamera.")
        return

    
    cols = st.columns(3)
    with cols[0]:
        st.write("#### Pencerminan:")
        h_flip = st.checkbox('Flip Horizontal')
        v_flip = st.checkbox('Flip Vertikal')
    with cols[1]:
        st.write("#### Filter:")
        filter_type = st.selectbox("Pilih Filter", ["Gambar Asli", "Grayscale", "Negative", "Black and White", "Sketch", "Blur", "Edge", "Emboss", "Sepia", "Heatmap", ])
    # buat bar dengan streamlit
    with cols[2]: 
        st.write("#### Rotasi:")
        rotation_angle = st.slider("Rotation Angle", -180, 180, 0)
    
    # Menyiapkan wadah kosong untuk menampilkan frame
    frame_container = st.empty()
    # Loop untuk menampilkan frame dari kamera
    while True:
        # Baca frame dari kamera
        ret, frame = cap.read()
        
        # Periksa apakah bacaan frame berhasil
        if not ret:
            st.error("Tidak dapat menerima frame.")
            break
        
        if h_flip: 
            frame = horizontal_flip(frame)
            
        if v_flip: 
            frame = vertical_flip(frame)
        # Gambar Asli
        if filter_type == 'Gambar Asli': 
            pass
        
        # Grayscale
        elif filter_type == 'Grayscale': 
            frame = grayscale_effect(frame)
            
        # Negative
        elif filter_type == 'Negative': 
            frame = negative_effect(frame)
            
        # Black and White
        elif filter_type == 'Black and White': 
            frame = blackWhite_effect(frame)
            
        elif filter_type == 'Sketch': 
            frame = sketch_effect(frame)
            
        elif filter_type == 'Blur': 
            frame = blur_effect(frame)
           
        elif filter_type == 'Edge': 
            frame = edge_effect(frame)
            
        elif filter_type == 'Emboss': 
            frame = emboss_effect(frame)
            
        elif filter_type == 'Sepia': 
            frame = sepia_effect(frame)
            
        elif filter_type == 'Heatmap': 
            frame = heatmap_effect(frame)
            
        # Rotasi
        frame = rotate_image(frame, rotation_angle)
        
        # Tempat kosong untuk menampilkan frame 
        frame_container.image(frame, channels="BGR")
        
if __name__ == "__main__":
    main()
