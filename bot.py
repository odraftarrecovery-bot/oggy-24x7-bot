import os
import time
import asyncio
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import logging

TOKEN = os.environ.get("BOT_TOKEN")
START_TIME = datetime.now()

# Logging setup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uptime = datetime.now() - START_TIME
    hours = int(uptime.total_seconds() // 3600)
    minutes = int((uptime.total_seconds() % 3600) // 60)
    
    await update.message.reply_text(
        f"🔥 *OGGY BHAI 24/7 BOT* 🔥\n\n"
        f"✅ Status: Running on GitHub\n"
        f"⏱️ Uptime: {hours}h {minutes}m\n"
        f"🔄 Auto-restart: Every 6 hours\n\n"
        f"Commands:\n"
        f"/start - Show menu\n"
        f"/status - Check bot\n"
        f"/get_hack - Get scripts\n\n"
        f"💀 *CHUMT KA DARINDA*",
        parse_mode="Markdown"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uptime = datetime.now() - START_TIME
    hours = int(uptime.total_seconds() // 3600)
    
    await update.message.reply_text(
        f"📊 *Bot Status*\n\n"
        f"🟢 Running: Yes\n"
        f"⏱️ Session: {hours} hours\n"
        f"🔄 Next restart: {6 - hours} hours\n"
        f"✅ Working!",
        parse_mode="Markdown"
    )

async def get_hack(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🔨 *OGGY BHAI HACK*\n\n"
        f"Features: Anti-Ban, ESP, Headshot, Radar\n\n"
        f"📱 *GG Script:*\n"
        f"```lua\n"
        f"gg.setRanges(gg.REGION_C_ALLOC)\n"
        f"gg.searchNumber('0x2F4A8C', gg.TYPE_DWORD)\n"
        f"gg.getResults(1)\n"
        f"gg.editAll('9999', gg.TYPE_FLOAT)\n"
        f"gg.toast('OGGY ACTIVE')\n"
        f"```",
        parse_mode="Markdown"
    )

def main():
    print(f"[+] OGGY BHAI BOT STARTING at {START_TIME}")
    
    if not TOKEN:
        print("[-] ERROR: BOT_TOKEN not found!")
        return
    
    print(f"[+] Bot token: {'OK' if TOKEN else 'MISSING'}")
    print("[+] Creating application...")
    
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("get_hack", get_hack))
    
    print("[+] Starting polling...")
    app.run_polling()

if __name__ == "__main__":
    main()
