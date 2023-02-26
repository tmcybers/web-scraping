import requests
from bs4 import BeautifulSoup

# Define the base URL and create a list of URLs for each page
base_url = 'https://www.tinder.com/'
page_numbers = list(range(1, 11))
urls = [base_url + str(page) for page in page_numbers]

# Loop through each URL and scrape the data
for url in urls:
    # Send a GET request to the website
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the data you want to scrape
    articles = soup.find_all('article')
    for article in articles:
        title = article.find('h2').text.strip()
        author = article.find('span', {'class': 'author'}).text.strip()
        date = article.find('time')['datetime']
        content = article.find('div', {'class': 'content'}).text.strip()

        # Do something with the scraped data
        print(title, author, date, content)
