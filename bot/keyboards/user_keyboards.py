from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config

def quality_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("480p", callback_data="quality_480p"),
            InlineKeyboardButton("720p", callback_data="quality_720p"),
        ],
        [
            InlineKeyboardButton("1080p", callback_data="quality_1080p"),
            InlineKeyboardButton("4K", callback_data="quality_4k"),
        ]
    ])

def audio_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(opt, callback_data=f"audio_{opt}")] 
        for opt in Config.AUDIO_OPTIONS
    ])

def category_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(opt, callback_data=f"category_{opt}")] 
        for opt in Config.CATEGORIES
    ])

def priority_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(opt, callback_data=f"priority_{opt}")] 
        for opt in Config.PRIORITIES
    ])