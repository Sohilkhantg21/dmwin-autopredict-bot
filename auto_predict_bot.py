import requests
import telebot
import random
import time

bot = telebot.TeleBot("8106825482:AAGLGukBs0DCQFdWWSzd2gEbW5WvRBTSFj4")
channel_username = "@loopprediction"

last_period = None

def get_latest_period():
    try:
        url = "https://dmwin1.com/api/lottery/getLastLotteryResult?gameCode=WinGo_1min"
        headers = {
            "accept": "application/json, text/plain, */*",
            "user-agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers).json()
        return response["data"]["period"]
    except Exception as e:
        print(f"❌ Error fetching period: {e}")
        return None

def send_prediction(period):
    prediction = random.choice(["🟢 BIG", "🔴 SMALL"])
    msg = f"""
🎯 Prediction for Period: <b>{period}</b>

🔮 Our Prediction: <b>{prediction}</b>

📢 Join Channel: {channel_username}
"""
    bot.send_message(chat_id=channel_username, text=msg, parse_mode="html")

print("✅ Bot is running...")

while True:
    try:
        current_period = get_latest_period()
        if current_period and current_period != last_period:
            print(f"🆕 New Period Detected: {current_period}")
            last_period = current_period
            send_prediction(current_period)
        time.sleep(5)
    except Exception as err:
        print(f"❌ Error in loop: {err}")
        time.sleep(10)
