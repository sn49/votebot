import discord
from discord.ext import commands
import json

bot = commands.Bot(command_prefix="!")

f = open("token.json", "r")
token = json.load(f)["token"]


@bot.event
async def on_reaction_add(reaction, user):

    if user.bot:
        return

    print(reaction.message.channel.id)

    if reaction.message.channel.id == 837517586001952780:
        for react in reaction.message.reactions:
            if reaction == react:
                continue
            if user in await react.users().flatten():
                await reaction.remove(user)


@bot.command()
async def 투표(ctx, subject, *select):

    print(select)
    if subject == None:
        await ctx.send("투표 주제를 입력해주세요.")
        return

    if len(select) == 0:
        message = await ctx.send(ctx.message.content.replace("$투표 ", ""))
        await message.add_reaction("👍")
        await message.add_reaction("👎")
    else:
        if len(select) > 6:
            await ctx.send("최대 6개까지 설정가능합니다.")
            return
        count = 0
        sendmsg = f"{subject}\n"
        emojis = ["👍", "✌️", "👩‍👦‍👦", "🍀", "🖐️", "🎲"]
        for sel in select:
            sendmsg += f"{emojis[count]} {sel}\n"
            count += 1
        message = await ctx.send(sendmsg)
        for i in range(count):
            await message.add_reaction(emojis[i])


bot.run(token)
