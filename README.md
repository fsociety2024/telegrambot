Telegram Boot Notification Bot

This project is a simple Telegram bot that sends a message to your Telegram chat when your system (e.g., laptop or server) boots up.

✨ Features
•	📤 Sends a notification when the system starts
•	💬 Can receive and respond to simple text messages
•	🐍 Built with Python using the python-telegram-bot library

🧰 Requirements
•	Python 3.7 or higher
•	A Telegram bot token from BotFather
•	Internet access (use a proxy if Telegram API is blocked in your country)

⚙️ Installation
Clone this repository:
git clone https://github.com/fsociety2024/telegrambot.git
cd telegrambot

Install the required packages:
pip install -r requirements.txt

Create a .env file in the root directory and fill it like this:
TOKEN=your_telegram_bot_token
CHAT_ID=your_telegram_chat_id

🚀 Running the Bot
Simply run:
python bot.py

🔁 Run Automatically on System Startup (Windows)
To configure the bot to run automatically on system startup using Task Scheduler on Windows, follow these steps:
•	Open the Start menu and search for “Task Scheduler”.
•	In the right-hand Actions pane, click on “Create Basic Task…”.
•	Name the task (e.g., “Telegram Boot Bot”) and click Next.
•	Select “When the computer starts” and click Next.
•	Choose “Start a program” and click Next.
•	In the 'Program/script' field, enter the path to the Python executable (e.g., C:\Python39\python.exe).
•	In the 'Add arguments' field, enter the full path to your bot script (e.g., C:\Users\YourUser\telegrambot\bot.py).
•	Click Finish. The bot will now run automatically when the system starts.

🛡️ Notes
•	This is a basic example and not intended for production use.
•	Free hosting platforms may not be suitable for bots that require 24/7 uptime.
