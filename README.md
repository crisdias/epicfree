# Steam Discussion Scraper

This is a Python script that scrapes comments from a Steam discussion thread and sends their content, as plain text, to a Telegram chat. It also stores a hash of each comment, so that the same comment is not sent twice.

This script was created in order to get alerts for free PC games, from [this url](https://steamcommunity.com/groups/GrabFreeGames/discussions/1/483366528924521316/).

## Dependencies

This script requires the following Python libraries:

- beautifulsoup4
- requests
- python-telegram-bot

These can be installed via pip:

```
pip install -r requirements.txt
```

## Usage

1. Create a Telegram bot and get its token. You can follow the instructions [here](https://core.telegram.org/bots#creating-a-new-bot) to create a new bot and obtain its token.
2. Add the bot to a Telegram group or channel where you want to receive the comments.
3. Set the environment variable TELEGRAM_BOT_TOKEN to the token of your bot.
4. Set the environment variable TELEGRAM_CHAT_ID to the ID of the group or channel where you want to receive the comments. You can find the ID by following the instructions [here](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id).
5. Alternatively, you can /start a conversation with you bot and set TELEGRAM_CHAT_ID to your own user id. You can find your ID by following the instructions [here](https://stackoverflow.com/questions/31078710/how-to-obtain-telegram-chat-id-for-a-specific-user).
6. Set the environment variable WAIT to the number of minutes to wait between each check for new comments. For example, to wait 5 minutes, set WAIT to 5.
7. Set the environment variable STEAM_URL to the Steam discussion page.
8. Run bot.py:
```
python bot.py
```

The script will start scraping the comments and sending them to your Telegram group or channel. It will save the current page number to a file (current_page.txt) so that it can resume from where it left off the next time it is run. You can always edit this file if needed.

To stop the script, press Ctrl+C/Cmd-C.

## Docker Usage

1. Build the Docker image:
```
docker build -t steam-discussion-scraper .
```

2. Run the Docker container, setting the environment variables as necessary:
```
docker run -e TELEGRAM_BOT_TOKEN=<bot_token> -e TELEGRAM_CHAT_ID=<chat_id> -e WAIT=<minutes> -e STEAM_URL=<steam_url> steam-discussion-scraper
```

## License

This script is released under the [MIT License](https://opensource.org/licenses/MIT).
