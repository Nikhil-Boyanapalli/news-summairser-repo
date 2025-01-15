

# News Summarizer Application

A Python-based application that allows users to summarize news articles, extract key information (such as title, author, publication date), and perform sentiment analysis. The application uses the `Tkinter` GUI for a user-friendly interface and integrates various libraries like `Newspaper3k`, `TextBlob`, and `NLTK` to process and analyze articles.

## Features
- **Article Summarization:** Extracts and summarizes key parts of news articles (title, author, publication date, summary).
- **Sentiment Analysis:** Analyzes the sentiment of the article text, categorizing it as positive, negative, or neutral.
- **User-Friendly Interface:** A simple and interactive GUI built with `Tkinter` that allows users to input URLs and view summarized content.
- **Custom Author Extraction:** Automatically extracts the author’s name, even if it is not directly available in the metadata, by searching for patterns like `"By: Author Name"` in the article text.

## Libraries Used
- `Tkinter`: For creating the graphical user interface.
- `Newspaper3k`: To download and parse news articles.
- `TextBlob`: For performing sentiment analysis on the article text.
- `NLTK`: For text processing, including tokenization.

## Setup and Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/news-summarizer.git
   cd news-summarizer
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download additional NLTK resources if required:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('punkt_tab')
   ```

4. Run the application:
   ```bash
   python news_summarizer.py
   ```

## Usage
- Enter a news article URL in the input field.
- Click the **Summarize** button to fetch the article’s details and summary.
- View the title, author, publication date, summary, and sentiment analysis of the article.

## Example

After entering a URL, the GUI will display the following:
- **Title**: "Example Article Title"
- **Author**: "John Doe"
- **Publication Date**: "2025-01-01"
- **Summary**: "This is a summary of the article content..."
- **Sentiment**: "Polarity: 0.2, Sentiment: positive"

## Contributing
Feel free to fork the repository, submit issues, and create pull requests. Contributions are welcome!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Tips:
- **Requirements File:** Make sure to include a `requirements.txt` file with the following content:
  ```text
  nltk
  newspaper3k
  textblob
  tk
  ```
- **Adjust the URL in the cloning command** to match your GitHub username or organization.

