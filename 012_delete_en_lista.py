"""
De esta lista, elimina los colores 'azul', 'marrón', 'negro' y 'rosa'. 
Debes utilizar al menos una vez las posiciones negativas para eliminar un color. 
Después, imprime la lista para ver los colores que se han eliminado.

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
"""

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']

#  eliminar 'azul'

del colores[1]
#  eliminar 'marrón'
del colores[4]

#  eliminar 'negro' 
del colores[6]

#  eliminar 'rosa'
del colores[-3]

print(colores)

