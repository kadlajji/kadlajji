import pandas as pd
from nltk import tokenize
import nltk
nltk.download('punkt')
import spacy
import pickle
import streamlit as st
from pickle import load

afinn = pd.read_csv('C:\\Users\\kkdk0001\\Desktop\\DA\\DS\\Project 2 (P170) -- Hotel Rating Classification\\Afinn.csv',sep = ',',encoding = 'latin-1')

affinity_score = afinn.set_index('word')['value'].to_dict()

st.title('Project 2 (P170) -- Hotel Rating Classification')
st.subheader('Hotel Rating Classification')
st.sidebar.header('User Input')

nlp = spacy.load('en_core_web_sm')
sentiment_lexicon = affinity_score

def calculate_sentiment(text: str =None):
    sent_score = 0
    if text:
        sentence =nlp(text)
        for word in sentence:
            sent_score += sentiment_lexicon.get(word.lemma_,0)
    return sent_score
    
def main():
    
    text = st.sidebar.text_area('Input Review','Type here')
    
    sent = calculate_sentiment(text)
    
    if sent >= 10:
        new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">Positive Review</p>'
        st.markdown(new_title, unsafe_allow_html=True)
    elif sent >= 0:
        new_title = '<p style="font-family:sans-serif; color:Blue; font-size: 42px;">Neutral Review</p>'
        st.markdown(new_title, unsafe_allow_html=True)
    elif sent < 0:  
        new_title = '<p style="font-family:sans-serif; color:Red; font-size: 42px;">Negative Review</p>'
        st.markdown(new_title, unsafe_allow_html=True)
    
    st.markdown(sent)
    st.markdown(text)


if __name__ == '__main__':
  main()
    
    
    
    