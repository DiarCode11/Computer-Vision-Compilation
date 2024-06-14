import cv2
import numpy as np
from ultralytics import YOLO  # Pastikan Anda memiliki pustaka yang benar untuk YOLO

def segment_strawberries(frame, model_path='model/segment_model.pt'):
    # Muat model YOLO
    model = YOLO(model_path)
    
    # Jalankan inferensi pada frame
    results = model(frame)  # Mengembalikan daftar objek Hasil

    # Buat masker kosong untuk menggambar semua segmentasi
    masker_kombinasi = np.zeros_like(frame, dtype=np.uint8)

    jumlah_deteksi = 0
    
    # Proses masker segmentasi
    for result in results:
        if hasattr(result, 'masks') and result.masks is not None:
            masker = result.masks.data.cpu().numpy()  # Konversi masker ke array numpy

            for mask in masker:
                jumlah_deteksi += 1
                mask = mask.squeeze()  # Hapus entri dimensi tunggal jika ada
                mask = (mask * 255).astype(np.uint8)  # Konversi masker ke gambar biner (0 dan 255)
                
                # Periksa apakah dimensi masker sesuai dengan frame
                if mask.shape != frame.shape[:2]:
                    mask = cv2.resize(mask, (frame.shape[1], frame.shape[0]), interpolation=cv2.INTER_NEAREST)
                
                # Buat masker berwarna untuk overlay
                masker_berwarna = np.zeros_like(frame, dtype=np.uint8)
                masker_berwarna[mask > 0] = (0, 255, 0)  # Atur warna masker (hijau dalam contoh ini)
                
                # Gabungkan masker berwarna dengan masker kombinasi
                masker_kombinasi = cv2.addWeighted(masker_kombinasi, 1, masker_berwarna, 0.5, 0)

    # Gabungkan frame asli dengan masker kombinasi
    frame_segmentasi = cv2.addWeighted(frame, 1, masker_kombinasi, 0.5, 0)
    return frame_segmentasi, jumlah_deteksi
