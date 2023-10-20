import streamlit as st
import os
import json
from scripts.translation import translate

root_path = os.getcwd()

st.set_page_config(page_title="Bhinneka Translation",
                   page_icon="🦄",
                   layout="wide",
                   initial_sidebar_state="auto")

st.markdown("# Terjemahan Otomatis")
st.sidebar.header("Terjemahan Otomatis")

with st.sidebar:
    model_option = st.selectbox(
        'Choose Models',
        ('IBM1', 'IBM2', 'IBM3'))

# Create a two-column layout.
col1, col2 = st.columns(2)

# Create a drop-down menu in the first column to allow users to select the source language.
source_language = col1.selectbox("Select the source language:", ["Indonesia", "Beaye", "Melayu Ambon",
                                                                 "Melayu Kupang", "Uab Meto", "Makasar",
                                                                 "Soppeng", "Kaili-Rai"])

# Create a text input field in the first column where users can enter the text to be translated.
text_input = col1.text_area("Enter the text to be translated:", height=200)

# Create a drop-down menu in the second column to allow users to select the target language.
target_language = col2.selectbox("Select the target language:", ["Indonesia", "Beaye", "Melayu Ambon",
                                                                 "Melayu Kupang", "Uab Meto", "Makasar",
                                                                 "Soppeng", "Kaili-Rai"])

# Create a button to translate the text.
translate_button = col1.button("Translate")

# Translate the text if the button is clicked.
translated_text = "Hasil Terjemahan"
if translate_button:
    with open(f"{root_path}/pages/lang_code.json", "r") as fp:
        code = json.load(fp)

    # get language code
    src_code = code[source_language] if source_language in code else ''
    trg_code = code[target_language] if target_language in code else ''

    path_model = f"{root_path}/models/{src_code}/{model_option.lower()}/"
    produced_text, translate_prob = translate(str(text_input), str(path_model), trg_code)
    translated_text = " ".join(produced_text).capitalize()

# Display the translated text in the second column.
col2.text_area("Translation:", translated_text, height=200, disabled=True)

# Display a warning message if the button is clicked but there is no text in the input field.
if translate_button and not text_input:
    st.warning("Please enter text to be translated.")


