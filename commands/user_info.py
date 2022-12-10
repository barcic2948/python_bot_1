import datetime as dt

import hikari
import lightbulb
from lightbulb import commands


@lightbulb.option("target", "The member to get information about.", hikari.Member)
@lightbulb.command("userinfo", "Get info on a server member.")
@lightbulb.implements(commands.SlashCommand)
async def user_info(ctx: lightbulb.context.Context) -> None:
    target_ = ctx.options.target
    target = (
        target_
        if isinstance(target_, hikari.Member)
        else ctx.get_guild().get_member(target_)
    )
    if not target:
        await ctx.respond("That user is not in the server.")
        return

    created_at = int(target.created_at.timestamp())
    joined_at = int(target.joined_at.timestamp())
    roles = (await target.fetch_roles())[1:] 

    embed = (
        hikari.Embed(
            title="User information",
            description=f"ID: {target.id}",
            colour=hikari.Colour(0x563275),
            timestamp=dt.datetime.now().astimezone(),
        )
        .set_author(name="Information")
        .set_footer(
            text=f"Requested by {ctx.member.display_name}",
            icon=ctx.member.avatar_url,
        )
        .set_thumbnail(target.avatar_url)
        .add_field(name="Discriminator", value=target.discriminator, inline=True)
        .add_field(name="Bot?", value=target.is_bot, inline=True)
        .add_field(name="No. of roles", value=len(roles), inline=True)
        .add_field(
            name="Created on",
            value=f"<t:{created_at}:d> (<t:{created_at}:R>)",
            inline=False,
        )
        .add_field(
            name="Joined on",
            value=f"<t:{joined_at}:d> (<t:{joined_at}:R>)",
            inline=False,
        )
        .add_field(name="Roles", value=" | ".join(r.mention for r in roles))
    )

    await ctx.respond(embed)


def load(bot: lightbulb.BotApp):
    bot.command(user_info)


def unload(bot: lightbulb.BotApp):
    bot.remove_command(bot.get_slash_command("userinfo"))