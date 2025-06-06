# Lambda - Saudação e Recomendação Musical (Estilo Grunge)

## 📋 Descrição

Esta função AWS Lambda foi desenvolvida para gerar uma saudação personalizada de acordo com o horário do dia (bom dia, boa tarde ou boa noite) e recomendar aleatoriamente uma música do gênero **grunge**. A função pode ser usada em aplicações como assistentes virtuais, APIs de entretenimento, bots de chat ou sistemas que respondem com mensagens dinâmicas e criativas.

---

## ✅ Funcionalidade

A função recebe um nome (opcional) como entrada. Com base no horário atual da execução (fuso UTC), ela determina o período do dia e retorna uma saudação acompanhada de uma sugestão de música grunge.

---

## 🧪 Exemplos de Entrada e Saída

### 🔹 Exemplo 1 – Entrada com nome

**Input (event):**
```json
{
  "nome": "Pedro"
}

### 🔹 Exemplo 2 – Entrada sem nome
{
  "nome": ""
}

### 🔹 Exemplo 1 – Saída com nome
{
    "mensagem": "Boa noite, Pedro! Que tal ouvir: 'Jeremy - Pearl Jam'?"
}

### 🔹 Exemplo 2 – Saída sem nome
{
    "mensagem": "Boa noite, ! Que tal ouvir: 'Fell on Black Days - Soundgarden'?"
}
