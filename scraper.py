import requests
from bs4 import BeautifulSoup
def fetch_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            print("Failed to fetch page:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred while fetching the page:", str(e))
        return None

def parse_html(html_content):
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        title = soup.title.text
        return title
    except Exception as e:
        print("An error occurred while parsing HTML:", str(e))
        return None


def main():
    url = "https://www.geeksforgeeks.org/set-in-java/"
    html_content = fetch_page(url)
    if html_content:
        data = parse_html(html_content)
        if data:
            # Process the extracted data further
            print(data)
        else:
            print("No data extracted.")
    else:
        print("Failed to fetch HTML content.")

if __name__ == "__main__":
    main()
