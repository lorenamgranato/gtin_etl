# GTIN ETL

Processo ETL de validação de GTINs coletados no mercado e agregação de informações.

### Regras de Negócio
1. Validação de GTIN existente através da identificação do endereço do fabricante (arquivo [gs1.ls](inputs/gs1.ls))

### Requisitos de instalação
- `Git`
- `Python`

### Execução do código
- Acesse o diretório desejado no seu computador via terminal e clone o projeto:  
`git clone https://github.com/lorenapnmarcon/gtin_etl`
- Instale uma máquina virtual (venv) para executar o projeto:  
`python -m venv env`
- Ative sua venv:   
`env\Scripts\activate.bat`
- Instale as dependências  
`pip install -r requirements.txt`
- Execute o código  
`python main.py`
- Desative sua venv  
`deactivate`

### Autores
- [**Lorena Marçon**](https://github.com/lorenapnmarcon)
