import json, smtplib, ssl
import sendgrid
import os
from sendgrid.helpers.mail import *
import base64

with open('test_mail.json') as f:
	data = json.load(f)
""" UNCOMMENT THIS ONLY IF YOU ARE SURE TO SEND 950 mail
with open('team_mail.json') as f:
	data = json.load(f)
"""
count_success = 0

for d in data:
	team = d['name']
	mails = d['emails']
	#print (team,mails)

	for m in mails:

		try:
			sg = sendgrid.SendGridAPIClient(api_key="{XXX_REDACTED_XXX}")
			from_email = Email("contact@fword.wtf")
			to_email = To(m)
			mail = Mail(from_email, to_email)
			mail.dynamic_template_data = {
				'team' : team
			}
			mail.template_id = "d-9669ed3cda7042acac1c701f00531de1"

			with open("/home/kooli/Documents/Certs/Certs/"+team+".png", 'rb') as sigf:
				sig = sigf.read()
			encoded = base64.b64encode(sig).decode()
			attachment = Attachment()
			attachment.file_content = FileContent(encoded)
			attachment.file_type = FileType('image/png')
			attachment.file_name = FileName(team+".png")
			attachment.disposition = Disposition('attachment')
			attachment.content_id = ContentId('Example Content ID')
			mail.attachment = attachment

			response = sg.client.mail.send.post(request_body=mail.get())
			print(response.status_code)
			print(response.body)
			print("Succesfully sent to",end=" ")
			print(team,end=" - ")
			print(m)
			count_success+=1
			print("Succes Count: ",end='')
			print(str(count_success))
		except Exception:
			print("Error: ",end='')
			print(team,end=" - ")
			print(m)
			continue

