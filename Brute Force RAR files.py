from pyunpack import Archive

def carregar_word_list(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            lista_senhas = arquivo.read().splitlines()
            return lista_senhas
    except Exception as e:
        print(f"Erro ao carregar a word list: {e}")
        return []

def descompactar_arquivo_rar(caminho_arquivo_rar, destino, lista_senhas=None):
    try:
        if lista_senhas is None:
            lista_senhas = []  # Se nenhuma word list for fornecida, cria uma lista vazia

        with Archive(caminho_arquivo_rar) as arquivo_rar:
            if lista_senhas:
                for senha in lista_senhas:
                    try:
                        arquivo_rar.extractall(destino, password=senha)
                        print(f"Arquivo descompactado com sucesso! Senha: {senha}")
                        return True
                    except Exception as e:
                        pass
                print("Nenhuma senha válida encontrada na word list.")
                return False
            else:
                arquivo_rar.extractall(destino)
                print("Arquivo descompactado com sucesso (sem senha)!")
                return True
    except Exception as e:
        print(f"Erro ao descompactar o arquivo: {e}")
        return False

# Exemplo de uso:
caminho_arquivo_rar = 'caminho/do/arquivo.rar'
destino = 'caminho/da/pasta_de_destino'
nome_arquivo_word_list = 'caminho/do/arquivo_word_list.txt'

lista_senhas = carregar_word_list(nome_arquivo_word_list)
descompactar_arquivo_rar(caminho_arquivo_rar, destino, lista_senhas)
