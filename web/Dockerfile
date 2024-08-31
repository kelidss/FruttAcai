# Use a imagem oficial do Nginx como base
FROM nginx:1.27

# Copie o arquivo de configuração personalizado do Nginx para o contêiner
# Supondo que você tenha um arquivo nginx.conf na mesma pasta do Dockerfile
COPY nginx.conf /etc/nginx/nginx.conf

# Copie o conteúdo do site para o diretório padrão do Nginx
# Supondo que você tenha uma pasta chamada html na mesma pasta do Dockerfile
COPY html/ /usr/share/nginx/html

# Exponha a porta 80 para acesso externo
EXPOSE 80

# Inicie o Nginx quando o contêiner for iniciado
CMD ["nginx", "-g", "daemon off;"]
