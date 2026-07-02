"""
Telegram message templates for Aigram.

All messages use Telegram HTML formatting and are in English.
Analysis content language is determined by the language flag.
"""

from typing import Final


# Analyze Command Messages

ANALYZE_STARTED: Final[str] = """🔍 <b>Analysis Started</b>

<code>Type:</code> {analysis_type}
<code>Messages:</code> {message_count}
<code>Language:</code> {language}

<i>This may take a few minutes...</i>"""


ANALYZE_BUSY: Final[str] = """⏳ <b>Analysis In Progress</b>

Another analysis is currently running for this chat.

<i>Please wait for it to complete before starting a new one.</i>"""


# Error Messages

ERROR_TIMEOUT: Final[str] = """⏱ <b>Analysis Timeout</b>

The analysis took too long and was cancelled.

Try with fewer messages or use the <code>en</code> flag for faster processing."""


ERROR_INVALID_COUNT: Final[str] = """❌ <b>Invalid Message Count</b>

Please specify a number between <code>10</code> and <code>10,000</code>.

<b>Example:</b> <code>/analyze=500</code>"""


ERROR_NO_MESSAGES: Final[str] = """❌ <b>Not Enough Messages</b>

This chat needs at least <code>10</code> messages for analysis."""


ERROR_FETCH_FAILED: Final[str] = """❌ <b>Could Not Fetch Messages</b>

Failed to retrieve messages from this chat.

Please try again later."""


ERROR_ANALYSIS_FAILED: Final[str] = """❌ <b>Analysis Failed</b>

An error occurred while analyzing the conversation.

Please try again or use fewer messages."""


ERROR_TRANSLATION_FAILED: Final[str] = """⚠️ <b>Translation Failed</b>

The analysis was generated but translation to Persian failed.

The English version will be sent instead."""


# Help Text

ANALYZE_HELP: Final[str] = """📊 <b>Analyze Command</b>

Analyze conversation patterns and dynamics.

<b>Usage:</b>
<code>/analyze=COUNT [TYPE] [LANGUAGE]</code>

<b>Examples:</b>
• <code>/analyze=500</code> - Last 500 messages (Persian)
• <code>/analyze=fun=1000</code> - Fun analysis
• <code>/analyze=200 en</code> - English output

<b>Analysis Types:</b>
• <code>fun</code> - Casual, humorous
• <code>romance</code> - Relationship dynamics  
• <code>general</code> - Professional (default)

<b>Language:</b>
• Default: Persian analysis
• Add <code>en</code> for English

<b>Limits:</b>
• 10-10,000 messages
• One analysis per chat at a time

<i>Analysis takes a few minutes to complete.</i>"""


# Format helpers

def format_analyze_started(
    analysis_type: str,
    message_count: int,
    language: str
) -> str:
    """Format the analysis started message."""
    lang_display = "Persian" if language == "persian" else "English"
    return ANALYZE_STARTED.format(
        analysis_type=analysis_type.title(),
        message_count=message_count,
        language=lang_display
    )
