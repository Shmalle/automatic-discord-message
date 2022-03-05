How to setup this:

1. Get python 3.8.7: https://www.python.org/ftp/python/3.8.7/python-3.8.7-amd64.exe

2. During installation, tick the box "ADD TO PATH" once you see it.

3. Go to Discord-settings-->Avanced-->Developer Mode (turn ON)

4. Right-click the channel you want the messages in and click "copy ID", then paste it in the "channel.txt" file in the "textfiles" folder. 

5. Right-click the server-name and click "copy id". Afterwards, create the follwing link: https://discord.com/channels/[ID-that-you've-just-copied]/[Channel-ID-that-you've-copied-before]
   It should look something like this: https://discord.com/channels/82828140172439/0234924769124
   Paste that link into "channellink.txt".

6. Get the accounts token that you want to use. Remember: Account-token means full account access. 
   Open Discord IN THE BROWSER and press CTRL+SHIFT+I.
   Afterwards, you will have to click the "Network" tab. 
   Write a message into any channel or direct messages. 
   You will be provided a list of a lot of things on the right side, search for the entry called "messages". Doubleclick it.
   Scroll down in the thing that just popped out. Search for "Authorization". There will be the Token, it looks like this:     OzM5MjYzNTEyOTI0MjU4NDc1.XyX6zA.U2SnzlqRCidSFd4k_5ZHHtn0iM8
   Paste it into "token.txt"

7. Whatever the account is supposed to send, put it into "message.txt"

8. Write the interval, in which the messages should be sent, in seconds into "time.txt" (E.g. if the interval is 15, it will send the message every 15 seconds). Remember that if the interval is too short, the script will possibly fail.
   I've used 40 seconds for an eternity and its working fine. 

9. Go back to your file-explorer and go to the address-bar. Clear it and type "cmd.exe", then press enter. A command prompt will show up. Type "py AutoMessage.py" to start the script 

HMU if there are any problems.
https://shmalle.xyz/contact
Shmalle#1337 on Discord
