# Alura Space Django

## Para executar o projeto

Instalar o virtualenv
```bash
sudo apt install python3-virtualenv
```

Criar um ambiente virtual (Linux/MacOS)
```bash
virtualenv venv
```
ou
```bash
virtualenv -p python3 venv
```

Criar um ambiente virtual (Windows)
```bash
python -m virtualenv venv
```

Ativar o ambiente virtual venv (Linux/MacOS)
```bash
. venv/bin/activate
```
ou
```bash
source venv/bin/activate
```

Ativar o ambiente virtual venv (Windows)
```bash
venv/Scripts/activate
```

Atualizar o pip
```bash
pip install --upgrade pip
```

Para executar o servidor e o projeto Django
```bash
python manage.py runserver
```

## Para Criar um novo projeto Django

Para instalar o Django se ele não estiver no arquivo `requirements.txt`
```bash
pip install django
```
ou
```bash
pip install django==4.1
```

Depois de instalar uma nova biblioteca exporte novamente as bibliotecas usadas para o arquivo `requirements.txt`
```bash
pip freeze > requirements.txt
```

Para ver as opções do Django
```bash
django-admin help
```

Para criar um novo projeto Django
```bash
django-admin startproject setup .
```
