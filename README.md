
# 🛠 Oficina LERE - Sistema de Gerenciamento de Clientes

Sistema web desenvolvido com Django para gerenciar clientes de uma oficina mecânica. Permite o cadastro, visualização, edição e remoção de informações dos clientes, além de manter um histórico de serviços executados.

---

## 🚀 Por que esse projeto?

Este projeto foi criado com o objetivo de praticar e consolidar meus conhecimentos em desenvolvimento backend com Django, especialmente no uso de:

- Operações CRUD com banco de dados
- Autenticação de usuários
- Organização de views e templates
- Estruturação de um sistema web funcional

---

## ⚙️ Como rodar o projeto

### 🔹 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/oficina-lere.git
cd oficina-lere
```

### 🔹 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 🔹 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 🔹 4. Rode as migrações

```bash
python manage.py migrate
```

### 🔹 5. Crie um superusuário

```bash
python manage.py createsuperuser
```

### 🔹 6. Inicie o servidor

```bash
python manage.py runserver
```

### 🔹 7. Acesse o sistema

```bash
http://127.0.0.1:8000/
```

---

## 🛠 Tecnologias utilizadas

- Python
- Django
- HTML/CSS (usando Django Templates)
- SQLite (banco padrão, facilmente substituível por PostgreSQL)

---

## 📌 Funcionalidades principais

- Autenticação de usuários
- Cadastro de clientes
- Edição, visualização e exclusão de dados
- Listagem organizada de clientes
- Interface simples e objetiva

