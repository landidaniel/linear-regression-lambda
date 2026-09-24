import json
import os
import joblib
import pandas as pd


MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "model",
    "linear_salary_model.joblib",
)

# Carrega o modelo quando o ambiente da Lambda é iniciado.
model = joblib.load(MODEL_PATH)


def lambda_handler(event, context):
    try:
        # O evento inteiro pode ser o corpo da requisição.
        body = event

        # Function URL e API Gateway normalmente enviam
        # o JSON dentro da propriedade "body".
        if isinstance(event, dict) and "body" in event:
            body = event["body"]

            if isinstance(body, str):
                body = json.loads(body)

        ano = int(body["ano"])

        X = pd.DataFrame({
            "ano": [ano],
        })

        prediction = float(model.predict(X)[0])

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
            },
            "body": json.dumps({
                "ano": ano,
                "salario_mensal_brl": round(prediction, 2),
            }),
        }

    except KeyError:
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json",
            },
            "body": json.dumps({
                "erro": "O campo 'ano' é obrigatório.",
            }),
        }

    except (TypeError, ValueError):
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json",
            },
            "body": json.dumps({
                "erro": "O campo 'ano' deve ser um número inteiro.",
            }),
        }

    except json.JSONDecodeError:
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json",
            },
            "body": json.dumps({
                "erro": "O corpo da requisição não contém um JSON válido.",
            }),
        }

    except Exception as error:
        print(f"Erro interno: {error}")

        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
            },
            "body": json.dumps({
                "erro": "Erro interno ao realizar a previsão.",
            }),
        }