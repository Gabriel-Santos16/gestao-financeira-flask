# gestao-financeira-flask
Site simples feito com flask para organizar finanças 


## tecnologias usadas 
- [Python 3](https://www.python.org/)
- [flask](https://flask.palletsprojects.com/)
- [flask_sqlachemy](https://flask-sqlalchemy.readthedocs.io/)
- [flask_wtf](https://flask-wtf.readthedocs.io/)
- [flask_login](https://pypi.org/project/Flask-Login/)


## estrutura do projeto

   gestao-financeira-flask
    |
    ├── models/
    ├── modulos/
    │ 	├── auth/
    │ 	├── templates/
    │ 	│ 	├── static/
    │ 	│ 	├── auth.py
    │ 	│ 	└── rotas.py
    │    	│ 
    │ 	├── main/
    │ 	│ 	├── templates/
    │ 	│ 	├── static/
    │ 	│ 	├── main.py
    │ 	│ 	├── formulario.py
    │ 	│ 	└── rotas.py
    │       │   
    │ 	└── user/
    │  	   ├── templates/
    │ 	   ├── static/
    │ 	   ├── user.py
    │ 	   ├── formulario.py
    │ 	   └── rotas.py
    │ 
    ├── app.py
    ├── config.p
    ├── extensions.py
    ├── requirements.txt
    └── README.md


## funcionalidades

	Modelos de tabela com sqlalchemy

	CRUD completo

	Criação automatica do banco de dados

	Relacionamento com tabela de usuarios,transacoes e  categorias	

	Modelos de formulario com flask_wtf

	Sistema de login e cadastro de usuarios com flask login
   
	Uso de I.A para estilização de paginas
	
	
## como rodar o projeto localmente 

- Clone o repositório
	git clone https://github.com/seu-usuario/gestao-financeira-flask.git
- NA pasta do projeto 

	- Crie e ative o ambiente virtual
		python -m venv .venv
	 	Windows:
			.venv\Scripts\activate
 		Linux/Mac:
			source .venv/bin/activate

	- Instale as dependências
		pip install -r requirements.txt

	- crie arquivo .env com: 
		DATABASE_URL='sqlite:///database.db'
		SECRET_KEY='sua-chave-secreta'

	- Execute o projeto
		python app.py
