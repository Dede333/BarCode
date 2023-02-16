# Importation de fonctions de la bibliothéque barcode
from barcode import Code128
from barcode import Code39
from barcode import EAN13
from barcode.writer import ImageWriter

# Exemple de code EAN13 et sauvegarde dans un fichier (résultat)
# Par défaut le format SVG est utilisé
my_code = EAN13('590987612345')
my_code.save("bar_code_svg")

# Idem que ci-dessus, mais passage au format PNG
my_code = EAN13('590987612345', writer=ImageWriter())
my_code.save("bar_code_png")

# Exemple code 39 avec CheckSum
my_code = Code39('123')
my_code.save("bar_code_39_with_checksum_svg")

# Exemple code 39 sans CheckSum
my_code = Code39('123', None, False)
my_code.save("bar_code_39_no_checksum_svg")

# Exemple code 128
my_code = Code128('123')
my_code.save("bar_code_128_svg")