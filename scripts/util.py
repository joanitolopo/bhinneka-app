import streamlit as st
import pandas as pd
import spacy
import string

init_tok = spacy.blank('id')


def tokenize(text):
    tokens = [token.text.lower() for token in init_tok.tokenizer(text) if token.text not in string.punctuation]
    return tokens


@st.cache_data
def get_parallel_data():
    parallel_data = "https://raw.githubusercontent.com/joanitolopo/bhinneka-korpus/main/parallel.xlsx"
    dataset = pd.read_excel(parallel_data, index_col=0)
    dataset = dataset.reset_index().drop(columns=["Id"], axis=1)
    return dataset
