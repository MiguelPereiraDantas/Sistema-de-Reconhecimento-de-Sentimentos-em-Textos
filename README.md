# Sistema de Reconhecimento de Sentimentos em Textos

Este é um simples sistema de reconhecimento de sentimentos em textos desenvolvido em Python usando a biblioteca NLTK.

## Pré-requisitos

Certifique-se de ter Python instalado em seu sistema. Você pode instalar as dependências usando o seguinte comando:

```bash
pip install nltk
```

## Configuração

Antes de executar o aplicativo, você precisa baixar os recursos necessários do NLTK. Execute o seguinte comando para baixar todos os recursos disponíveis:
```bash
python -m nltk.downloader all
```
## Uso

Você pode utilizar este sistema para analisar o sentimento de diferentes textos. O exemplo abaixo demonstra como usar a função `analyze_sentiment`:
```python
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Baixe todos os recursos disponíveis
nltk.download('all')

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)['compound']

    if sentiment_score >= 0.05:
        return 'Positivo'
    elif sentiment_score <= -0.05:
        return 'Negativo'
    else:
        return 'Neutro'

if __name__ == "__main__":
    # Exemplo de uso
    texto = "Eu amo programar em Python! É tão divertido."
    resultado_sentimento = analyze_sentiment(texto)

    print(f'Texto: {texto}')
    print(f'Sentimento: {resultado_sentimento}')
```

Certifique-se de ajustar o `texto` na variável texto conforme necessário.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas ou enviar pull requests.

## Licença

Este projeto está licenciado sob a Licença MIT