# get the path to the shapefile 
layer = "S:/pasta/QGIS/Plantas/pasta/camada_final.shp"

# The format is:
# vlayer = QgsVectorLayer(data_source, layer_name, provider_name)

vlayer = QgsVectorLayer(layer, "camada_final", "ogr")
if not vlayer.isValid():
    print("Layer failed to load!")
else:
    for feature in vlayer.getFeatures():
        print(feature.attributes()[1])
        
        #Bloco de código que retorna a lista completa de atributo da camada, ou o atributo selecionado pelo índice. Parte dos Estudos da documentação do Qgis.
