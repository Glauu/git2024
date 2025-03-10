import os

pasta_raiz = '//nas.prodam/smg_cgpatri/CGPATRI_DEAPI_ACERVO_PLANTAS/GEORREFERENCIAMENTO/PLANTAS DGPI GEOREFERENCIADAS/'

for i in os.listdir(pasta_raiz):
    #se i for uma pasta entrar na pasta e listar outras pastas
    nome_pasta = os.path.join(pasta_raiz, i)
    for j in os.listdir(nome_pasta):
        arquivos_pasta_dgpi = os.path.join(nome_pasta, j)
        
        if os.path.isdir(arquivos_pasta_dgpi):
            subpasta_revisão = os.path.join(arquivos_pasta_dgpi, j)
            print(f"{j} é uma subpasta")
            pass
        else:
            print(f'Pasta Planta {i} " " " " Arquivos: {j}', sep=" ")
#Até aqui código retorna qual é uma subpasta

#Esse bloco de código visava listar as subpastas da árvore de arquivo formando o path com a junção dos nomes de cada subpasta. Para formar o path do shapefile, o arquivo que precisávamos utilizar, era necessário juntar o nome das pastas, para verificar inconsistências.
