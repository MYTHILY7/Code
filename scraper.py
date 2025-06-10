from newspaper import Article

url = "https://www.theverge.com/2024/6/4/24170329/apple-openai-chatgpt-ios18-integration"

try:
    article = Article(url)
    article.download()
    article.parse()

    print("📰 Title:", article.title)
    print("📅 Published Date:", article.publish_date)
    print("✍️ Content Snippet:\n", article.text[:500])

except Exception as e:
    print("❌ Failed to scrape article:", e)
