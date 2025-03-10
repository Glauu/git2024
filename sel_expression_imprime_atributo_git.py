from qgis.core import QgsProject, QgsFeature, QgsFeatureRequest
 
# Nome das camadas
layer_assinalacao_name = 'assinalacao'
layer_documento_name = 'documento'
 
# Nome dos campos
field_assinalacao = 'sq'
field_documento = 'sq'

layer_assinalacao = QgsProject.instance().mapLayersByName(layer_assinalacao_name)[0]
layer_documento = QgsProject.instance().mapLayersByName(layer_documento_name)[0]

expression = "'sq' IS NOT NULL"
request = QgsFeatureRequest()
request.setFilterExpression(expression)

print(expression)

for i in layer_documento.getFeatures(request):
   print(i.attributes()[18])
   
   
   #Bloco de código para pesquisar camadas no projeto, filtrar um campo por expressão e imprimir o conteúdo desse campo.
   Feito a partir do estudo da documentação do qgis.
