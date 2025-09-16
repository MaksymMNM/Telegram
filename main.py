import feedparser
import telebot
import time
import os

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@Ukrainian_Global_News"

bot = telebot.TeleBot(TOKEN)

# храним уже отправленные ссылки, чтобы не дублировать
sent_links = set()

def check_news():
    feed = feedparser.parse("https://www.pravda.com.ua/rss/view_news/")
    for entry in feed.entries:
        if entry.link not in sent_links:
            message = f"📰 {entry.title}\n{entry.link}"
            bot.send_message(CHANNEL_ID, message)
            sent_links.add(entry.link)

if __name__ == "__main__":
    while True:
        check_news()
        time.sleep(180)  # проверяем каждые 5 минут
