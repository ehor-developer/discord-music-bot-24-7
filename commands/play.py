import discord
import asyncio
import random

playing = False
music_list = ["music/1.mp3",
              "music/2.mp3", "music/3.mp3", "music/4.mp3", "music/5.mp3", "music/6.mp3",]
prev_music_src = None

async def play_music(voice_client):
    global prev_music_src

    while True:
        available_music_list = [music for music in music_list if music != prev_music_src]
        
        if not available_music_list:
            available_music_list = music_list
        
        music_src = random.choice(available_music_list)
        prev_music_src = music_src

        audio_options = {
            "options": "-filter:a volume=0.1",
        }

        audio_source = discord.FFmpegPCMAudio(music_src, **audio_options)
        voice_client.play(audio_source, after=lambda e: print("音声再生完了"))

        while voice_client.is_playing():
            await asyncio.sleep(1)

async def play_command(interaction: discord.Interaction):
    user = interaction.user
    voice_state = interaction.guild.get_member(user.id).voice

    if voice_state and voice_state.channel:
        voice_channel = voice_state.channel
        voice_client = discord.utils.get(
            interaction.client.voice_clients, guild=interaction.guild)

        if not voice_client:
            voice_client = await voice_channel.connect()

        if voice_client.is_playing():
            await interaction.response.send_message("再生済みです")
        else:
            await interaction.response.send_message("音声を再生します")
            await play_music(voice_client)

        await voice_client.disconnect()
    else:
        await interaction.response.send_message("ボイスチャンネルに接続していません。")
