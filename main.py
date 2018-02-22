import discord
import asyncio
import random
import time



client = discord.Client()



LARANJAesc =0xD24B36
msg_id = None
msg_user = None



@client.event
async def on_ready():
    print('Olá Mundo!')
    print(client.user.name)
    print(client.user.id)


@client.event
async def on_message(message):
    if message.content.lower().startswith('++oi'):
        await client.send_message(message.channel, "Estou On-Line")

    if message.content.lower().startswith('++help'):
        await client.send_message(message.channel, "✏++oi ➡ Verifica se o BOT está online\n"
                                                   "✏++frase ➡ Receba uma frase que te alegrará\n"
                                                   "✏++ping 🏓➡ (Precisa digitar o EMOJI de raquete) Jogue Ping-Pong com o BOT\n"
                                                   "✏++game ➡ Selecione os Games que Você Joga"
                                 )

    if message.content.lower().startswith('++frase'):
        await client.send_message(message.channel, "Se eu pudesse deixar algum presente à você, deixaria aceso o sentimento de amar a vida dos seres humanos. A consciência de aprender tudo o que foi ensinado pelo tempo a fora. Lembraria os erros que foram cometidos para que não mais se repetissem. A capacidade de escolher novos rumos. Deixaria para você, se pudesse, o respeito aquilo que é indispensável. Além do pão, o trabalho. Além do trabalho, a ação. E, quando tudo mais faltasse, um segredo: o de buscar no interior de si mesmo a resposta e a força para encontrar a saída")


    if message.content.lower().startswith('++ping 🏓'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> PONG 🏓" % (userID))

    if message.content.lower().startswith('++game'):
        embed =discord.Embed(
            title="Selecione o Game que Você Joga",
            color=LARANJAesc,
            description="- Clash Royale = 👑\n"
                        "- Arena Of Valor = ⚔\n"
                        "- Minecraft = 💎\n"
                        "- Brawl Stars = 🎯\n"
                        "- Futebol Games = ⚽\n"
                        "- NOVA Legacy = 🔫\n"
                        "- Outros Jogos = 🎮",
     )

    botmsg = await client.send_message(message.channel, embed=embed)
    await client.add_reaction(botmsg, "👑")
    await client.add_reaction(botmsg, "⚔")
    await client.add_reaction(botmsg, "💎")
    await client.add_reaction(botmsg, "🎯")
    await client.add_reaction(botmsg, "⚽")
    await client.add_reaction(botmsg, "🔫")
    await client.add_reaction(botmsg, "🎮")

    global msg_id
    msg_id = botmsg.id
    global msg_user
    msg_user = message.author


@client.event
async def on_reaction_add(reaction, user):
    msg= reaction.message

    if reaction.emoji == "👑" and msg.id == msg_id:
     role = discord.utils.find(lambda r: r.name == "Clash Royale", msg.server.roles)
    await client.add_roles(user, role)

    if reaction.emoji == "⚔" and msg.id == msg_id:
     role = discord.utils.find(lambda r: r.name == "Arena Of Valor", msg.server.roles)
    await client.add_roles(user, role)

    if reaction.emoji == "💎" and msg.id == msg_id:
     role = discord.utils.find(lambda r: r.name == "Minecraft", msg.server.roles)
    await client.add_roles(user, role)

    if reaction.emoji == "🎯" and msg.id == msg_id:
     role = discord.utils.find(lambda r: r.name == "Brawl Stars", msg.server.roles)
    await client.add_roles(user, role)

    if reaction.emoji == "⚽" and msg.id == msg_id:
     role = discord.utils.find(lambda r: r.name == "Futebol Games", msg.server.roles)
    await client.add_roles(user, role)

    if reaction.emoji == "🔫" and msg.id == msg_id:
     role = discord.utils.find(lambda r: r.name == "NOVA Legacy", msg.server.roles)
    await client.add_roles(user, role)

    if reaction.emoji == "🎮" and msg.id == msg_id:
     role = discord.utils.find(lambda r: r.name == "Outros Jogos", msg.server.roles)
    await client.add_roles(user, role)




@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message

    if reaction.emoji == "👑" and msg.id == msg_id:
     role = discord.utils.find(lambda r: r.name == "Clash Royale", msg.server.roles)
    await client.remove_roles(user, role)

    if reaction.emoji == "⚔" and msg.id == msg_id:
     role = discord.utils.find(lambda r: r.name == "Arena Of Valor", msg.server.roles)
    await client.remove_roles(user, role)

    if reaction.emoji == "💎" and msg.id == msg_id:
     role = discord.utils.find(lambda r: r.name == "Minecraft", msg.server.roles)
    await client.remove_roles(user, role)

    if reaction.emoji == "🎯" and msg.id == msg_id:
     role = discord.utils.find(lambda r: r.name == "Brawl Stars", msg.server.roles)
    await client.remove_roles(user, role)

    if reaction.emoji == "⚽" and msg.id == msg_id:
     role = discord.utils.find(lambda r: r.name == "Futebol Games", msg.server.roles)
    await client.remove_roles(user, role)

    if reaction.emoji == "🔫" and msg.id == msg_id:
     role = discord.utils.find(lambda r: r.name == "NOVA Legacy", msg.server.roles)
    await client.remove_roles(user, role)

    if reaction.emoji == "🎮" and msg.id == msg_id:
     role = discord.utils.find(lambda r: r.name == "Outros Jogos", msg.server.roles)
    await client.remove_roles(user, role)





client.run('NDE1Mjc2OTAzNzQ2NzY0ODIx.DWzkZw.ruEd9PYlVSSHa3KKpZ6OEr6Ad9o')

