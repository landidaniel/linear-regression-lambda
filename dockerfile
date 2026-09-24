FROM public.ecr.aws/lambda/python:3.12

COPY requirements.txt ${LAMBDA_TASK_ROOT}/

RUN pip install --no-cache-dir \
    -r ${LAMBDA_TASK_ROOT}/requirements.txt \
    --target ${LAMBDA_TASK_ROOT}

COPY app/ ${LAMBDA_TASK_ROOT}/app/
COPY model/ ${LAMBDA_TASK_ROOT}/model/

CMD ["app.lambda_function.lambda_handler"]
