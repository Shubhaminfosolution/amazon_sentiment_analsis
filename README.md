# Amazon Sentiment Analysis Using NLP and Flask

## Project Overview
This project analyzes the sentiment of Amazon product reviews using Natural Language Processing (NLP). It processes a dataset of Amazon reviews, cleans the text, applies sentiment analysis, and provides real-time sentiment predictions through a Flask web application. The model classifies reviews as positive or negative based on the text content.

## Features
- Sentiment analysis on **568,454 Amazon product reviews**.
- Real-time sentiment prediction using Flask web interface.
- Data preprocessing including text cleaning, tokenization, and stopword removal using **nltk**.
- Visualization of sentiment trends using **matplotlib** and **seaborn**.
- Model deployment via Flask for easy access to predictions.

## Technologies Used
- **Python**: Core programming language for building the model and processing data.
- **Flask**: Web framework for creating the user interface and handling real-time predictions.
- **Pandas**: Data manipulation and cleaning.
- **nltk**: Natural Language Processing for sentiment classification.
- **matplotlib**, **seaborn**: Data visualization tools to create insightful charts and graphs.

## How to Run the Project

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Shubhaminfosolution/amazon_sentiment_analysis.git
    cd amazon_sentiment_analysis
    ```

2. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Flask application**:
    ```bash
    python app.py
    ```

4. **Open the web application**:
    - Access the app via `http://127.0.0.1:5000/` in your browser.
    - Enter the review text to get real-time sentiment analysis.

## Dataset
The dataset used contains **568,454 Amazon product reviews**. The CSV file includes columns for the review text, rating, and the corresponding sentiment (positive or negative).

## Results
- The model effectively classifies sentiment with a high accuracy, based on text content.
- Real-time sentiment analysis via the Flask app provides instant predictions for user input.
- Visualizations highlight the distribution of positive and negative reviews.

## Future Improvements
- Improve the model accuracy by experimenting with advanced NLP models like BERT or transformers.
- Extend the web app functionality to allow bulk uploads of reviews for batch processing.
- Add multi-class sentiment analysis to capture neutral sentiments.

## Contributing
Feel free to contribute to this project by submitting pull requests. For major changes, please open an issue to discuss what you would like to change.
