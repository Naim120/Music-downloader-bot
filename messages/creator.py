from telegram.utils.helpers import escape_markdown as es


def start_msg(name):
    msg = f"""*Hey {es(name,version=2)}* ✋✋ *welcome to Jiosaavn downloader bot* ⚡⚡\n
    _Just send me a jiosaavn song or album link I will send you the audio_\n
made by @phantom2152 😈😈"""
    return msg


def help_msg():
    help = """ℹ️⁉⁉ *help*\n
*just send me a jiosaavn song,album or playlist link, I will send you the audio with lyrics*⚡⚡"""
    return help

def important_msg():
    important = """*Some important notes:*\n
Sometimes bot might late reply due to 30 minutes inactivity heroku rule. Pls wait for 10-12 seconds.\n\n
Pls give one link at a time and don't spam the bot.\n\n
To see the proper link format click here: https://cdn.jsdelivr.net/gh/Naim120/Music-downloader-bot@f738f3e3f809f54c04e706bc0094b6f4dcb74d0e/Link%20format.jpg"""
    return important
