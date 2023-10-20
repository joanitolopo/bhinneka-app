import streamlit as st
import os
import json
from scripts.util import get_parallel_data
from urllib.error import URLError

st.set_page_config(page_title="DataFrame Demo", page_icon="📊")

st.markdown("# DataFrame Demo")
st.sidebar.header("DataFrame Demo")
st.write(
    """This demo shows how to use and explore Bhinneka Parallel Korpus"""
)

with open(f"{os.getcwd()}/pages/lang_code.json", "r") as fp:
    code = json.load(fp)

try:
    df = get_parallel_data()
    languages = st.multiselect(
        "Choose languages", ["Indonesia", "English", "Melayu Ambon",
                             "Beaye", "Melayu Kupang", "Uab Meto", "Makasar"]
    )

    if not languages:
        st.error("Please select at least one language.")
    else:
        map_codes = [code[lang] if lang in code else '' for lang in languages]
        data = df[map_codes]
        st.dataframe(data)

except URLError as e:
    st.error(
        """
        **This demo requires internet access.**
        Connection error: %s
    """
        % e.reason
    )
