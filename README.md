# Web Scraper

## Overview
This Python script scrapes real estate house rental websites to extract property details including addresses, locations, and prices using BeautifulSoup. The data is then stored in Google Sheets using Selenium for easy management and analysis.

## Features
- Scrapes real estate websites for house rental listings.
- Extracts property details such as address, location, and rental price.
- Automates data entry into Google Sheets for centralized storage.
- Configurable scraping intervals and target websites.

## Applications
This project can be useful in various scenarios, including:
- **Property Management**: Automate the collection and tracking of rental property listings.
- **Market Analysis**: Gather data for analyzing rental trends and pricing in specific areas.
- **Personal Research**: Collect rental property information for personal use or comparison.

## Installation
1. Clone the repository : git clone https://github.com/your-username/web-scraper.git
2. Install dependencies : pip install -r requirements.txt

## Demo
### **GIF Preview**
![Demo](https://img-c.udemycdn.com/redactor/raw/2020-08-25_15-50-47-7e40268135497ea3e84762091f48779d.gif)

- You should end up with a spreadsheet that looks something like this.
### **Expected Spreadsheet Output**
<img src="https://img-c.udemycdn.com/redactor/raw/2020-08-25_15-53-33-5cc79771a88de0ff918068a99ecbc371.png" width="600">

## Usage
1. Set up your Google Sheets credentials and configure target websites in `main.py`.
2. Run the script to start scraping and updating Google Sheets.

