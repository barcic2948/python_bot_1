import lightbulb

with open("./secrets/token.txt") as f:
    token = f.read().strip()

bot = lightbulb.BotApp(token)

bot.load_extensions_from("./commands")

@bot.command
@lightbulb.option("text", "text to repeat")
@lightbulb.command("echo", "repeats the given text")
@lightbulb.implements(lightbulb.SlashCommand)
async def echo(ctx: lightbulb.Context) -> None:
    await ctx.respond(ctx.options.text)


bot.run()