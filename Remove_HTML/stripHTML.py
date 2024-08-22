from bs4 import BeautifulSoup
import re

def strip_html_tags(html):
    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Extract text without HTML tags
    text = soup.get_text(separator=' ', strip=True)

    # Remove extra whitespaces
    text = re.sub('\s+', ' ', text).strip()

    return text

# Example HTML text
html_text = """
HTML HERE
"""

# Call the function to strip HTML tags
plain_text = strip_html_tags(html_text)

# Print the resultp[i]
print(plain_text)