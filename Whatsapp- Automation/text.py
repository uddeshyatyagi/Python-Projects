from twilio.rest import Client 
 
account_sid = 'AC6bfd6c24cb66217aee287a026414b0ec' 
auth_token = <Enter your unique auth token>
client = Client(account_sid, auth_token) 
def send(): 
    message = client.messages.create( 
                                  from_='whatsapp:+14155238886',  
                                  body='checking u after every 1 hour !!!',      
                                  to='whatsapp:+914446699978' 
                              ) 
 
    print(message.sid)