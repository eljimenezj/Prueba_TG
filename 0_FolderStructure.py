# -*- coding: utf-8 -*-
"""
Prueba Trascender Global

Script para separar las imagenes y organizarlas en carpetas de acuerdo a su 
label, esto respectivamente para train, validation y test
@author: Edgar Leandro Jimenez eljimenezj@gmail.com
"""

import os, shutil

# Debe redirigir la ruta en el lugar donde tiene las iamgenes de la prueba

os.chdir("D:\\Users\\edgarjj\\Desktop\\Prueba Trascender Global\\64x64_SIGNS")

for folder_source in os.listdir():
    path = os.path.join(os.getcwd(), folder_source)
    
    for f in os.listdir(folder_source):
        folderName = f[0]
        h = os.path.join(path,folderName)
        
        if not os.path.exists(h):
            os.mkdir(h)            
            shutil.copy(os.path.join(folder_source, f), h)
        else:
            shutil.copy(os.path.join(folder_source,f), h)