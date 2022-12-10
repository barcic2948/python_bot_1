import lightbulb

@lightbulb.command("ping", "checks that the bot is alive")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond("Pong!")

def load(bot: lightbulb.BotApp):
    bot.command(ping)


def unload(bot: lightbulb.BotApp):
    bot.remove_command(bot.get_slash_command("ping"))