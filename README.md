# AI Web Scraper

An intelligent, interactive web scraper for extracting and processing content from websites, designed for simplicity and flexibility. This tool enables users to scrape website data (e.g., Black Friday deals), parse it into meaningful results, and iteratively refine the output with custom instructions.

---

## Features

- **Web Scraping**: Automatically scrape data from any website using Selenium and BeautifulSoup.
- **AI Parsing**: Leverages LangChain with Ollama LLM to intelligently extract requested content.
- **Interactive User Interface**: Built with Streamlit for an easy-to-use, interactive experience.
- **Iterative Refinement**: Users can continuously provide new parsing instructions for additional modifications.
- **Content Filtering**: Extract relevant content like product names, prices, and discounts.

---

## Requirements

Ensure you have the following installed:

- Python 3.8+
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
