# Weather Scraper

This simple Python script allows you to retrieve real-time weather information for a specified city using web scraping. The script utilizes the BeautifulSoup library to parse HTML content and requests library to make HTTP requests.

## Prerequisites
- Python 3.x
- BeautifulSoup4
- Requests

You can install the required libraries using the following command:
```bash
pip install beautifulsoup4 requests
```

## Usage
1. Import the necessary libraries:
   ```python
   from bs4 import BeautifulSoup
   import requests
   ```

2. Define a user agent to mimic a web browser:
   ```python
   headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
   ```

3. Define the `weather` function, which takes a city name as input, performs a Google search for the weather of that city, and prints the relevant information:
   ```python
   def weather(city):
       
   ```

4. Get user input for the city name and call the `weather` function:
   ```python
   city = input("Enter city name >> ")
   city = city + "weather"
   weather(city)
   ```

Note: Ensure you are respectful of the terms of service of the website you are scraping. Web scraping may be against the terms of service of certain websites.

## Disclaimer
This script is for practise purposes only. Use it responsibly and be aware of the legality and terms of service of the websites you are scraping. The script may break if the structure of the target website changes.
