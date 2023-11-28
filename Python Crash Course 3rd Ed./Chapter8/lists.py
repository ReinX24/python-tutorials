def show_messages(messages):
    """Printing each message in messages list"""
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    """Moving each message in messages to sent_messages list"""
    while messages:
        sent_messages.append(messages.pop())


messages = ['hello there', 'what\'s up', 'goodbye']
sent_messages = []

# Modifying the original list
# send_messages(messages, sent_messages)

# Passing in a copy instead of modifying the original
send_messages(messages[:], sent_messages)

# Checking if our messages list is empty
print(messages)
print(sent_messages)
# show_messages(messages)
# show_messages(sent_messages)
