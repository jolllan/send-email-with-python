import smtplib, ssl
from config import mailConfig as conf

# on rentre les informations sur le destinataire
email_receiver = input("Veuillez saisir l'adresse mail \n >  ") # = 'anothemr.example@yahoo.com'

# on crée la connexion
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
context.set_ciphers('DEFAULT@SECLEVEL=1')

with smtplib.SMTP(conf.smtp_address, conf.smtp_port) as server:
    server.starttls(context=context)
    # connexion au compte
    server.login(conf.email_address, conf.email_password)
    # envoi du mail
    server.sendmail(conf.email_address, email_receiver, "Voici le mail a envoyé")
