from ultralytics import YOLO
import numpy as np
import cv2

def detect_strawberries(frame, model_path='model/obj_detection_model.pt'):
    # Load a model
    model = YOLO(model_path)  # pretrained YOLOv8n model
    
    # Run batched inference on a list of images
    results = model(frame)  # return a list of Results objects
    
    for result in results:
        boxes = result.boxes.data  # Ambil koordinat bounding box dari hasil deteksi
        
        detection_counts = len(boxes)
        
        # Loop melalui setiap kotak pembatas dan gambar kotak pembatas pada gambar
        for box in boxes:
            x1, y1, x2, y2, probs, label = box.tolist()  # Konversi tensor menjadi daftar koordinat
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # Konversi ke integer
            
            probs = float(probs)  # Konversi probabilitas ke float
            
            # Gambar kotak pembatas pada gambar
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            
            # Tampilkan probabilitas di atas kotak pembatas
            label_text = f'Stroberi matang: {probs:.2f}'
            frame = cv2.putText(frame, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            
    return frame, detection_counts

