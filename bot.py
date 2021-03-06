import os

import discord
import tokage
from discord.ext import commands

TOKEN = os.environ.get("BOT_TOKEN")
extensions = ["roll", "roles", "utils", "search", "cancer", "anilist"]
startup_extensions = ["cogs." + extension for extension in extensions]


class SynBot(commands.Bot):
    def __init__(self):
        game = discord.Game(name="s!help | syn help", type=2)
        prefix = commands.when_mentioned_or("syn ", "s!")
        super().__init__(command_prefix=prefix, description="Misc Bot", activity=game)

    async def close(self):
        await self.t_client.cleanup()
        await super().close()

    async def on_message(self, message):
        if message.author.bot:
            return
        await self.process_commands(message)

    async def on_ready(self):
        self.t_client = tokage.Client()
        self.owner_id = 111158853839654912
        print('Logged in!')
        print(self.user.name)
        print(self.user.id)
        print('------')
        print("Cogs loaded:")
        for extension in startup_extensions:
            try:
                self.load_extension(str(extension))
                print('"%s" loaded successfully' % extension.split(".")[1])
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__, e)
                print('Failed to load extension {}\n{}'.format(extension, exc))
        print('------')


SynBot().run(TOKEN)
