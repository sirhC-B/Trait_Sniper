import os
import smtplib


SENDER_EMAIL = "enigmasniper22@gmail.com"
EMAIL_PW = "code4694"
rec_mail = ["chris_boesener@gmx.net","maxi.schelske@web.de"]


def sending_mail(reciver=rec_mail, body="Das ist die Default-nachricht."):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(SENDER_EMAIL,EMAIL_PW)
        print("Login success")

        subject = "Meta Data Alert!"

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(SENDER_EMAIL, reciver[0],msg)
        smtp.sendmail(SENDER_EMAIL, reciver[1],msg)


        print("email has been sent to ", reciver)