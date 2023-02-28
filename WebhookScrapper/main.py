import requests
from telethon import TelegramClient, events
from discord_webhook import DiscordWebhook, DiscordEmbed

# Put the Discord webhook URL 
DISCORD_WEBHOOK =  ""

# Put the Telegram API ID and API Hash 
api_id = 
api_hash = ""


def send_discord(message):
    embed = DiscordEmbed(description=message, color=0x0000FF)
    embed.set_author(name="Made By Infinity??..")
    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/l_Xd4R7gVvaUMGoyOWdjizO6kuCISzwUWgpqn7WJUzM/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/1057576716807192666/fdd9b6107161dcb5e171e7f48daaf538.png")
    webhook = DiscordWebhook(url=DISCORD_WEBHOOK, embeds=[embed])
    webhook.execute()
print(f'Sending message to: {DISCORD_WEBHOOK}')
client = TelegramClient('session_name', api_id, api_hash)
client.start()


@client.on(events.NewMessage(chats=('cpscr')))
async def my_event_handler(event):
        message = event.message.message
        send_discord(message)

client.run_until_disconnected()
