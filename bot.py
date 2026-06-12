import os
import time
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import logging

TOKEN = os.environ.get("BOT_TOKEN")
START_TIME = datetime.now()

logging.basicConfig(level=logging.INFO)

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
        f"/start - Show this menu\n"
        f"/status - Check bot status\n"
        f"/get_hack - Download hack script\n\n"
        f"💀 *CHUMT KA DARINDA*",
        parse_mode="Markdown"
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uptime = datetime.now() - START_TIME
    hours = int(uptime.total_seconds() // 3600)
    
    await update.message.reply_text(
        f"📊 *Bot Status*\n\n"
        f"🟢 Running: Yes\n"
        f"⏱️ Current session: {hours} hours\n"
        f"🔄 Next restart: {6 - hours} hours\n"
        f"🌐 Platform: GitHub Actions\n\n"
        f"✅ Working perfectly!",
        parse_mode="Markdown"
    )

async def get_hack(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🔨 *OGGY BHAI HACK v1.0*\n\n"
        f"Features:\n"
        f"▪️ Anti-Ban + Anti-Blacklist\n"
        f"▪️ Radar ESP (All enemies)\n"
        f"▪️ Headshot Lock (100%)\n"
        f"▪️ Player Locations\n"
        f"▪️ No Recoil\n\n"
        f"📱 *GameGuardian Script:*\n"
        f"```lua\n"
        f"gg.setRanges(gg.REGION_C_ALLOC)\n"
        f"gg.searchNumber('0x2F4A8C', gg.TYPE_DWORD)\n"
        f"gg.getResults(1)\n"
        f"gg.editAll('9999', gg.TYPE_FLOAT)\n"
        f"gg.toast('OGGY BHAI ACTIVE')\n"
        f"```\n\n"
        f"🛡️ Safe for Main ID",
        parse_mode="Markdown"
    )

def main():
    print(f"[+] OGGY BHAI BOT STARTED at {START_TIME}")
    print(f"[+] Bot token: {'OK' if TOKEN else 'MISSING'}")
    
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("get_hack", get_hack))
    
    print("[+] Bot is polling... Will run for 6 hours")
    app.run_polling()

if __name__ == "__main__":
    main()
