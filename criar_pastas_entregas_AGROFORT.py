import os

diretorio_base = 'C:/GeoCoder/Clientes/Nicholas/Teste'
fazendas = ['Campo Alegre', 'Santa Leonor','São Miguel 1', 'São Miguel 2', 'Teste', 'Teste2']
suddiretorios = ['dwg', 'entregas', 'dados de campo', 'dados de projeto']


for diretorio in fazendas:

	# Criar pastas das fazendas
	diretorio_final = os.path.join(diretorio_base, diretorio)

	if not os.path.exists(diretorio_final):
		os.mkdir(diretorio_final)
	else:
		print(f'Os diretório {diretorio_final} já existe')
	
	# Criar subdiretórios para cada fazenda
	for subdiretorio in suddiretorios:

		subdiretorio_final = os.path.join(diretorio_final, subdiretorio)

		if not os.path.exists(subdiretorio_final):
			os.mkdir(subdiretorio_final)
		else:
			print(f'o Subdiretório {subdiretorio_final} já existe')

		if subdiretorio_final.endswith('entregas'):
			os.chdir(subdiretorio_final)

			subdiretorio_final_dji = os.path.join(subdiretorio_final, 'dji') 
			if not os.path.exists(subdiretorio_final_dji):
				os.mkdir(subdiretorio_final_dji)

			os.chdir(subdiretorio_final_dji)

			subdiretorio_final_shapefile = os.path.join(subdiretorio_final, 'dji', 'shapefile')
			if not os.path.exists(subdiretorio_final_shapefile):
				os.mkdir(subdiretorio_final_shapefile)
				