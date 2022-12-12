import random

import hikari
import lightbulb
from lightbulb import commands

@lightbulb.option("message", "The number, sides and bonus of dice to roll.")
@lightbulb.command("dice", "Roll one or more dice.")
@lightbulb.implements(commands.SlashCommand)
async def dice(ctx: lightbulb.context.Context) -> None:
    # Extract the options from the context
    message  = ctx.options.message
    target = message.replace(" ", "").lower()
    
    if target.find("d") == -1:
        await ctx.respond("Invalid Command")
        return

    number = target[0: target.find("d")]
    if not number: number = 1

    if target.find("+") == -1:
        bonus = 0
        lenght = len(target)
    else:
        lenght = target.find("+")
        bonus = target[target.find("+") + 1:]

    sides = target[target.find("d") + 1: lenght]

    try:
        number = int(number)
        sides = int(sides)
        bonus = int(bonus)
    except:
        await ctx.respond("Invalid Command")
        return

    # Option validation
    if number > 25:
        await ctx.respond("No more than 25 dice can be rolled at once.")
        return

    if sides > 100:
        await ctx.respond("The dice cannot have more than 100 sides.")
        return

    rolls = [random.randint(1, sides) for _ in range(number)]
    retrolls = " + ".join(f"{r}" for r in rolls) + (f" + {bonus} (bonus)" if bonus else "")+ f" = **{sum(rolls) + bonus:,}**"

    await ctx.respond(
        f"Resoult for {ctx.member.display_name} | Message: {message} | Resoult: {retrolls}"
    )


def load(bot: lightbulb.BotApp) -> None:
    bot.command(dice)


def unload(bot: lightbulb.BotApp) -> None:
    bot.remove_command(bot.get_slash_command("dice"))