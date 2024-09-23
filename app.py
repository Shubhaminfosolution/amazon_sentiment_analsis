from flask import Flask, render_template, request
import pickle
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

app = Flask(__name__)

MODEL = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)


def polarity_scores_roberta(text):
    encoded_text = tokenizer(text, return_tensors='pt')
    output = model(**encoded_text)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    scores_dict = {
        'negative': scores[0],
        'neutral': scores[1],
        'positive': scores[2]
    }
    return scores_dict


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text_input = request.form['text_input']

        try:
          
            sentiment_scores = polarity_scores_roberta(text_input)

           
            sentiment = max(sentiment_scores, key=sentiment_scores.get)

            
            return render_template('index.html', prediction=f"Sentiment: {sentiment}")
        
        except Exception as e:
        
            return render_template('index.html', prediction=f"Error in prediction: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
