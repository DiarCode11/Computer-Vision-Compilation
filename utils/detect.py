from ultralytics import YOLO
import numpy as np
import cv2

def detect_strawberries(frame, model_path='model/obj_detection_model.pt'):
    # Load a model
    model = YOLO(model_path)  # pretrained YOLOv8n model

    # Run batched inference on a list of images
    results = model(frame)  # return a list of Results objects

    # Process results list
    
    for result in results:
        boxes = result.boxes.data  # Ambil koordinat bounding box dari hasil deteksi
        
        # Loop melalui setiap kotak pembatas dan gambar kotak pembatas pada gambar
        for box in boxes:
            x1, y1, x2, y2, probs, label = box.tolist()  # Konversi tensor menjadi daftar koordinat
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # Konversi ke integer
            
            # Gambar kotak pembatas pada gambar
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            
    return frame
        
        
        
        
        # print(result.boxes.data.tolist())
        

        # boxes = result.boxes  # Boxes object for bounding box outputs
        # for box in boxes:
        #     x1, y1, x2, y2 = box  # extract coordinates of the bounding box
        #     cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)  # Draw rectangle on the original image



    # # Process results list
    # for result in results:
    #     boxes = result.boxes  # Boxes object for bounding box outputs
    #     masks = result.masks  # Masks object for segmentation masks outputs
    #     keypoints = result.keypoints  # Keypoints object for pose outputs
    #     probs = result.probs  # Probs object for classification outputs
    #     obb = result.obb  # Oriented boxes object for OBB outputs
        
   