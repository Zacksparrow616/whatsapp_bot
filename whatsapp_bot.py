from twilio.rest import Client

account_sid = 'AC1c9eeaf88c45b4517989fe6c922bf99b'
auth_token = 'e1227c7dd6747d979922cee9947354f0'
client = Client(account_sid, auth_token)

def automation_function():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='This is my Whatsapp BOT for sending automated messages',
        #body='hey u ... whats up',
        to='whatsapp:+917381788563'
    )
    print(message.sid)