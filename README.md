
# AI Financial News Analysis

This repository contains an AI-driven project aimed at analyzing financial news headlines and their correlation with stock market movements. It utilizes natural language processing (NLP) techniques, statistical analysis, and visualization to extract insights from financial data and news headlines.

## Project Overview
This project was developed as part of **10 Academy AI Mastery - Week 1 Challenge**. The primary objectives are:

1. **Sentiment Analysis**:
   - Analyze financial news headlines to calculate sentiment scores.
   - Investigate how sentiment affects stock prices.
2. **Stock Market Analysis**:
   - Use financial indicators like SMA, RSI, and MACD to analyze stock trends.
   - Correlate stock movements with sentiment data.
3. **Data Visualization**:
   - Generate charts and plots for financial trends, sentiment analysis, and correlations.
4. **Statistical Analysis**:
   - Perform correlation analysis between sentiment scores and stock returns.

## Features
- **NLP Pipeline**:
  - Tokenize and clean financial news headlines.
  - Compute sentiment scores using libraries like `nltk` and `TextBlob`.
- **Financial Indicators**:
  - Calculate SMA, RSI, MACD, and other key metrics for stock analysis.
- **EDA and Visualization**:
  - Visualize trends in sentiment and stock movements using `matplotlib` and `seaborn`.
- **Integration with CI/CD**:
  - Automated workflows for testing and validation using GitHub Actions.

## Directory Structure
```plaintext
├── data
│   ├── raw
│   │   └── yfinance_data.csv     # Raw financial data
├── notebook
│   ├── correlation_analysis_notebook.ipynb
│   ├── financial_analysis_notebook.ipynb
│   └── stock_news.ipynb
├── scripts
│   ├── data_processing.py       # Data preprocessing functions
│   ├── sentiment_analysis.py    # NLP sentiment analysis
│   └── correlation_analysis.py  # Statistical correlation functions
├── src
│   ├── app.py                  # Main script to run the project
├── test
│   ├── test_data_processing.py  # Unit tests for data processing
│   └── test_sentiment_analysis.py # Unit tests for sentiment analysis
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
```

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/AI-Financial-News-Analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd AI-Financial-News-Analysis
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Run the main script**:
   ```bash
   python src/app.py
   ```
2. **Jupyter Notebooks**:
   - Explore the notebooks in the `notebook/` directory for detailed analyses.

## Results
- Sentiment analysis provides insights into the mood of financial news headlines.
- Stock indicators such as SMA, RSI, and MACD help in identifying trends.
- Correlation analysis reveals relationships between sentiment and stock performance.

## Testing
Run unit tests to validate functionality:
```bash
pytest test/
```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
