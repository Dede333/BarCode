# Import de la Bibliothèque qrcode
import qrcode

# La donnée à encoder ici une simple URL
data = 'https://github.com/dede333'

# Encodage de la donnée avec la fonction make
img = qrcode.make(data)

# Sauvegarde du QRC dans une image
img.save('MonQRCode1.png')