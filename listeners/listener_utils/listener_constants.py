# This file defines constant messages used by the Slack bot for when a user mentions the bot without text,
# when summarizing a channel's conversation history, and a default loading message.
# Used in `app_mentioned_callback`, `dm_sent_callback`, and `handle_summary_function_callback`.

MENTION_WITHOUT_TEXT = """
Hej! Du nævnte mig, men skrev ikke nogen besked.
    Prøv at nævne mig igen i denne tråd med lidt mere info, så hjælper jeg dig gerne!
"""

SUMMARIZE_CHANNEL_WORKFLOW = """
En bruger er netop blevet medlem af denne Slack-kanal.
Lav venligst et hurtigt resumé af samtalen indtil nu, så de kan komme godt med.
Undlad at bruge brugernavne eller ID'er i dit svar.
"""

DEFAULT_LOADING_TEXT = "Tænker..."
