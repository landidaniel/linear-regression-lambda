# Linear Regression on AWS Lambda

Projeto educacional de Machine Learning para estimar o salário mensal de desenvolvedores a partir do ano.

O modelo foi treinado com Scikit-learn, salvo com Joblib, empacotado com Docker e preparado para execução na AWS Lambda.

## Tecnologias

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Docker
- AWS Lambda

## Estrutura

```text
linear_regression/
├── app/
│   └── lambda_function.py
├── model/
│   └── linear_salary_model.joblib
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

## Modelo

O modelo utilizado é uma `LinearRegression` do Scikit-learn.

Entrada:

```json
{
  "ano": 2026
}
```

Saída esperada:

```json
{
  "ano": 2026,
  "salario_mensal_brl": 13500.42
}
```

O valor exato depende do modelo treinado.

## Função Lambda

O handler configurado é:

```text
app.lambda_function.lambda_handler
```

O modelo utilizado pela função está em:

```text
model/linear_salary_model.joblib
```

## Executar localmente

Crie e ative o ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Teste a função:

```bash
python -c 'from app.lambda_function import lambda_handler; print(lambda_handler({"ano": 2026}, None))'
```

## Executar com Docker

Construa a imagem:

```bash
docker build -t linear-salary-lambda .
```

Execute o container:

```bash
docker run --rm -p 9000:8080 linear-salary-lambda
```

Em outro Terminal, teste:

```bash
curl -XPOST \
  "http://localhost:9000/2015-03-31/functions/function/invocations" \
  -d '{"ano": 2026}'
```

## Deploy

Fluxo utilizado:

```text
Modelo Joblib
      ↓
Docker
      ↓
Amazon ECR
      ↓
AWS Lambda
      ↓
Function URL ou API Gateway
```

O `Dockerfile` utiliza a imagem oficial:

```text
public.ecr.aws/lambda/python:3.12
```

## Observação

Os arquivos utilizados para gerar os dados e treinar o modelo foram removidos da versão final para manter o projeto mais enxuto.

O repositório contém apenas o modelo treinado e os arquivos necessários para sua execução:

```text
app/lambda_function.py
model/linear_salary_model.joblib
```

## Segurança

Não inclua no repositório:

- chaves da AWS;
- senhas;
- tokens;
- arquivos `.env`;
- chaves privadas;
- arquivos `.pem`.

## Autor

Daniel Landi

Projeto desenvolvido para fins educacionais em Machine Learning, Docker, AWS Lambda e computação em nuvem.
