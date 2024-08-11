# Smartphone Data Scraper

This project involves scraping smartphone data from a popular Tech gadget reviver website, followed by data cleaning and Exploratory Data Analysis (EDA). The goal is to gather comprehensive data on smartphones available on that website and analyze it to gain insights.

# Status

Since web scrapping is the process of gathering data, but some website doesn't allow it, I have scrapped a popular website which reviews tech gadgets like Mobiles, Laptops, etc. Currently waiting for the positive response from the website team.

## Project Overview

1. **Web Scraping**: The scraper fetches data on smartphones from website. It handles multiple pages dynamically and stores the data in a single HTML file.
2. **Data Cleaning**: The raw data collected from the website is cleaned to ensure accuracy and consistency.
3. **Exploratory Data Analysis (EDA)**: Various analyses are performed on the cleaned data to extract valuable insights.

## Web Scraping

The web scraping is implemented using Selenium and BeautifulSoup. The script dynamically handles page navigation to scrape data from multiple pages. Here’s a brief overview of the scraping process:

- **Navigating Pages**: The scraper starts from the first page and navigates through all available pages up to a specified limit (or dynamically if the total number of pages is not known).
- **Data Extraction**: Extracts relevant information such as smartphone names, prices, ratings, etc.
- **Data Storage**: Saves the extracted data into a single HTML file.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- Selenium
- Chromedriver (or another WebDriver for your browser)
