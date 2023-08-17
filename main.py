import discord
from discord import app_commands
from commands import join, play, bye
from env import discord_api_key

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f"ログイン中のユーザー{client.user}")
    await tree.sync()
    await client.change_presence(activity=discord.Activity(name="音楽", type=discord.ActivityType.playing))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await tree.process_commands(message)

@tree.command(name="join", description="ボットが現在のボイスチャンネルに参加します")
async def join_command(interaction: discord.interactions):
    await join.join_command(interaction)

@tree.command(name="play", description="ランダム音楽をループ再生します")
async def play_command(interaction: discord.interactions):
    await play.play_command(interaction)

@tree.command(name="bye", description="ボットが現在のボイスチャットから切断します")
async def bye_command(interaction: discord.interactions):
    await bye.bye_command(interaction)

client.run(discord_api_key)