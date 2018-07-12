import imapclient
import pyzmail

# conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
# conn.login('UserName', 'Password')
# conn.select_folder('INBOX', readonly=True)

# UIDs = conn.search(['SINCE 20-Aug-2015'])

# email_id = UIDs[0]
# raw_msg = conn.fetch([email_id], ['BODY[]', 'FLAGS'])

# message = pyzmail.PyzMessage.factory(raw_msg[email_id][b'BODY[]'])
# print(message.get_subject())
# print(message.get_addresses('from'))
# print(message.get_addresses('to'))
# print(message.get_addresses('bcc'))
# print(message.text_part)
# print(message.html_part)

# body = message.text_part.get_payload().decode('UTF-8')

# print(conn.list_folders())
# conn.select_folder('Spam')
# UIDs = conn.search(['ON 10-Jul-2018'])
# email_id = UIDs[0]

# conn.logout()
