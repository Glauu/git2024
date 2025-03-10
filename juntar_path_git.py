import os
import qgis

project = QgsProject.instance()
#camada_dgpi_1 = qgis.core.QgsProject()- cria um novo projeto qgis
pasta_raiz = '//pasta/pasta/ACERVO_PLANTAS/GEORREFERENCIAMENTO/PLANTAS DGPI GEOREFERENCIADAS'
for nome_pasta_1 in os.listdir(pasta_raiz):
    nome_pasta_2 = os.path.join(nome_pasta_1 + '.shp')
    print(nome_pasta_2)
    pasta_dgpi = os.path.join(pasta_raiz, nome_pasta)
    print(pasta_dgpi)
    if os.path.isdir(pasta_dgpi):
        dgpi_shapefile = os.path.join(pasta_raiz, nome_pasta_1 + nome_pasta_2)
        print(dgpi_shapefile)
        layer = qgis.core.QgsVectorLayer(dgpi_shapefile, nome_pasta, 'ogr')
        project.addMapLayer(layer)
qgis.utils.iface.mapCanvas().refreshAllLayers()

#Essa foi uma das tentativas de enviar em massa arquivos shp ao qgis para criar uma nova camada vetorial, baseando-se na formação do path dos arquivos pegando o nome das pastas para criá-los, considerado que o nome das pastas individualizadas de shapefile era igual ao das subpastas. Porém não foi possível concluir a tarefa, pois existiam versões de cada shapefile que representavam versões alteradas das plantas e nesse momento foi considerada só a existência de uma pasta raiz (do shapefile) e uma subpasta para cada planta, mas o número de versões do mesmo shapefile era variável e isso mudaria o path dos arquivos.shp.
