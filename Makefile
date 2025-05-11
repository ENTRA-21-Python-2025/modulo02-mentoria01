# Makefile para Windows

# Comando para executar o programa
run:
	python exemplo_input_output.py

# Comando para limpar arquivos temporários Python
clean:
	del /Q *.pyc
	del /Q __pycache__

# Comando para verificar a versão do Python
version:
	python --version

# Comando para instalar dependências (caso necessário no futuro)
install:
	pip install -r requirements.txt

# Comando para mostrar ajuda
help:
	@echo Comandos disponíveis:
	@echo make run     - Executa o programa
	@echo make clean   - Remove arquivos temporários
	@echo make version - Mostra a versão do Python
	@echo make install - Instala dependências
	@echo make help    - Mostra esta mensagem de ajuda 