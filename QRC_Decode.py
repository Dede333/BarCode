import cv2

# Lecture du fichier image du QR code
img = cv2.imread("MonQRCode1.png")

# Initialise la fonction QRCode detector de cv2
detector = cv2.QRCodeDetector()

# Détection et décodage du QRCode
data, bbox, straight_qrcode = detector.detectAndDecode(img)

# Si il y a un QRCode dans l'image
if bbox is not None:
    print(f"Données du QRCode:\n{data}")
    # Affiche l'image avec les lignes
    # taille de la zone du QRCode
    n_lines = len(bbox)
    bbox = bbox.astype(int)
    for i in range(n_lines):
        # draw all lines
        point1 = tuple(bbox[i][0])
        point2 = tuple(bbox[(i+1) % n_lines][0])
        # open_cv utilise la convention de couleur BGR (bleu, vert, rouge) !
        cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)

# Affichage du résultat
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
