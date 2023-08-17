import discord

async def bye_command(interaction: discord.Interaction):
    user = interaction.user
    if user.voice and user.voice.channel:
        voice_channel = user.voice.channel
        voice_client = interaction.guild.voice_client
        if voice_client and voice_client.channel == voice_channel:
            await voice_client.disconnect()
            await interaction.response.send_message("ボイスチャンネルから切断します。")
        else:
            await interaction.response.send_message("ボイスチャンネルに接続しているボットが違います。")
    else:
        await interaction.response.send_message("ボイスチャンネルに接続していません。")
