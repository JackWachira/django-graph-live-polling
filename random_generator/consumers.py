from channels import Group
from channels.auth import channel_session_user


@channel_session_user
def ws_disconnect(message):
    user_group = message.channel_session.get('random-points')
    if user_group:
        Group(user_group).discard(message.reply_channel)
