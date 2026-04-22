import json
from datetime import datetime

def generate_daily_digest(news_data):
    # Sort news items by importance/relevance (this could be a specific key in your data)
    sorted_news = sorted(news_data, key=lambda x: x.get('importance', 0), reverse=True)

    # HTML Email Template
    html_content = f"""
    <html>
    <head>
        <title>Daily News Digest</title>
    </head>
    <body>
        <h1>Daily News Digest for {datetime.utcnow().strftime('%Y-%m-%d')}</h1>
        <p>Total News Count: {len(sorted_news)}</p>
        <table border="1">
            <tr>
                <th>Category</th>
                <th>Title (Chinese)</th>
                <th>Title (English)</th>
                <th>Content Summary</th>
                <th>Source</th>
                <th>Original Link</th>
            </tr>
    """

    for item in sorted_news:
        html_content += f"""
            <tr>
                <td>{item.get('category', 'N/A')}</td>
                <td>{item.get('title_chinese', 'N/A')}</td>
                <td>{item.get('title_english', 'N/A')}</td>
                <td>{item.get('summary', 'N/A')}</td>
                <td>{item.get('source', 'N/A')}</td>
                <td><a href="{item.get('link', '#')}">Read More</a></td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """
    return html_content

# Example usage (assuming you have news data)
# news_data = json.loads(your_json_string)
# print(generate_daily_digest(news_data))