import discord

async def join_command(interaction: discord.Interaction):
    user = interaction.user
    if user.voice and user.voice.channel:
        voice_channel = user.voice.channel
        await voice_channel.connect()
        await interaction.response.send_message("ボイスチャンネルに接続します。")
    else:
        await interaction.response.send_message("ボイスチャンネルに接続していません。")