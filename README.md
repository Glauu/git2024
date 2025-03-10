# Scripts para tarefas no Sistema SIG Qgis <img src="https://github.com/Glauu/git2024/blob/main/globo_terrestre_emoji.png" width="40" heigth="40" >
Tive sorte de ter a minha primeira oportunidade de programar em meu atual emprego, meus projetos básicos iniciais já foram feitos visando solucionar questões reais no trabalho com geoprocessamento.
Claro que problemas ocorreram, então várias tentativas foram feitas para solucionar os obstáculos pelo caminho e descobrir a melhor forma de realizar o trabalho.
Os códigos a seguir foram desenvolvidos com estudo da Documentão Python, Documentação do Qgis e IA.

## Uma breve descrição de cada um deles:

* **Script** - _busca_shp_envia_qgis_
  
  Foi Desenvolvido para varrer pastas de arquivos e adicionar em massa à uma camada vetorial. Tínhamos um prazo para entregar uma camada vetorial para homologação com mais 1300 polígonos, que estavam armazenados em pastas e subpastas locais.

#### o que faz:

Busca arquivos na pasta que sejam da extensão ".shp" adiciona um a um em uma camada vetorial no qgis, informa os aquivos que não são ".shp"

* **Script** - _localiza_shp_
  
  Esse foi o programa que enviou os shapefiles para a camada após resolver várias questões com as pastas, entre acesso bloqueado, falta de alguns shapefiles, entre outros.
  O estudo da documentação da biblioteca OS também ajudou a enxergar uma opção melhor para fazer isso em vez do conceito "juntar path" mostrado anteriormente.

  #### o que faz:
 
  Localiza de forma mais eficiente o aquivo desejado nas subpastas e envia para o qgis formando camadas individuais, depois foram unidos em uma camada única dentro do qgis.

* **Script** - _entrar_na_pasta_lista_

  Desenvolvido para listar as pastas individualizadas de shapefiles na arvóre de arquivos, excetuando pastas cujo acesso estava bloqueado. 

#### o que faz:

Cria uma lista das pastas acessíveis e bloqueadas. O intuito era passar essa lista para o TI e solicitar o desbloqueio.

* **Script** _listar_pastas_arquivos_subpastas_

  As pastas dos shapefiles tinham subpastas com o mesmo nome, a ideia inicial era formar o path do shapefile. Num primeiro momento presumindo que os nomes eram exatamente iguais essa foi a poposta. Nem sempre o programa tem o nome do que faz, as vezes eu uso um dos porquês de ele estar sendo feito para nomeá-los, mas com o tempo vou melhorando isso.  

#### o que faz:

Pega o nome da pasta e junta com o da subpasta, imprime uma lista com o nome das pastas e subpastas, aí foi possivel verificar que os nomes não eram iguais, pois as vezes os poligonos (arquivos ".shp") possuiam mais de uma versão.

* **Script** _juntar_path_

  Essa foi uma das tentativas de enviar em massa arquivos shp ao qgis para criar uma nova camada vetorial, baseando-se na formação do path dos arquivos, considerando que o nome das pastas individualizadas de shapefile era igual ao das subpastas. Porém não foi possível concluir a tarefa, pois existiam versões de cada shapefile que representavam versões alteradas das plantas e nesse momento foi considerada só a existência de uma pasta raiz (do shapefile) e uma subpasta para cada shapefile, mas o número de versões do mesmo era variável e isso mudaria o path dos arquivos.shp.

#### o que faz:

Junta o nome das pastas formando o path dos shapefiles.
  
 **Script** - _sel_expression_imprime_atributo_git_
 
 Foi desenvolvido para efetuar o preenchimento do campo de uma camada a partir do mesmo campo em outra camada, essa é uma das etapas para encontrar a solução. 

#### o que faz:

Seleciona as camadas no projeto atual, filtra as feições com uma expressão na calculadora de campo, imprime o  conteúdo do campo referenciado pelo índice e mostra como uma lista.

 **Script** - _selecionar_por_espressao_

  Precisávamos buscar em duas camadas de nomes:"Assinalação" e "Documento" um campo específico (campo sq), esses campos em cada camada são representados pelas variáveis "sq_doc" e "sq_ass". Foram selecionadas duas expressões da calculadora de campo do qgis para buscar as feições na camada, as expressões foram usadas separadamente para filtrar as feições da camada vetorial.

#### o que faz:
Seleciona as camadas no projeto atual, filtra as feições com expressões da calculadora de campo, compara os valores dos campos e imprime apenas os que são iguais.



  
