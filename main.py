from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyromod import listen
from aiohttp import ClientSession
from config import Config
import helper
import time
import sys
import shutil
import os, re
import requests
import headers
import logging

bot = Client(
    "bot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
    await m.reply_text(
        f"😈**Hi bruh!**\n**🟢I'm Alive You can Use by /master**\n\n"
        "**<-URL Acceptable->**\n"
        "-`All Non-Drm+Drm Protected Url`\n"
        "-`Mpeg Dash Url`\n"
        "-`Vision IAS`\n"
        "-`PhysicsWallah`\n"
        "-`ClassPlus Url`\n"
        "-`Allen Institute`\n\n"
        "**Thanks for using me**\n\n"
        "**Developer -** `@St2Master`"
    )

@bot.on_message(filters.command("stop"))
async def restart_handler(bot, m):
    if m.chat.id not in Config.VIP_USERS:
        await bot.send_message(
            m.chat.id,
            f"**Oopss! You are not a Premium member **\n\n"
            "**PLEASE UPGRADE YOUR PLAN**\n\n"
            "**/upgrade for Plan Details**\n"
            f"**Send me your user id for authorization your User id** - `{m.chat.id}`"
        )
        return
    await m.reply_text("🚦**STOPPED**🚦", True)
    os.execl(sys.executable, sys.executable, *sys.argv)


@bot.on_message(filters.command(["master"]))
async def account_login(bot: Client, m: Message):
    try:
        editable = await m.reply_text('**Send 🗂️Master TXT🗂️ file for download**')
        input: Message = await bot.listen(editable.chat.id)
        path = f"./downloads/{m.chat.id}"
        temp_dir = "./temp"
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        os.makedirs(temp_dir)
        if input.document:
            x = await input.download()
            await input.delete(True)
            file_name = os.path.splitext(os.path.basename(x))[0]
            with open(x, "r") as f:
                content = f.read()
            content = content.split("\n")
            links = [i.split("://", 1) for i in content]
            os.remove(x)
        else:
            content = input.text
            content = content.split("\n")
            links = [i.split("://", 1) for i in content]
            await input.delete(True)

        await editable.edit(f"Total links🔗 found are **{len(links)}**\n\nSend starting number (default = 1)")
        input0: Message = await bot.listen(editable.chat.id)
        raw_text = input0.text
        await input0.delete(True)

        await editable.edit("**Enter Batch Name or /d for filename**")
        input1: Message = await bot.listen(editable.chat.id)
        raw_text0 = input1.text
        await input1.delete(True)
        if raw_text0 == '/d':
            b_name = file_name
        else:
            b_name = raw_text0

        await editable.edit("**Enter App Name**")
        input111: Message = await bot.listen(editable.chat.id)
        app_name = input111.text
        await input111.delete(True)

        await editable.edit("**Enter resolution (e.g., 360, 480, 720)**")
        input2: Message = await bot.listen(editable.chat.id)
        raw_text2 = input2.text
        await input2.delete(True)

        await editable.edit("**Enter Your Channel Name or Owner Name**")
        input3: Message = await bot.listen(editable.chat.id)
        raw_text3 = input3.text
        await input3.delete(True)
        MR = "『ᎷΔŞŦᏋᏒ』❤️" if raw_text3 == 'de' else raw_text3

        await editable.edit("**Send Thumbnail URL or `no`**")
        input6: Message = await bot.listen(editable.chat.id)
        thumb = input6.text
        await input6.delete(True)

        await editable.edit("**Send Channel ID or `/d` to use current chat**")
        input7: Message = await bot.listen(editable.chat.id)
        channel_id = m.chat.id if "/d" in input7.text else input7.text
        await input7.delete()
        await editable.edit("**Processing started...**")

        await bot.send_message(chat_id=channel_id, text=f'🎯**Target Batch - {b_name}**')
        await editable.delete()
        count = int(raw_text) if len(links) > 1 else 1
        mpd = None

        for i in range(count - 1, len(links)):
            V = links[i][1]
            url = "https://" + V

            # 🔹 Handle rwa-play-on PDF and Proxy links
            if "rwa-play-on.vercel.app/pdf" in url:
                pdf_file = helper.download_pdf_proxy(url, f"{name}.pdf")
                if pdf_file:
                    await bot.send_document(chat_id=channel_id, document=pdf_file, caption=cc1)
                    count += 1
                    os.remove(pdf_file)
                continue

            elif "rwa-play-on.vercel.app/proxy" in url:
                vid_file = helper.download_m3u8_proxy(url, f"{name}.mp4")
                if vid_file:
                    await bot.send_video(chat_id=channel_id, video=vid_file, caption=cc)
                    count += 1
                    os.remove(vid_file)
                continue

            if "*" in url:
                mpd, keys = url.split("*")
            elif "vimeo" in url:
                text = requests.get(url, headers=headers.allen).text
                pattern = r'https://[^/?#]+\.[^/?#]+(?:/[^/?#]+)+\.(?:m3u8)'
                urls = re.findall(pattern, text)
                for url in urls:
                    break
            elif 'classplusapp.com' in url:
                if '4b06bf8d61c41f8310af9b2624459378203740932b456b07fcf817b737fbae27' in url:
                    pattern = re.compile(r'https://videos\.classplusapp\.com/([a-f0-9]+)/([a-zA-Z0-9]+)\.m3u8')
                    match = pattern.match(url)
                    if match:
                        urlx = f"https://videos.classplusapp.com/b08bad9ff8d969639b2e43d5769342cc62b510c4345d2f7f153bec53be84fe35/{match.group(2)}/{match.group(2)}.m3u8"
                        url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={urlx}', headers=headers.cp).json()['url']
                else:
                    url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers=headers.cp).json()['url']
            elif '/master.mpd' in url:                
                id =  url.split("/")[-2] 
                policy = requests.post('https://api.penpencil.xyz/v1/files/get-signed-cookie', headers=headers.pw, json={'url': f"https://d1d34p8vz63oiq.cloudfront.net/" + id + "/master.mpd"}).json()['data']
                url = "https://sr-get-video-quality.selav29696.workers.dev/?Vurl=" + "https://d1d34p8vz63oiq.cloudfront.net/" + id + f"/hls/{raw_text2}/main.m3u8" + policy
            elif "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers=headers.vision) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            name1 = links[i][0].replace("\t", "").replace(":", " ").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}){name1[:60]}'
            
            if "drive" in url or ".pdf" in url or "pdfs" in url:
                try:
                    cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                    os.system(cmd)
                    await bot.send_document(chat_id=channel_id, document=f'{name}.pdf', caption=cc1)
                    count += 1
                    os.remove(f'{name}.pdf')
                except FloodWait as e:
                    await m.reply_text(str(e))
                    time.sleep(e.x)
                    continue

            elif mpd and keys:
                prog = await bot.send_message(channel_id, f"**Downloading...** `{name}`")
                await helper.download_and_dec_video(mpd, keys, path, name, raw_text2)
                await prog.delete(True)
                await helper.merge_and_send_vid(bot, m, cc, name, prog, path, url, thumb, channel_id)
                count += 1
                time.sleep(3)
            else:
                prog = await bot.send_message(channel_id, f"**Downloading...** `{name}`")
                res_file = await helper.download_video(url, cmd, name)
                filename = res_file
                await prog.delete(True)
                await helper.send_vid(bot, m, cc, filename, thumb, name, prog, url, channel_id)
                count += 1
                time.sleep(1)

        await bot.send_message(channel_id, "🌟**All Lectures Downloaded Successfully!**🌟")

    except Exception as e:
        await m.reply_text(f"**⚠️ Download Failed ⚠️**\n\n**Reason:** {e}")
        return

import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

def run_web():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), SimpleHTTPRequestHandler)
    print(f"🌐 Web server running on port {port}")
    server.serve_forever()

threading.Thread(target=run_web, daemon=True).start()

bot.run()
