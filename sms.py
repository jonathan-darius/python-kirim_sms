from twilio.rest import Client
from informasi import account_sid, auth_token, nomor_saya, my_twilio

client = Client(account_sid, auth_token)

pesan = client.messages \
                .create(
                     body="Test Ini SMS dari Jonathan",
                     from_= my_twilio,
                     to=nomor_saya,
                 )

print(pesan.sid)