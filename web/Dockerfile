# Use a imagem oficial do Nginx como base
FROM nginx:1.27

COPY build/ /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
