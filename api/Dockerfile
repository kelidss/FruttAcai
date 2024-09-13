# Usa uma imagem base com Python
FROM python:3.10.12

# Define o diretorio de trabalho dentro do container
WORKDIR /api

# Copia o arquivo requirements.txt para o diretorio de trabalho
COPY requirements.txt requirements.txt

# Instala as dependencias da aplicacao
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteudo da pasta atual para o diretorio de trabalho
COPY . /api

# Expoe a porta 5000 (a porta padrao que o Flask usa)
EXPOSE 5000

# Define a variavel de ambiente para dizer ao Flask que esta em producao ou debug
# Nao sei se realmente precisa (acredito que nao)
ENV FLASK_ENV=debug

# Define o comando padrao para rodar a aplicacao
CMD ["python", "-u", "main.py"]