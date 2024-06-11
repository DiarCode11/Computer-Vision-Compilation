import cv2
import numpy as np

def horizontal_flip (frame): 
    flipped_frame = cv2.flip(frame, 1)
    return flipped_frame

def vertical_flip (frame): 
    flipped_frame = cv2.flip(frame, 0)
    return flipped_frame

def grayscale_effect (frame): 
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(grayscale_frame, cv2.COLOR_GRAY2RGB)
    return frame

def negative_effect (frame): 
    return 255 - frame
    
def blackWhite_effect (frame): 
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    binary_frame = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY)[1]# Melakukan invert pada gambar biner
    negative_binary_frame = cv2.bitwise_not(binary_frame)
    frame = cv2.cvtColor(negative_binary_frame, cv2.COLOR_GRAY2RGB)
    return frame

def sketch_effect (frame): 
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)# Konversi gambar ke dalam format grayscale
    inverted_frame = cv2.bitwise_not(gray_frame)# Inversi gambar (membuat efek negatif)
    blurred_frame = cv2.GaussianBlur(inverted_frame, (85, 85), 0) # Aplikasikan efek blur pada gambar
    sketched_frame = cv2.divide(gray_frame, 255 - blurred_frame, scale=256)# Menghasilkan efek sketsa dengan menggunakan operasi subtraksi
    frame = cv2.cvtColor(sketched_frame, cv2.COLOR_GRAY2RGB)
    return frame

def blur_effect(frame): 
    frame = cv2.GaussianBlur(frame, (21, 21), 0)
    return frame
    
def edge_effect(frame): 
    # Konversi gambar ke dalam format grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Terapkan operator Sobel pada gambar untuk mendeteksi tepi
    sobel_x = cv2.Sobel(gray_frame, cv2.CV_64F, 1, 0, ksize=5)
    sobel_y = cv2.Sobel(gray_frame, cv2.CV_64F, 0, 1, ksize=5)
    # Gabungkan hasil dari operator Sobel
    edge_frame = cv2.sqrt(cv2.addWeighted(cv2.pow(sobel_x, 2.0), 1.0, cv2.pow(sobel_y, 2.0), 1.0, 0.0))
    # Konversi gambar kembali ke dalam skala 8-bit
    edge_frame = cv2.normalize(edge_frame, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    frame = cv2.cvtColor(edge_frame, cv2.COLOR_GRAY2RGB)
    return frame
    
def emboss_effect(frame): 
    # Kernel filter emboss
    kernel = np.array([[0, -1, -1],
                    [1,  0, -1],
                    [1,  1,  0]])
    # Terapkan filter emboss pada gambar
    frame = cv2.filter2D(frame, -1, kernel)
    return frame

def sepia_effect(frame): 
    # Matriks transformasi warna untuk efek sepia
    sepia_matrix = np.array([[0.393, 0.769, 0.189],
                            [0.349, 0.686, 0.168],
                            [0.272, 0.534, 0.131]])
    # Terapkan transformasi warna untuk efek sepia
    sepia_frame = cv2.transform(frame, sepia_matrix)
    # Penanganan nilai piksel yang melebihi 255
    sepia_frame = np.where(sepia_frame > 255, 255, sepia_frame)
    frame = sepia_frame.astype(np.uint8)
    return frame
    
def heatmap_effect(frame): 
    # Terapkan filter Gaussian untuk memperhalus gambar
    frame = cv2.heatmap = cv2.applyColorMap(frame, cv2.COLORMAP_JET)
    return frame
    
def rotate_image(image, angle):
    image_cv = np.array(image)
    (h, w) = image_cv.shape[:2]
    center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    frame = cv2.warpAffine(image_cv, M, (w, h))
    return frame