How to setup all of this crap:

1. First of all, please download python and go through the Setup, you will need at least python 3. Download here: https://www.python.org/ftp/python/3.8.7/python-3.8.7-amd64.exe

2. During installation, tick the box "ADD TO PATH" once you see it.

3. Afterwards, you'll have to activate the Developer Mode in Discord. Go to Discord-settings-->Appearance-->scroll down-->Developer Mode (turn ON)

4. Search the channel you want the message to be sent in to and right-click its name, then click "copy ID". Paste it in the "channel.txt" file in the "textfiles" file. 

5. Right-click the servername and click "copy id". Afterwards, create the follwing link: https://discord.com/channels/[ID that you've just copied]/[Channel-ID that you've copied before]
   It will have to look something like this: https://discord.com/channels/82828140172439/0234924769124
   Paste your link into "channellink.txt".

6. This is the tricky part, you will have to copy your token. Remember: Accounttoken means full Account access. 
   Open Discord and press CTRL+SHIFT+I.
   Afterwards, you will have to click the "Network" tab. 
   Write a message into any channel or direct messages. 
   You will be provided a list of a lot of things on the right side, search for the entry called "messages". Doubleclick it.
   Scroll down in the thing that just popped out. Search for "Authorization". There will be the Token, it looks like this: NzM5MjYzNTEyOTI0MjU4NDc1.XyX6zA.U2SnzlqRCidSFd4k_5ZHHtn0iM8
   Nice! Paste it into "token.txt"

7. What do you want to send? Write it into "message.txt"

8. In what interval do you want it to be sent? Write it into "time.txt" ATTENTION: Please provide the time in seconds. Please rememeber: If the interval is too short, the script will possibly fail.
   I've used 40 seconds for an eternity and its working fine. 

9. Right click in the folder. Press "open powershell window here" or something like that. Then execute this: "py AutoMessage.py"


I just tried this on my own, via using the tutorial I just wrote here. It works totally fine. If you're receiving errors, hit me up: https://discord.gg/NMgKDfSqrv

