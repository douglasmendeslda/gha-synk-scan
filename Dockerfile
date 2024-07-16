# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Instale o Node.js
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g snyk

# Instale dependências Python
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copie o código da ação para o contêiner
COPY . /app
WORKDIR /app

# Comando para verificar arquivos Terraform
CMD ["python", "scripts/check_terraform_files.py"]
