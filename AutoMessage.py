from http.client import HTTPSConnection
from sys import stderr
from json import dumps
from time import sleep
import random
import datetime

now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#define token
with open('./textfiles/token.txt', 'r') as file:
	token = file.readlines()[0]
token = token.strip()
print(token)
#end define token

#define chanellink
with open('./textfiles/channellink.txt', 'r') as file:
	channellink = file.read()
print(channellink)
#end define chanellink

#define channelid
with open('./textfiles/channel.txt', 'r') as file:
	channelid = file.read()
print(channelid)
#end define channelid

#define sleep
with open('./textfiles/time.txt', 'r') as file:
	x = file.read()
print(x)
#end define sleep

#define message_content
with open('./textfiles/message.txt', 'r') as file:
	message = file.read()
header_data = {
	"content-type": "application/json",
	"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
	"authorization": f"{token}",
	"host": "discordapp.com",
	"referer": f"{channellink}"}


def get_connection():
	return HTTPSConnection("discordapp.com", 443)


def send_message(conn, channel_id, message_data):
    try:
        conn.request(
            "POST", f"/api/v6/channels/{channelid}/messages", message_data, header_data)
        resp = conn.getresponse()

        if 199 < resp.status < 300:
            print("SUCCESS")
            pass

        else:
            stderr.write(f"Received HTTP {resp.status}: {resp.reason}\n")
            pass

    except:
        stderr.write("ERROR\n")

def main():
	message_data = {
		"content": f"{message}",
		"tts": "false",
		}
	send_message(get_connection(), (f"{channelid}"), dumps(message_data))


if __name__ == '__main__':
	while True:
		main()
		convertedInt = int(x)
		sleep(int(x))
