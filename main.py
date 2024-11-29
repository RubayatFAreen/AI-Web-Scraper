import streamlit as st
from scrape import scrape_website, split_dom_content, clean_body_content, extract_body_content
from parse import parse_with_ollama

st.title("AI Web Scraper")
url = st.text_input("Enter a website URL:")

if st.button("Scrape Site"):
    st.write("Scraping the website...")
    try:
        result = scrape_website(url)
        body_content = extract_body_content(result)
        products = clean_body_content(body_content)
        st.session_state.products = products
        st.success("Scrape complete!")

        with st.expander("View Products"):
            st.write(products)
    except Exception as e:
        st.error(f"Error: {e}")

if "products" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")
            try:
                dom_chunks = split_dom_content(st.session_state.products)
                result = parse_with_ollama(dom_chunks, parse_description)
                st.write(result)
            except Exception as e:
                st.error(f"Error: {e}")
