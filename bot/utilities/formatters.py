# bot/utilities/formatters.py
from datetime import datetime
from typing import Dict, List

def format_stats(stats: Dict) -> str:
    """Format statistics data into a visually rich message"""
    return f"""
📊 *SYSTEM STATISTICS* 📊
    
📦 *Requests Overview*
{_progress_bar(stats['completed_requests'], stats['total_requests'])}
┌───────────────────────┬──────────────┐
│ Total Requests        │ {_pad_number(stats['total_requests'], 12)} │
│ Completed             │ {_pad_number(stats['completed_requests'], 12)} │
│ Rejected              │ {_pad_number(stats['rejected_requests'], 12)} │
│ Average Response Time │ {_pad_text(f"{stats['avg_response_time']:.1f}h", 12)} │
└───────────────────────┴──────────────┘

📂 *Content Distribution*
{_format_distribution(stats['category_distribution'])}

🎧 *Audio Preferences*
{_format_distribution(stats['audio_distribution'])}

🚨 *Priority Breakdown*
{_format_distribution(stats['priority_distribution'])}

⏰ Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""

def format_request(request: Dict) -> str:
    """Format individual request details"""
    status_icon = {
        'pending': '🟡',
        'accepted': '🟢',
        'rejected': '🔴',
        'ongoing': '🟠',
        'completed': '✅'
    }.get(request['status'], '⚪')
    
    return f"""
📄 *REQUEST DETAILS* 📄
    
{status_icon} *Status*: {request['status'].upper()}
🆔 *ID*: `{request['request_id']}`
    
📛 *Title*: {_escape_markdown(request['anime_name'])}
    
⚙️ *Specifications*
├─ Quality: {request['quality']}
├─ Audio: {request['audio']}
├─ Category: {request['category']}
└─ Priority: {_priority_icon(request['priority'])} {request['priority']}

⏳ *Timestamps*
├─ Submitted: {request['timestamp'].strftime('%Y-%m-%d %H:%M')}
└─ Updated: {request.get('status_date', 'N/A')}

📝 *Admin Notes*: {request.get('admin_notes', 'No notes available')}
"""

def format_user_stats(user_data: Dict) -> str:
    """Format user-specific statistics"""
    return f"""
👤 *USER STATISTICS* 👤
    
┌──────────────────────────┬──────────────┐
│ Daily Requests Remaining │ {_pad_number(user_data['remaining_daily'], 12)} │
│ Pending Requests         │ {_pad_number(user_data['pending_requests'], 12)} │
│ Total Submissions        │ {_pad_number(user_data['total_requests'], 12)} │
│ Success Rate             │ {_pad_text(f"{user_data['success_rate']}%", 12)} │
└──────────────────────────┴──────────────┘
    
⭐ Average Rating: {_star_rating(user_data.get('avg_rating', 0))}
"""

def format_feedback(feedback: Dict) -> str:
    """Format feedback entry"""
    return f"""
⭐ {_star_rating(feedback['rating'])} Review
📅 {feedback['timestamp'].strftime('%Y-%m-%d')}
💬 {feedback.get('comment', 'No comment provided')}
"""

def _progress_bar(current: int, total: int, length: int = 20) -> str:
    """Generate a progress bar visualization"""
    filled = int(round(length * current / total)) if total > 0 else 0
    return f"`{'█' * filled}{'░' * (length - filled)}` {current}/{total}"

def _format_distribution(dist: Dict) -> str:
    """Format distribution data as a table"""
    max_value = max(dist.values()) if dist.values() else 1
    return '\n'.join([
        f"{k}: `{'▰' * int(10 * v/max_value)}{'▱' * (10 - int(10 * v/max_value))}` {v}"
        for k, v in dist.items()
    ])

def _priority_icon(priority: str) -> str:
    icons = {
        'low': '🔹',
        'normal': '🔸',
        'high': '🔺',
        'urgent': '🚨'
    }
    return icons.get(priority.lower(), '🔸')

def _star_rating(rating: float) -> str:
    """Convert numeric rating to star emojis"""
    full_stars = int(rating)
    half_star = 1 if rating - full_stars >= 0.5 else 0
    empty_stars = 5 - full_stars - half_star
    return '⭐' * full_stars + '✨' * half_star + '☆' * empty_stars

def _pad_number(number: int, width: int) -> str:
    """Right-align numbers with padding"""
    return f"{number:{width},}"

def _pad_text(text: str, width: int) -> str:
    """Center-align text with padding"""
    return f"{text:^{width}}"

def _escape_markdown(text: str) -> str:
    """Escape special MarkdownV2 characters"""
    escape_chars = '_*[]()~`>#+-=|{}.!'
    return ''.join(['\\' + char if char in escape_chars else char for char in text])