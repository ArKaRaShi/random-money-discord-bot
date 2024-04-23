import asyncio
import random
import discord
from discord.ext import commands
from config import TOKEN

game_round = 1

class MyView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(MyButton(label="Chest 1", custom_id="button1"))
        self.add_item(MyButton(label="Chest 2", custom_id="button2"))
        self.add_item(MyButton(label="Chest 3", custom_id="button3"))

class MyButton(discord.ui.Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.clicked_event = asyncio.Event()  # Create an event for each button

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"You choose {self.label}!")
        self.clicked_event.set()  # Set the event when the button is clicked
        self.view.stop()  # Stop the view when a button is clicked

def run_discord_bot():
    token = TOKEN
    intents = discord.Intents.default()
    intents.message_content = True
    command_prefix = '!'
    bot = commands.Bot(intents=intents, command_prefix=command_prefix)
    
    @bot.event
    async def on_ready():
        print("{0.user} on work!!".format(bot))

    def reward(base, increment, size):
        reward_list = [f"{base + increment * x}฿" for x in range(size)]
        return reward_list

    async def game_driver(ctx):
        total_money = 0
        reward_config = [[100, 100], [150, 80], [200, 60]]
        global game_round
        while game_round <= 3:
            view = MyView()
            reward_list = reward(reward_config[game_round - 1][0], reward_config[game_round - 1][1], 3)
            reward_money = reward_list[random.randint(1, 100) % 3]
            total_money += int(reward_money.split('฿')[0])

            await ctx.send(f"Round {game_round}!")
            for i in range(3):
                with open('chest.png', 'rb') as f:
                    picture = discord.File(f)
                await ctx.send(file=picture)

            await ctx.send(f"There are {', '.join(reward_list)} in the above 3 chests")
            await ctx.send("Choose the choices below", view=view)

            # Wait for a button click event
            try:
                await view.wait()
            except asyncio.TimeoutError:
                await ctx.send("Timeout!")
                return

            # Find out which button was clicked
            for item in view.children:
                if item.clicked_event.is_set():
                    await ctx.send(f"Got {reward_money} from {item.label}")
                    break

            await ctx.send(f"Total money: {total_money}฿")
            game_round += 1

    @bot.command()
    async def gamestart(ctx):
        await ctx.send("Moneyyyyyyy!!")
        await game_driver(ctx)

    async def main():
        await bot.start(token=token)
        
    asyncio.run(main())

if __name__ == "__main__":
    run_discord_bot()
