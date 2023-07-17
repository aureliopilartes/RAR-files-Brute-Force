# Aurelios Pilartes 

from pyunpack import Archive

def descompactar_arquivo_rar(caminho_arquivo_rar, destino, lista_senhas=None):
    try:
        with Archive(caminho_arquivo_rar) as arquivo_rar:
            if lista_senhas:
                for senha in lista_senhas:
                    try:
                        arquivo_rar.extractall(destino, password=senha)
                        print(f"Arquivo descompactado com sucesso! Senha: {senha}")
                        return True
                    except Exception as e:
                        pass
                print("Nenhuma senha válida encontrada na lista.")
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
lista_senhas = ['senha1', 'senha2', 'senha3']  # Adicione aqui as senhas que deseja testar

descompactar_arquivo_rar(caminho_arquivo_rar, destino, lista_senhas)
