layer_assinalacao_name = 'assinalacao'
layer_documento_name = 'documento'

layer_assinalacao = QgsProject.instance().mapLayersByName(layer_assinalacao_name)[0]
layer_documento = QgsProject.instance().mapLayersByName(layer_documento_name)[0]


expression = '"sq" IS NOT NULL'
request = QgsFeatureRequest().setFilterExpression(expression)

expression1 = "length('sq') <=7 "
request1 = QgsFeatureRequest()
request1.setFilterExpression(expression1)

for i in layer_documento.getFeatures(request):
    sq_doc = i['sq']
    for j in layer_assinalacao.getFeatures(request1):
        if len(sq_ass)<= 7:
            sq_ass_len7 = sq_ass
            print(sq_ass '/' sq_doc)
        else:
            pass
        break
        
        #Precisávamos buscar em duas camadas de nomes:"Assinalação" e "Documento" um campo específico (campo sq), esses campos em cada camada são representados pelas variáveis "sq_doc" e "sq_ass". Foram selecionadas duas expressões da calculadora de campo do qgis para buscar as feições na camada, as expressões foram usadas separadamente para filtrar as feições da camada vetorial.
