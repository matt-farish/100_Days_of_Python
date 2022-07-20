#Day 45 of Udemy's 100 Days of Python programming course
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# article_text = soup.find(name = "a", class_="titlelink")
# article_link = article_text.get("href")
# article_upvote = soup.find(name = "span", class_ = "score")

articles = soup.findAll(name = "a", class_= "titlelink")
article_texts = []
article_links = []
for article in articles:
    text = article.getText()
    article_texts.append(text)
    link = article.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name = "span", class_ = "score")]


largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])



# print(article_scores)




# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
    
# soup = BeautifulSoup(contents, "html.parser")

# # print(soup.title.string)

# # print(soup.prettify())

# all_anchor_tags = soup.find_all(name = "a")


# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name = "h1", id = "name")
# print(heading)