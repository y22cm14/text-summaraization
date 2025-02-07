import re
from collections import defaultdict

def simple_tokenize(text):
    sentences = re.split(r'(?<=[.!?]) +', text)
    return sentences

def calculate_word_frequencies(words):
    word_frequencies = defaultdict(int)
    for word in words:
        word_frequencies[word] += 1
    return word_frequencies

def score_sentences(sentences, word_frequencies):
    sentence_scores = defaultdict(int)
    for sentence in sentences:
        for word in re.findall(r'\w+', sentence.lower()):
            if word in word_frequencies:
                sentence_scores[sentence] += word_frequencies[word]
    return sentence_scores

def summarize(text, num_sentences=1):
    """Generates a summary of the text."""
    sentences = simple_tokenize(text)
    words = re.findall(r'\w+', text.lower())
    word_frequencies = calculate_word_frequencies(words)
    sentence_scores = score_sentences(sentences, word_frequencies)
    summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    return ' '.join(summarized_sentences)

if __name__ == "__main__":
    text = input("Enter the text: ")
    summary = summarize(text)
    print("Original Text:\n", text)
    print("\nSummarized Text:\n", summary)