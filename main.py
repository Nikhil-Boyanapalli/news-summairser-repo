import tkinter as tk
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from textblob import TextBlob
from newspaper import Article

def summarise():
    url = utext.get('1.0', 'end').strip()
    article = Article(url)

    article.download()
    article.parse()

    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')
    
    title.delete('1.0','end')
    title.insert('1.0',article.title)

    if article.authors:
        extracted_authors = ', '.join(article.authors)
    else:
        # Try to find "By: Author Name" in the article text
        match = re.search(r"(?i)\bby:\s*(.*)", article.text)
        extracted_authors = match.group(1).strip() if match else "Author(s) not found"
        
    author.delete('1.0','end')
    author.insert('1.0',article.author)

    publication.delete('1.0','end')
    publication.insert('1.0',article.publication)

    summary.delete('1.0','end')
    summary.insert('1.0',article.summary)
    
    analysis = TextBlob(article.text)
    sentiment.delete('1.0' , 'end')
    sentiment.insert('1.0', f'Polarity: {analysis.polarityt}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity<0 else "neutral"}')    



    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')
    
    
    

root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')

tlabel = tk.Label(root, text = "Title")
tlabel.pack()

title  = tk.Text(root, height=1, width=140)
title.config(state = 'disabled', bg = '#dddddd')
title.pack()

alabel = tk.Label(root, text = "Author")
alabel.pack()

author  = tk.Text(root, height=1, width=140)
author.config(state = 'disabled', bg = '#dddddd')
author.pack()

plabel = tk.Label(root, text = "Publication Date")
plabel.pack()

publication  = tk.Text(root, height=1, width=140)
publication.config(state = 'disabled', bg = '#dddddd')
publication.pack()

slabel = tk.Label(root, text = "Summary")
slabel.pack()

summary  = tk.Text(root, height=20, width=140)
summary.config(state = 'disabled', bg = '#dddddd')
summary.pack()

selabel = tk.Label(root, text = "Sentiment Analysis")
selabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg = '#dddddd')
sentiment.pack()

ulabel = tk.Label(root, text = "URL")
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

btn = tk.Button(root, text="Summarize", command = summarise)
btn.pack()

root.mainloop()