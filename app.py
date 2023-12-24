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
    texto = "Estou Tão feliz!"
    resultado_sentimento = analyze_sentiment(texto)

    print(f'Texto: {texto}')
    print(f'Sentimento: {resultado_sentimento}')
