# Usa uma imagem base com Python
FROM python:3.10.12

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt requirements.txt

# Instala as dependências da aplicação
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo da pasta atual para o diretório de trabalho
COPY . .

# Expõe a porta 5000 (a porta padrão que o Flask usa)
EXPOSE 5000

# Define a variável de ambiente para dizer ao Flask que está em produção
ENV FLASK_ENV=production

# Define o comando padrão para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]