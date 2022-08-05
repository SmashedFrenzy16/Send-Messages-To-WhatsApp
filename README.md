# Send Messages To WhatsApp
This program made in Python lets you send messages to people without having to manually open your WhatsApp client. You never need to move a finger ever again because of this clear and concise script! Run `python3 send_wa_messages.py` in a terminal if you have Python 3.

NOTE: Replace any mentions of `<Enter Phone Number Here>` with your private direct message recipient's phone number. Also replace any mentions of `"<Enter Group ID Here>` with your group client ID found by doing this:

- Open any group you want and click on the “Group Info” section.

- Scroll all the way down and look for the “Invite via link” option. Tap on that option.

- There you’ll see a link. Copy the link. The suffix part of the link is the id of the group.

- (These steps were taken from towardsdatascience.com hosted by medium.com: https://towardsdatascience.com/automate-whatsapp-messages-with-python-in-3-steps-d64cf0de4539)

ANOTHER NOTE: Please make sure that you are logged into WhatsApp Web because the `pywhatkit` module (`pip install pywhatkit`) requires that.
