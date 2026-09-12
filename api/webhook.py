import os
import requests

BOT_TOKEN = os.environ.get("BOT_TOKEN")

def handler(request):
    if request.method != "POST":
        return {
            "statusCode": 200,
            "body": "TikTok Telegram Bot is running!"
        }

    data = request.get_json()

    if not data or "message" not in data:
        return {
            "statusCode": 200,
            "body": "OK"
        }

    message = data["message"]
    chat_id = message["chat"]["id"]
    text = message.get("text", "")

    if text == "/start":
        reply = (
            "🤖 TikTok Downloader Bot\n\n"
            "Kirim link TikTok ke sini.\n"
            "Contoh:\n"
            "https://www.tiktok.com/..."
        )

        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": reply
            }
        )

    elif "tiktok.com" in text:
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": "⏳ Link diterima. Downloader sedang diproses..."
            }
        )

    return {
        "statusCode": 200,
        "body": "OK"
    }
