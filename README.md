# WebScrapping with Selenium and BeautifulSoup

This project involves web scraping smartphones data from a popular tech gadgets website, followed by data cleaning and Exploratory Data Analysis (EDA). The goal is to gather comprehensive data on smartphones available on that website and analyze it to gain insights.

## Project Overview

1. **Web Scraping**: [scrapping.py](https://github.com/dilkushsingh/WebScraping-with-Selenium-and-BeautifulSoup/blob/main/scrapping.py) fetches HTML source code from website. It handles multiple pages dynamically and stores the data in a single HTML file.
2. **Data Gathering**: Loaded the scrapped HTML content into soup object and then extracted the relevant info and created DataFrame from it. Extracted the DataFrame to csv file for make it suitable for further analysis.

## Web Scraping

The web scraping is implemented using Selenium. The script dynamically handles page navigation to scrape data from multiple pages. Here’s a brief overview of the scraping process:
- **Desired Page**: The smartphones data is on a specific page which is navigated through clicking specific elements.
- **Filtering Data**: Applied the filter that price should be greater than 5000Rs.
- **Navigating Pages**: The scraper starts from the first page and navigates through all available pages up to there are no more pages.
- **Data Storage**: Saves the extracted data repeatedly for every page into a single HTML file.

## Data Fetching
This Webscrapped data is directly available on github along with notebooks for Data Cleaning and EDA, if you directly want to use data in jupyter notebook then write following code:
```bash
pip3 install kaggle
!kaggle datasets download -d dilkushsingh/smartphones-dataset-upto-july24
```

## Prerequisites

Ensure you have the following installed:

- **Python 3.x**
- **Selenium** if not then install using cmd command $pip install selenium
- **BeautifulSoup** if not then install using cmd command $pip install beautifulsoup4
- **Web Browser** prefer web browser that have compatible web driver.
- **Chromedriver** web driver according to my web browser.
