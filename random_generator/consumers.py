def ws_connect(message):
    message.reply_channel.send({
        'accept': True,
        'text': "Hello"
    })


def ws_disconnect(message):
    pass
