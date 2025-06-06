# Função Lambda: Saudação Inteligente com Recomendação de Música Grunge

## Descrição
Esta função AWS Lambda recebe um nome como entrada e retorna uma saudação personalizada baseada no horário do dia (manhã, tarde ou noite), junto com a recomendação aleatória de uma música grunge clássica.

A função está preparada para ser acionada diretamente ou via API Gateway, tratando adequadamente o evento recebido.

---

## Entrada (Input)

- JSON contendo o campo opcional `nome` (string).

Exemplo de corpo JSON esperado:

```json
{
  "nome": "Pedro"
}
