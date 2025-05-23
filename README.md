# Telegram Boot Notification Bot

This project is a simple Telegram bot that sends a message to your Telegram chat when your system (e.g., laptop or server) boots up.

---

## ✨ Features

- 📤 Sends a notification when the system starts
- 💬 Can receive and respond to simple text messages
- 🐍 Built with Python using the `python-telegram-bot` library

---

## 🧰 Requirements

- Python 3.7 or higher
- A Telegram bot token from [BotFather](https://t.me/BotFather)
- Internet access (use a proxy if Telegram API is blocked in your country)

---

## ⚙️ Installation

1. Clone this repository:

bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name


2. Install the required packages:

bash
pip install -r requirements.txt


3. Create a `.env` file in the root directory and fill it like this:


TOKEN=your_telegram_bot_token
CHAT_ID=your_telegram_chat_id


🚀 Running the Bot

Simply run:

bash
python bot.py


You can set up this script to run automatically when your system boots (e.g., using Task Scheduler on Windows or crontab on Linux).

🛡️ Notes

This is a basic example and not intended for production use.

Free hosting platforms may not be suitable for bots that require 24/7 uptime.

