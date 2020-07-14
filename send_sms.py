#!/usr/bin/env python

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = "AC1784f796686f0073d3047cff234ca18c"
auth_token = "db522ca782ef139c109216032aada1d2"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    from_="+12032631054",
    to="+15712014507",
)

print(message.sid)
