
# FastAPI-products

## Descrição
Este é um exemplo de aplicação FastAPI para listagem e inserção de produtos, utilizando um simples banco de dados em memória representado por um arquivo JSON. Este projeto serve como uma demonstração prática de como utilizar FastAPI para criar APIs REST simples.

## Funcionalidades
- **Listagem de Produtos**: Permite ao usuário obter uma lista de todos os produtos armazenados no banco de dados.
- **Inserção de Produtos**: Permite ao usuário adicionar novos produtos ao banco de dados.

## Tecnologias Utilizadas
- FastAPI
- Pydantic
- Uvicorn

## Instalação e Execução

### Pré-requisitos
- Python 3.6+
- pip

### Configuração do Ambiente
```bash
python -m venv venv
source venv/bin/activate  # Para Windows use `venv\Scripts\activate`
```

### Instalação de Dependências
```bash
pip install -r requirements.txt
```

### Execução
```bash
uvicorn main:app --reload
```

## Uso

Após iniciar o servidor, você pode acessar a documentação interativa da API em `http://127.0.0.1:8000/docs` onde você pode testar as funcionalidades da API diretamente pelo navegador.

### Exemplos de Chamadas de API

- **Obter Produtos**:
  ```bash
  curl -X 'GET' \
    'http://127.0.0.1:8000/products' \
    -H 'accept: application/json'
  ```

- **Adicionar Produto**:
  ```bash
  curl -X 'POST' \
    'http://127.0.0.1:8000/products' \
    -H 'Content-Type: application/json' \
    -d '{
    "name": "Novo Produto",
    "price": 1234.56
  }'
  ```

