import os
import qgis.core

pasta ='S:/CGPATRI_DIPI/cadastro_croquis/Glaucy/analise_vetorial/Plantas'
list_arq = os.listdir(pasta)
for i in list_arq:
    if i.endswith('.shp'):
        layer = qgis.core.QgsVectorLayer(pasta, i, 'ogr')
        print(layer.name())
    else:
        print("Não é um arquivo shp")
        
        #Essa foi uma tentativa de enviar arquivos shp diretamente para o qgis afim de criar uma nova camada vetorial de forma automática e em massa, varrendo a árvore de arquivos em busca dos arquivos .shp.  Essa tentaiva não foi a mais frutífera pois haviam inconsistências na árvore de arquivos que demandaram outra abordagem.
        
    
