from telegram import Update
from telegram.ext import (
    ContextTypes, 
    ConversationHandler, 
    CommandHandler, 
    MessageHandler, 
    filters
)
from config import Config
from database import Database
from utilities import validators
from keyboards import user_keyboards

db = Database()

# Conversation states
SELECT_ANIME, SELECT_QUALITY, SELECT_AUDIO, SELECT_CATEGORY, SELECT_PRIORITY = range(5)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"🎉 Welcome {user.first_name}!\n\n"
        "Use /request to submit new anime requests\n"
        "Use /stats to check your request status\n"
        "Use /help for assistance"
    )

async def new_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_data = await db.get_user(user.id)
    
    if user_data['pending_requests'] >= Config.REQUEST_LIMITS['pending']:
        await update.message.reply_text("⚠️ You have too many pending requests!")
        return ConversationHandler.END
        
    context.user_data['request_data'] = {}
    await update.message.reply_text("📝 Please enter the anime name:")
    return SELECT_ANIME

async def receive_anime_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['request_data']['anime_name'] = update.message.text
    await update.message.reply_text(
        "🎚 Select quality preference:",
        reply_markup=user_keyboards.quality_keyboard()
    )
    return SELECT_QUALITY

async def receive_quality(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    context.user_data['request_data']['quality'] = query.data.split("_")[1]
    await query.edit_message_text(
        "🔊 Select audio preference:",
        reply_markup=user_keyboards.audio_keyboard()
    )
    return SELECT_AUDIO

async def receive_audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    context.user_data['request_data']['audio'] = query.data.split("_")[1]
    await query.edit_message_text(
        "📺 Select category:",
        reply_markup=user_keyboards.category_keyboard()
    )
    return SELECT_CATEGORY

async def receive_category(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    context.user_data['request_data']['category'] = query.data.split("_")[1]
    await query.edit_message_text(
        "🚨 Select priority level:",
        reply_markup=user_keyboards.priority_keyboard()
    )
    return SELECT_PRIORITY

async def receive_priority(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    context.user_data['request_data']['priority'] = query.data.split("_")[1]
    
    # Save to database
    request_id = await db.create_request(
        user_id=update.effective_user.id,
        data=context.user_data['request_data']
    )
    
    await query.edit_message_text(
        "✅ Request submitted!\n"
        f"📋 ID: {request_id}\n\n"
        "You can check status using /stats"
    )
    return ConversationHandler.END

# Add to your ConversationHandler
request_conversation = ConversationHandler(
    entry_points=[CommandHandler('request', new_request)],
    states={
        SELECT_ANIME: [MessageHandler(filters.TEXT, receive_anime_name)],
        SELECT_QUALITY: [CallbackQueryHandler(receive_quality, pattern="^quality_")],
        SELECT_AUDIO: [CallbackQueryHandler(receive_audio, pattern="^audio_")],
        SELECT_CATEGORY: [CallbackQueryHandler(receive_category, pattern="^category_")],
        SELECT_PRIORITY: [CallbackQueryHandler(receive_priority, pattern="^priority_")]
    },
    fallbacks=[CommandHandler('cancel', lambda u,c: ConversationHandler.END)]
)