import os
import qgis.core

pasta ='S:/pasta/pasta/Glaucy/analise_vetorial/Plantas'
list_arq = os.listdir(pasta)
for i in list_arq:
    if i.endswith('.shp'):
        layer = qgis.core.QgsVectorLayer(pasta, i, 'ogr')
        print(layer.name())
    else:
        print("Não é um arquivo shp")
        
        
        Script busca arquivos na pasta que sejam da extensão .shp adiciona um a um em uma camada vetorial no qgis, informa os aquivos que não são .shp
