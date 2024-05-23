import os


#Alterar o diretório base
diretorio_base = 'C:/GeoCoder/Clientes/Nicholas/Teste'

#Adicionar os diretórios a serem gerados em uma lista
fazendas = ['Campo Alegre', 'Santa Leonor','São Miguel 1', 'São Miguel 2', 'Teste', 'Teste2']

#Adicionar os subdiretórios a ser adicionados em cada diretório em uma lista
suddiretorios = ['dwg', 'entregas', 'dados de campo', 'dados de projeto']


for diretorio in fazendas:

	# Criar pastas das fazendas
	diretorio_final = os.path.join(diretorio_base, diretorio)

	# Verificar a existencia do diretório, e criá-lo
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


		# Entrar somente na pasta 'entregas' de cada diretório criado
		if subdiretorio_final.endswith('entregas'):
			# Alterar o diretório para '/entregas'
			os.chdir(subdiretorio_final)

			# Dentro de 'entregas', criar a pasta 'dji'
			subdiretorio_final_dji = os.path.join(subdiretorio_final, 'dji') 
			if not os.path.exists(subdiretorio_final_dji):
				os.mkdir(subdiretorio_final_dji)

			# alterar o diretório para '/entregas/dji'
			os.chdir(subdiretorio_final_dji)

			# Dentro do diretório 'entregas/dji', criar a pasta 'shapefile'
			subdiretorio_final_shapefile = os.path.join(subdiretorio_final, 'dji', 'shapefile')
			if not os.path.exists(subdiretorio_final_shapefile):
				os.mkdir(subdiretorio_final_shapefile)
				