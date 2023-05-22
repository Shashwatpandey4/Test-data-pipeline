import requests
from bs4 import BeautifulSoup
import pandas as pd

# Set the search query
query = "data science"

# Send a GET request to Google search with the query
url = f"https://www.google.com/search?q={query}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
}
response = requests.get(url, headers=headers)
html_content = response.content

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find the search result elements
result_elements = soup.find_all("div", class_="g")

# Create empty lists to store the extracted data
titles = []
urls = []

# Iterate through the first 5 search results and extract the titles and URLs
for result_element in result_elements[:5]:
    # Extract the title
    title_element = result_element.find("h3")
    title = title_element.get_text(strip=True) if title_element else "N/A"
    titles.append(title)

    # Extract the URL
    link_element = result_element.find("a")
    url = link_element["href"] if link_element else "N/A"
    urls.append(url)

# Create a DataFrame from the extracted data
data = {
    "Title": titles,
    "URL": urls
}
df = pd.DataFrame(data)

# Save the DataFrame to a Parquet file
df.to_parquet("google_search_results.parquet", index=False)
