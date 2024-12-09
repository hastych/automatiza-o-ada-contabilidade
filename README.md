
# Automação de Fluxo da Ada Contabilidade

Este projeto automatiza o envio, processamento e registro de arquivos no fluxo da Ada Contabilidade utilizando AWS.

## Tecnologias
- Python
- AWS S3, SNS, SQS, Lambda, Elasticache
- Boto3

## Como Usar
1. Configure o `config.json`.
2. Execute `infra/create_resources.py` para criar os recursos.
3. Execute `app/upload_to_s3.py` para enviar arquivos.
4. Execute `app/process_message.py` para processar mensagens e registrar no banco.

## Autor
Gustavo Lira
