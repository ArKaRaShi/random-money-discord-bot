# Random Money Game
This is a simple Discord bot for a random money game consisting of three rounds. Each round presents the player with three chests to choose from, each containing a different amount of money. The player selects one chest per round, and the bot reveals the amount of money inside. The total amount of money accumulated across all rounds is displayed at the end.

## Installation
To run this bot, you need to have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

Clone the repository:
```
git clone https://github.com/ArKaRaShi/random-money-discord-bot.git
```
Replace `your_username` and `your_repository` with your GitHub username and the name of your repository.
Install discord.py
```
pip install
```

Finally, Add 1 picture to the same repoitory named 'chest.png'

## Configuration

Before running the bot, you need to set up a Discord bot and obtain a token. Follow these steps:

1. Create a Discord application and bot on the [Discord Developer Portal](https://discord.com/developers/applications).
2. Copy the token of your bot.
3. Inside in `config.py`, There has a variable named `TOKEN`, Assign your bot token to it:
```python
TOKEN = "your_bot_token"
```

## Usage
Run the bot by executing the main.py file:
```
python main.py
```
Once the bot is running, you can interact with it on Discord.

## Commands
gamestart: Starts the money game.

## How the Game Works
1. The game consists of three rounds.
2. In each round, the bot presents three chests to the player.
3. Each chest contains a different amount of money randomly generated based on predefined configurations.
4. The player selects one chest per round.
5. The bot reveals the amount of money inside the chosen chest.
6. The total amount of money accumulated across all rounds is displayed at the end.
7. Enjoy playing the game and have fun accumulating money!
