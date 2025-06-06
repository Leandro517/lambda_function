import json
import datetime
import random

def lambda_handler(event, context):
    # Se o evento vier do API Gateway, o corpo fica em event['body'] como string
    if 'body' in event:
        body = json.loads(event['body'])
    else:
        body = event
    
    nome = body.get('nome', 'amigo')
    
    agora = datetime.datetime.utcnow()
    hora = agora.hour
    
    if 5 <= hora < 12:
        saudacao = "Bom dia"
    elif 12 <= hora < 18:
        saudacao = "Boa tarde"
    else:
        saudacao = "Boa noite"
    
    musicas = [
        "Smells Like Teen Spirit - Nirvana",
        "Black Hole Sun - Soundgarden",
        "Alive - Pearl Jam",
        "Man in the Box - Alice In Chains",
        "Heart-Shaped Box - Nirvana",
        "Rooster - Alice In Chains",
        "Plush - Stone Temple Pilots",
        "Jeremy - Pearl Jam",
        "Fell on Black Days - Soundgarden",
        "Would? - Alice In Chains",
        "Interstate Love Song - Stone Temple Pilots",
        "Come As You Are - Nirvana",
        "Even Flow - Pearl Jam",
        "Spoonman - Soundgarden",
        "Daughter - Pearl Jam"
    ]
    
    musica_recomendada = random.choice(musicas)
    
    mensagem = f"{saudacao}, {nome}! Que tal ouvir: '{musica_recomendada}'?"
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'mensagem': mensagem
        })
    }
